# Human Approval Workflow

## Purpose

This workflow defines how Daedalus-generated engineering work moves from draft output to approved planning baseline.

Daedalus is an engineering copilot. It may generate architecture, documentation, skeleton code, validation steps, rollback procedures, and task breakdowns. It may not approve its own output or execute infrastructure changes without a human decision point.

This workflow exists to prevent generated plans from becoming operational changes without review.

## Scope

This workflow applies to all Daedalus-generated engineering packages, including:

- Architecture plans
- Infrastructure-as-Code skeletons
- Kubernetes manifests
- Ansible skeletons
- Change plans
- Rollback procedures
- Validation checklists
- ADR recommendations
- ClickUp-style task breakdowns
- Memory updates
- Security reviews
- Threat models

## Approval Principle

Daedalus may recommend.

The engineer approves.

Execution occurs only after approval.

## Workflow Stages

```text
User Request
    ↓
Daedalus Generated Engineering Package
    ↓
Human Review
    ↓
Validation Checklist
    ↓
Risk Review
    ↓
Rollback Review
    ↓
Approval Decision
    ↓
Approved Planning Baseline
    ↓
Future Execution Workflow
```

## Stage 1 — User Request

The workflow begins when the engineer submits a request such as:

```text
Design a production-style Vaultwarden deployment for my Zero Trust lab.
```

The request should describe the desired system, constraints, target environment, required technologies, and expected outputs.

If the request is incomplete, Daedalus should make reasonable assumptions and list them clearly.

## Stage 2 — Daedalus Generation

Daedalus produces an engineering package using the active workflow contract and output contract.

The generated package should include:

- Requirement interpretation
- Assumptions
- Constraints
- Proposed architecture
- Security considerations
- Threat model
- Implementation phases
- Generated skeletons
- Validation checklist
- Rollback plan
- Task breakdown
- ADR recommendations
- Human approval gates

Daedalus must clearly mark the package as generated and not yet approved.

## Stage 3 — Human Review

The engineer reviews the package for technical correctness, operational fit, and security risk.

Review should answer:

- Does the architecture match the requested objective?
- Are assumptions clearly stated?
- Are risks visible?
- Are dependencies identified?
- Are generated skeletons safe and reviewable?
- Are validation steps specific?
- Is rollback realistic?
- Are approval gates present?
- Does the output avoid storing or exposing secrets?
- Does the plan avoid live execution?

The review may result in approval, revision, rejection, or deferral.

## Stage 4 — Validation Checklist Review

The generated validation checklist must be reviewed before the package can be approved.

A valid checklist should include:

- Pre-change validation
- Configuration validation
- Connectivity validation
- Security validation
- Backup validation
- Restore validation
- Monitoring validation
- Access-control validation
- Failure-mode validation
- Post-change validation

The checklist must be specific enough for an engineer to run without guessing.

## Stage 5 — Risk Review

Risk review determines whether the proposed design introduces unacceptable operational or security exposure.

Daedalus-generated risk analysis should identify:

- Security risks
- Availability risks
- Data-loss risks
- Misconfiguration risks
- Identity and access risks
- Network exposure risks
- Secrets-management risks
- Backup and recovery risks
- Monitoring gaps
- Operational complexity

Risks should include mitigations or documented tradeoffs.

## Stage 6 — Rollback Review

The rollback plan must be reviewed before approval.

A valid rollback plan should include:

- Rollback trigger conditions
- Required backups or snapshots
- Restore sequence
- DNS or ingress rollback steps
- Storage rollback considerations
- Secret rotation considerations
- Verification after rollback
- Known rollback limitations

If rollback is incomplete, the package should not be approved.

## Stage 7 — Approval Decision

The engineer chooses one of the following outcomes.

### Approved

The package is accepted as a planning baseline.

Approved output may be:

- Committed to Git
- Converted into tasks
- Used to generate ADRs
- Used to build implementation branches
- Used as the baseline for future automation

### Approved with Conditions

The package is acceptable only after specific changes are made.

Conditions should be documented before work continues.

Examples:

- Replace assumed storage class with actual lab storage class
- Add backup encryption details
- Add restore testing
- Add network policy skeletons
- Add monitoring alerts

### Revision Required

The package needs meaningful correction before it can become a baseline.

Reasons may include:

- Missing rollback plan
- Vague validation steps
- Incorrect architecture
- Unsafe exposure
- Missing security controls
- Missing human approval gates

### Rejected

The package is not suitable for the environment or violates project boundaries.

Reasons may include:

- Attempts autonomous execution
- Stores secrets
- Produces unsafe configuration
- Ignores Zero Trust segmentation
- Assumes live access without approval

### Deferred

The package is not rejected, but work should pause.

Reasons may include:

- Missing lab prerequisites
- Hardware not ready
- Network design undecided
- WGU or work priorities take precedence
- Integration phase not yet reached

## Approval Record

Every approved package should include an approval record.

Recommended format:

```markdown
## Approval Record

- Status: Draft | Approved | Approved with Conditions | Revision Required | Rejected | Deferred
- Reviewer: <human reviewer>
- Review Date: <YYYY-MM-DD>
- Related ADRs:
  - <ADR number or recommendation>
- Conditions:
  - <condition if applicable>
- Notes:
  - <review notes>
```

## Human Approval Gates

Daedalus outputs should include approval gates at these points:

1. Before accepting architecture as baseline
2. Before creating implementation tasks
3. Before generating execution-ready automation
4. Before applying infrastructure changes
5. Before modifying DNS, ingress, firewall, or identity controls
6. Before storing memory as authoritative project context
7. Before marking a package complete

## Non-Executable Phase I Boundary

During Phase I, Daedalus must not:

- Execute infrastructure changes
- Apply Kubernetes manifests
- Run Ansible playbooks
- Modify Proxmox
- Modify PBS
- Modify Rapid7
- Modify GitHub or Gitea through API automation
- Modify ClickUp through API automation
- Modify DNS or firewall rules
- Store secrets
- Generate production credentials
- Claim work has been deployed

Phase I output is limited to planning, generation, documentation, validation design, rollback design, and review support.

## Relationship to Change Management

This workflow supports the Daedalus change-management model.

The change-management model defines the overall control boundary. This workflow defines how a generated package is reviewed and approved before it becomes an engineering baseline.

## Relationship to ADRs

When a package introduces an architectural decision, Daedalus should recommend one or more ADRs.

Examples:

- Select Kubernetes as deployment target
- Use Traefik as ingress controller
- Require encrypted backups
- Require restricted administrative access
- Keep Daedalus read-only during Phase III integrations

Recommended ADRs are not authoritative until reviewed and committed by the engineer.

## Relationship to Memory

Daedalus may recommend memory updates based on approved outputs.

Memory updates should not become authoritative unless:

- The engineering package is approved
- The memory entry is specific
- The memory entry does not contain secrets
- The memory entry references source documentation or ADRs
- The engineer accepts the memory update

## Phase I Success Criteria

This workflow is successful when every generated engineering package can be classified as one of the following:

- Draft
- Approved
- Approved with Conditions
- Revision Required
- Rejected
- Deferred

A package should never silently become approved.

## Operating Rule

If approval status is unclear, the package is not approved.

