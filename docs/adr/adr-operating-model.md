# ADR Operating Model

## Purpose

Architecture Decision Records (ADRs) preserve the engineering reasoning behind Daedalus decisions.

Daedalus should not only generate architecture, code skeletons, validation plans, and rollback procedures. It should also identify meaningful decisions that need to be recorded so future work can explain why the lab was built a certain way.

The ADR operating model defines when ADRs are created, how they are structured, how they are reviewed, and how they relate to Daedalus memory.

## Core Principle

Daedalus may recommend ADRs.

The engineer approves ADRs.

Approved ADRs become durable project memory.

## ADR Goals

ADRs should help answer questions such as:

- Why was this architecture chosen?
- What alternatives were considered?
- What risks were accepted?
- What assumptions existed at the time?
- What decision would need to change if the environment changes?
- What systems or workflows depend on this decision?

## ADR Non-Goals

ADRs are not:

- General documentation
- Runbooks
- Meeting notes
- Random memory entries
- Task lists
- Implementation logs
- Secret stores
- Replacement for approval gates

An ADR should capture an important decision, not every small action.

## When Daedalus Should Recommend an ADR

Daedalus should recommend an ADR when a request includes or produces a decision involving:

- Network segmentation
- Authentication or authorization model
- Secrets management
- Backup and restore design
- Monitoring architecture
- Ingress or exposure model
- High availability design
- Storage backend selection
- Kubernetes deployment pattern
- Proxmox or PBS architecture
- Tool selection
- Security control selection
- Risk acceptance
- Major integration boundaries
- Human approval or execution boundaries

## When Daedalus Should Not Recommend an ADR

Daedalus should avoid ADRs for:

- Minor wording changes
- Formatting changes
- Temporary experiments
- One-off commands
- Unapproved assumptions
- Generated credentials
- Reversible low-impact changes
- Draft ideas that have not been reviewed

## ADR File Location

Approved ADRs should live here:

```text
docs/adr/
```

Recommended naming format:

```text
NNNN-short-decision-name.md
```

Example:

```text
docs/adr/0004-use-human-approval-gates.md
```

## ADR Numbering

ADR numbers should be sequential.

Existing ADRs should not be renumbered after they are merged.

If an ADR is replaced or superseded, create a new ADR and link the older ADR as superseded.

## ADR Status Values

Each ADR should use one of the following statuses:

| Status | Meaning |
|---|---|
| Proposed | Daedalus or the engineer has proposed the decision but it has not been approved |
| Accepted | The decision is approved and should be treated as authoritative |
| Superseded | A newer ADR replaces this decision |
| Deprecated | The decision is no longer preferred but may still describe existing state |
| Rejected | The decision was considered and intentionally not adopted |

## Required ADR Structure

Each ADR should use this structure:

```markdown
# ADR NNNN: Decision Title

## Status

Proposed | Accepted | Superseded | Deprecated | Rejected

## Date

YYYY-MM-DD

## Context

Describe the problem, environment, assumptions, and constraints that led to the decision.

## Decision

State the decision clearly.

## Alternatives Considered

List reasonable alternatives and why they were not selected.

## Consequences

Describe the positive and negative effects of the decision.

## Risks

Identify operational, security, availability, cost, complexity, and maintenance risks.

## Validation Requirements

Describe how the decision should be validated.

## Rollback or Reversal

Describe what would be required to undo or replace the decision.

## Related Artifacts

Link related docs, prompts, runbooks, templates, generated packages, or previous ADRs.
```

## Daedalus ADR Recommendation Format

When Daedalus recommends ADRs inside an engineering package, it should include:

```markdown
## Recommended ADRs

### ADR Candidate: <title>

- Reason: <why this decision needs a record>
- Proposed status: Proposed
- Related decision area: <network/security/storage/etc.>
- Suggested file name: docs/adr/NNNN-short-title.md
- Human approval required: Yes
```

Daedalus should not mark an ADR as accepted unless the engineer explicitly approves it.

## Relationship to Engineering Memory

Approved ADRs are one of the strongest forms of Daedalus memory.

Daedalus may use accepted ADRs to answer future questions such as:

- Why is a VLAN isolated?
- Why is a service exposed only through Traefik?
- Why are integrations read-only in Phase I?
- Why does execution require human approval?

Daedalus should prefer accepted ADRs over conversational memory when explaining design rationale.

## Memory Authority Levels

| Source | Authority Level |
|---|---|
| Accepted ADR | High |
| Approved runbook | High |
| Project charter | High |
| Security model | High |
| Generated example | Medium |
| Proposed ADR | Medium-low |
| Uncommitted notes | Low |
| Chat-only context | Low |

If memory conflicts with an accepted ADR, the ADR wins until it is superseded.

## ADR Review Rules

Before an ADR is accepted, the engineer should verify:

- The context is accurate
- The decision is clear
- The alternatives are reasonable
- Risks are not hidden
- Consequences are realistic
- Validation requirements are testable
- Rollback or reversal is described
- The ADR does not contain secrets
- The ADR does not claim work was completed if it was only planned

## Human Approval Boundary

Daedalus may:

- Identify ADR candidates
- Draft ADRs
- Recommend decision records
- Link ADRs to engineering packages
- Explain accepted ADRs
- Flag contradictions between new plans and existing ADRs

Daedalus may not:

- Accept ADRs without engineer approval
- Supersede ADRs without engineer approval
- Hide alternatives
- Store secrets in ADRs
- Treat draft ADRs as authoritative
- Execute infrastructure changes based only on an ADR

## ADR Lifecycle

```text
Engineering request
    ↓
Daedalus identifies decision points
    ↓
Daedalus recommends ADR candidates
    ↓
Engineer reviews ADR candidates
    ↓
Engineer approves or rejects ADRs
    ↓
Accepted ADRs are committed to Git
    ↓
Daedalus can use accepted ADRs as durable memory
```

## Phase I Requirements

During Phase I, Daedalus should:

- Recommend ADR candidates inside generated engineering packages
- Use existing ADRs as project context when available
- Avoid treating unapproved recommendations as accepted design
- Keep ADRs in Markdown
- Keep ADRs reviewable in Git
- Require human approval before decisions become authoritative

## Phase I Exit Criteria

This model is successful when Daedalus can generate an engineering package that includes:

- Clear decision points
- ADR candidate recommendations
- Suggested ADR file names
- Rationale for each ADR
- Human approval requirement
- No secrets
- No false claims of execution

## Example ADR Candidates for Vaultwarden

A Vaultwarden engineering package may recommend ADRs such as:

```text
ADR Candidate: Use Traefik as the ingress controller for Vaultwarden
ADR Candidate: Require encrypted backups before production use
ADR Candidate: Restrict administrative access to management network or approved identity path
ADR Candidate: Keep Phase I deployment generation offline until human approval gates exist
```

## Operating Rule

If Daedalus cannot explain why a major design choice was made, the decision probably needs an ADR.
