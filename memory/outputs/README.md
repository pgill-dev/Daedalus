# Generated Outputs

This directory stores proposed and approved Daedalus-generated outputs.

## Purpose

Generated outputs provide a reviewable record of engineering plans, IaC drafts, configuration drafts, documentation, scripts, and implementation packages.

## Record Types

This directory may contain:

- Engineering packages
- IaC packages
- Configuration drafts
- Script drafts
- Documentation outputs
- Final review packages

## Rules

Daedalus may create proposed outputs.

Daedalus must not treat outputs as approved unless a human approves them.

Daedalus must not include plaintext secrets.

Daedalus must include validation and rollback guidance for infrastructure-impacting outputs.

## Recommended Naming

Use names like:

```text
YYYY-MM-DD-<system>-engineering-package.md
YYYY-MM-DD-<system>-iac-package.md
YYYY-MM-DD-<system>-config-draft.md
```

Example:

```text
2026-07-06-cloudflare-access-iac-package.md
```
