"""Repository detection tests for Daedalus."""

from __future__ import annotations

from pathlib import Path

import pytest

from daedalus.paths import find_repo_root, repo_path


def create_repo_markers(root: Path) -> None:
    """Create required repository marker files."""

    (root / "docs").mkdir(parents=True)
    (root / "memory").mkdir(parents=True)
    (root / "README.md").write_text("# Daedalus\n", encoding="utf-8")
    (root / "docs" / "DAEDALUS-OPERATING-MANUAL.md").write_text(
        "# Daedalus Operating Manual\n",
        encoding="utf-8",
    )
    (root / "memory" / "README.md").write_text(
        "# Daedalus Project Memory\n",
        encoding="utf-8",
    )


def test_find_repo_root_from_root(tmp_path: Path) -> None:
    """find_repo_root should detect the repository root from root."""

    create_repo_markers(tmp_path)

    assert find_repo_root(tmp_path) == tmp_path.resolve()


def test_find_repo_root_from_nested_directory(tmp_path: Path) -> None:
    """find_repo_root should walk upward from nested directories."""

    create_repo_markers(tmp_path)
    nested = tmp_path / "docs" / "workflows"
    nested.mkdir(parents=True)

    assert find_repo_root(nested) == tmp_path.resolve()


def test_find_repo_root_raises_outside_repo(tmp_path: Path) -> None:
    """find_repo_root should fail outside a Daedalus repository."""

    with pytest.raises(FileNotFoundError):
        find_repo_root(tmp_path)


def test_repo_path_builds_path_inside_repo(tmp_path: Path) -> None:
    """repo_path should build paths relative to the detected repository root."""

    create_repo_markers(tmp_path)

    expected = tmp_path / "memory" / "outputs"
    assert repo_path("memory", "outputs", root=tmp_path) == expected
