# ADR-0001: Establish Project Memory

## Status

Approved

## Date

2026-07-06

## Context

Daedalus needs a structured way to maintain continuity across engineering sessions.

Relying only on chat history is fragile because project context can become scattered, incomplete, or unavailable.

A repository-based project memory gives Daedalus a stable source of truth for architecture notes, decisions, plans, outputs, validation records, rollback plans, and threat models.

## Decision

Daedalus will use a `memory/` directory in the repository as its baseline project memory system.

Memory records will be stored as Markdown files.

The memory system will separate architecture notes, decisions, plans, outputs, validation, rollback, and threat modeling records.

## Consequences

Daedalus gains a persistent engineering context.

Future outputs can reference prior decisions and approved project direction.

Human approval remains required before using generated outputs against live infrastructure.

The memory system must be maintained deliberately to avoid becoming stale or inaccurate.
