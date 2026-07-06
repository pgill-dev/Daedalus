# Daedalus Project Index

## Purpose

This index maps the Daedalus repository so humans and Daedalus can quickly find the correct workflow, prompt, template, schema, or memory location.

## Core Documents

| Path | Purpose |
|---|---|
| `README.md` | Main project overview |
| `docs/ARCHITECTURE-OVERVIEW.md` | High-level platform architecture |
| `docs/DAEDALUS-OPERATING-MANUAL.md` | Main operating manual |
| `docs/CLI-USAGE.md` | CLI usage documentation |
| `docs/PORTFOLIO-SUMMARY.md` | Portfolio-ready project summary |
| `docs/PROJECT-INDEX.md` | Repository index |
| `docs/QUICKSTART.md` | How to use the repository |
| `docs/ROADMAP.md` | Project roadmap |
| `docs/WORKFLOW-MAP.md` | Workflow relationship map |
| `memory/README.md` | Project memory overview |

## Workflows

| Path | Purpose |
|---|---|
| `docs/workflows/engineering-request-workflow.md` | Defines request intake |
| `docs/workflows/engineering-package-workflow.md` | Defines engineering package process |
| `docs/workflows/security-review-workflow.md` | Defines security review process |
| `docs/workflows/validation-and-rollback-workflow.md` | Defines validation and rollback process |
| `docs/workflows/iac-generation-guardrails.md` | Defines safe IaC generation rules |
| `docs/workflows/adr-workflow.md` | Defines architecture decision records |
| `docs/workflows/ci-validation-workflow.md` | Defines repository, schema, and CLI CI validation |
| `docs/workflows/schema-validation-workflow.md` | Defines standalone JSON schema validation |

## Diagrams

| Path | Purpose |
|---|---|
| `docs/diagrams/README.md` | Diagram index |
| `docs/diagrams/daedalus-workflow.mmd` | End-to-end workflow diagram |
| `docs/diagrams/repository-architecture.mmd` | Repository architecture diagram |
| `docs/diagrams/human-in-the-loop-model.mmd` | Human approval model diagram |
| `docs/diagrams/zero-trust-lab-relationship.mmd` | Daedalus and lab relationship diagram |
| `docs/diagrams/platform-architecture.mmd` | Layered platform architecture diagram |

## GitHub Issue Templates

| Path | Purpose |
|---|---|
| `.github/ISSUE_TEMPLATE/engineering-request.md` | Engineering request intake form |
| `.github/ISSUE_TEMPLATE/bug-report.md` | Bug report form |
| `.github/ISSUE_TEMPLATE/documentation-update.md` | Documentation update form |
| `.github/ISSUE_TEMPLATE/workflow-improvement.md` | Workflow improvement form |

## GitHub Workflows

| Path | Purpose |
|---|---|
| `.github/workflows/validate-repo.yml` | Runs repository validation, schema validation, CLI tests, and CLI smoke checks |

## Workflow Prompts

| Path | Purpose |
|---|---|
| `prompts/workflows/engineering-request-review.md` | Reviews request readiness |
| `prompts/workflows/security-review.md` | Performs proposed security review |
| `prompts/workflows/validation-checklist.md` | Generates validation checklist |
| `prompts/workflows/rollback-plan.md` | Generates rollback plan |
| `prompts/workflows/iac-generation.md` | Generates proposed IaC packages |
| `prompts/workflows/adr-generation.md` | Generates ADRs |

## Output Contracts

| Path | Purpose |
|---|---|
| `prompts/output-contracts/engineering-package.md` | Engineering package structure |
| `prompts/output-contracts/iac-package.md` | IaC package structure |

## System Prompts

| Path | Purpose |
|---|---|
| `prompts/system/daedalus-operating-rules.md` | Core Daedalus behavior rules |

## Templates

| Path | Purpose |
|---|---|
| `templates/engineering-package-template.md` | Engineering package template |
| `templates/security-review-template.md` | Security review template |
| `templates/validation-checklist-template.md` | Validation checklist template |
| `templates/rollback-plan-template.md` | Rollback plan template |
| `templates/iac-package-template.md` | IaC package template |
| `templates/adr-template.md` | ADR template |
| `templates/ansible/playbook-skeleton.yml` | Safe Ansible skeleton |
| `templates/kubernetes/base-manifest.yaml` | Safe Kubernetes skeleton |
| `templates/terraform/main.tf` | Terraform/OpenTofu main skeleton |
| `templates/terraform/variables.tf` | Terraform/OpenTofu variables skeleton |
| `templates/terraform/outputs.tf` | Terraform/OpenTofu outputs skeleton |
| `templates/scripts/safe-bash-template.sh` | Safe Bash script template |
| `templates/scripts/safe-powershell-template.ps1` | Safe PowerShell script template |

## Schemas

| Path | Purpose |
|---|---|
| `schemas/engineering-package.schema.json` | Engineering package schema |
| `schemas/security-review.schema.json` | Security review schema |
| `schemas/validation-checklist.schema.json` | Validation checklist schema |
| `schemas/rollback-plan.schema.json` | Rollback plan schema |
| `schemas/iac-package.schema.json` | IaC package schema |
| `schemas/adr.schema.json` | ADR schema |

## CLI and Tooling

| Path | Purpose |
|---|---|
| `daedalus/cli.py` | CLI entry point |
| `daedalus/generators/` | Artifact generators |
| `scripts/validate_repo.py` | Repository validation script |
| `scripts/validate_schemas.py` | JSON schema validation script |
| `tests/` | CLI, generator, repo detection, and schema validation tests |
| `pytest.ini` | Pytest configuration |
| `pyproject.toml` | Python project metadata |

## Memory

| Path | Purpose |
|---|---|
| `memory/architecture/` | Architecture notes |
| `memory/decisions/` | ADRs and decision records |
| `memory/outputs/` | Generated outputs |
| `memory/plans/` | Engineering plans and requests |
| `memory/rollback/` | Rollback plans and records |
| `memory/threat-models/` | Threat models and security reviews |
| `memory/validation/` | Validation checklists and results |

## Examples

| Path | Purpose |
|---|---|
| `examples/engineering-request.md` | Example engineering request |
| `examples/end-to-end/internal-docs-service/` | Complete end-to-end workflow example |
| `examples/cli/` | CLI usage examples |
