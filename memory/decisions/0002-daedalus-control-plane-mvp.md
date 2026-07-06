# ADR-0002: Use Daedalus as the Lab Engineering Control Plane

## Status

Proposed

## Date

2026-07-06

## Decision Owner

Human reviewer or owner.

## Related Records

- Engineering Request: memory/plans/2026-07-06-daedalus-lab-control-plane-engineering-request.md
- Engineering Package: memory/outputs/2026-07-06-daedalus-lab-control-plane-engineering-package.md
- Security Review: memory/threat-models/2026-07-06-daedalus-lab-control-plane-security-review.md
- Validation Checklist: memory/validation/2026-07-06-daedalus-lab-control-plane-validation-checklist.md
- Rollback Plan: memory/rollback/2026-07-06-daedalus-lab-control-plane-rollback-plan.md
- Supersedes:
- Superseded by:

## Context

The self-hosted Zero Trust lab needs a consistent engineering workflow.

Daedalus now contains the baseline operating model, project memory, templates, schemas, validation tooling, GitHub workflows, and CLI commands needed to support engineering planning.

A decision is needed on whether Daedalus should be treated as the lab engineering control plane for future planning and documentation work.

## Decision

Use Daedalus as the lab engineering control plane for proposed infrastructure work.

Future meaningful lab changes should start with a request, move through engineering package generation, include validation and rollback when applicable, and record decisions in project memory.

Daedalus will not execute infrastructure changes automatically.

## Options Considered

### Option 1: Continue Ad Hoc Lab Changes

**Summary:** Continue making lab changes without a structured Daedalus workflow.

**Pros:**

- Fastest in the moment
- Lowest process overhead

**Cons:**

- Decisions are easy to lose
- Rollback may be skipped
- Security review may be inconsistent
- Harder to show engineering discipline

### Option 2: Use Daedalus for Documentation Only

**Summary:** Use Daedalus only as a documentation repository.

**Pros:**

- Simple
- Low operational risk
- Useful for portfolio review

**Cons:**

- Does not fully support engineering workflow
- Less useful for real lab operations
- CLI and validation tooling are underused

### Option 3: Use Daedalus as Engineering Control Plane

**Summary:** Use Daedalus as the structured intake, planning, review, validation, rollback, and memory system for the lab.

**Pros:**

- Strong engineering discipline
- Human approval remains central
- Better decision history
- Better validation and rollback culture
- Stronger portfolio demonstration

**Cons:**

- Requires consistent use
- Adds process overhead
- Project memory must be maintained

## Rationale

Using Daedalus as the engineering control plane provides the strongest balance between usefulness, safety, and professional engineering discipline.

It keeps the human in control while ensuring future lab work is planned, reviewed, validated, and documented.

## Consequences

### Positive Consequences

- Lab work becomes more repeatable
- Decisions are preserved
- Validation and rollback become default expectations
- Security review becomes part of the process
- The project better demonstrates platform engineering maturity

### Negative Consequences

- More up-front documentation is required
- Small changes may feel slower
- Memory records must be maintained

### Neutral Consequences

- Implementation remains manual
- Future web interface or local LLM integration can build on this model
- CLI commands may expand over time

## Security Considerations

- Daedalus must not include plaintext secrets.
- Proposed artifacts must not be treated as approved.
- Approval gates must remain visible.
- Public exposure, identity, backup, and privileged automation changes require security review.
- Sensitive lab details should be minimized.

## Validation Impact

Validation should include:

- Repository validation
- Schema validation
- CLI tests
- GitHub Actions status
- Artifact status review
- Approval gate review

## Rollback Impact

Rollback can be performed by reverting the package commit, marking this ADR as rejected or superseded, and restoring the previous operating model.

## Human Approval

**Approval required:** Yes  
**Approved by:**  
**Approval date:**  
**Approval notes:**  

## Follow-Up Actions

- Complete Step 25 MVP closeout.
- Tag the repository after MVP baseline is complete.
- Use Daedalus for the next real lab request.
