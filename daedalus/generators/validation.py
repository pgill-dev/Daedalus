"""Validation checklist generator."""

from __future__ import annotations

from pathlib import Path

from daedalus.generators.common import safe_slug, today_iso, write_file


def build_validation_checklist(title: str) -> str:
    """Build a proposed validation checklist."""

    return f"""# Validation Checklist: {title}

## Metadata

**Date:** {today_iso()}  
**Author:** Daedalus  
**Status:** Proposed  
**Related Request:**  
**Related Package:**  
**Risk Level:** Low | Medium | High | Critical  

## Summary

Briefly describe what this checklist validates.

## Pre-Change Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| PRE-001 |  |  |  | Not Tested |  |

## Post-Change Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| POST-001 |  |  |  | Not Tested |  |

## Negative Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| NEG-001 |  |  |  | Not Tested |  |

## Rollback Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| RBV-001 |  |  |  | Not Tested |  |

## Human Approval Gate

The following require human confirmation:

- Validation execution
- Validation pass/fail status
- Evidence acceptance
- Residual risk acceptance
"""


def create_validation_checklist(root: Path, title: str, force: bool = False) -> Path:
    """Create a validation checklist under memory/validation."""

    slug = safe_slug(title)
    path = root / "memory" / "validation" / f"{today_iso()}-{slug}-validation-checklist.md"
    return write_file(path, build_validation_checklist(title), force=force)
