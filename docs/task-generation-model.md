# Task Generation Model

## Purpose

This document defines how Daedalus converts engineering requests and generated engineering packages into structured project-management tasks.

The goal is to make infrastructure work actionable without requiring Daedalus to directly connect to ClickUp, GitHub Projects, Jira, or any other project-management platform during Phase I.

Daedalus may generate task structures.
Daedalus may not create, update, close, assign, or execute tasks through external systems during Phase I.

## Scope

This model applies to all Daedalus-generated engineering packages that include project-management output.

It governs:

- Epic generation
- Task generation
- Subtask generation
- Milestone recommendations
- Dependency mapping
- Acceptance criteria
- Validation task creation
- Rollback task creation
- Documentation task creation
- Human approval task creation

## Phase I Boundary

During Phase I, Daedalus operates in generate-only mode.

Daedalus may produce:

- ClickUp-style task hierarchies
- Markdown task lists
- CSV-style task output
- JSON task output
- Suggested labels
- Suggested priorities
- Suggested dependencies
- Suggested owners or roles
- Acceptance criteria

Daedalus may not:

- Connect to ClickUp
- Create live tasks
- Assign tasks to users
- Change task status
- Close tasks
- Modify sprint boards
- Trigger automations
- Create production changes from task output

## Task Hierarchy

Daedalus should organize work using the following hierarchy:

```text
Project
└── Epic
    └── Task
        └── Subtask
```

For small work items, Daedalus may omit epics and produce only tasks and subtasks.

For infrastructure deployments, Daedalus should prefer epics.

## Standard Epic Categories

When generating an engineering plan, Daedalus should consider the following epic categories:

1. Requirements and Design
2. Architecture Documentation
3. Security Review
4. Infrastructure Preparation
5. Manifest or IaC Generation
6. Secrets and Access Planning
7. Deployment Planning
8. Validation and Testing
9. Backup and Restore
10. Rollback Planning
11. Monitoring and Alerting
12. Documentation and Runbooks
13. Human Approval
14. Post-Implementation Review

Not every project requires every epic.
Daedalus should include only relevant epics.

## Standard Task Fields

Each task should include:

```yaml
title: ""
description: ""
epic: ""
phase: ""
priority: "low | medium | high | critical"
status: "proposed"
owner_role: ""
dependencies: []
acceptance_criteria: []
validation_method: ""
rollback_related: true | false
approval_required: true | false
artifacts: []
```

## Priority Model

Daedalus should assign priorities using operational impact.

### Critical

Use for tasks that protect against unacceptable risk or block safe progress.

Examples:

- Define rollback plan
- Define secret handling model
- Validate backups
- Confirm TLS enforcement
- Confirm administrative access restrictions

### High

Use for tasks required before implementation can proceed.

Examples:

- Generate architecture design
- Create Kubernetes manifests
- Define persistent storage requirements
- Identify ingress and DNS requirements

### Medium

Use for tasks that improve operational maturity but do not block early review.

Examples:

- Write runbook
- Define monitoring dashboard
- Create ADR recommendations
- Create documentation index

### Low

Use for cleanup, polish, or optional improvements.

Examples:

- Improve diagrams
- Refine labels
- Add examples
- Add formatting improvements

## Dependency Rules

Daedalus must not generate implementation tasks that precede required planning tasks.

The default dependency order is:

```text
Requirements
↓
Architecture
↓
Risk Review
↓
Change Plan
↓
Artifact Generation
↓
Validation Plan
↓
Rollback Plan
↓
Human Approval
↓
Execution Readiness
```

If a task requires prior approval, Daedalus must mark it clearly.

## Required Approval Tasks

For every engineering package that proposes infrastructure changes, Daedalus should generate at least one explicit human approval task.

Example:

```yaml
title: "Approve Vaultwarden deployment plan"
description: "Review architecture, risks, validation checklist, rollback plan, and generated IaC skeletons before any deployment activity."
epic: "Human Approval"
phase: "approval"
priority: "critical"
status: "proposed"
owner_role: "Engineer"
dependencies:
  - "Complete architecture review"
  - "Complete security review"
  - "Complete rollback review"
acceptance_criteria:
  - "Architecture reviewed"
  - "Security risks accepted or mitigated"
  - "Rollback path confirmed"
  - "No secrets committed"
  - "No live execution performed before approval"
validation_method: "Manual human review"
rollback_related: true
approval_required: true
artifacts:
  - "engineering package"
  - "rollback plan"
  - "validation checklist"
```

## Validation Tasks

Every generated project should include validation tasks.

Validation tasks should answer:

- How do we know it works?
- How do we know it is secure enough for the intended environment?
- How do we know backups work?
- How do we know rollback works?
- How do we know documentation is accurate?

Example validation task:

```yaml
title: "Validate Vaultwarden ingress and TLS behavior"
description: "Confirm Vaultwarden is only reachable through the approved ingress path and requires TLS."
epic: "Validation and Testing"
phase: "validation"
priority: "critical"
status: "proposed"
owner_role: "Engineer"
dependencies:
  - "Generate Traefik ingress skeleton"
acceptance_criteria:
  - "HTTP does not expose the application directly"
  - "HTTPS endpoint presents valid certificate"
  - "Administrative interface is restricted"
  - "Ingress route matches approved architecture"
validation_method: "Manual review and controlled test after approval"
rollback_related: false
approval_required: true
artifacts:
  - "ingress manifest"
  - "validation checklist"
```

## Rollback Tasks

Any task that changes infrastructure should have a rollback-related task.

Rollback tasks should define:

- What is being rolled back
- Trigger conditions
- Required backups or snapshots
- Restore steps
- Validation after rollback
- Human approval requirement

Example rollback task:

```yaml
title: "Prepare Vaultwarden rollback procedure"
description: "Document rollback steps for application manifests, persistent storage, ingress configuration, and backup restoration."
epic: "Rollback Planning"
phase: "rollback"
priority: "critical"
status: "proposed"
owner_role: "Engineer"
dependencies:
  - "Define Vaultwarden architecture"
  - "Define backup strategy"
acceptance_criteria:
  - "Rollback trigger conditions documented"
  - "Manifest rollback path documented"
  - "Persistent data restore path documented"
  - "Ingress rollback path documented"
  - "Post-rollback validation documented"
validation_method: "Manual review before approval"
rollback_related: true
approval_required: true
artifacts:
  - "rollback plan"
  - "backup plan"
```

## Documentation Tasks

Daedalus should generate documentation tasks for any engineering package that creates or modifies architecture.

Documentation tasks may include:

- Architecture document update
- ADR creation
- Runbook creation
- Validation checklist update
- Rollback plan update
- README update
- Inventory update
- Network diagram update

Documentation is not optional for Phase I engineering packages.

## Security Task Requirements

Security tasks should be included when the project touches:

- Identity and access management
- Secrets
- TLS
- Ingress
- Firewall policy
- Network segmentation
- Backups
- Monitoring
- Logging
- Administrative interfaces
- External exposure
- Persistent data

Security tasks should be tied to specific controls or risks where possible.

## Task Output Formats

Daedalus may produce tasks in multiple formats depending on workflow needs.

### Markdown Format

Use Markdown when tasks are intended for review in Git.

```markdown
## Epic: Security Review

### Task: Review Vaultwarden administrative access model

**Priority:** Critical  
**Status:** Proposed  
**Owner Role:** Engineer  
**Approval Required:** Yes

#### Description
Review how administrative access is restricted and documented.

#### Dependencies
- Define ingress architecture
- Define authentication requirements

#### Acceptance Criteria
- Admin interface exposure reviewed
- Access restriction documented
- Risk accepted or mitigated
```

### YAML Format

Use YAML when tasks may later be converted into an API payload.

```yaml
- title: "Review Vaultwarden administrative access model"
  epic: "Security Review"
  priority: "critical"
  status: "proposed"
  owner_role: "Engineer"
  approval_required: true
  dependencies:
    - "Define ingress architecture"
    - "Define authentication requirements"
  acceptance_criteria:
    - "Admin interface exposure reviewed"
    - "Access restriction documented"
    - "Risk accepted or mitigated"
```

### CSV-Compatible Format

Use CSV-compatible tables when importing into project-management systems manually.

Required columns:

```text
Epic,Task,Description,Priority,Status,Owner Role,Dependencies,Acceptance Criteria,Approval Required
```

## ClickUp Alignment

Daedalus may generate ClickUp-style output, but Phase I does not connect to ClickUp.

Suggested mapping:

```text
Daedalus Project      → ClickUp Space or Folder
Daedalus Epic         → ClickUp List or Parent Task
Daedalus Task         → ClickUp Task
Daedalus Subtask      → ClickUp Subtask
Priority              → ClickUp Priority
Status                → ClickUp Status
Owner Role            → Assignee recommendation, not live assignment
Acceptance Criteria   → Task checklist
Dependencies          → Task relationships
Approval Required     → Label or custom field
```

## Required Labels

Daedalus may recommend labels such as:

- `phase-i`
- `planning`
- `security-review`
- `iac`
- `kubernetes`
- `ansible`
- `validation`
- `rollback`
- `human-approval`
- `documentation`
- `adr`
- `memory-candidate`

Labels are recommendations only during Phase I.

## Human Approval Boundary

Task generation does not equal authorization.

A generated task list is not approval to:

- Deploy workloads
- Modify infrastructure
- Change firewall rules
- Apply manifests
- Run Ansible
- Create secrets
- Update DNS
- Change production systems

All execution remains blocked until human approval is explicitly granted through the approved workflow.

## Review Requirements

Before a generated task set is accepted, the engineer should verify:

- Tasks map to the engineering package
- Critical risks are represented
- Validation tasks exist
- Rollback tasks exist
- Approval tasks exist
- No task assumes unauthorized execution
- No task contains secrets
- Dependencies are logical
- Acceptance criteria are measurable
- Documentation tasks are included

## Phase I Exit Criteria

This model is acceptable for Phase I when Daedalus can generate a task hierarchy that includes:

- At least one design task
- At least one security review task
- At least one IaC or manifest generation task when applicable
- At least one validation task
- At least one rollback task
- At least one documentation task
- At least one human approval task
- Clear dependencies
- Measurable acceptance criteria
- No live task-system integration

## Example Prompt Alignment

For the Vaultwarden acceptance workflow, Daedalus should generate tasks for:

- Architecture review
- Kubernetes namespace planning
- Traefik ingress design
- Persistent storage planning
- Backup and restore design
- Secrets handling design
- Monitoring design
- Manifest skeleton generation
- Ansible skeleton generation
- Validation checklist creation
- Rollback plan creation
- ADR recommendations
- Human approval

## Operating Principle

Daedalus creates task structure.
The engineer reviews task structure.
External task systems are updated only after human approval.
