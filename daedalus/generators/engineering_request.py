"""Engineering request generator."""

from __future__ import annotations

from pathlib import Path

from daedalus.generators.common import safe_slug, today_iso, write_file


def build_engineering_request(title: str) -> str:
    """Build a proposed engineering request Markdown document."""

    return f"""# Engineering Request: {title}

## Request Summary

Briefly describe the engineering work being requested.

## Request Type

- [ ] Architecture planning
- [ ] Documentation
- [ ] Infrastructure as Code
- [ ] Configuration generation
- [ ] Validation checklist
- [ ] Rollback plan
- [ ] Threat model
- [ ] Security review
- [ ] Other

## Target System or Component

Describe the system, service, lab component, repository, or environment this request affects.

## Current State

Describe the current known state.

## Desired Outcome

Describe what success should look like.

## Constraints

- No automatic execution
- Human approval required before infrastructure-impacting changes
- No plaintext secrets

## Risk Level

- [ ] Low — documentation or planning only
- [ ] Medium — configuration or IaC proposal
- [ ] High — infrastructure-impacting change
- [ ] Critical — affects access, identity, backups, or security boundaries

## Human Approval Requirement

- [ ] I understand this request will not be automatically executed.
- [ ] I understand generated changes must be reviewed before use.

## Requested Outputs

- [ ] Engineering plan
- [ ] Architecture note
- [ ] ADR
- [ ] IaC/config draft
- [ ] Validation checklist
- [ ] Rollback plan
- [ ] Threat model
- [ ] Documentation update
- [ ] Final implementation package

## Acceptance Criteria

- [ ] Scope is clear
- [ ] Risks are documented
- [ ] Rollback path exists, if applicable
- [ ] Validation steps are included, if applicable
- [ ] Human approval point is identified

## Metadata

**Created:** {today_iso()}  
**Status:** Proposed  
"""


def create_engineering_request(root: Path, title: str, force: bool = False) -> Path:
    """Create an engineering request under memory/plans."""

    slug = safe_slug(title)
    path = root / "memory" / "plans" / f"{today_iso()}-{slug}-engineering-request.md"
    return write_file(path, build_engineering_request(title), force=force)
