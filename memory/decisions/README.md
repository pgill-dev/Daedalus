# Architecture Decision Records

This directory stores Daedalus Architecture Decision Records.

## Purpose

Architecture Decision Records preserve the reasoning behind important technical and operational decisions.

ADRs help Daedalus and human reviewers understand why a decision was made, what alternatives were considered, and what consequences were accepted.

## Rules

Daedalus may propose ADRs.

Daedalus must not mark an ADR as approved without human approval.

Daedalus must not overwrite approved ADRs without creating a new superseding ADR.

Daedalus must preserve historical decisions.

Daedalus must reference related engineering packages, validation records, rollback plans, and security reviews when applicable.

## Status Values

Use one of the following:

- Proposed
- Approved
- Superseded
- Deprecated
- Rejected

## Naming Convention

Use four-digit numbering and a short descriptive name:

```text
0001-project-memory.md
0002-engineering-request-workflow.md
0003-iac-generation-guardrails.md
```

## Supersession

If a decision changes:

1. Create a new ADR.
2. Mark the old ADR as `Superseded`.
3. Add a `Superseded by` reference in the old ADR.
4. Add a `Supersedes` reference in the new ADR.

## Recommended Review Checklist

Before approving an ADR, confirm:

- [ ] Decision is clearly stated
- [ ] Context is documented
- [ ] Alternatives are considered
- [ ] Rationale is documented
- [ ] Consequences are listed
- [ ] Security impact is considered
- [ ] Validation impact is considered
- [ ] Rollback impact is considered
- [ ] Human approval fields are complete
