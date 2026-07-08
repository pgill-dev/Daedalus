# Daedalus Roadmap

## Phase I — Engineering Brain

### Objective

Create the reasoning engine and structured engineering output process.

### Deliverables

- Local LLM runtime
- System prompt
- Prompt library
- Engineering personas
- Markdown output templates
- Architecture templates
- Validation checklist template
- Rollback plan template

### Exit Criteria

A request such as:

> Build Vaultwarden.

Produces:

- Architecture
- Risks
- Checklist
- Validation plan
- Rollback plan
- ClickUp-style task hierarchy
- Git repository structure

## Phase II — Project Management

### Objective

Integrate project planning outputs with task-management and Git workflows.

### Integrations

- ClickUp
- GitHub or Gitea

### Deliverables

- Epic generation
- Task generation
- Milestone generation
- Sprint plan generation
- Repository skeleton generation

### Exit Criteria

One prompt creates a complete engineering project plan with tasks and repository structure.

## Phase III — Infrastructure Awareness

### Objective

Allow Daedalus to understand the environment without making changes.

### Integrations

- Proxmox
- Kubernetes
- Proxmox Backup Server

### Capabilities

Read-only:

- Inventory
- VM status
- Cluster health
- Backup status

Generate:

- IaC
- Kubernetes manifests
- Documentation
- Change plans

### Exit Criteria

Daedalus can reference current lab state and produce accurate plans without write access.

## Phase IV — Engineering Memory

### Objective

Preserve architecture decisions, design rationale, runbooks, and lessons learned.

### Store

- Architecture decisions
- Network diagrams
- Inventory
- Runbooks
- Lessons learned
- Change history

### Example Query

> Why is VLAN 30 isolated?

Daedalus should answer with the original design rationale and supporting documentation.

## Phase V — Security Engineering

### Objective

Integrate security validation and hardening workflows.

### Integrations

- Rapid7
- CIS benchmarks
- STIG references
- GOAD lab findings

### Generate

- Hardening recommendations
- Validation checklists
- Risk assessments
- Threat models
- Remediation plans

### Exit Criteria

Daedalus can produce security-aware engineering packages tied to findings, controls, and validation steps.

## Phase VI — Controlled Automation

### Objective

Enable human-approved execution after planning and validation.

### Workflow

```text
User request
  ↓
Architecture
  ↓
ClickUp tasks
  ↓
Git artifacts
  ↓
IaC generation
  ↓
Human approval
  ↓
Execution
  ↓
Validation
  ↓
Documentation update
```

### Required Controls

- Explicit approval
- Change summary
- Validation plan
- Rollback plan
- Audit trail
- No silent execution

## Outliers

Do not build:

- Another chatbot
- Another ChatGPT wrapper
- Voice assistant
- Autonomous infrastructure controller

The differentiator is engineering reasoning.
