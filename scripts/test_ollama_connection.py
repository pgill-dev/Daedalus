#!/usr/bin/env python3
"""
Daedalus Phase I - Ollama Connection Smoke Test

Purpose:
    Validate that a local Ollama service is reachable before running the full
    Daedalus engineering package generator.

What this script does:
    1. Loads the local Daedalus config example.
    2. Checks whether the Ollama API is reachable.
    3. Lists available local Ollama models.
    4. Verifies whether the configured model is installed.
    5. Sends a small engineering-focused prompt to Ollama.
    6. Writes the test result to memory/outputs as Markdown.

What this script does NOT do:
    - It does not touch Proxmox.
    - It does not touch Kubernetes.
    - It does not touch PBS.
    - It does not touch Rapid7.
    - It does not create ClickUp tasks.
    - It does not execute infrastructure changes.
    - It does not store secrets.

Expected usage:
    python scripts/test_ollama_connection.py

Optional usage:
    python scripts/test_ollama_connection.py --model llama3.1:8b
    python scripts/test_ollama_connection.py --url http://localhost:11434
    python scripts/test_ollama_connection.py --no-generate
"""

from __future__ import annotations

import argparse
import json
import sys
import textwrap
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    import yaml
except ModuleNotFoundError:
    yaml = None


@dataclass(frozen=True)
class OllamaSmokeTestConfig:
    """Runtime configuration for the Ollama smoke test."""

    repo_root: Path
    config_path: Path
    output_dir: Path
    ollama_url: str
    model: str
    timeout_seconds: int


@dataclass(frozen=True)
class OllamaModel:
    """Small representation of an Ollama model returned by /api/tags."""

    name: str
    modified_at: str | None = None
    size: int | None = None


class DaedalusSmokeTestError(RuntimeError):
    """Raised when the smoke test cannot complete successfully."""


# -----------------------------
# Path and config helpers
# -----------------------------


def find_repo_root(start: Path) -> Path:
    """Find the Git repository root by walking upward from the start path."""
    current = start.resolve()

    for path in [current, *current.parents]:
        if (path / ".git").exists():
            return path

    raise DaedalusSmokeTestError(
        "Could not find repo root. Run this script from inside the Daedalus repo."
    )


def read_yaml_file(path: Path) -> dict[str, Any]:
    """Read a YAML file into a dictionary."""
    if yaml is None:
        raise DaedalusSmokeTestError(
            "Missing Python dependency: pyyaml. Install it with: python -m pip install pyyaml"
        )

    if not path.exists():
        raise DaedalusSmokeTestError(f"Config file not found: {path}")

    try:
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or {}
    except Exception as exc:  # noqa: BLE001 - keep CLI error readable
        raise DaedalusSmokeTestError(f"Could not parse YAML config file: {path}\n{exc}") from exc

    if not isinstance(data, dict):
        raise DaedalusSmokeTestError(f"Config file did not parse into a mapping: {path}")

    return data


def get_nested(data: dict[str, Any], keys: list[str], default: Any = None) -> Any:
    """Safely retrieve nested dictionary values."""
    current: Any = data

    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]

    return current


def build_config(args: argparse.Namespace) -> OllamaSmokeTestConfig:
    """Build runtime config from CLI args and config/daedalus.local.example.yml."""
    repo_root = find_repo_root(Path.cwd())
    config_path = repo_root / "config" / "daedalus.local.example.yml"
    config_data = read_yaml_file(config_path)

    configured_url = get_nested(config_data, ["llm", "ollama_url"])
    if configured_url is None:
        configured_url = get_nested(config_data, ["llm", "base_url"])
    if configured_url is None:
        configured_url = "http://localhost:11434"

    configured_model = get_nested(config_data, ["llm", "model"], "llama3.1:8b")
    configured_output_dir = get_nested(config_data, ["paths", "output_dir"], "memory/outputs")
    configured_timeout = get_nested(config_data, ["llm", "timeout_seconds"], 120)

    output_dir = repo_root / str(configured_output_dir)

    return OllamaSmokeTestConfig(
        repo_root=repo_root,
        config_path=config_path,
        output_dir=output_dir,
        ollama_url=(args.url or str(configured_url)).rstrip("/"),
        model=args.model or str(configured_model),
        timeout_seconds=int(args.timeout or configured_timeout),
    )


# -----------------------------
# Ollama API helpers
# -----------------------------


def http_json_request(
    url: str,
    *,
    method: str = "GET",
    payload: dict[str, Any] | None = None,
    timeout_seconds: int = 30,
) -> dict[str, Any]:
    """Send a JSON request to Ollama and return decoded JSON."""
    body: bytes | None = None
    headers = {"Accept": "application/json"}

    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request = urllib.request.Request(url=url, data=body, headers=headers, method=method)

    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise DaedalusSmokeTestError(f"HTTP error from Ollama: {exc.code} {exc.reason}\n{detail}") from exc
    except urllib.error.URLError as exc:
        raise DaedalusSmokeTestError(
            "Could not reach Ollama. Confirm Ollama is installed and running.\n"
            f"URL: {url}\n"
            f"Error: {exc}"
        ) from exc
    except TimeoutError as exc:
        raise DaedalusSmokeTestError(f"Timed out connecting to Ollama at {url}") from exc

    if not raw.strip():
        return {}

    try:
        decoded = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise DaedalusSmokeTestError(f"Ollama returned non-JSON response from {url}:\n{raw}") from exc

    if not isinstance(decoded, dict):
        raise DaedalusSmokeTestError(f"Ollama returned unexpected JSON type from {url}: {type(decoded)}")

    return decoded


def list_models(config: OllamaSmokeTestConfig) -> list[OllamaModel]:
    """List models available to the local Ollama instance."""
    data = http_json_request(
        f"{config.ollama_url}/api/tags",
        timeout_seconds=config.timeout_seconds,
    )

    raw_models = data.get("models", [])
    if not isinstance(raw_models, list):
        raise DaedalusSmokeTestError("Ollama /api/tags returned an unexpected models field.")

    models: list[OllamaModel] = []
    for item in raw_models:
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        if not name:
            continue
        models.append(
            OllamaModel(
                name=str(name),
                modified_at=str(item.get("modified_at")) if item.get("modified_at") else None,
                size=int(item["size"]) if isinstance(item.get("size"), int) else None,
            )
        )

    return models


def model_is_available(model_name: str, models: list[OllamaModel]) -> bool:
    """Return True if the configured model appears in Ollama's local model list."""
    available_names = {model.name for model in models}
    return model_name in available_names


def run_generation_test(config: OllamaSmokeTestConfig) -> str:
    """Run a small deterministic-ish generation test through Ollama."""
    prompt = textwrap.dedent(
        """
        You are Daedalus, an Infrastructure Security Engineer.

        Generate a brief Markdown smoke-test response with exactly these headings:

        # Daedalus Ollama Smoke Test
        ## Status
        ## Engineering Boundary
        ## Next Step

        Requirements:
        - Confirm this is only a local model connectivity test.
        - Do not claim any infrastructure was changed.
        - Do not generate secrets.
        - Keep the answer under 200 words.
        """
    ).strip()

    payload = {
        "model": config.model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "top_p": 0.9,
        },
    }

    data = http_json_request(
        f"{config.ollama_url}/api/generate",
        method="POST",
        payload=payload,
        timeout_seconds=config.timeout_seconds,
    )

    response_text = data.get("response")
    if not isinstance(response_text, str) or not response_text.strip():
        raise DaedalusSmokeTestError("Ollama generation completed but returned an empty response.")

    return response_text.strip()


# -----------------------------
# Output helpers
# -----------------------------


def format_size_bytes(size: int | None) -> str:
    """Format a byte size for Markdown output."""
    if size is None:
        return "unknown"

    units = ["B", "KB", "MB", "GB", "TB"]
    value = float(size)
    unit_index = 0

    while value >= 1024 and unit_index < len(units) - 1:
        value /= 1024
        unit_index += 1

    return f"{value:.2f} {units[unit_index]}"


def write_markdown_report(
    config: OllamaSmokeTestConfig,
    models: list[OllamaModel],
    generation_response: str | None,
    generation_skipped: bool,
) -> Path:
    """Write a Markdown smoke-test report to memory/outputs."""
    config.output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_path = config.output_dir / f"ollama-smoke-test-{timestamp}.md"

    model_available = model_is_available(config.model, models)

    model_lines = []
    if models:
        for model in models:
            model_lines.append(
                f"- `{model.name}` — size: {format_size_bytes(model.size)}, modified: {model.modified_at or 'unknown'}"
            )
    else:
        model_lines.append("- No local models returned by Ollama.")

    generation_section: str
    if generation_skipped:
        generation_section = "Generation test skipped with `--no-generate`."
    elif generation_response:
        generation_section = generation_response
    else:
        generation_section = "Generation test did not produce output."

    markdown = f"""# Daedalus Ollama Smoke Test Report

## Test Metadata

- Timestamp: `{timestamp}`
- Repo root: `{config.repo_root}`
- Config path: `{config.config_path}`
- Ollama URL: `{config.ollama_url}`
- Configured model: `{config.model}`
- Output directory: `{config.output_dir}`

## Connectivity Result

Daedalus successfully reached the Ollama API at:

```text
{config.ollama_url}
```

## Configured Model Check

- Configured model: `{config.model}`
- Model available locally: `{model_available}`

## Local Ollama Models

{chr(10).join(model_lines)}

## Generation Test Output

{generation_section}

## Phase I Boundary Confirmation

This smoke test only validates local LLM connectivity. It does not execute infrastructure changes, modify live systems, create secrets, call external project-management APIs, or approve deployment actions.

## Next Step

If connectivity and generation are successful, run the full Phase I engineering package runner without `--dry-run`.
"""

    output_path.write_text(markdown, encoding="utf-8")
    return output_path


# -----------------------------
# CLI
# -----------------------------


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Validate local Ollama connectivity for Daedalus Phase I.",
    )
    parser.add_argument(
        "--model",
        help="Override configured Ollama model name, for example llama3.1:8b.",
    )
    parser.add_argument(
        "--url",
        help="Override configured Ollama base URL, for example http://localhost:11434.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        help="Override Ollama request timeout in seconds.",
    )
    parser.add_argument(
        "--no-generate",
        action="store_true",
        help="Only test Ollama model listing; do not run a text generation test.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Run the Ollama smoke test."""
    args = parse_args(argv or sys.argv[1:])

    try:
        config = build_config(args)

        print("Daedalus Ollama Connection Smoke Test")
        print(f"Repo root: {config.repo_root}")
        print(f"Config: {config.config_path}")
        print(f"Ollama URL: {config.ollama_url}")
        print(f"Model: {config.model}")
        print(f"Output dir: {config.output_dir}")
        print()

        models = list_models(config)
        print(f"Ollama reachable: yes")
        print(f"Models found: {len(models)}")

        if models:
            for model in models:
                marker = "<-- configured" if model.name == config.model else ""
                print(f"- {model.name} {marker}".rstrip())

        if not model_is_available(config.model, models):
            print()
            print("Configured model was not found locally.")
            print(f"Pull it with: ollama pull {config.model}")
            report_path = write_markdown_report(
                config=config,
                models=models,
                generation_response=None,
                generation_skipped=True,
            )
            print(f"Smoke-test report written to: {report_path}")
            return 2

        generation_response: str | None = None
        generation_skipped = bool(args.no_generate)

        if args.no_generate:
            print()
            print("Generation test skipped because --no-generate was set.")
        else:
            print()
            print("Running small generation test...")
            generation_response = run_generation_test(config)
            print("Generation test: passed")

        report_path = write_markdown_report(
            config=config,
            models=models,
            generation_response=generation_response,
            generation_skipped=generation_skipped,
        )

        print()
        print(f"Smoke-test report written to: {report_path}")
        return 0

    except DaedalusSmokeTestError as exc:
        print("Daedalus Ollama smoke test failed.", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
