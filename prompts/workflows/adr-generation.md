# ADR Generation Prompt

## Purpose

Use this prompt to generate an Architecture Decision Record for Daedalus.

ADRs should capture important engineering decisions, their context, options considered, tradeoffs, consequences, and approval status.

## Input

Provide one or more of the following:

- Engineering request
- Engineering package
- Security review
- Architecture note
- Existing decision
- Implementation plan
- Human decision statement

## Instructions

Generate a proposed ADR.

Do not mark the ADR as approved unless the human explicitly states that the decision is approved.

Separate facts from assumptions.

Document options considered.

Document consequences.

Document security, validation, and rollback impact.

## Required Output Format

```markdown
# ADR-<Number>: <Title>

## Status

Proposed | Approved | Superseded | Deprecated | Rejected

## Date

YYYY-MM-DD

## Decision Owner

Human reviewer or owner.

## Related Records

- Engineering Request:
- Engineering Package:
- Security Review:
- Validation Checklist:
- Rollback Plan:
- Supersedes:
- Superseded by:

## Context

Describe the situation, problem, constraint, or opportunity that requires a decision.

## Decision

State the decision clearly.

## Options Considered

### Option 1: <Name>

**Summary:**  
**Pros:**  
**Cons:**  

### Option 2: <Name>

**Summary:**  
**Pros:**  
**Cons:**  

## Rationale

Explain why the chosen option was selected.

## Consequences

### Positive Consequences

- 

### Negative Consequences

- 

### Neutral Consequences

- 

## Security Considerations

Describe impact to access, identity, secrets, trust boundaries, exposure, logging, monitoring, and backups.

## Validation Impact

Describe how the decision should be validated.

## Rollback Impact

Describe whether the decision can be reversed and what rollback would require.

## Human Approval

**Approval required:** Yes | No  
**Approved by:**  
**Approval date:**  
**Approval notes:**  

## Follow-Up Actions

- 
```

## Rules

Daedalus may draft ADRs.

Daedalus must not approve ADRs by default.

Daedalus must not delete old ADRs.

Daedalus must mark replaced decisions as superseded instead of overwriting them.

Daedalus must preserve reasoning, not just the final answer.
