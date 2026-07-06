# Engineering Package Workflow

## Purpose

The engineering package workflow defines what Daedalus produces after an engineering request has passed readiness review.

The package is a reviewable engineering deliverable, not an automatically executed change.

## Workflow

1. Engineering request is submitted.
2. Engineering request is reviewed.
3. Missing context is resolved or assumptions are documented.
4. Daedalus generates an engineering package.
5. Human reviews the package.
6. Human approves, rejects, revises, or archives the package.
7. Approved work may be implemented manually by a human or through a separate controlled process.

## Package Status

### Proposed

The package has been generated but is not approved for use.

### Approved

A human has reviewed and approved the package.

### Rejected

A human has rejected the package.

### Superseded

A newer package or decision has replaced this package.

## Required Package Sections

Each package must include:

- Metadata
- Request summary
- Scope
- Current state
- Desired outcome
- Assumptions
- Risks
- Proposed engineering plan
- Generated artifacts
- Validation checklist
- Rollback plan
- Threat model notes
- Human approval gate
- Completion criteria
- Follow-up actions

## Human Approval

Human approval is required before:

- Running commands
- Applying configurations
- Deploying Infrastructure as Code
- Changing access control
- Changing identity or authentication behavior
- Modifying backups or retention
- Exposing services outside the lab
- Treating generated output as authoritative

## Validation

Validation must include expected results.

A validation checklist should be clear enough that another engineer can independently verify the outcome.

## Rollback

Rollback must describe:

- When rollback should happen
- What steps reverse the change
- How rollback success is validated

If rollback is not possible or not applicable, the package must state why.

## Threat Model Notes

Threat model notes should identify:

- Protected assets
- Trust boundaries
- Likely threats
- Mitigations
- Security assumptions

## Storage

Proposed engineering packages should be stored under:

```text
memory/outputs/
```

Approved decision records should be stored under:

```text
memory/decisions/
```

Architecture updates should be stored under:

```text
memory/architecture/
```

## Completion

An engineering package is complete when it is reviewable, traceable, validated, reversible where applicable, and clearly bound to a human approval gate.
