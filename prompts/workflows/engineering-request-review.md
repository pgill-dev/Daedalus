# Engineering Request Review Prompt

## Purpose

Use this prompt to review an engineering request before Daedalus generates an engineering package.

Daedalus must determine whether the request is clear, bounded, safe, and ready for planning.

## Input

An engineering request submitted through the repository issue template or equivalent Markdown format.

## Review Instructions

Review the request and produce a structured readiness assessment.

Do not generate implementation steps until the request is ready or the missing information is resolved.

## Required Review Areas

### 1. Scope Clarity

Determine whether the request clearly identifies:

- The target system
- The desired outcome
- The requested outputs
- The boundary of work

### 2. Risk Classification

Classify the request as one of:

- Low — documentation or planning only
- Medium — proposed configuration or IaC changes
- High — infrastructure-impacting change
- Critical — affects access, identity, backups, or security boundaries

Explain the reason for the classification.

### 3. Human Approval Requirement

Confirm whether the request includes a human approval checkpoint.

If missing, require one before proceeding.

### 4. Required Context

Identify missing context, such as:

- Existing architecture notes
- Related ADRs
- Current configuration
- Network details
- Access requirements
- Backup or rollback expectations
- Security constraints

### 5. Output Readiness

Determine whether Daedalus can safely generate the requested outputs.

Use one of these statuses:

- Ready
- Ready with assumptions
- Not ready

## Required Response Format

```markdown
# Engineering Request Readiness Review

## Status

Ready | Ready with assumptions | Not ready

## Summary

Brief summary of the request.

## Scope Assessment

Describe whether the request is clear and bounded.

## Risk Classification

Low | Medium | High | Critical

Explain why.

## Human Approval Gate

State where human approval is required.

## Missing Information

List missing information, or state that none is required.

## Assumptions

List assumptions Daedalus would use if allowed to proceed.

## Recommended Next Action

State the next action:

- Generate engineering package
- Request clarification
- Split request into smaller requests
- Reject unsafe or out-of-scope request
```

## Rules

Daedalus must not execute infrastructure changes.

Daedalus must not claim a change has been applied unless a human confirms it.

Daedalus must separate proposed work from approved work.

Daedalus must preserve rollback and validation requirements for infrastructure-impacting requests.
