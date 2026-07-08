# Daedalus Engineering Memory Model

## Purpose

The engineering memory model defines how Daedalus preserves project context, architecture rationale, operational lessons, and reusable engineering knowledge.

Daedalus should not rely only on conversational memory or ad hoc notes. It should maintain structured engineering memory that can be reviewed, version controlled, corrected, and cited during future planning.

This document supports Phase I by defining the baseline memory rules before Daedalus receives live infrastructure access or automation capability.

## Memory Principle

Daedalus memory exists to answer engineering questions with traceable context.

Examples:

- Why was a VLAN isolated?
- Why was a service deployed behind Traefik?
- Why was a tool selected over an alternative?
- What rollback procedure was approved?
- What validation checks were required before deployment?
- What lessons were learned from a previous change?

Daedalus should preserve rationale, not just facts.

## Memory Scope

### In Scope

Daedalus may store and reference:

- Architecture decisions
- Design rationale
- Network segmentation decisions
- Approved deployment patterns
- Rejected alternatives
- Validation results
- Rollback procedures
- Lessons learned
- Runbook references
- Inventory summaries
- Security assumptions
- Threat-model findings
- Human approval records
- Change-management notes
- Project milestones

### Out of Scope

Daedalus must not store:

- Passwords
- API tokens
- Private keys
- SSH keys
- Recovery keys
- Production secrets
- Session cookies
- Personal credentials
- Sensitive user data unrelated to engineering
- Unapproved operational changes
- Speculative facts as confirmed truth

Secrets must be referenced by location or handling procedure only, never stored directly.

Example acceptable reference:

```text
Vaultwarden admin token is managed outside Daedalus and must be injected through the approved secret-management process.
```

Example unacceptable memory entry:

```text
Vaultwarden admin token is: <secret value>
```

## Memory Types

Daedalus memory should be organized into clear categories.

### Architecture Memory

Stores high-level system design context.

Examples:

- Network zones
- Service placement
- Ingress patterns
- Storage strategy
- Backup architecture
- Identity boundaries
- Monitoring assumptions

Suggested location:

```text
memory/architecture/
```

### ADR Memory

Stores architecture decision records or links to ADRs.

Examples:

- Why Daedalus is separate from the Zero Trust Engineering Lab
- Why human approval is required
- Why Phase I has no live infrastructure access
- Why a service is deployed through Kubernetes instead of a standalone VM

Suggested location:

```text
docs/adr/
```

### Inventory Memory

Stores human-reviewed infrastructure inventory summaries.

Examples:

- Cluster names
- VM roles
- Kubernetes namespaces
- Storage pools
- Backup targets
- Service ownership

Suggested location:

```text
memory/inventory/
```

Inventory memory must distinguish between:

- Verified inventory
- Manually provided inventory
- Generated inventory
- Stale inventory
- Planned inventory

### Runbook Memory

Stores operational procedures.

Examples:

- Backup validation procedure
- Restore procedure
- Certificate renewal procedure
- Cluster health check
- Service restart steps
- Incident response procedure

Suggested location:

```text
memory/runbooks/
```

### Lessons-Learned Memory

Stores observations from completed work.

Examples:

- What failed during a deployment
- What validation caught before production
- Which assumptions were wrong
- Which rollback steps were missing
- What should be improved next time

Suggested location:

```text
memory/lessons-learned/
```

### Change Memory

Stores human-reviewed change history summaries.

Examples:

- What was proposed
- What was approved
- What was executed
- Who approved it
- What validation passed
- Whether rollback was needed

Suggested location:

```text
memory/changes/
```

## Memory Entry Format

Each memory entry should be written in Markdown and include enough metadata to be reviewed later.

Recommended front matter:

```yaml
title: "Short memory title"
type: "architecture | adr | inventory | runbook | lesson | change"
status: "draft | proposed | approved | deprecated"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
owner: "human engineer"
source: "manual | generated | validated | imported"
sensitivity: "public | internal | restricted"
related_docs:
  - "docs/example.md"
related_adrs:
  - "docs/adr/0001-example.md"
```

Recommended body structure:

```markdown
# Title

## Summary

Brief explanation of the memory item.

## Context

Why this information matters.

## Decision or Fact

The approved decision, verified fact, or captured lesson.

## Rationale

Why the decision was made or why the lesson matters.

## Validation

How this was verified, if applicable.

## Related Artifacts

- Architecture docs
- ADRs
- Runbooks
- Change plans
- Generated outputs

## Review Notes

Human review comments, corrections, or caveats.
```

## Memory Confidence Levels

Daedalus must clearly distinguish confidence levels.

| Level | Meaning | Use |
|---|---|---|
| Verified | Confirmed by human review or source artifact | Safe to use as project context |
| Proposed | Generated or suggested but not approved | May be referenced as draft only |
| Stale | May no longer reflect the environment | Must be revalidated before use |
| Deprecated | No longer valid | Should not guide new work |
| Unknown | Insufficient evidence | Must ask for validation or mark assumption |

Daedalus must not treat proposed or stale memory as verified.

## Human Review Requirement

Memory becomes authoritative only after human review.

Daedalus may generate memory drafts, but it must not silently promote them to approved memory.

Required promotion flow:

```text
Generated memory draft
    ↓
Human review
    ↓
Correction if needed
    ↓
Git commit
    ↓
Approved memory
```

## Memory Update Rules

When new information conflicts with existing memory, Daedalus should not overwrite the old entry silently.

Instead, it should:

1. Identify the conflict.
2. Cite the conflicting memory entry.
3. Propose an update.
4. Mark the older memory as deprecated if approved.
5. Create or update an ADR if the change affects architecture.

## Memory and ADR Relationship

ADRs explain decisions.

Memory preserves usable project context.

Example:

```text
ADR:
Why VLAN 30 is isolated.

Memory:
Current known systems in VLAN 30, related runbooks, validation notes, and lessons learned.
```

Daedalus should prefer ADRs for design rationale and memory files for operational context.

## Memory and Security

Memory must follow least disclosure.

Rules:

- Do not store secrets.
- Do not store credentials.
- Do not store sensitive personal data.
- Do not expose restricted infrastructure details in public-facing outputs without review.
- Mark sensitive internal details as restricted.
- Keep public portfolio language separate from internal operational details.

## Example Memory Entry

```markdown
---
title: "VLAN 30 Isolation Rationale"
type: "architecture"
status: "approved"
created: "2026-07-08"
updated: "2026-07-08"
owner: "human engineer"
source: "validated"
sensitivity: "internal"
related_docs:
  - "docs/security-model.md"
related_adrs:
  - "docs/adr/0002-human-approval-required.md"
---

# VLAN 30 Isolation Rationale

## Summary

VLAN 30 is isolated to separate lab services from general network access and reduce lateral movement risk.

## Context

The Zero Trust Engineering Lab requires segmentation between management, user-facing services, and experimental workloads.

## Decision or Fact

VLAN 30 is treated as an isolated service or workload network. Access must be explicitly routed, firewalled, or proxied.

## Rationale

Isolation limits blast radius, supports controlled ingress, and provides a safer test range for infrastructure security work.

## Validation

Validation should confirm that unauthorized inter-VLAN traffic is denied and approved service paths remain functional.

## Related Artifacts

- Network diagram
- Firewall rules
- Security model
- Change-management record

## Review Notes

Review whenever network architecture changes or new services are attached to VLAN 30.
```

## Phase I Expectations

During Phase I, Daedalus should be able to:

- Generate memory draft files.
- Reference ADRs and project docs.
- Preserve rationale for generated engineering packages.
- Mark all generated memory as proposed until reviewed.
- Avoid storing secrets.
- Avoid claiming generated memory is verified.

## Phase I Exit Criteria

This memory model is acceptable when Daedalus can:

- Produce memory entries from engineering packages.
- Tie memory entries to ADRs and docs.
- Mark confidence and review status.
- Avoid storing sensitive secrets.
- Preserve design rationale in a reusable format.
- Support future questions such as:

```text
Why did we choose this architecture?
What validation was required?
What rollback plan was approved?
What assumptions were made?
What lessons did we learn?
```

## Operating Principle

Daedalus remembers engineering context so future work is traceable, reviewable, and safer.

Memory supports engineering judgment.

Memory does not replace human review.
