# Rollback Plan: Internal Documentation Service Behind Identity-Aware Access

## Metadata

**Date:** 2026-07-06  
**Author:** Daedalus  
**Status:** Proposed  
**Related Request:** 01-engineering-request.md  
**Related Package:** 03-engineering-package.md  
**Risk Level:** High  

## Summary

This rollback plan describes how to return the environment to a safe state if the internal documentation service deployment causes access issues, unintended exposure, or routing problems.

## Rollback Trigger

Rollback should begin if any of the following occur:

- The service is reachable without authentication.
- A non-approved user can access the service.
- The hostname routes to the wrong internal service.
- The service exposes sensitive content.
- Existing access paths are disrupted.
- Validation fails and the issue cannot be corrected immediately.

## Preconditions

Before rollback, confirm:

- A human owner has authorized rollback.
- Current evidence has been preserved.
- Known-good access configuration is available.
- Existing service dependencies are understood.
- Rollback will not remove unrelated access policies.

## Required Known-Good State

Required rollback references:

- Previous access policy configuration
- Previous tunnel or reverse proxy route
- Previous DNS state
- Service deployment state before change
- Approved user or group list
- Relevant logs

## Rollback Steps

1. Stop further changes.
2. Preserve current logs, screenshots, and configuration evidence.
3. Disable the new documentation service access route.
4. Remove or disable the new public hostname, if created.
5. Stop the documentation service or disconnect it from the access path.
6. Restore the previous tunnel or reverse proxy configuration.
7. Restore the previous access policy, if modified.
8. Verify unrelated services still work.
9. Run rollback validation checks.
10. Record rollback result in `memory/rollback/` if this were a real implementation.

## Rollback Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| RB-VAL-001 | New hostname disabled | Hostname no longer reaches service | HTTP result | Not Tested |  |
| RB-VAL-002 | Unauthenticated access denied | No unauthenticated access exists | HTTP result | Not Tested |  |
| RB-VAL-003 | Previous access config restored | Known-good policy is active | Config reference | Not Tested |  |
| RB-VAL-004 | Existing services unaffected | Existing access paths still work | Test result | Not Tested |  |
| RB-VAL-005 | Logs preserved | Evidence remains available | Log reference | Not Tested |  |

## Risks During Rollback

| Risk | Impact | Mitigation |
|---|---|---|
| Removing wrong route | Could break unrelated service | Confirm route and hostname before changes |
| Losing evidence | Incident review becomes harder | Preserve logs before rollback |
| Partial rollback | Exposure or outage may remain | Run rollback validation |
| Policy mismatch | Approved users may lose access | Restore known-good policy |

## Escalation Plan

If rollback does not restore the expected state:

1. Stop all further changes.
2. Preserve logs and screenshots.
3. Disable the affected hostname or route.
4. Notify the human owner.
5. Review access policy and route configuration manually.
6. Restore from known-good backup or configuration reference.
7. Record failed rollback details.

## Human Approval Gate

The following require human approval or confirmation:

- Starting rollback
- Running rollback commands
- Accepting rollback results
- Declaring rollback complete
