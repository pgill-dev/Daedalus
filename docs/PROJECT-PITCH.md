# Daedalus Project Pitch

## Elevator Pitch

Daedalus is an AI-assisted engineering copilot for a self-hosted Zero Trust lab.

It does not execute changes automatically. Instead, it produces structured, reviewable engineering artifacts such as plans, security reviews, validation checklists, rollback plans, ADRs, and proposed IaC while preserving human approval.

## 30-Second Version

Daedalus is the engineering layer around my Zero Trust lab.

Instead of treating the lab as a collection of services, I built a platform that manages the engineering process: request intake, planning, risk review, validation, rollback, and decision tracking.

It includes a Python CLI, GitHub Actions validation, JSON schemas, templates, diagrams, and end-to-end examples.

## 2-Minute Version

Daedalus is a repository-driven AI-assisted engineering platform.

The goal is to safely use AI as an infrastructure engineering copilot without allowing it to become an autonomous operator.

The system is built around a human-in-the-loop model. Every generated artifact is proposed by default. Infrastructure-impacting changes require human approval, validation, rollback planning, and security review.

The platform includes workflows for engineering requests, engineering packages, security reviews, validation, rollback, IaC generation guardrails, and architecture decision records.

I also added a local Python CLI that generates standard artifacts and GitHub Actions that validate repository structure, JSON schemas, and CLI behavior.

The project demonstrates infrastructure engineering process design, Zero Trust thinking, documentation architecture, CI validation, and safe AI-assisted engineering workflows.

## Technical Highlights

- Python CLI package
- Artifact generators
- GitHub Actions CI
- JSON schema validation
- Repository validation
- Pytest test suite
- Mermaid architecture diagrams
- Markdown-based project memory
- ADR workflow
- Security review workflow
- Validation and rollback workflow
- IaC guardrails

## Core Message

Daedalus is not about replacing the engineer.

Daedalus is about giving the engineer a repeatable, safe, reviewable process for infrastructure work.

## Portfolio Framing

This project should be framed as:

```text
AI-assisted infrastructure engineering platform
```

Not simply:

```text
Home lab documentation
```

The stronger story is that Daedalus is the engineering platform that operates around the lab.
