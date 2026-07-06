# Daedalus CLI Usage

## Purpose

The Daedalus CLI provides local helper commands for generating proposed engineering artifacts from the repository structure.

The CLI does not execute infrastructure changes.

The CLI only creates local Markdown artifacts for human review.

## Current Commands

```text
daedalus --help
daedalus init-check
daedalus new-request "<title>"
daedalus new-package "<title>"
daedalus new-adr "<title>"
daedalus new-validation "<title>"
daedalus new-rollback "<title>"
```

You can also run the CLI without installing it:

```powershell
python -m daedalus.cli --help
python -m daedalus.cli init-check
```

## Install for Local Development

From the repository root:

```powershell
python -m pip install -e .
```

Then run:

```powershell
daedalus --help
```

## Repository Check

Use this command to verify that the CLI can detect the Daedalus repository:

```powershell
python -m daedalus.cli init-check
```

Expected result:

```text
Daedalus repository detected: <repo path>
Init check passed.
```

## Create an Engineering Request

```powershell
python -m daedalus.cli new-request "Deploy internal documentation service"
```

Creates a file under:

```text
memory/plans/
```

Example generated path:

```text
memory/plans/YYYY-MM-DD-deploy-internal-documentation-service-engineering-request.md
```

## Create an Engineering Package

```powershell
python -m daedalus.cli new-package "Deploy internal documentation service"
```

Creates a file under:

```text
memory/outputs/
```

Example generated path:

```text
memory/outputs/YYYY-MM-DD-deploy-internal-documentation-service-engineering-package.md
```

## Create an ADR

```powershell
python -m daedalus.cli new-adr "Use identity-aware access for internal documentation"
```

Creates a file under:

```text
memory/decisions/
```

The CLI automatically selects the next ADR number based on existing ADR files.

Example generated path:

```text
memory/decisions/0003-use-identity-aware-access-for-internal-documentation.md
```

## Create a Validation Checklist

```powershell
python -m daedalus.cli new-validation "Deploy internal documentation service"
```

Creates a file under:

```text
memory/validation/
```

Example generated path:

```text
memory/validation/YYYY-MM-DD-deploy-internal-documentation-service-validation-checklist.md
```

## Create a Rollback Plan

```powershell
python -m daedalus.cli new-rollback "Deploy internal documentation service"
```

Creates a file under:

```text
memory/rollback/
```

Example generated path:

```text
memory/rollback/YYYY-MM-DD-deploy-internal-documentation-service-rollback-plan.md
```

## Overwrite Protection

By default, the CLI does not overwrite existing files.

If a generated file already exists, the CLI exits with an error.

To overwrite intentionally:

```powershell
python -m daedalus.cli new-request "Deploy internal documentation service" --force
```

Use `--force` carefully.

## Recommended CLI Workflow

```text
1. Create an engineering request.
2. Review and edit the request manually.
3. Create an engineering package.
4. Create validation and rollback artifacts.
5. Create an ADR if the decision is significant.
6. Review all generated artifacts.
7. Commit proposed artifacts to Git.
```

## Example Git Commit Flow

```powershell
git status
git add .
git commit -m "Add proposed internal docs service package"
git push origin main
git status
```

## Safety Reminder

Generated files are proposed by default.

Do not run generated commands, apply generated configurations, deploy IaC, or modify infrastructure without human approval.
