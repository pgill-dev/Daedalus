# Validation Checklist: Internal Documentation Service Behind Identity-Aware Access

## Metadata

**Date:** 2026-07-06  
**Author:** Daedalus  
**Status:** Proposed  
**Related Request:** 01-engineering-request.md  
**Related Package:** 03-engineering-package.md  
**Risk Level:** High  

## Summary

This checklist validates that the internal documentation service is reachable only through the approved identity-aware access path and that rollback can restore a safe state.

## Pre-Change Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| PRE-001 | Confirm approved implementation window | Human owner confirms timing | Approval note | Not Tested |  |
| PRE-002 | Confirm known-good access config exists | Current access policy is backed up or documented | Config reference | Not Tested |  |
| PRE-003 | Confirm target service host | Internal host and port are identified | Hostname/IP note | Not Tested |  |
| PRE-004 | Confirm approved users or groups | Approved allow list is documented | Group/user list | Not Tested |  |
| PRE-005 | Confirm no plaintext secrets in proposed files | No credentials are present | Review note or scan result | Not Tested |  |

## Post-Change Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| POST-001 | Confirm service health | Service responds through approved path | Screenshot or curl output | Not Tested |  |
| POST-002 | Confirm approved user access | Approved user can reach the service | Screenshot or access log | Not Tested |  |
| POST-003 | Confirm access logs | Successful access is logged | Log excerpt | Not Tested |  |
| POST-004 | Confirm service target | Hostname routes to correct internal service | Config and test evidence | Not Tested |  |
| POST-005 | Confirm documentation content review | No secrets or sensitive content are published | Review note | Not Tested |  |

## Negative Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| NEG-001 | Test unauthenticated access | Access is denied | Screenshot or HTTP result | Not Tested |  |
| NEG-002 | Test unauthorized authenticated user | Access is denied | Access log or screenshot | Not Tested |  |
| NEG-003 | Test direct public access bypass | Service is not reachable outside approved path | Network test result | Not Tested |  |
| NEG-004 | Test unknown route | Unknown hostname does not expose service | HTTP result | Not Tested |  |

## Rollback Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| RBV-001 | Confirm route disabled | New hostname no longer reaches service | HTTP result | Not Tested |  |
| RBV-002 | Confirm service stopped or isolated | Documentation service is not reachable unintentionally | Service status | Not Tested |  |
| RBV-003 | Confirm previous access config restored | Known-good config is active | Config reference | Not Tested |  |
| RBV-004 | Confirm logs preserved | Rollback evidence remains available | Log reference | Not Tested |  |

## Human Approval Gate

The following require human confirmation:

- Validation execution
- Validation pass/fail status
- Evidence acceptance
- Residual risk acceptance
