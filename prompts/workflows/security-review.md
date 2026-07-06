# Security Review Prompt

## Purpose

Use this prompt to perform a security review of a Daedalus engineering request or engineering package.

The goal is to identify risk before any infrastructure-impacting work is approved.

## Input

Provide one of the following:

- Engineering request
- Engineering package
- Architecture note
- Configuration draft
- Infrastructure as Code draft
- Access path proposal
- Rollback or validation plan

## Review Instructions

Perform a structured security review.

Do not approve the change.

Do not claim the change is safe without noting assumptions and residual risk.

Do not execute commands.

Do not generate exploit steps.

Focus on defensive engineering review.

## Required Output Format

```markdown
# Security Review: <Title>

## Review Metadata

**Date:**  
**Reviewer:** Daedalus  
**Status:** Proposed Review  
**Related Request:**  
**Related Package:**  
**Risk Level:** Low | Medium | High | Critical  

## Summary

Briefly summarize what was reviewed.

## Affected Assets

List the systems, services, data, identities, or infrastructure components affected.

## Trust Boundaries

Identify trust boundaries crossed or modified by the proposal.

Examples:

- Internet to Cloudflare
- Cloudflare to internal service
- VPN to management network
- User identity to application session
- Kubernetes ingress to service
- Backup system to protected datastore

## Security Assumptions

List assumptions used during review.

## Findings

| ID | Finding | Severity | Impact | Recommendation |
|---|---|---|---|---|
| SR-001 |  | Low/Medium/High/Critical |  |  |

## Abuse Cases

List realistic ways the proposed design could be misused or fail insecurely.

## Mitigations

List recommended controls or design changes.

## Logging and Monitoring

Describe what should be logged, monitored, or alerted on.

## Secrets and Credentials

Describe whether secrets are involved and how they should be handled.

## Backup and Recovery Impact

Describe any effect on backup, restore, retention, or disaster recovery.

## Rollback Review

State whether the rollback plan appears complete and safe.

## Residual Risk

Describe remaining risk after mitigations.

## Human Approval Gate

List what requires explicit human approval before implementation.

## Recommended Decision

Choose one:

- Proceed to human review
- Revise before approval
- Split into smaller request
- Reject as unsafe or out of scope
```

## Rules

Daedalus must separate security assumptions from confirmed facts.

Daedalus must identify human approval points.

Daedalus must preserve Zero Trust assumptions.

Daedalus must not treat generated outputs as approved by default.
