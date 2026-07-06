# Daedalus Quickstart

## Purpose

This quickstart explains how to use the Daedalus repository.

## 1. Start with the Operating Manual

Read:

```text
docs/DAEDALUS-OPERATING-MANUAL.md
```

This explains what Daedalus is, how it behaves, and how the workflow operates.

## 2. Review the Project Index

Read:

```text
docs/PROJECT-INDEX.md
```

This maps the repository structure and tells you where each workflow, prompt, template, schema, and memory record lives.

## 3. Review the Workflow Map

Read:

```text
docs/WORKFLOW-MAP.md
```

This shows how engineering requests become engineering packages, security reviews, validation checklists, rollback plans, and ADRs.

## 4. Create an Engineering Request

Use:

```text
.github/ISSUE_TEMPLATE/engineering-request.md
```

or copy:

```text
examples/engineering-request.md
```

A good request should include:

- Summary
- Target system
- Current state
- Desired outcome
- Constraints
- Risk level
- Requested outputs
- Human approval acknowledgement

## 5. Run a Readiness Review

Use:

```text
prompts/workflows/engineering-request-review.md
```

The readiness review determines whether the request is:

- Ready
- Ready with assumptions
- Not ready

## 6. Generate an Engineering Package

Use:

```text
prompts/output-contracts/engineering-package.md
templates/engineering-package-template.md
```

Engineering packages should include:

- Scope
- Assumptions
- Risks
- Proposed plan
- Generated artifacts
- Validation
- Rollback
- Security notes
- Human approval gate

## 7. Perform Security Review

Use:

```text
prompts/workflows/security-review.md
templates/security-review-template.md
```

Security review is required when work affects:

- Access
- Identity
- Public exposure
- Secrets
- Backups
- Trust boundaries
- Privileged automation
- Infrastructure as Code

## 8. Generate Validation and Rollback

Use:

```text
prompts/workflows/validation-checklist.md
templates/validation-checklist-template.md
prompts/workflows/rollback-plan.md
templates/rollback-plan-template.md
```

Validation should include:

- Pre-change validation
- Post-change validation
- Negative validation
- Rollback validation

Rollback should include:

- Trigger
- Preconditions
- Known-good state
- Ordered steps
- Validation
- Escalation plan

## 9. Create ADRs for Major Decisions

Use:

```text
prompts/workflows/adr-generation.md
templates/adr-template.md
```

Store ADRs in:

```text
memory/decisions/
```

## 10. Review the End-to-End Example

Read:

```text
examples/end-to-end/internal-docs-service/
```

This demonstrates the full flow:

```text
Engineering request
  -> Readiness review
  -> Engineering package
  -> Security review
  -> Validation checklist
  -> Rollback plan
  -> ADR
```

## 11. Commit Changes

After adding or editing artifacts:

```powershell
git status
git add .
git commit -m "<clear commit message>"
git push origin main
git status
```

Final status should show:

```text
nothing to commit, working tree clean
```

## Safety Reminder

Daedalus outputs are proposed by default.

Do not run generated commands, apply generated configurations, or deploy generated IaC without human review and approval.
