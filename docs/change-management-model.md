# Daedalus Change Management Model

## Purpose

This document defines the change management model for Daedalus.

Daedalus is an AI-assisted infrastructure security engineering platform. It may plan, document, generate, validate, and recommend infrastructure changes, but it must not execute changes without explicit human approval.

The purpose of this model is to ensure every Daedalus-generated engineering package includes clear approval gates, validation steps, risk awareness, and rollback procedures.

## Core Principle

Daedalus plans.

The engineer approves.

Automation executes only after explicit approval.

## Change Management Objectives

Daedalus change management exists to:

- Prevent unreviewed infrastructure changes
- Preserve engineering intent
- Document assumptions and constraints
- Identify risks before implementation
- Produce validation procedures
- Produce rollback procedures
- Maintain architecture decision records
- Support repeatable engineering workflows
- Keep humans accountable for approval decisions

## Change Types

Daedalus should classify work into one of the following change types.

### Documentation Change

A documentation change modifies project notes, diagrams, runbooks, architecture documents, or decision records.

Examples:

- Updating a runbook
- Adding an architecture decision record
- Documenting VLAN design rationale
- Updating a project README

Risk level is usually low, but documentation changes should still be reviewed for accuracy.

### Planning Change

A planning change creates or modifies engineering plans, task breakdowns, design proposals, or implementation phases.

Examples:

- Creating a Vaultwarden deployment plan
- Generating ClickUp tasks
- Drafting a Kubernetes migration plan
- Writing a backup strategy

Planning changes do not modify infrastructure directly.

### Configuration Change

A configuration change modifies application, infrastructure, network, security, or system configuration.

Examples:

- Updating Traefik routing
- Modifying Kubernetes manifests
- Changing firewall rules
- Adjusting backup schedules
- Updating Ansible variables

Configuration changes require validation and rollback planning.

### Infrastructure Change

An infrastructure change creates, removes, or modifies infrastructure resources.

Examples:

- Deploying a new VM
- Creating Kubernetes namespaces
- Adding persistent volumes
- Modifying Proxmox resources
- Changing storage or backup targets

Infrastructure changes require explicit approval before execution.

### Security Change

A security change modifies access control, identity, secrets, hardening, monitoring, or exposure boundaries.

Examples:

- Changing administrative access
- Updating firewall policy
- Enabling external ingress
- Rotating secrets
- Applying CIS or STIG hardening
- Adding Rapid7 validation checks

Security changes require explicit approval, documented risk review, and rollback procedures.

## Required Change Package Sections

Every Daedalus-generated change package should include the following sections:

1. Change Summary
2. Business or Engineering Justification
3. Scope
4. Assumptions
5. Constraints
6. Affected Systems
7. Risk Assessment
8. Security Impact
9. Implementation Plan
10. Validation Plan
11. Rollback Plan
12. Human Approval Gate
13. Post-Change Documentation Updates
14. Architecture Decision Record Recommendations

## Risk Levels

Daedalus should assign a risk level to each proposed change.

### Low Risk

Low-risk changes are unlikely to impact availability, security, or data integrity.

Examples:

- Documentation updates
- Non-executing skeleton generation
- Draft task creation
- Local-only examples

### Medium Risk

Medium-risk changes may affect configuration, access paths, or operational behavior but have a clear rollback path.

Examples:

- Updating Kubernetes manifests
- Adjusting backup schedules
- Changing monitoring configuration
- Modifying internal routing

### High Risk

High-risk changes may affect availability, security boundaries, data integrity, secrets, identity, or external exposure.

Examples:

- Firewall changes
- Public ingress exposure
- Secret rotation
- Storage migration
- Proxmox cluster changes
- Production-like service deployment

High-risk changes require explicit human approval and a tested rollback plan.

## Approval Gates

Daedalus must use approval gates to prevent unreviewed execution.

### Gate 1: Planning Approval

The engineer reviews the architecture, assumptions, constraints, and proposed implementation phases.

No code or infrastructure changes occur at this gate.

### Gate 2: Artifact Approval

The engineer reviews generated artifacts such as:

- Kubernetes manifests
- Ansible playbooks
- Terraform/OpenTofu skeletons
- Configuration files
- Runbooks
- Validation scripts

No deployment occurs until the artifacts are approved.

### Gate 3: Execution Approval

The engineer explicitly approves execution of the reviewed change.

This approval must include:

- Target environment
- Change window or execution time
- Rollback readiness
- Validation method
- Responsible engineer

### Gate 4: Post-Change Review

After execution, the engineer reviews:

- Validation results
- Logs or health checks
- Monitoring status
- Backup status when applicable
- Documentation updates
- Lessons learned

## Execution Boundaries

During Phase I, Daedalus has no execution capability.

Allowed Phase I actions:

- Generate plans
- Generate documentation
- Generate skeleton code
- Generate validation checklists
- Generate rollback procedures
- Generate task breakdowns
- Generate ADR recommendations

Disallowed Phase I actions:

- Deploy infrastructure
- Modify firewall rules
- Modify DNS
- Modify Kubernetes clusters
- Modify Proxmox
- Modify PBS
- Modify secrets
- Modify production or production-like services
- Claim that a change was executed

## Validation Requirements

Every implementation plan should include validation steps.

Validation should answer:

- Did the service deploy successfully?
- Is the service reachable only through approved paths?
- Is TLS working correctly?
- Are logs and metrics available?
- Are backups configured?
- Has restore been tested or planned?
- Are secrets handled safely?
- Are access controls enforced?
- Does monitoring detect failure conditions?

## Rollback Requirements

Every implementation plan should include rollback procedures.

Rollback should answer:

- What condition triggers rollback?
- What is the last known-good state?
- What files, manifests, or configuration must be restored?
- What services must be restarted?
- What data must be preserved?
- How is rollback validated?
- What documentation must be updated after rollback?

## Documentation Requirements

Daedalus should recommend documentation updates after every change.

Potential documentation targets:

- README files
- Runbooks
- Architecture diagrams
- ADRs
- Network documentation
- Inventory records
- Backup documentation
- Security model documentation
- Lessons learned

## ADR Requirements

Daedalus should recommend an architecture decision record when a change introduces or modifies:

- Security boundaries
- Network segmentation
- Identity or access control
- Storage architecture
- Backup strategy
- Ingress or external exposure
- Platform tooling
- Automation strategy
- Monitoring architecture
- Human approval model

## Example Approval Statement

The following is an example human approval statement:

```text
I approve this change for implementation in the lab environment.
Target environment: Zero Trust Engineering Lab
Approved scope: Vaultwarden Kubernetes deployment skeleton only
Approved by: <engineer name>
Approval date: <YYYY-MM-DD>
Rollback reviewed: Yes
Validation reviewed: Yes
```

## Success Criteria

This change management model is successful when Daedalus consistently produces change packages that are:

- Reviewable
- Traceable
- Risk-aware
- Security-aware
- Validation-driven
- Rollback-ready
- Human-approved before execution

## Failure Criteria

This model fails if Daedalus:

- Skips approval gates
- Claims unexecuted work was completed
- Produces infrastructure changes without rollback plans
- Recommends unsafe exposure paths
- Generates secrets or credentials
- Treats itself as an autonomous operator
- Ignores validation
- Ignores documentation updates
