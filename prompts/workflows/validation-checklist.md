# Validation Checklist Prompt

## Purpose

Use this prompt to generate a validation checklist for a Daedalus engineering package.

The checklist must help a human verify readiness, success, failure conditions, and rollback success.

## Input

Provide one of the following:

- Engineering request
- Engineering package
- Configuration draft
- Infrastructure as Code draft
- Architecture note
- Security review

## Instructions

Generate a validation checklist.

Separate checks into:

1. Pre-change validation
2. Post-change validation
3. Negative validation
4. Rollback validation

Each validation check must include:

- Check ID
- Check description
- Expected result
- Evidence to collect
- Pass/fail field
- Notes field

Do not claim that validation has passed unless a human provides evidence.

Do not execute commands.

## Required Output Format

```markdown
# Validation Checklist: <Title>

## Metadata

**Date:**  
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
| PRE-001 |  |  |  |  |  |

## Post-Change Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| POST-001 |  |  |  |  |  |

## Negative Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| NEG-001 |  |  |  |  |  |

## Rollback Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| RBV-001 |  |  |  |  |  |

## Human Approval Gate

The following require human confirmation:

- Validation execution
- Validation pass/fail status
- Evidence acceptance
- Residual risk acceptance
```

## Rules

Daedalus must separate expected results from actual results.

Daedalus must not mark checks as passed by default.

Daedalus must require human confirmation before closing validation.
