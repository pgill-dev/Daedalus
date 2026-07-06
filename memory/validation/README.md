# Validation Records

This directory stores Daedalus validation checklists and validation result records.

## Purpose

Validation records provide evidence that proposed or implemented engineering work was checked against expected outcomes.

## Record Types

This directory may contain:

- Pre-change validation checklists
- Post-change validation checklists
- Negative validation records
- Rollback validation records
- Human validation notes
- Evidence summaries

## Rules

Daedalus may propose validation checks.

Daedalus must not mark validation checks as passed without human evidence.

Daedalus must separate expected results from actual results.

Daedalus must preserve failed validation results instead of hiding them.

## Recommended Naming

Use names like:

```text
YYYY-MM-DD-<system>-validation-checklist.md
YYYY-MM-DD-<system>-validation-results.md
```

Example:

```text
2026-07-06-cloudflare-access-validation-checklist.md
```
