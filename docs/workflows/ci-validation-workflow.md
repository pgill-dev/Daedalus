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
- Schema metadata
- Schema ID uniqueness
- Schema title uniqueness
- Real Git merge conflict markers
- Obvious plaintext secret patterns
- Markdown top-level headings where appropriate
- CLI package installation
- CLI unit tests
- CLI smoke commands

## Commands Run by CI

```bash
python scripts/validate_repo.py
python scripts/validate_schemas.py
python -m pytest
daedalus --help
daedalus init-check
```

## Validation Layers

### Repository Validation

Repository validation confirms that expected files and directories exist and that common repository hygiene issues are not present.

Script:

```text
scripts/validate_repo.py
```

### Schema Validation

Schema validation confirms that JSON schemas are structurally healthy, have required metadata, and do not duplicate schema IDs or titles.

Script:

```text
scripts/validate_schemas.py
```

### CLI Tests

CLI tests confirm that artifact generators and repository detection continue to work.

Test path:

```text
tests/
```

### CLI Smoke Checks

CLI smoke checks confirm that the installed command is available and can detect the repository.

Commands:

```bash
daedalus --help
daedalus init-check
```

## Important Validation Notes

GitHub issue templates use YAML frontmatter and are exempt from the top-level heading check.

The merge conflict check flags real Git conflict marker lines.

Safe written example:

```text
&lt;&lt;&lt;&lt;&lt;&lt;&lt; branch
--- conflict separator ---
&gt;&gt;&gt;&gt;&gt;&gt;&gt; branch
```

This documentation intentionally avoids writing the exact raw marker sequence so the repository validator does not flag the explanation itself.

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

## Common Failure Types

### Missing Required File

The repository validation script expects a file that does not exist.

Fix by adding the missing file or updating `scripts/validate_repo.py` if the requirement changed intentionally.

### Invalid JSON

A schema file contains invalid JSON.

Fix the JSON syntax and rerun validation.

### Duplicate Schema ID or Title

A schema file has the same `$id` or `title` as another schema.

Update the duplicate metadata so each schema is unique.

### Merge Conflict Marker

A file contains unresolved Git conflict marker lines from a merge.

Remove the marker lines and keep the intended content.

### CLI Test Failure

A CLI behavior changed but tests were not updated, or a real bug was introduced.

Fix the CLI or update the tests to match the intended behavior.

## Completion Criteria

CI validation is healthy when:

- Repository validation passes
- Schema validation passes
- CLI tests pass
- CLI smoke checks pass
- GitHub Actions reports a green check
