"""Tests for Daedalus schema validation tooling."""

from __future__ import annotations

import json
from pathlib import Path

from scripts.validate_schemas import validate_all_schemas, validate_schema_file


def write_schema(path: Path, schema_id: str, title: str) -> None:
    """Write a minimal valid schema."""

    path.write_text(
        json.dumps(
            {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "$id": schema_id,
                "title": title,
                "type": "object",
                "required": [],
                "properties": {},
            },
            indent=2,
        ),
        encoding="utf-8",
    )


def test_validate_schema_file_accepts_minimal_schema(tmp_path: Path) -> None:
    """A minimal schema with required metadata should pass."""

    schema_path = tmp_path / "example.schema.json"
    write_schema(schema_path, "https://example.com/schema", "Example Schema")

    assert validate_schema_file(schema_path) == []


def test_validate_schema_file_rejects_missing_metadata(tmp_path: Path) -> None:
    """Schemas missing required metadata should fail."""

    schema_path = tmp_path / "bad.schema.json"
    schema_path.write_text(
        json.dumps({"type": "object"}),
        encoding="utf-8",
    )

    errors = validate_schema_file(schema_path)

    assert any("missing required field '$schema'" in error for error in errors)
    assert any("missing required field '$id'" in error for error in errors)
    assert any("missing required field 'title'" in error for error in errors)


def test_validate_all_schemas_rejects_duplicate_ids(tmp_path: Path) -> None:
    """Duplicate schema IDs should fail validation."""

    schema_dir = tmp_path / "schemas"
    schema_dir.mkdir()

    write_schema(schema_dir / "one.json", "https://example.com/schema", "Schema One")
    write_schema(schema_dir / "two.json", "https://example.com/schema", "Schema Two")

    errors = validate_all_schemas(schema_dir)

    assert any("duplicate $id" in error for error in errors)


def test_validate_all_schemas_rejects_duplicate_titles(tmp_path: Path) -> None:
    """Duplicate schema titles should fail validation."""

    schema_dir = tmp_path / "schemas"
    schema_dir.mkdir()

    write_schema(schema_dir / "one.json", "https://example.com/schema-one", "Same Title")
    write_schema(schema_dir / "two.json", "https://example.com/schema-two", "Same Title")

    errors = validate_all_schemas(schema_dir)

    assert any("duplicate title" in error for error in errors)


def test_validate_all_schemas_accepts_unique_schemas(tmp_path: Path) -> None:
    """Unique valid schemas should pass."""

    schema_dir = tmp_path / "schemas"
    schema_dir.mkdir()

    write_schema(schema_dir / "one.json", "https://example.com/schema-one", "Schema One")
    write_schema(schema_dir / "two.json", "https://example.com/schema-two", "Schema Two")

    assert validate_all_schemas(schema_dir) == []
