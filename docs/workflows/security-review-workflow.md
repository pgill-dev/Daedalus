# Security Review Workflow

## Purpose

The security review workflow defines how Daedalus evaluates proposed engineering work before it is approved for use.

Security review is required for any engineering package that affects infrastructure, access paths, identity, secrets, backups, public exposure, or trust boundaries.

## Workflow Summary

1. Engineering request is submitted.
2. Daedalus performs request readiness review.
3. Daedalus generates an engineering package.
4. Daedalus performs a security review against the proposed package.
5. Human reviews the security findings.
6. Human approves, rejects, or requests revision.
7. Approved work may proceed through a separate implementation process.

## Security Review Triggers

A security review is required when a request or package involves:

- Authentication
- Authorization
- Identity providers
- Public exposure
- Cloudflare Tunnel or reverse proxy paths
- Remote access services
- Firewall rules
- Secrets
- Service accounts
- Backup systems
- Logging or monitoring
- Network segmentation
- Kubernetes ingress
- Infrastructure as Code
- Privileged automation

## Risk Levels

### Low

Documentation or planning-only changes with no operational impact.

### Medium

Configuration or IaC proposals that could affect services if applied.

### High

Changes that affect access paths, network exposure, authentication, backups, or privileged services.

### Critical

Changes that affect identity boundaries, public exposure, secrets, recovery, or administrative control.

## Required Review Areas

Every security review must evaluate:

- Assets affected
- Trust boundaries
- Authentication and authorization
- Network exposure
- Secrets handling
- Logging and monitoring
- Backup and recovery impact
- Rollback path
- Abuse cases
- Human approval requirements

## Human Approval

Security review findings must be reviewed by a human before infrastructure-impacting work is treated as approved.

Daedalus must not downgrade security risk without justification.

Daedalus must not mark security findings as remediated unless a human confirms remediation.

## Output Location

Security reviews should be stored under:

```text
memory/threat-models/
```

or referenced inside the related engineering package.

## Completion Criteria

A security review is complete when:

- Affected assets are identified
- Trust boundaries are documented
- Key threats are listed
- Mitigations are proposed
- Residual risk is stated
- Approval requirements are clear
- Follow-up actions are documented
