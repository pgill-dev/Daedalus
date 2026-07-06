# ADR-0001: Separate Daedalus from the Zero Trust Engineering Lab

## Status

Accepted

## Context

The Zero Trust Engineering Lab and Daedalus are related but demonstrate different skill sets.

The lab demonstrates infrastructure, networking, virtualization, security architecture, and operations.

Daedalus demonstrates internal tooling, AI-assisted engineering workflows, documentation systems, change planning, and controlled automation design.

Combining both into one project would weaken the portfolio story by making Daedalus look like a feature of the lab instead of a separate engineering platform.

## Decision

Daedalus will be maintained as a separate project and repository.

The Zero Trust Engineering Lab is the test range. Daedalus is the engineering platform that helps operate, document, and improve the test range.

## Consequences

### Positive

- Stronger portfolio narrative
- Cleaner project boundaries
- Easier roadmap management
- Easier public/private separation
- Better demonstration of internal tooling ability

### Negative

- Requires separate documentation
- Requires separate repository management
- Requires clear references between the two projects

## Notes

Daedalus may use the Zero Trust Engineering Lab as its primary environment and benchmark target, but the projects should remain distinct.
