# ADR-0002: Use Identity-Aware Access for Internal Documentation Service

## Status

Proposed

## Date

2026-07-06

## Decision Owner

Human reviewer or owner.

## Related Records

- Engineering Request: 01-engineering-request.md
- Engineering Package: 03-engineering-package.md
- Security Review: 04-security-review.md
- Validation Checklist: 05-validation-checklist.md
- Rollback Plan: 06-rollback-plan.md
- Supersedes:
- Superseded by:

## Context

The lab needs an internal documentation service that can be accessed by approved users without exposing the service directly to the public internet.

Because documentation may contain operational details, architecture notes, or sensitive internal references, access must be restricted and auditable.

## Decision

Use an identity-aware access layer in front of the internal documentation service.

The service should not be directly exposed to the public internet.

Only approved users or groups should be allowed to access the service.

## Options Considered

### Option 1: Direct Public Exposure

**Summary:** Expose the documentation service directly to the internet.

**Pros:**

- Simple access path
- Fewer moving parts

**Cons:**

- Increased exposure
- Higher risk of unauthenticated access
- Weaker alignment with Zero Trust assumptions
- Less control over authorization

### Option 2: VPN-Only Access

**Summary:** Require users to connect to a VPN before accessing the service.

**Pros:**

- Keeps service internal
- Familiar access pattern
- Can reduce public exposure

**Cons:**

- Requires VPN client
- Less granular per-application access
- May not provide application-level identity policy
- Can increase operational overhead

### Option 3: Identity-Aware Access

**Summary:** Put the documentation service behind an identity-aware access provider or equivalent access layer.

**Pros:**

- Stronger alignment with Zero Trust assumptions
- Application-level access control
- Better auditability
- Avoids direct unauthenticated public exposure
- Supports allow-listing approved users or groups

**Cons:**

- Requires correct policy configuration
- Requires validation of authentication and authorization
- Adds dependency on access provider or tunnel

## Rationale

Identity-aware access best matches the lab's Zero Trust model because it requires authentication and authorization before users reach the service.

This approach also supports negative validation, logging, and policy-based access control.

## Consequences

### Positive Consequences

- Reduces risk of direct public exposure
- Supports user or group based access control
- Improves auditability
- Aligns with Daedalus human approval and validation workflows

### Negative Consequences

- Misconfiguration could still expose the service
- Requires access policy maintenance
- Adds dependency on identity-aware access provider

### Neutral Consequences

- Documentation service deployment still requires runtime, DNS, logging, and backup decisions
- Human approval remains required before implementation

## Security Considerations

- Access policy must deny unauthenticated users.
- Access policy must deny non-approved authenticated users.
- Service should not be reachable through direct public ports.
- Logs should capture allowed and denied access.
- Documentation content must be reviewed for secrets.
- Tunnel or reverse proxy routing must be validated.

## Validation Impact

Validation must include:

- Approved user access test
- Unauthenticated denial test
- Unauthorized user denial test
- Direct public access bypass test
- Logging confirmation
- Route target confirmation

## Rollback Impact

Rollback must include:

- Disabling new route or hostname
- Restoring known-good access policy
- Stopping or isolating the documentation service
- Confirming unauthenticated access remains denied
- Preserving logs and evidence

## Human Approval

**Approval required:** Yes  
**Approved by:**  
**Approval date:**  
**Approval notes:**  

## Follow-Up Actions

- Select documentation platform.
- Confirm identity provider.
- Confirm approved users or groups.
- Confirm runtime platform.
- Convert example package into a real implementation package if needed.
