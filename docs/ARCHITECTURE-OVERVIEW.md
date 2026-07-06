# Daedalus Architecture Overview

## Purpose

This document describes the architecture of Daedalus at a high level.

Daedalus is an AI-assisted engineering platform designed to support a self-hosted Zero Trust lab. It provides structured workflows, project memory, templates, schemas, validation tooling, and a local CLI for generating reviewable engineering artifacts.

Daedalus is not an autonomous operator.

## Architecture Summary

Daedalus is organized around five major layers:

1. Human approval layer
2. Workflow and documentation layer
3. Project memory layer
4. Artifact generation layer
5. Validation and quality layer

```text
Human Engineer
  -> Engineering Request
  -> Daedalus Workflow System
  -> Proposed Artifacts
  -> Human Review
  -> Manual Implementation
  -> Validation Evidence
  -> Project Memory Update
```

## Layer 1: Human Approval Layer

The human approval layer is the control point for the platform.

Daedalus may generate proposed work, but a human must approve before any infrastructure-impacting change is used.

Human approval is required before:

- Running generated commands
- Applying generated configuration
- Deploying Infrastructure as Code
- Changing identity or access control
- Modifying backups or recovery systems
- Exposing services externally
- Accepting residual risk
- Marking proposed work as approved

## Layer 2: Workflow and Documentation Layer

The workflow layer defines how engineering work moves through Daedalus.

Primary workflows:

| Workflow | Purpose |
|---|---|
| Engineering Request Workflow | Defines how work enters Daedalus |
| Engineering Package Workflow | Defines the main proposed engineering deliverable |
| Security Review Workflow | Reviews access, trust boundary, secrets, and exposure risks |
| Validation and Rollback Workflow | Defines verification and recovery steps |
| IaC Generation Guardrails | Controls safe generation of configuration and IaC |
| ADR Workflow | Records major architecture decisions |
| CI Validation Workflow | Keeps the repository and CLI healthy |
| Schema Validation Workflow | Validates JSON schema structure and metadata |

## Layer 3: Project Memory Layer

Project memory gives Daedalus persistent context.

Memory is stored in the repository under:

```text
memory/
```

Memory areas:

| Path | Purpose |
|---|---|
| `memory/architecture/` | Architecture notes |
| `memory/decisions/` | ADRs and decision records |
| `memory/outputs/` | Generated outputs |
| `memory/plans/` | Engineering plans and requests |
| `memory/rollback/` | Rollback records |
| `memory/threat-models/` | Threat models and security reviews |
| `memory/validation/` | Validation records |

Daedalus should reference memory when generating future work.

Daedalus must not silently overwrite approved memory records.

## Layer 4: Artifact Generation Layer

The artifact generation layer contains prompts, templates, schemas, and CLI helpers.

### Prompts

Prompts define how Daedalus should reason through a workflow.

```text
prompts/workflows/
prompts/output-contracts/
prompts/system/
```

### Templates

Templates provide reusable artifact structures.

```text
templates/
```

Examples:

- Engineering package template
- Security review template
- Validation checklist template
- Rollback plan template
- ADR template
- IaC package template
- Safe script templates
- Ansible, Kubernetes, and Terraform/OpenTofu skeletons

### Schemas

Schemas provide machine-checkable structure for key artifact types.

```text
schemas/
```

### CLI

The CLI creates local proposed artifacts from standard templates.

```text
daedalus/
```

Current commands:

```text
daedalus init-check
daedalus new-request
daedalus new-package
daedalus new-adr
daedalus new-validation
daedalus new-rollback
```

## Layer 5: Validation and Quality Layer

The validation layer checks repository health and CLI behavior.

Validation components:

| Component | Purpose |
|---|---|
| `scripts/validate_repo.py` | Validates required structure and hygiene |
| `scripts/validate_schemas.py` | Validates schema metadata and uniqueness |
| `tests/` | Tests CLI, generators, repo detection, and schema validation |
| `.github/workflows/validate-repo.yml` | Runs validation and tests in CI |

Current CI checks:

```text
python scripts/validate_repo.py
python scripts/validate_schemas.py
python -m pytest
daedalus --help
daedalus init-check
```

## Data Flow

```text
Human Request
  -> GitHub Issue or Markdown Request
  -> Readiness Review
  -> Engineering Package
  -> Security Review
  -> Validation Checklist
  -> Rollback Plan
  -> ADR if needed
  -> Human Approval
  -> Manual Implementation
  -> Evidence Collection
  -> Project Memory Update
```

## Trust Boundaries

Daedalus recognizes several trust boundaries:

- Human engineer to Daedalus-generated proposal
- Proposed artifact to approved artifact
- Repository memory to live infrastructure
- Identity-aware access provider to internal lab service
- Public network to protected access path
- CLI-generated file to human-reviewed change

The most important boundary is between proposed work and implemented work.

Daedalus must not cross that boundary automatically.

## Safety Model

Daedalus uses the following safety model:

```text
Proposed by default
Human approved before use
Validated before success
Rollback planned before change
Security reviewed before exposure
Recorded after outcome
```

## Repository Architecture

```text
.github/
  ISSUE_TEMPLATE/
  workflows/

daedalus/
  cli.py
  generators/

docs/
  workflows/
  diagrams/

examples/

memory/

prompts/

schemas/

scripts/

templates/

tests/
```

## Design Decisions

Key design decisions are recorded in ADRs.

Current foundational decisions include:

- Establish repository-based project memory
- Use human-in-the-loop approval model
- Use proposed-by-default artifacts
- Use structured workflows for requests, packages, security review, validation, rollback, and ADRs
- Use a CLI for local artifact generation
- Use CI for repository and CLI validation

## Current Maturity

Daedalus is currently at the baseline platform stage.

Completed capabilities:

- Operating model
- Project memory
- Workflow definitions
- Templates
- JSON schemas
- End-to-end example
- Local CLI
- CLI tests
- GitHub Actions validation
- Architecture diagrams
- Collaboration templates

Planned capabilities:

- Expanded CLI commands
- Real lab engineering package
- Release checklist
- Changelog
- Web interface skeleton
- Deeper schema validation
- More lab-specific examples

## Summary

Daedalus is structured as a safe engineering control plane for a Zero Trust lab.

It does not replace the human engineer.

It gives the human engineer a repeatable process, persistent memory, and reviewable artifacts for planning and maintaining infrastructure.
