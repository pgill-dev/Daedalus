# LinkedIn Project Summary

## Short Post Version

I started building **Daedalus**, an AI-assisted engineering platform for my self-hosted Zero Trust lab.

The goal is not to create an autonomous operator. The goal is to create an engineering copilot that helps produce structured, reviewable infrastructure work while keeping a human in the approval loop.

Daedalus currently includes:

- Engineering request workflow
- Engineering package workflow
- Security review workflow
- Validation and rollback workflow
- Infrastructure as Code generation guardrails
- Architecture Decision Records
- Project memory
- Local CLI tooling
- GitHub Actions validation
- JSON schema validation
- End-to-end example package

The idea is simple:

```text
The lab is the test range.
Daedalus is the engineer.
```

This project is helping me turn lab work into documented engineering work with planning, risk review, validation, rollback, and decision tracking built in from the start.

## Longer Post Version

I have been building a project called **Daedalus**.

Daedalus is an AI-assisted engineering platform for a self-hosted Zero Trust lab. It is designed to act as an infrastructure engineering copilot that helps plan, document, review, validate, and prepare infrastructure work while keeping a human in the approval loop.

It is intentionally not an autonomous operator.

The platform produces structured engineering artifacts such as:

- Engineering requests
- Readiness reviews
- Engineering packages
- Security reviews
- Validation checklists
- Rollback plans
- Architecture Decision Records
- Infrastructure as Code drafts
- Project memory records

The repository now includes a local CLI, GitHub Actions validation, JSON schema validation, templates, diagrams, and an end-to-end example showing how a request moves through the system.

The bigger goal is to show the difference between just having a home lab and engineering a platform around that lab.

The lab is the test range.

Daedalus is the engineer.

## Resume Bullet Options

- Designed and built Daedalus, an AI-assisted infrastructure engineering platform for a self-hosted Zero Trust lab, with structured workflows for engineering requests, security review, validation, rollback, ADRs, and project memory.
- Developed a Python CLI for generating proposed engineering artifacts, including engineering requests, packages, ADRs, validation checklists, and rollback plans.
- Implemented GitHub Actions CI to validate repository structure, JSON schemas, CLI behavior, and project quality gates.
- Created an engineering governance model with human approval gates, proposed-by-default artifacts, IaC safety guardrails, and rollback requirements.
- Built an end-to-end infrastructure planning example demonstrating request intake, readiness review, engineering package creation, security review, validation, rollback, and decision tracking.

## Interview Talking Points

### What is Daedalus?

Daedalus is an AI-assisted engineering platform for a self-hosted Zero Trust lab. It helps generate structured engineering artifacts while keeping a human responsible for approval and execution.

### Why did you build it?

I wanted my lab work to demonstrate engineering discipline, not just service deployment. Daedalus gives the lab a process for requests, plans, security review, validation, rollback, and decision tracking.

### What problem does it solve?

It prevents lab infrastructure work from becoming scattered, undocumented, or risky. It creates a repeatable workflow for planning and reviewing changes before implementation.

### What makes it safe?

Daedalus is proposed-by-default. It does not execute infrastructure changes. Every infrastructure-impacting artifact requires human approval, validation, and rollback planning.

### What does it demonstrate?

It demonstrates infrastructure engineering, Zero Trust thinking, documentation architecture, GitHub governance, CLI development, CI validation, schema validation, and AI-assisted workflow design.
