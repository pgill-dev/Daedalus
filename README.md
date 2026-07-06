# Daedalus

Daedalus is an AI-assisted engineering platform for a self-hosted Zero Trust lab.

It is designed to act as an infrastructure engineering copilot that helps plan, document, review, validate, and prepare infrastructure work while keeping a human in the approval loop.

Daedalus is not an autonomous operator.

## Mission

Design and build an AI-assisted engineering platform that serves as an infrastructure engineer for a self-hosted Zero Trust lab.

The system should plan, document, reason about, and assist in building and maintaining infrastructure while keeping a human in the approval loop.

## Project Concept

The lab is the test range.

Daedalus is the engineer.

Daedalus exists to bring engineering discipline to infrastructure work by producing structured artifacts such as:

- Engineering requests
- Readiness reviews
- Engineering packages
- Architecture Decision Records
- Security reviews
- Validation checklists
- Rollback plans
- Threat models
- Infrastructure as Code drafts
- Project memory records

## Current Scope

Daedalus supports:

- Engineering planning
- Documentation generation
- Infrastructure as Code generation
- Project memory maintenance
- Architecture decision tracking
- Validation checklist creation
- Rollback planning
- Threat modeling support
- Security review support

Daedalus does not automatically execute infrastructure changes.

## Human-in-the-Loop Rule

All infrastructure-impacting outputs require human review and approval before use.

Daedalus may generate proposed changes.

Daedalus may not directly apply changes to production or lab infrastructure.

## Repository Structure

```text
.github/
  ISSUE_TEMPLATE/
    engineering-request.md

docs/
  DAEDALUS-OPERATING-MANUAL.md
  PORTFOLIO-SUMMARY.md
  PROJECT-INDEX.md
  QUICKSTART.md
  ROADMAP.md
  WORKFLOW-MAP.md
  workflows/

examples/
  end-to-end/

memory/
  architecture/
  decisions/
  outputs/
  plans/
  rollback/
  threat-models/
  validation/

prompts/
  output-contracts/
  system/
  workflows/

schemas/

templates/
```

## Core Workflows

| Workflow | Purpose |
|---|---|
| Engineering Request Workflow | Defines how work enters Daedalus |
| Engineering Package Workflow | Defines the main engineering deliverable |
| Security Review Workflow | Reviews risk before approval |
| Validation and Rollback Workflow | Defines verification and recovery steps |
| IaC Generation Guardrails | Controls safe IaC/config/script generation |
| ADR Workflow | Records major architecture decisions |
| Project Memory Workflow | Maintains persistent project context |

## Standard Flow

```text
Human request
  -> Engineering request
  -> Readiness review
  -> Engineering package
  -> Security review
  -> Validation checklist
  -> Rollback plan
  -> ADR if needed
  -> Human approval
  -> Manual implementation
  -> Evidence and memory update
```

## Example

The repository includes an end-to-end example:

```text
examples/end-to-end/internal-docs-service/
```

This example demonstrates the full Daedalus workflow for deploying an internal documentation service behind identity-aware access.

## Current Build Status

- [x] Baseline repository
- [x] Project memory
- [x] Engineering request workflow
- [x] Engineering package contract
- [x] Security review workflow
- [x] Validation and rollback workflow
- [x] IaC generation guardrails
- [x] ADR workflow
- [x] Operating manual and project index
- [x] End-to-end engineering package example
- [x] Portfolio README and roadmap

## Key Documents

| Document | Purpose |
|---|---|
| `docs/DAEDALUS-OPERATING-MANUAL.md` | Main operating manual |
| `docs/PROJECT-INDEX.md` | Repository map |
| `docs/WORKFLOW-MAP.md` | Workflow relationships |
| `docs/QUICKSTART.md` | How to use the repo |
| `docs/ROADMAP.md` | Planned development path |
| `docs/PORTFOLIO-SUMMARY.md` | Portfolio-ready project summary |

## Safety Model

Daedalus follows these rules:

- Proposed by default
- Human approval required
- No automatic execution
- No plaintext secrets
- Validation required
- Rollback required when applicable
- Security review required for access, identity, exposure, backups, or privileged automation
- ADRs required for major decisions

## Status

Daedalus is currently in baseline platform development.

The repository contains the core operating model, workflows, templates, schemas, and an end-to-end example.

Future work will focus on turning these workflows into usable tooling, automation helpers, and interface-driven engineering workflows.
