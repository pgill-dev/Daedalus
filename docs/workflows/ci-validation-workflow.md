# CI Validation Workflow

## Purpose

The CI validation workflow defines how GitHub Actions checks the Daedalus repository on every push and pull request to `main`.

This workflow helps confirm that the repository structure, schemas, CLI, and tests remain healthy as the project evolves.

## Workflow File

```text
.github/workflows/validate-repo.yml
```

## What CI Checks

The current workflow checks:

- Repository structure
- Required files and directories
- JSON schema syntax
- Real Git merge conflict markers
- Obvious plaintext secret patterns
- Markdown top-level headings where appropriate
- CLI package installation
- CLI unit tests
- CLI smoke commands

## Important Validation Notes

GitHub issue templates use YAML frontmatter and are exempt from the top-level heading check.

The merge conflict check only flags real Git conflict marker lines:

```text
<<<<<<< branch
=======
>>>>>>> branch
```

It should not flag Markdown tables, YAML frontmatter, or normal separators.

## Commands Run by CI

```bash
python scripts/validate_repo.py
python -m pytest
daedalus --help
daedalus init-check
```

## Human Approval Model

CI validation does not approve infrastructure work.

CI only verifies repository quality and tooling health.

Human approval is still required before:

- Applying generated configurations
- Running generated infrastructure commands
- Deploying Infrastructure as Code
- Changing access or identity systems
- Accepting residual risk

## Failure Handling

If CI fails:

1. Open the failed GitHub Actions run.
2. Read the failing step.
3. Reproduce the command locally when possible.
4. Fix the issue.
5. Commit the fix.
6. Push again.
7. Confirm CI passes.

## Completion Criteria

CI validation is healthy when:

- Repository validation passes
- CLI tests pass
- CLI smoke checks pass
- GitHub Actions reports a green check
