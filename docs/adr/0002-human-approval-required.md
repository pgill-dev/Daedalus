# ADR-0002: Require Human Approval Before Execution

## Status

Accepted

## Context

Daedalus is intended to assist with infrastructure engineering. Infrastructure changes can affect availability, security, data integrity, and recovery posture.

Allowing an AI-assisted system to execute changes without approval would introduce unnecessary operational risk.

## Decision

Daedalus will not automatically execute infrastructure changes.

All future execution workflows must require explicit human approval after presenting:

- Change summary
- Target systems
- Risk assessment
- Validation plan
- Rollback plan
- Expected impact

## Consequences

### Positive

- Reduces operational risk
- Supports change-management discipline
- Makes the project more credible for security engineering
- Aligns with controlled automation principles

### Negative

- Slower than full automation
- Requires more user interaction
- Adds approval workflow complexity

## Notes

The goal is not autonomy. The goal is engineering leverage.
