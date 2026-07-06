#!/usr/bin/env python3
"""Validate Daedalus JSON schema files.

This script uses only the Python standard library.
It checks schema files for valid JSON, required metadata, unique IDs, and unique titles.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = REPO_ROOT / "schemas"

REQUIRED_SCHEMA_FIELDS = [
    "$schema",
    "$id",
    "title",
    "type",
]


def load_schema(path: Path) -> dict:
    """Load a JSON schema file."""

    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, dict):
        raise ValueError("schema root must be a JSON object")

    return data


def validate_schema_file(path: Path) -> list[str]:
    """Validate one schema file and return a list of errors."""

    errors: list[str] = []

    try:
        schema = load_schema(path)
    except Exception as exc:
        return [f"{path.relative_to(REPO_ROOT)}: invalid JSON or schema root: {exc}"]

    for field in REQUIRED_SCHEMA_FIELDS:
        if field not in schema:
            errors.append(f"{path.relative_to(REPO_ROOT)}: missing required field '{field}'")

    if schema.get("type") != "object":
        errors.append(f"{path.relative_to(REPO_ROOT)}: root type should be 'object'")

    if "required" in schema and not isinstance(schema["required"], list):
        errors.append(f"{path.relative_to(REPO_ROOT)}: 'required' must be a list")

    if "properties" in schema and not isinstance(schema["properties"], dict):
        errors.append(f"{path.relative_to(REPO_ROOT)}: 'properties' must be an object")

    return errors


def validate_all_schemas(schema_dir: Path = SCHEMA_DIR) -> list[str]:
    """Validate all schemas and return a list of errors."""

    errors: list[str] = []

    if not schema_dir.exists():
        return [f"schema directory not found: {schema_dir.relative_to(REPO_ROOT)}"]

    schema_files = sorted(schema_dir.glob("*.json"))

    if not schema_files:
        return [f"no schema files found in {schema_dir.relative_to(REPO_ROOT)}"]

    ids: dict[str, Path] = {}
    titles: dict[str, Path] = {}

    for path in schema_files:
        file_errors = validate_schema_file(path)
        errors.extend(file_errors)

        if file_errors:
            continue

        schema = load_schema(path)

        schema_id = str(schema.get("$id", "")).strip()
        title = str(schema.get("title", "")).strip()

        if not schema_id:
            errors.append(f"{path.relative_to(REPO_ROOT)}: empty $id")
        elif schema_id in ids:
            errors.append(
                f"{path.relative_to(REPO_ROOT)}: duplicate $id also used by "
                f"{ids[schema_id].relative_to(REPO_ROOT)}"
            )
        else:
            ids[schema_id] = path

        if not title:
            errors.append(f"{path.relative_to(REPO_ROOT)}: empty title")
        elif title in titles:
            errors.append(
                f"{path.relative_to(REPO_ROOT)}: duplicate title also used by "
                f"{titles[title].relative_to(REPO_ROOT)}"
            )
        else:
            titles[title] = path

    return errors


def main() -> int:
    """Run schema validation."""

    print("Daedalus schema validation starting...")
    print(f"Schema directory: {SCHEMA_DIR}")

    errors = validate_all_schemas()

    if errors:
        print(f"Schema validation failed with {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Schema validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
