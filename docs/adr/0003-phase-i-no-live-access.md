# ADR-0003: Phase I Has No Live Infrastructure Access

## Status

Accepted

## Context

The first phase of Daedalus focuses on the reasoning engine, prompt structure, documentation quality, and output consistency.

Connecting to live infrastructure too early would increase complexity and distract from the core differentiator: engineering reasoning.

## Decision

Phase I will not connect to live infrastructure.

Daedalus Phase I will generate:

- Architecture documents
- Engineering plans
- Task lists
- IaC skeletons
- Validation checklists
- Rollback plans
- ADRs

## Consequences

### Positive

- Faster baseline development
- Lower risk
- Easier testing
- Clearer focus
- No accidental infrastructure changes

### Negative

- No real-time inventory awareness
- Requires the engineer to provide lab context manually
- Infrastructure integrations are deferred

## Notes

Read-only infrastructure awareness is planned for a later phase.
