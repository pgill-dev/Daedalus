"""Generator tests for Daedalus."""

from __future__ import annotations

from pathlib import Path

import pytest

from daedalus.generators.adr import create_adr, next_adr_number
from daedalus.generators.common import safe_slug, write_file
from daedalus.generators.engineering_package import create_engineering_package
from daedalus.generators.engineering_request import create_engineering_request
from daedalus.generators.rollback import create_rollback_plan
from daedalus.generators.validation import create_validation_checklist


def test_safe_slug_handles_basic_title() -> None:
    """safe_slug should create conservative file-name slugs."""

    assert safe_slug("Deploy Internal Docs!") == "deploy-internal-docs"


def test_safe_slug_handles_empty_title() -> None:
    """safe_slug should return untitled for empty input."""

    assert safe_slug("   ") == "untitled"


def test_write_file_refuses_overwrite(tmp_path: Path) -> None:
    """write_file should avoid accidental overwrite by default."""

    path = tmp_path / "example.md"
    write_file(path, "# Example\n")

    with pytest.raises(FileExistsError):
        write_file(path, "# Changed\n")


def test_write_file_allows_force_overwrite(tmp_path: Path) -> None:
    """write_file should overwrite when force is true."""

    path = tmp_path / "example.md"
    write_file(path, "# Example\n")
    write_file(path, "# Changed\n", force=True)

    assert path.read_text(encoding="utf-8") == "# Changed\n"


def test_create_engineering_request(tmp_path: Path) -> None:
    """Engineering request generator should write to memory/plans."""

    path = create_engineering_request(tmp_path, "Deploy Internal Docs")

    assert path.exists()
    assert path.parent == tmp_path / "memory" / "plans"
    assert "# Engineering Request: Deploy Internal Docs" in path.read_text(encoding="utf-8")


def test_create_engineering_package(tmp_path: Path) -> None:
    """Engineering package generator should write to memory/outputs."""

    path = create_engineering_package(tmp_path, "Deploy Internal Docs")

    assert path.exists()
    assert path.parent == tmp_path / "memory" / "outputs"
    assert "# Engineering Package: Deploy Internal Docs" in path.read_text(encoding="utf-8")


def test_next_adr_number_with_existing_decision(tmp_path: Path) -> None:
    """ADR numbering should increment from existing decision records."""

    decisions = tmp_path / "memory" / "decisions"
    decisions.mkdir(parents=True)
    (decisions / "0001-project-memory.md").write_text("# ADR-0001\n", encoding="utf-8")
    (decisions / "0002-access-model.md").write_text("# ADR-0002\n", encoding="utf-8")

    assert next_adr_number(tmp_path) == "0003"


def test_create_adr(tmp_path: Path) -> None:
    """ADR generator should write to memory/decisions with next number."""

    decisions = tmp_path / "memory" / "decisions"
    decisions.mkdir(parents=True)
    (decisions / "0001-project-memory.md").write_text("# ADR-0001\n", encoding="utf-8")

    path = create_adr(tmp_path, "Use Identity Aware Access")

    assert path.name == "0002-use-identity-aware-access.md"
    assert "# ADR-0002: Use Identity Aware Access" in path.read_text(encoding="utf-8")


def test_create_validation_checklist(tmp_path: Path) -> None:
    """Validation generator should write to memory/validation."""

    path = create_validation_checklist(tmp_path, "Deploy Internal Docs")

    assert path.exists()
    assert path.parent == tmp_path / "memory" / "validation"
    assert "# Validation Checklist: Deploy Internal Docs" in path.read_text(encoding="utf-8")


def test_create_rollback_plan(tmp_path: Path) -> None:
    """Rollback generator should write to memory/rollback."""

    path = create_rollback_plan(tmp_path, "Deploy Internal Docs")

    assert path.exists()
    assert path.parent == tmp_path / "memory" / "rollback"
    assert "# Rollback Plan: Deploy Internal Docs" in path.read_text(encoding="utf-8")
