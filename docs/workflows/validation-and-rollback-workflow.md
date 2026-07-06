# Validation and Rollback Workflow

## Purpose

The validation and rollback workflow defines how Daedalus prepares safe, reviewable verification and recovery steps for proposed engineering work.

Daedalus must not treat an engineering package as complete unless the package includes validation and rollback guidance when applicable.

## Workflow Summary

1. Engineering request is reviewed.
2. Engineering package is generated.
3. Validation requirements are identified.
4. Rollback requirements are identified.
5. Human reviews the validation and rollback plan.
6. Human approves, revises, or rejects the package.
7. If implemented manually, validation is performed by a human.
8. If the change fails, rollback is performed by a human using the approved rollback plan.

## Validation Types

### Pre-Change Validation

Checks performed before implementation to confirm the environment is ready.

Examples:

- Confirm current service health
- Confirm backup exists
- Confirm DNS records
- Confirm current access path
- Confirm current firewall behavior
- Confirm current configuration snapshot
- Confirm affected systems are reachable

### Post-Change Validation

Checks performed after implementation to confirm the desired outcome.

Examples:

- Confirm service is reachable
- Confirm authentication works
- Confirm authorization policy works
- Confirm logs are generated
- Confirm monitoring detects the service
- Confirm no unintended exposure exists
- Confirm backups still run

### Negative Validation

Checks that confirm something should not be possible.

Examples:

- Unauthenticated users cannot access the service
- Non-approved users cannot authenticate
- Internal-only services are not publicly reachable
- Disabled access paths remain disabled
- Secrets are not exposed in logs or files

### Rollback Validation

Checks performed after rollback to confirm the environment returned to a known-good state.

Examples:

- Previous service path works
- Previous config is restored
- Access control returns to expected behavior
- Monitoring is healthy
- No orphaned resources remain

## Rollback Requirements

Rollback plans must include:

- Rollback trigger
- Rollback owner or approver
- Required backups or known-good configs
- Ordered rollback steps
- Rollback validation steps
- Known limitations
- Escalation notes if rollback fails

## Human Approval

Human approval is required before:

- Applying proposed changes
- Running generated commands
- Executing rollback steps
- Declaring validation complete
- Declaring rollback successful
- Accepting residual risk

## Not Allowed

Daedalus must not:

- Execute validation commands against live infrastructure automatically
- Execute rollback steps automatically
- Claim validation passed without human-provided evidence
- Claim rollback succeeded without human confirmation
- Hide failed validation results
- Omit rollback for infrastructure-impacting work unless justified

## Storage

Validation records should be stored under:

```text
memory/validation/
```

Rollback records should be stored under:

```text
memory/rollback/
```

## Completion Criteria

This workflow is satisfied when:

- Pre-change validation is defined
- Post-change validation is defined
- Negative validation is included when applicable
- Rollback trigger is defined
- Rollback steps are ordered
- Rollback validation is included
- Human approval gate is clearly stated
