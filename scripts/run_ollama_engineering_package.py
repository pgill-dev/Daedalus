#!/usr/bin/env python3
"""
Daedalus Phase I Ollama Engineering Package Runner

Purpose:
    Generate a structured engineering package from Daedalus repo-defined
    prompts, workflow contracts, and output contracts using a local Ollama model.

Phase I Boundary:
    - No infrastructure execution
    - No live system modification
    - No secrets collection
    - No API calls to Proxmox, Kubernetes, PBS, Rapid7, GitHub, or ClickUp
    - Generates Markdown only for human review

Example:
    python scripts/run_ollama_engineering_package.py --workflow vaultwarden
    python scripts/run_ollama_engineering_package.py --workflow vaultwarden --dry-run
    python scripts/run_ollama_engineering_package.py --model llama3.1:8b
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
from typing import Any, Dict, Optional

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - user-facing dependency message
    yaml = None  # type: ignore


REPO_ROOT_MARKERS = ("README.md", "pyproject.toml", ".git")
DEFAULT_CONFIG_CANDIDATES = (
    "config/daedalus.local.yml",
    "config/daedalus.local.example.yml",
)

WORKFLOW_ALIASES = {
    "vaultwarden": "prompts/workflows/vaultwarden-engineering-request.md",
    "vaultwarden-engineering-request": "prompts/workflows/vaultwarden-engineering-request.md",
}

DEFAULT_SYSTEM_PROMPT = "prompts/system/daedalus-system-prompt.md"
DEFAULT_OUTPUT_CONTRACT = "prompts/output-contracts/engineering-package-v1.md"
DEFAULT_OUTPUT_DIR = "memory/outputs"
DEFAULT_OLLAMA_URL = "http://localhost:11434"
DEFAULT_MODEL = "llama3.1:8b"


@dataclass(frozen=True)
class RunnerConfig:
    repo_root: Path
    config_path: Optional[Path]
    ollama_url: str
    model: str
    system_prompt_path: Path
    workflow_path: Path
    output_contract_path: Path
    output_dir: Path
    temperature: Optional[float]
    num_ctx: Optional[int]


def find_repo_root(start: Path) -> Path:
    """Walk upward until a Daedalus repo root is found."""
    current = start.resolve()

    for candidate in [current, *current.parents]:
        if any((candidate / marker).exists() for marker in REPO_ROOT_MARKERS):
            return candidate

    raise SystemExit(
        "ERROR: Could not locate repository root. Run this script from inside the Daedalus repo."
    )


def read_text(path: Path, label: str) -> str:
    if not path.exists():
        raise SystemExit(f"ERROR: Missing {label}: {path}")
    if not path.is_file():
        raise SystemExit(f"ERROR: Expected {label} to be a file: {path}")
    return path.read_text(encoding="utf-8")


def load_yaml(path: Optional[Path]) -> Dict[str, Any]:
    if path is None:
        return {}

    if yaml is None:
        raise SystemExit(
            "ERROR: PyYAML is not installed. Install it with: python -m pip install pyyaml"
        )

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - user-facing parse error
        raise SystemExit(f"ERROR: Failed to parse YAML config {path}: {exc}") from exc

    return data or {}


def get_nested(config: Dict[str, Any], *keys: str, default: Any = None) -> Any:
    current: Any = config
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def choose_config(repo_root: Path, explicit_config: Optional[str]) -> Optional[Path]:
    if explicit_config:
        path = (repo_root / explicit_config).resolve()
        if not path.exists():
            raise SystemExit(f"ERROR: Config file not found: {path}")
        return path

    for relative in DEFAULT_CONFIG_CANDIDATES:
        path = repo_root / relative
        if path.exists():
            return path

    return None


def resolve_workflow(repo_root: Path, workflow_arg: str) -> Path:
    if workflow_arg in WORKFLOW_ALIASES:
        return repo_root / WORKFLOW_ALIASES[workflow_arg]

    raw_path = Path(workflow_arg)
    if raw_path.suffix == ".md":
        return raw_path if raw_path.is_absolute() else repo_root / raw_path

    return repo_root / "prompts" / "workflows" / f"{workflow_arg}.md"


def build_runner_config(args: argparse.Namespace) -> RunnerConfig:
    repo_root = find_repo_root(Path.cwd())
    config_path = choose_config(repo_root, args.config)
    config = load_yaml(config_path)

    ollama_url = args.ollama_url or get_nested(config, "llm", "base_url", default=DEFAULT_OLLAMA_URL)
    model = args.model or get_nested(config, "llm", "model", default=DEFAULT_MODEL)

    system_prompt = args.system_prompt or get_nested(
        config, "paths", "system_prompt", default=DEFAULT_SYSTEM_PROMPT
    )
    output_contract = args.output_contract or get_nested(
        config, "paths", "output_contract", default=DEFAULT_OUTPUT_CONTRACT
    )
    output_dir = args.output_dir or get_nested(
        config, "paths", "output_dir", default=DEFAULT_OUTPUT_DIR
    )

    temperature = args.temperature
    if temperature is None:
        temperature = get_nested(config, "llm", "temperature", default=None)

    num_ctx = args.num_ctx
    if num_ctx is None:
        num_ctx = get_nested(config, "llm", "num_ctx", default=None)

    return RunnerConfig(
        repo_root=repo_root,
        config_path=config_path,
        ollama_url=str(ollama_url).rstrip("/"),
        model=str(model),
        system_prompt_path=repo_root / system_prompt,
        workflow_path=resolve_workflow(repo_root, args.workflow),
        output_contract_path=repo_root / output_contract,
        output_dir=repo_root / output_dir,
        temperature=temperature,
        num_ctx=num_ctx,
    )


def build_prompt_bundle(config: RunnerConfig) -> str:
    system_prompt = read_text(config.system_prompt_path, "system prompt")
    workflow = read_text(config.workflow_path, "workflow prompt")
    output_contract = read_text(config.output_contract_path, "output contract")

    return textwrap.dedent(
        f"""
        # Daedalus Phase I Engineering Package Request

        You are operating inside the Daedalus Phase I boundary.

        Absolute rules:
        - Do not claim infrastructure changes were executed.
        - Do not generate real secrets, passwords, private keys, tokens, or API credentials.
        - Do not instruct automatic execution against live systems.
        - Do not skip human approval gates.
        - Produce Markdown suitable for Git review.

        ---

        ## System Prompt

        {system_prompt}

        ---

        ## Workflow Contract

        {workflow}

        ---

        ## Output Contract

        {output_contract}

        ---

        ## Operator Instruction

        Generate the requested engineering package now.
        Follow the workflow contract and output contract exactly.
        The result must be complete, reviewable, and safe for human approval.
        """
    ).strip() + "\n"


def ollama_generate(config: RunnerConfig, prompt: str) -> str:
    endpoint = f"{config.ollama_url}/api/generate"

    options: Dict[str, Any] = {}
    if config.temperature is not None:
        options["temperature"] = config.temperature
    if config.num_ctx is not None:
        options["num_ctx"] = config.num_ctx

    payload: Dict[str, Any] = {
        "model": config.model,
        "prompt": prompt,
        "stream": False,
    }
    if options:
        payload["options"] = options

    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=600) as response:
            body = response.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise SystemExit(
            "ERROR: Could not reach Ollama.\n"
            f"Endpoint: {endpoint}\n"
            "Check that Ollama is installed and running, then try: ollama list\n"
            f"Details: {exc}"
        ) from exc

    try:
        data = json.loads(body)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ERROR: Ollama returned invalid JSON: {exc}\nBody:\n{body[:500]}") from exc

    if "error" in data:
        raise SystemExit(f"ERROR: Ollama returned an error: {data['error']}")

    generated = data.get("response")
    if not generated:
        raise SystemExit(f"ERROR: Ollama response did not include generated text. Response: {data}")

    return str(generated).strip() + "\n"


def write_output(config: RunnerConfig, content: str, workflow_name: str, suffix: str = "md") -> Path:
    config.output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    safe_workflow = workflow_name.replace("\\", "-").replace("/", "-").replace(" ", "-")
    output_path = config.output_dir / f"{safe_workflow}-engineering-package-{timestamp}.{suffix}"
    output_path.write_text(content, encoding="utf-8")
    return output_path


def format_output_document(generated: str, config: RunnerConfig, prompt_bundle: str) -> str:
    generated_at = datetime.now().isoformat(timespec="seconds")
    config_display = str(config.config_path.relative_to(config.repo_root)) if config.config_path else "none"

    metadata = textwrap.dedent(
        f"""
        # Daedalus Generated Engineering Package

        > Generated by Daedalus Phase I Ollama runner. Human review required before implementation.

        ## Generation Metadata

        - Generated At: {generated_at}
        - Model: {config.model}
        - Ollama URL: {config.ollama_url}
        - Config: {config_display}
        - System Prompt: {config.system_prompt_path.relative_to(config.repo_root)}
        - Workflow: {config.workflow_path.relative_to(config.repo_root)}
        - Output Contract: {config.output_contract_path.relative_to(config.repo_root)}
        - Phase Boundary: Generate-only; no live infrastructure execution

        ---

        """
    ).lstrip()

    return metadata + generated.strip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a Daedalus engineering package using local Ollama."
    )
    parser.add_argument(
        "--workflow",
        default="vaultwarden",
        help="Workflow alias or markdown path. Default: vaultwarden",
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Optional config path relative to repo root. Default: config/daedalus.local.yml if present, else config/daedalus.local.example.yml",
    )
    parser.add_argument("--model", default=None, help="Override Ollama model name.")
    parser.add_argument("--ollama-url", default=None, help="Override Ollama base URL.")
    parser.add_argument("--system-prompt", default=None, help="Override system prompt markdown path.")
    parser.add_argument("--output-contract", default=None, help="Override output contract markdown path.")
    parser.add_argument("--output-dir", default=None, help="Override output directory.")
    parser.add_argument("--temperature", type=float, default=None, help="Override model temperature.")
    parser.add_argument("--num-ctx", type=int, default=None, help="Override Ollama context window.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not call Ollama. Write the assembled prompt bundle to the output directory instead.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = build_runner_config(args)
    prompt_bundle = build_prompt_bundle(config)

    print("Daedalus Phase I Ollama Runner")
    print(f"Repo root:       {config.repo_root}")
    print(f"Config:          {config.config_path or 'none'}")
    print(f"Model:           {config.model}")
    print(f"Ollama URL:      {config.ollama_url}")
    print(f"Workflow:        {config.workflow_path.relative_to(config.repo_root)}")
    print(f"Output contract: {config.output_contract_path.relative_to(config.repo_root)}")
    print(f"Output dir:      {config.output_dir.relative_to(config.repo_root)}")

    if args.dry_run:
        output_path = write_output(config, prompt_bundle, args.workflow, suffix="prompt.md")
        print("\nDry run complete. Prompt bundle written to:")
        print(output_path)
        return 0

    print("\nCalling Ollama. This may take a bit depending on model and hardware...")
    generated = ollama_generate(config, prompt_bundle)
    output_document = format_output_document(generated, config, prompt_bundle)
    output_path = write_output(config, output_document, args.workflow, suffix="md")

    print("\nEngineering package generated:")
    print(output_path)
    print("\nNext review steps:")
    print("1. Open the generated Markdown file.")
    print("2. Review against docs/phase-i-validation-checklist.md.")
    print("3. Do not execute anything without human approval.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
