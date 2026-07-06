# Release Checklist

## Purpose

This checklist defines the steps required before tagging a Daedalus release.

A release should represent a known-good repository state with passing validation, tests, and documentation.

## Release Candidate Information

**Release version:**  
**Release date:**  
**Release owner:**  
**Release status:** Proposed | Approved | Tagged | Superseded  

## Pre-Release Checklist

### Repository Health

- [ ] Working tree is clean
- [ ] Latest commit is pushed to `main`
- [ ] GitHub Actions are green
- [ ] No unresolved merge conflict markers
- [ ] No plaintext secrets are present
- [ ] Required repository structure is present

### Local Validation

Run:

```powershell
python scripts/validate_repo.py
python scripts/validate_schemas.py
python -m pytest
python -m daedalus.cli init-check
```

Confirm:

- [ ] Repository validation passes
- [ ] Schema validation passes
- [ ] Pytest passes
- [ ] CLI init-check passes

### Documentation Review

Confirm the following are current:

- [ ] `README.md`
- [ ] `CHANGELOG.md`
- [ ] `docs/ROADMAP.md`
- [ ] `docs/QUICKSTART.md`
- [ ] `docs/PROJECT-INDEX.md`
- [ ] `docs/ARCHITECTURE-OVERVIEW.md`
- [ ] `docs/DAEDALUS-OPERATING-MANUAL.md`
- [ ] `docs/PORTFOLIO-SUMMARY.md`

### Workflow Review

Confirm the following are present and accurate:

- [ ] Engineering request workflow
- [ ] Engineering package workflow
- [ ] Security review workflow
- [ ] Validation and rollback workflow
- [ ] IaC generation guardrails
- [ ] ADR workflow
- [ ] CI validation workflow
- [ ] Schema validation workflow

### Safety Review

Confirm release preserves:

- [ ] Proposed-by-default artifact model
- [ ] Human approval gates
- [ ] No automatic infrastructure execution
- [ ] No plaintext secrets
- [ ] Validation requirements
- [ ] Rollback requirements
- [ ] Security review triggers
- [ ] ADR decision tracking

### CLI Review

Confirm CLI commands work:

```powershell
python -m daedalus.cli --help
python -m daedalus.cli init-check
```

Optional smoke commands:

```powershell
python -m daedalus.cli new-request "Release smoke test"
python -m daedalus.cli new-package "Release smoke test"
python -m daedalus.cli new-adr "Release smoke test decision"
python -m daedalus.cli new-validation "Release smoke test"
python -m daedalus.cli new-rollback "Release smoke test"
```

If optional smoke files are created only for testing, remove them before release unless intentionally keeping them.

## Tagging Procedure

After validation passes and the working tree is clean:

```powershell
git tag v0.2.0
git push origin v0.2.0
```

## Rollback Procedure

If a release tag is created incorrectly:

```powershell
git tag -d v0.2.0
git push origin :refs/tags/v0.2.0
```

Only delete a remote tag if it was created in error and the correction is intentional.

## Post-Release Checklist

- [ ] Confirm tag exists on GitHub
- [ ] Confirm release notes are accurate
- [ ] Confirm CI is green on the tagged commit
- [ ] Update roadmap if needed
- [ ] Begin next Unreleased section in changelog

## Human Approval Gate

Human approval is required before:

- Creating a release tag
- Publishing release notes
- Treating a release as a stable baseline
- Deleting or replacing a release tag
