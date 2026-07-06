"""Repository path helpers for the Daedalus CLI."""

from __future__ import annotations

from pathlib import Path


REQUIRED_REPO_MARKERS = [
    "README.md",
    "docs/DAEDALUS-OPERATING-MANUAL.md",
    "memory/README.md",
]


def find_repo_root(start: Path | None = None) -> Path:
    """Find the Daedalus repository root from the current directory."""

    current = (start or Path.cwd()).resolve()

    for candidate in [current, *current.parents]:
        if all((candidate / marker).exists() for marker in REQUIRED_REPO_MARKERS):
            return candidate

    raise FileNotFoundError(
        "Could not find Daedalus repo root. Run this command from inside the repository."
    )


def repo_path(*parts: str, root: Path | None = None) -> Path:
    """Return a path inside the Daedalus repository."""

    repo_root = root or find_repo_root()
    return repo_root.joinpath(*parts)
