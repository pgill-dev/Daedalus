# Engineering Request Workflow

## Purpose

The engineering request workflow defines how work enters Daedalus.

Daedalus should not produce infrastructure-impacting plans, configurations, IaC, validation procedures, rollback plans, or threat models without a clear request and a human approval checkpoint.

## Workflow Summary

1. A human submits an engineering request.
2. Daedalus reviews the request for readiness.
3. Daedalus identifies scope, risk, assumptions, and missing context.
4. A human clarifies or approves the request scope.
5. Daedalus generates the requested engineering package.
6. A human reviews the generated package.
7. A human decides whether to implement, revise, reject, or archive the output.

## Request Intake

Engineering requests should include:

- Request summary
- Request type
- Target system or component
- Current state
- Desired outcome
- Constraints
- Risk level
- Requested outputs
- Acceptance criteria
- Human approval acknowledgement

## Risk Levels

### Low

Documentation, notes, diagrams, summaries, or planning-only work.

Examples:

- Write a README
- Draft an architecture note
- Summarize an ADR
- Create a validation checklist for review

### Medium

Proposed configuration or Infrastructure as Code that is not automatically applied.

Examples:

- Draft an Ansible playbook
- Create a Kubernetes manifest
- Write a Terraform/OpenTofu module proposal
- Generate a service configuration template

### High

Work that may affect live infrastructure if applied by a human.

Examples:

- Network path changes
- Firewall rule proposals
- Reverse proxy changes
- Authentication or access changes
- Backup configuration changes

### Critical

Work affecting security boundaries, identity, recovery, secrets, or public exposure.

Examples:

- Identity provider changes
- Cloudflare Access policy changes
- Public tunnel exposure
- Backup deletion or retention changes
- Secrets handling
- Privileged automation

## Human Approval Gates

Human approval is required before:

- Applying generated configurations
- Running generated commands
- Deploying generated IaC
- Changing access controls
- Changing identity or authentication systems
- Modifying backup or recovery systems
- Exposing services outside the lab
- Marking a proposal as approved

## Daedalus Output Types

Daedalus may generate:

- Engineering plans
- Architecture notes
- ADRs
- IaC drafts
- Configuration drafts
- Validation checklists
- Rollback plans
- Threat models
- Documentation updates
- Final implementation packages

## Not Allowed

Daedalus must not:

- Execute infrastructure changes automatically
- Claim implementation occurred without human confirmation
- Bypass approval gates
- Hide assumptions
- Overwrite project memory without approval
- Treat generated output as approved by default

## Completion Criteria

An engineering request is complete when:

- The requested outputs are generated
- Risks are documented
- Assumptions are stated
- Validation steps are included when applicable
- Rollback steps are included when applicable
- Human approval points are clearly identified
- The request is committed to the repository or closed with notes
