"""ADR generator."""

from __future__ import annotations

from pathlib import Path

from daedalus.generators.common import safe_slug, today_iso, write_file


def build_adr(title: str, number: str) -> str:
    """Build a proposed ADR Markdown document."""

    return f"""# ADR-{number}: {title}

## Status

Proposed

## Date

{today_iso()}

## Decision Owner

Human reviewer or owner.

## Related Records

- Engineering Request:
- Engineering Package:
- Security Review:
- Validation Checklist:
- Rollback Plan:
- Supersedes:
- Superseded by:

## Context

Describe the situation, problem, constraint, or opportunity that requires a decision.

## Decision

State the decision clearly.

## Options Considered

### Option 1: <Name>

**Summary:**  

**Pros:**

- 

**Cons:**

- 

### Option 2: <Name>

**Summary:**  

**Pros:**

- 

**Cons:**

- 

## Rationale

Explain why the chosen option was selected.

## Consequences

### Positive Consequences

- 

### Negative Consequences

- 

### Neutral Consequences

- 

## Security Considerations

- 

## Validation Impact

- 

## Rollback Impact

- 

## Human Approval

**Approval required:** Yes  
**Approved by:**  
**Approval date:**  
**Approval notes:**  

## Follow-Up Actions

- 
"""


def next_adr_number(root: Path) -> str:
    """Return the next ADR number based on memory/decisions files."""

    decisions_dir = root / "memory" / "decisions"
    highest = 0

    for path in decisions_dir.glob("*.md"):
        prefix = path.name.split("-", 1)[0]
        if prefix.isdigit():
            highest = max(highest, int(prefix))

    return f"{highest + 1:04d}"


def create_adr(root: Path, title: str, force: bool = False) -> Path:
    """Create an ADR under memory/decisions."""

    number = next_adr_number(root)
    slug = safe_slug(title)
    path = root / "memory" / "decisions" / f"{number}-{slug}.md"
    return write_file(path, build_adr(title, number), force=force)
