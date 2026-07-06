# Daedalus Workflow Map

## Purpose

This document shows how Daedalus workflows connect.

## High-Level Flow

```text
Engineering Request
  -> Request Readiness Review
  -> Engineering Package
  -> Security Review
  -> Validation Checklist
  -> Rollback Plan
  -> ADR if decision is significant
  -> Human Approval
  -> Manual Implementation
  -> Evidence and Memory Update
```

## Workflow Relationships

| Stage | Input | Output | Stored In |
|---|---|---|---|
| Engineering request | Human need | Request issue or markdown | GitHub issue or `examples/` |
| Readiness review | Engineering request | Readiness assessment | Request comments or `memory/plans/` |
| Engineering package | Accepted request | Proposed package | `memory/outputs/` |
| Security review | Package or design | Security findings | `memory/threat-models/` |
| Validation checklist | Package or config | Validation plan | `memory/validation/` |
| Rollback plan | Package or config | Recovery plan | `memory/rollback/` |
| ADR | Significant decision | Decision record | `memory/decisions/` |
| Memory update | Final result | Persistent context | `memory/` |

## Request to Package Flow

```text
.github/ISSUE_TEMPLATE/engineering-request.md
  -> prompts/workflows/engineering-request-review.md
  -> prompts/output-contracts/engineering-package.md
  -> templates/engineering-package-template.md
```

## Security Review Flow

```text
Engineering package
  -> prompts/workflows/security-review.md
  -> templates/security-review-template.md
  -> memory/threat-models/
```

## Validation Flow

```text
Engineering package
  -> prompts/workflows/validation-checklist.md
  -> templates/validation-checklist-template.md
  -> memory/validation/
```

## Rollback Flow

```text
Engineering package
  -> prompts/workflows/rollback-plan.md
  -> templates/rollback-plan-template.md
  -> memory/rollback/
```

## IaC Flow

```text
Engineering package
  -> docs/workflows/iac-generation-guardrails.md
  -> prompts/workflows/iac-generation.md
  -> prompts/output-contracts/iac-package.md
  -> templates/iac-package-template.md
  -> memory/outputs/
```

## ADR Flow

```text
Significant decision
  -> docs/workflows/adr-workflow.md
  -> prompts/workflows/adr-generation.md
  -> templates/adr-template.md
  -> memory/decisions/
```

## Approval Gates

Human approval is required between proposed output and implementation.

```text
Proposed artifact
  -> Human review
  -> Approved / Rejected / Superseded
```

## Failure Flow

If validation fails:

```text
Failed validation
  -> Stop further changes
  -> Preserve evidence
  -> Execute approved rollback manually
  -> Validate rollback
  -> Record results
  -> Update memory
```

## Decision Flow

If a design choice affects architecture, access, identity, recovery, exposure, or long-term operations:

```text
Decision identified
  -> Draft ADR
  -> Human review
  -> Approve or reject
  -> Reference ADR in future packages
```
