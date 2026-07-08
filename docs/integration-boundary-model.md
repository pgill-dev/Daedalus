# Daedalus Integration Boundary Model

## Purpose

This document defines how Daedalus may interact with external systems across project phases.

Daedalus is designed to assist with engineering work, not silently operate infrastructure. Integrations must be introduced in a controlled way that preserves human approval, auditability, least privilege, and rollback planning.

This boundary model prevents Daedalus from becoming an uncontrolled automation layer.

## Core Principle

Daedalus may reason about systems before it connects to systems.

Daedalus may read from systems before it writes to systems.

Daedalus may generate changes before it executes changes.

Daedalus may never execute changes without explicit human approval.

## Operating Modes

Daedalus integrations are separated into four operating modes.

| Mode | Description | Phase I Status |
| --- | --- | --- |
| Offline | Uses local prompts, templates, examples, and docs only | Allowed |
| Read-only | Reads inventory, status, metadata, or configuration | Future |
| Generate-only | Produces proposed changes as files, diffs, manifests, or tasks | Allowed |
| Execute | Applies changes to systems | Blocked |

## Phase I Boundary

During Phase I, Daedalus must remain offline and generate-only.

Daedalus may use:

- Local prompt files
- Output contracts
- Markdown templates
- Engineering examples
- Local memory documents
- Schemas
- Test plans
- Validation checklists

Daedalus may generate:

- Architecture documents
- Change plans
- Runbooks
- ADRs
- Kubernetes manifest skeletons
- Ansible skeletons
- ClickUp-style task breakdowns
- Validation procedures
- Rollback procedures
- Security reviews
- Threat models

Daedalus may not:

- Connect to Proxmox
- Connect to Kubernetes
- Connect to PBS
- Connect to Rapid7
- Connect to GitHub APIs
- Connect to ClickUp APIs
- Modify DNS
- Modify firewall rules
- Modify secrets
- Execute shell commands against infrastructure
- Deploy workloads
- Restart services
- Change access control

## Integration Progression

Every integration must move through the following stages.

### Stage 0: Documented Intent

Before an integration exists, Daedalus must document:

- Integration purpose
- System owner
- Data being accessed
- Required permissions
- Risks
- Approval requirements
- Expected outputs
- Failure modes
- Rollback limitations

### Stage 1: Mock Integration

A mock integration uses sample data instead of live system access.

Example:

- Static Proxmox inventory JSON
- Example Kubernetes namespace list
- Example Rapid7 asset export
- Example ClickUp task payload

The goal is to validate Daedalus reasoning without touching real infrastructure.

### Stage 2: Read-only Integration

A read-only integration may retrieve information but may not change system state.

Read-only integrations must use:

- Least-privilege credentials
- Dedicated service accounts
- Documented access scope
- Logging where possible
- No secrets in repository
- No write permissions

### Stage 3: Generate-only Change Proposal

Daedalus may generate proposed changes from live system context, but the output must remain a file, diff, plan, or task.

Examples:

- Terraform/OpenTofu plan draft
- Ansible playbook skeleton
- Kubernetes manifest proposal
- Firewall rule recommendation
- Proxmox VM build plan
- ClickUp task hierarchy

Daedalus still may not apply the change.

### Stage 4: Human-approved Execution

Execution is a future capability and is not part of Phase I.

Before execution is allowed, Daedalus must produce:

- Change request
- Risk assessment
- Impact assessment
- Implementation plan
- Validation checklist
- Rollback plan
- Approval record
- Expected system state
- Post-change verification steps

The engineer must approve before execution.

## Approved Phase I Data Sources

The following data sources are approved for Phase I:

| Source | Access Type | Approved |
| --- | --- | --- |
| Local Markdown prompts | Read | Yes |
| Local templates | Read | Yes |
| Local examples | Read/write generated outputs | Yes |
| Local schemas | Read | Yes |
| Local memory docs | Read/write reviewed memory | Yes |
| Git repository files | Local read/write | Yes |

## Blocked Phase I Data Sources

The following data sources are blocked during Phase I:

| Source | Reason |
| --- | --- |
| Proxmox API | Live infrastructure access deferred |
| Kubernetes API | Live cluster access deferred |
| PBS API | Backup system access deferred |
| Rapid7 API | Security platform access deferred |
| ClickUp API | Project automation deferred |
| GitHub API | Remote automation deferred |
| Gitea API | Remote automation deferred |
| Firewall APIs | High-risk infrastructure changes |
| DNS providers | External availability risk |
| Secret managers | Secret handling model not implemented |

## Credential Rules

Daedalus repository files must never contain:

- Passwords
- API tokens
- Private keys
- Session cookies
- Recovery keys
- Vaultwarden admin tokens
- Cloudflare tokens
- Proxmox credentials
- Kubernetes kubeconfigs
- Rapid7 keys
- ClickUp tokens
- GitHub tokens

Credential references must use placeholders only.

Allowed examples:

```text
${PROXMOX_API_TOKEN}
${CLICKUP_API_TOKEN}
${KUBECONFIG}
${RAPID7_API_KEY}
```

Blocked examples:

```text
pveum token value pasted directly
actual kubeconfig contents
real bearer token
real password
real SSH private key
```

## Proxmox Boundary

Future Proxmox integration must begin as read-only.

Allowed read-only capabilities:

- List nodes
- List VMs
- Read VM status
- Read storage status
- Read cluster health
- Read network bridge names
- Read tags and descriptions

Blocked until approved execution exists:

- Create VM
- Delete VM
- Start VM
- Stop VM
- Restart VM
- Modify VM hardware
- Modify storage
- Modify network configuration
- Create snapshots
- Delete snapshots

## Kubernetes Boundary

Future Kubernetes integration must begin as read-only.

Allowed read-only capabilities:

- List namespaces
- List deployments
- List pods
- List services
- List ingress objects
- Read events
- Read resource status

Allowed generate-only outputs:

- Namespace manifests
- Deployment skeletons
- Service skeletons
- Ingress/IngressRoute skeletons
- NetworkPolicy skeletons
- ConfigMap skeletons without secrets
- Secret placeholders only

Blocked until approved execution exists:

- Apply manifests
- Delete resources
- Modify workloads
- Restart deployments
- Patch services
- Modify ingress
- Modify RBAC
- Create secrets

## Proxmox Backup Server Boundary

Future PBS integration must begin as read-only.

Allowed read-only capabilities:

- List datastores
- Read backup inventory
- Read verify job status
- Read prune job status
- Read sync job status

Blocked until approved execution exists:

- Delete backups
- Start backup jobs
- Start prune jobs
- Modify retention
- Modify datastore configuration
- Modify permissions

## Rapid7 Boundary

Future Rapid7 integration must begin as reporting-only.

Allowed read-only capabilities:

- Read asset inventory
- Read vulnerability findings
- Read scan status
- Read remediation data
- Export report data where permitted

Allowed generate-only outputs:

- Remediation task breakdowns
- Risk summaries
- Hardening recommendations
- Validation checklists
- CIS/STIG mapping notes

Blocked until approved execution exists:

- Start scans
- Stop scans
- Modify scan configs
- Modify sites
- Modify credentials
- Suppress findings
- Change risk settings

## ClickUp Boundary

ClickUp is a project-management integration and may be introduced earlier than infrastructure write access, but it must still begin as generate-only.

Allowed Phase I behavior:

- Generate ClickUp-style task lists in Markdown
- Generate task hierarchy proposals
- Generate milestones and sprint plans

Future read/write behavior:

- Create tasks only after explicit approval
- Attach generated documents only after review
- Never close tasks automatically during Phase I
- Never modify priorities without approval

## GitHub and Gitea Boundary

GitHub/Gitea integration must begin as local file generation.

Allowed Phase I behavior:

- Generate repository structures
- Generate Markdown documentation
- Generate templates
- Generate code skeletons
- Let the engineer commit and push manually

Future behavior:

- Generate branch names
- Generate pull request descriptions
- Generate commit message suggestions
- Create PRs only after explicit approval

Blocked until approved execution exists:

- Direct pushes
- Force pushes
- Branch deletion
- Repository setting changes
- Secret creation
- Workflow execution triggers

## Approval Requirements

Any future action that changes system state must include an approval gate.

An approval gate must include:

- Proposed action
- Target system
- Expected result
- Risk level
- Validation method
- Rollback method
- Human approver
- Timestamp or approval record

## Risk Levels

Daedalus must label integration actions by risk level.

| Risk | Meaning | Example |
| --- | --- | --- |
| Low | Documentation or local file generation only | Generate README section |
| Medium | Remote read-only data access | Read Proxmox VM inventory |
| High | Creates or modifies non-production resources | Create test namespace |
| Critical | Impacts availability, access, backups, secrets, or production services | Modify firewall, DNS, cluster, secrets |

Phase I must remain Low risk.

## Logging Expectations

Future integrations should log:

- Requested action
- Generated output path
- Source files used
- Target system if applicable
- Approval status
- Execution status if applicable
- Errors
- Validation results

Logs must not contain secrets.

## Failure Handling

If an integration fails, Daedalus should report:

- What failed
- What was attempted
- Whether any state changed
- Whether rollback is required
- What manual checks are needed
- What logs should be reviewed

Daedalus must not hide partial failures.

## Human Review Requirements

Before any generated artifact is treated as valid, a human engineer must review:

- Architecture assumptions
- Security assumptions
- Target environment constraints
- Secrets handling
- Network exposure
- Backup and restore plan
- Validation plan
- Rollback plan

## Phase I Compliance Checklist

Daedalus Phase I remains compliant when:

- No live infrastructure credentials are used
- No API writes are performed
- No deployments are executed
- All generated outputs are reviewable Markdown or skeleton files
- Generated code contains placeholders instead of secrets
- Human approval gates are present
- Rollback is included for change proposals
- Validation is included for change proposals

## Exit Criteria for Future Integration Work

Before moving beyond Phase I, Daedalus must have:

- Stable workflow prompts
- Stable output contract
- Repeatable runner behavior
- Validation checklist
- Test plan
- Memory model
- Change-management model
- Integration boundary model
- At least one successful generated engineering package

## Summary

The integration boundary model exists to keep Daedalus credible, safe, and useful.

Daedalus should first become excellent at engineering reasoning.

Only after that should it connect to infrastructure.

The correct progression is:

```text
Reason → Generate → Review → Validate → Approve → Execute
```

Phase I stops at:

```text
Reason → Generate → Review
```
