---
name: Engineering Request
about: Request Daedalus-assisted engineering work
title: "[Engineering Request]: "
labels: ["engineering-request", "needs-review"]
assignees: ""
---

# Engineering Request

## Request Summary

Briefly describe the engineering work being requested.

## Request Type

Select all that apply:

- [ ] Architecture planning
- [ ] Documentation
- [ ] Infrastructure as Code
- [ ] Configuration generation
- [ ] Validation checklist
- [ ] Rollback plan
- [ ] Threat model
- [ ] Security review
- [ ] Other

## Target System or Component

Describe the system, service, lab component, repository, or environment this request affects.

Examples:

- Proxmox VE
- Proxmox Backup Server
- Cloudflare Tunnel
- Guacamole
- Kubernetes
- Ansible
- Terraform/OpenTofu
- Documentation only

## Current State

Describe the current known state.

Include links to existing docs, ADRs, configs, screenshots, or memory records when available.

## Desired Outcome

Describe what success should look like.

## Constraints

List any known constraints.

Examples:

- No live changes
- No public exposure
- Must remain human-approved
- Must be reversible
- Must not affect production services
- Must use existing templates
- Must follow Zero Trust assumptions

## Risk Level

Select one:

- [ ] Low — documentation or planning only
- [ ] Medium — configuration or IaC proposal
- [ ] High — infrastructure-impacting change
- [ ] Critical — affects access, identity, backups, or security boundaries

## Human Approval Requirement

All Daedalus-generated infrastructure-impacting outputs require human review and approval before use.

- [ ] I understand this request will not be automatically executed.
- [ ] I understand generated changes must be reviewed before use.

## Requested Outputs

Select all requested outputs:

- [ ] Engineering plan
- [ ] Architecture note
- [ ] ADR
- [ ] IaC/config draft
- [ ] Validation checklist
- [ ] Rollback plan
- [ ] Threat model
- [ ] Documentation update
- [ ] Final implementation package

## Acceptance Criteria

Define what must be true for this request to be considered complete.

- [ ] Scope is clear
- [ ] Risks are documented
- [ ] Rollback path exists, if applicable
- [ ] Validation steps are included, if applicable
- [ ] Human approval point is identified

## Additional Notes

Add any extra context here.
