# Rollback Plan: Daedalus Lab Control Plane MVP

## Metadata

**Date:** 2026-07-06  
**Author:** Daedalus  
**Status:** Proposed  
**Related Request:** memory/plans/2026-07-06-daedalus-lab-control-plane-engineering-request.md  
**Related Package:** memory/outputs/2026-07-06-daedalus-lab-control-plane-engineering-package.md  
**Risk Level:** Medium  

## Summary

This rollback plan describes how to reverse the Daedalus lab control-plane package if it causes confusion, breaks validation, or should not be adopted.

## Rollback Trigger

Rollback should begin if:

- CI fails because of the package
- The package weakens approval language
- The package implies Daedalus can execute infrastructure changes
- The package includes sensitive details
- The package is rejected by human review
- The package conflicts with the operating manual

## Preconditions

Before rollback, confirm:

- Current Git commit is known
- The package commit is identifiable
- Any useful review notes are preserved
- Human owner approves rollback or rejection

## Required Known-Good State

Required rollback references:

- Previous Git commit before package
- Current green CI state
- Operating manual
- Existing project memory structure
- Existing validation and schema tooling

## Rollback Steps

1. Stop treating the package as accepted.
2. Preserve any review notes.
3. Revert the package commit if the package should be removed.
4. Alternatively, mark the package and ADR as `Rejected` or `Superseded`.
5. Re-run `python scripts/validate_repo.py`.
6. Re-run `python scripts/validate_schemas.py`.
7. Re-run `python -m pytest`.
8. Push the rollback commit if needed.
9. Confirm GitHub Actions passes.

## Rollback Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| RB-VAL-001 | Repository validation passes | No validation failures | Terminal output | Not Tested |  |
| RB-VAL-002 | Schema validation passes | No schema validation failures | Terminal output | Not Tested |  |
| RB-VAL-003 | Tests pass | pytest passes | Terminal output | Not Tested |  |
| RB-VAL-004 | CI passes | GitHub Actions green | GitHub result | Not Tested |  |
| RB-VAL-005 | ADR status is correct | ADR removed, rejected, or superseded | File review | Not Tested |  |

## Risks During Rollback

| Risk | Impact | Mitigation |
|---|---|---|
| Removing useful context | Loss of project history | Prefer rejected or superseded status if history matters |
| Reverting wrong commit | Unrelated work removed | Check commit hash before revert |
| Leaving stale references | Broken links or confusing docs | Run validation and review related files |

## Escalation Plan

If rollback does not restore the expected state:

1. Stop further changes.
2. Review Git log.
3. Identify affected files.
4. Restore from the last green commit.
5. Re-run validation.
6. Document outcome.

## Human Approval Gate

The following require human approval or confirmation:

- Starting rollback
- Reverting committed package files
- Marking the ADR rejected or superseded
- Declaring rollback complete
