# Rollback Plan Prompt

## Purpose

Use this prompt to generate a rollback plan for proposed Daedalus engineering work.

The rollback plan must describe how a human can return the environment to a known-good state if implementation fails or causes unexpected impact.

## Input

Provide one of the following:

- Engineering request
- Engineering package
- Configuration draft
- Infrastructure as Code draft
- Architecture note
- Security review
- Validation checklist

## Instructions

Generate a structured rollback plan.

The plan must include:

- Rollback trigger
- Preconditions
- Required backups or known-good state
- Ordered rollback steps
- Rollback validation
- Failure escalation
- Human approval gate

Do not execute rollback steps.

Do not claim rollback succeeded unless a human confirms it.

## Required Output Format

```markdown
# Rollback Plan: <Title>

## Metadata

**Date:**  
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

List what must be true before rollback can be performed.

## Required Known-Good State

List required backups, snapshots, configs, versions, or references needed for rollback.

## Rollback Steps

1. 

## Rollback Validation

| ID | Check | Expected Result | Evidence | Pass/Fail | Notes |
|---|---|---|---|---|---|
| RB-VAL-001 |  |  |  |  |  |

## Risks During Rollback

| Risk | Impact | Mitigation |
|---|---|---|
|  |  |  |

## Escalation Plan

State what to do if rollback does not restore the expected state.

## Human Approval Gate

The following require human approval or confirmation:

- Starting rollback
- Running rollback commands
- Accepting rollback results
- Declaring rollback complete
```

## Rules

Daedalus must not execute rollback.

Daedalus must not assume backups exist unless confirmed.

Daedalus must document rollback limitations.

Daedalus must require human confirmation before rollback is considered complete.
