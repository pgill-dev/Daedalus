"""Rollback plan generator."""

from __future__ import annotations

from pathlib import Path

from daedalus.generators.common import safe_slug, today_iso, write_file


def build_rollback_plan(title: str) -> str:
    """Build a proposed rollback plan."""

    return f"""# Rollback Plan: {title}

## Metadata

**Date:** {today_iso()}  
**Author:** Daedalus  
**Status:** Proposed  
**Related Request:**  
**Related Package:**  
**Risk Level:** Low | Medium | High | Critical  

## Summary

Briefly describe what this rollback plan covers.

## Rollback Trigger

Define exactly when rollback should begin.

## Preconditions

Before rollback, confirm:

- 

## Required Known-Good State

Required rollback references:

- 

## Rollback Steps

1. 

## Rollback Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| RB-VAL-001 |  |  |  | Not Tested |  |

## Risks During Rollback

| Risk | Impact | Mitigation |
|---|---|---|
|  |  |  |

## Escalation Plan

If rollback does not restore the expected state:

1. Stop further changes.
2. Preserve logs and evidence.
3. Notify the human approver or system owner.
4. Reassess using the latest known-good backup, snapshot, or configuration.

## Human Approval Gate

The following require human approval or confirmation:

- Starting rollback
- Running rollback commands
- Accepting rollback results
- Declaring rollback complete
"""


def create_rollback_plan(root: Path, title: str, force: bool = False) -> Path:
    """Create a rollback plan under memory/rollback."""

    slug = safe_slug(title)
    path = root / "memory" / "rollback" / f"{today_iso()}-{slug}-rollback-plan.md"
    return write_file(path, build_rollback_plan(title), force=force)
