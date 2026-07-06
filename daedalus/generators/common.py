"""Common generator helpers."""

from __future__ import annotations

from datetime import date
from pathlib import Path


def today_iso() -> str:
    """Return today's date in ISO format."""

    return date.today().isoformat()


def safe_slug(value: str) -> str:
    """Convert a title into a conservative file-name slug."""

    keep = []
    previous_dash = False

    for char in value.strip().lower():
        if char.isalnum():
            keep.append(char)
            previous_dash = False
        elif not previous_dash:
            keep.append("-")
            previous_dash = True

    slug = "".join(keep).strip("-")
    return slug or "untitled"


def write_file(path: Path, content: str, force: bool = False) -> Path:
    """Write a file, creating parent directories and avoiding accidental overwrite."""

    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists() and not force:
        raise FileExistsError(f"File already exists: {path}")

    path.write_text(content, encoding="utf-8")
    return path
