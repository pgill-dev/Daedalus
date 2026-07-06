# Current Lab Context

## Status

Proposed baseline memory record.

## Summary

Daedalus is being built as an AI-assisted engineering platform for a self-hosted Zero Trust lab.

The lab is the operational environment.

Daedalus is the engineering copilot that plans, documents, reviews, and assists with infrastructure work.

## Current Scope

Daedalus supports:

- Engineering planning
- Documentation generation
- Infrastructure as Code generation
- Architecture decision tracking
- Validation checklist creation
- Rollback planning
- Threat modeling support
- Project memory maintenance

Daedalus does not automatically execute infrastructure changes.

## Human-in-the-Loop Rule

All infrastructure-impacting outputs must be reviewed and approved by a human before use.

Daedalus may generate proposed changes.

Daedalus may not directly apply changes to production or lab infrastructure.

## Primary Environment

The target environment is a self-hosted Zero Trust engineering lab.

Known components may include:

- Proxmox VE
- Proxmox Backup Server
- Cloudflare Tunnel
- Guacamole or remote access services
- Kubernetes or containerized workloads
- Identity-aware access paths
- Internal documentation
- Infrastructure as Code repositories

## Current Phase

Phase 1: Baseline repository and project memory initialization.
