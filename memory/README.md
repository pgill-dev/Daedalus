# Daedalus Project Memory

This directory stores persistent project context for Daedalus.

Daedalus uses project memory to maintain continuity across engineering sessions without relying on chat history alone.

## Purpose

Project memory provides a structured location for:

- Architecture notes
- Engineering decisions
- Implementation plans
- Generated outputs
- Validation results
- Rollback plans
- Threat models

## Rules

Daedalus may read from project memory when planning or generating engineering work.

Daedalus must not overwrite prior records without human approval.

Daedalus should append new records when possible.

Daedalus must separate proposed changes from approved changes.

Daedalus does not execute infrastructure changes automatically.

## Directory Layout

| Directory | Purpose |
|---|---|
| `architecture/` | Current and historical architecture notes |
| `decisions/` | Architecture Decision Records and approval history |
| `plans/` | Engineering implementation plans |
| `outputs/` | Generated artifacts such as IaC, configs, and docs |
| `validation/` | Test plans, checklists, and verification results |
| `rollback/` | Rollback and recovery plans |
| `threat-models/` | Threat modeling notes and risk reviews |

## Memory Status

Current phase: Baseline project memory initialization.

Human approval required before using memory outputs for live infrastructure work.
