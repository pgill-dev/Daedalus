# Infrastructure as Code Generation Guardrails

## Purpose

This workflow defines how Daedalus generates Infrastructure as Code, configuration files, scripts, and deployment manifests safely.

Daedalus may generate proposed IaC.

Daedalus must not execute generated IaC.

Daedalus must not treat generated IaC as approved until a human reviews and approves it.

## Scope

These guardrails apply to:

- Ansible playbooks and roles
- Terraform or OpenTofu modules
- Kubernetes manifests
- Helm values
- Docker Compose files
- Shell scripts
- PowerShell scripts
- Systemd unit files
- Reverse proxy configs
- Firewall rule proposals
- Cloudflare Tunnel or Access configuration drafts
- Proxmox automation drafts

## Core Rules

Daedalus must:

- Generate IaC as proposed work
- Include assumptions
- Include risk notes
- Include validation steps
- Include rollback steps
- Avoid destructive defaults
- Avoid hard-coded secrets
- Avoid automatically applying changes
- Prefer least privilege
- Prefer idempotent operations
- Prefer dry-run or plan-first workflows
- Require human approval before execution

Daedalus must not:

- Execute commands
- Apply infrastructure changes
- Store secrets in generated files
- Disable security controls without warning
- Generate destructive commands without explicit rollback and approval notes
- Claim a deployment succeeded without human confirmation
- Hide uncertainty or assumptions

## Required IaC Output Sections

Any generated IaC package must include:

1. Purpose
2. Scope
3. Assumptions
4. Files generated
5. Safety notes
6. Required variables
7. Secrets handling
8. Validation steps
9. Rollback steps
10. Human approval gate

## Tool-Specific Guardrails

### Ansible

Ansible content should:

- Use readable task names
- Prefer idempotent modules over shell commands
- Use variables instead of hard-coded values
- Avoid storing secrets in plaintext
- Include inventory assumptions
- Include check-mode notes when applicable
- Include rollback notes

Avoid:

- Blind `shell` or `command` usage when a module exists
- Unscoped privilege escalation
- Hard-coded credentials
- Destructive tasks without confirmation

### Terraform / OpenTofu

Terraform or OpenTofu content should:

- Separate variables, outputs, and resources
- Avoid hard-coded secrets
- Include provider assumptions
- Include plan-first instructions
- Include state handling notes
- Include destroy risk warnings when applicable

Avoid:

- Unsafe defaults
- Public exposure by default
- Broad admin permissions
- Destroy operations without explicit approval

### Kubernetes

Kubernetes content should:

- Define namespaces clearly
- Use least-privilege service accounts
- Avoid privileged containers unless justified
- Include resource requests and limits where appropriate
- Avoid default public exposure
- Include ingress and network policy assumptions
- Include rollback notes

Avoid:

- HostPath mounts unless justified
- Privileged pods by default
- Cluster-admin bindings by default
- Public LoadBalancer exposure by default

### Scripts

Scripts should:

- Be readable
- Include comments
- Use safe defaults
- Support dry-run when reasonable
- Check prerequisites
- Fail safely
- Avoid destructive behavior by default

Scripts must not:

- Include secrets
- Delete data without explicit confirmation
- Disable protections silently
- Assume production safety

## Human Approval Gate

Human approval is required before:

- Running generated scripts
- Applying Ansible playbooks
- Running Terraform/OpenTofu apply
- Applying Kubernetes manifests
- Updating access policies
- Modifying firewall rules
- Modifying backup systems
- Changing privileged automation

## Completion Criteria

IaC generation is complete when:

- Generated files are listed
- Assumptions are documented
- Risks are documented
- Validation is included
- Rollback is included
- Human approval gate is stated
- Output is committed as proposed work
