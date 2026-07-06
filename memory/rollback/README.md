# Rollback Records

This directory stores Daedalus rollback plans and rollback result records.

## Purpose

Rollback records provide a reviewable recovery path for infrastructure-impacting work.

## Record Types

This directory may contain:

- Rollback plans
- Rollback validation records
- Known-good configuration references
- Recovery notes
- Human rollback approvals
- Failed rollback notes

## Rules

Daedalus may propose rollback steps.

Daedalus must not execute rollback steps automatically.

Daedalus must not claim rollback succeeded without human confirmation.

Daedalus must not assume backups or snapshots exist unless they are confirmed.

## Recommended Naming

Use names like:

```text
YYYY-MM-DD-<system>-rollback-plan.md
YYYY-MM-DD-<system>-rollback-results.md
```

Example:

```text
2026-07-06-cloudflare-access-rollback-plan.md
```
