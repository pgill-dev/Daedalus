# Validation Checklist: Daedalus Lab Control Plane MVP

## Metadata

**Date:** 2026-07-06  
**Author:** Daedalus  
**Status:** Proposed  
**Related Request:** memory/plans/2026-07-06-daedalus-lab-control-plane-engineering-request.md  
**Related Package:** memory/outputs/2026-07-06-daedalus-lab-control-plane-engineering-package.md  
**Risk Level:** Medium  

## Summary

This checklist validates that the Daedalus lab control-plane package is complete, reviewable, and safe to keep as proposed project memory.

## Pre-Change Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| PRE-001 | Confirm working tree is clean before applying package | `git status` shows clean state | Terminal output | Not Tested |  |
| PRE-002 | Confirm CI is green before package | Latest GitHub Actions run is green | GitHub screenshot or note | Not Tested |  |
| PRE-003 | Confirm package contains no secrets | No plaintext secrets are present | Review result | Not Tested |  |

## Post-Change Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| POST-001 | Run repository validation | `python scripts/validate_repo.py` passes | Terminal output | Not Tested |  |
| POST-002 | Run schema validation | `python scripts/validate_schemas.py` passes | Terminal output | Not Tested |  |
| POST-003 | Run tests | `python -m pytest` passes | Terminal output | Not Tested |  |
| POST-004 | Confirm package files are present | All package files exist in memory directories | Git status or file listing | Not Tested |  |
| POST-005 | Confirm GitHub Actions passes | CI run is green | GitHub Actions result | Not Tested |  |

## Negative Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| NEG-001 | Confirm no artifact is marked approved by default | Artifacts remain `Proposed` | File review | Not Tested |  |
| NEG-002 | Confirm no live commands are included | Package does not instruct automatic execution | File review | Not Tested |  |
| NEG-003 | Confirm no secrets are included | No passwords, keys, or tokens | File review or scan | Not Tested |  |

## Rollback Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| RBV-001 | Revert package if needed | Repo returns to prior state | Git log/status | Not Tested |  |
| RBV-002 | Re-run validation after rollback | Validation and tests pass | Terminal output | Not Tested |  |
| RBV-003 | Confirm ADR status updated if not reverting | ADR is marked Rejected or Superseded | File review | Not Tested |  |

## Human Approval Gate

The following require human confirmation:

- Validation execution
- Validation pass/fail status
- Evidence acceptance
- Treating this package as accepted project memory
