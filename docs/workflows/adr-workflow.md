# Architecture Decision Record Workflow

## Purpose

The Architecture Decision Record workflow defines how Daedalus records major engineering decisions.

Architecture Decision Records, or ADRs, preserve the reason behind technical choices so future work can reference approved decisions instead of re-litigating the same design questions.

## When to Create an ADR

Create an ADR when a decision affects:

- System architecture
- Security boundaries
- Identity or access control
- Public exposure
- Backup or recovery strategy
- Infrastructure as Code design
- Platform selection
- Network segmentation
- Data flow
- Operational process
- Long-term maintainability
- Human approval model

## When an ADR Is Not Required

An ADR is usually not required for:

- Small wording changes
- Formatting updates
- Temporary notes
- Minor documentation cleanup
- Non-functional file organization
- Experimental drafts that are not adopted

## ADR Statuses

### Proposed

The decision is drafted but not approved.

### Approved

A human has reviewed and approved the decision.

### Superseded

A newer ADR replaces this decision.

### Deprecated

The decision is no longer recommended but may still exist historically.

### Rejected

The decision was considered and rejected.

## Workflow Summary

1. Identify a decision that needs to be recorded.
2. Draft an ADR using the ADR template.
3. Document context, options, decision, and consequences.
4. Assign a status.
5. Human reviews the ADR.
6. Approved ADRs are committed to `memory/decisions/`.
7. Future Daedalus work references relevant ADRs.

## Required ADR Sections

Each ADR must include:

- Title
- Status
- Date
- Decision owner
- Context
- Decision
- Options considered
- Consequences
- Security considerations
- Validation impact
- Rollback impact
- Human approval
- Related records

## ADR Numbering

Use four-digit numbering:

```text
0001-project-memory.md
0002-engineering-request-workflow.md
0003-iac-generation-guardrails.md
```

Do not reuse ADR numbers.

If an ADR is superseded, create a new ADR and reference the old one.

## Storage Location

ADRs are stored in:

```text
memory/decisions/
```

## Human Approval

Daedalus may propose ADRs.

Daedalus must not mark an ADR as approved unless a human approves it.

Daedalus must not silently overwrite an approved ADR.

Daedalus must preserve historical decisions even when superseded.

## Completion Criteria

An ADR is complete when:

- The decision is clearly stated
- Context is documented
- Alternatives are listed
- Consequences are described
- Security impact is considered
- Validation and rollback impact are considered
- Approval status is clear
- Related records are referenced
