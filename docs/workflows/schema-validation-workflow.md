# Schema Validation Workflow

## Purpose

The schema validation workflow defines how Daedalus validates JSON schemas used for structured engineering artifacts.

Schemas help keep Daedalus outputs consistent, reviewable, and machine-checkable.

## Validation Script

```text
scripts/validate_schemas.py
```

## What the Script Checks

The script checks that:

- The `schemas/` directory exists
- Schema files exist
- Every schema file is valid JSON
- Every schema root is a JSON object
- Every schema has required metadata fields
- Schema IDs are unique
- Schema titles are unique
- Root schema type is `object`
- `required` is a list when present
- `properties` is an object when present

## Required Schema Metadata

Every schema should include:

```text
$schema
$id
title
type
```

## Current Schema Types

Daedalus currently includes schemas for:

- Engineering packages
- Security reviews
- Validation checklists
- Rollback plans
- IaC packages
- Architecture Decision Records

## Local Validation

Run:

```powershell
python scripts/validate_schemas.py
```

Expected result:

```text
Schema validation passed.
```

## CI Integration

Schema validation is intended to run in GitHub Actions as part of repository validation.

## Failure Handling

If schema validation fails:

1. Read the failing schema path.
2. Open the schema file.
3. Fix invalid JSON or missing metadata.
4. Confirm `$id` and `title` are unique.
5. Run validation locally.
6. Commit and push the fix.

## Human Approval Model

Schema validation does not approve engineering work.

It only checks that schema files are structurally healthy.

Human approval is still required before generated engineering artifacts are used against infrastructure.

## Completion Criteria

Schema validation is healthy when:

- All schema files load as JSON
- All schema files include required metadata
- IDs are unique
- Titles are unique
- Local validation passes
- CI validation passes
