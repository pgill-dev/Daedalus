# Threat Models and Security Reviews

This directory stores Daedalus threat models and security review records.

## Purpose

Security records help Daedalus maintain a reviewable history of risk decisions, trust boundaries, mitigations, and human approval gates.

## Record Types

This directory may contain:

- Threat models
- Security reviews
- Abuse-case reviews
- Trust-boundary notes
- Residual-risk records
- Security approval notes

## Rules

Daedalus may propose security findings.

Daedalus may not mark a risk accepted without human approval.

Daedalus must separate assumptions from confirmed facts.

Daedalus must not claim remediation has occurred unless a human confirms it.

## Recommended Naming

Use names like:

```text
YYYY-MM-DD-<system>-security-review.md
YYYY-MM-DD-<system>-threat-model.md
```

Example:

```text
2026-07-06-cloudflare-access-security-review.md
```
