#!/usr/bin/env python3
"""Validate baseline Daedalus repository structure.

This script intentionally uses only the Python standard library so it can run
inside GitHub Actions without installing dependencies.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


REQUIRED_PATHS = [
    "README.md",
    "docs/DAEDALUS-OPERATING-MANUAL.md",
    "docs/CLI-USAGE.md",
    "docs/PORTFOLIO-SUMMARY.md",
    "docs/PROJECT-INDEX.md",
    "docs/QUICKSTART.md",
    "docs/ROADMAP.md",
    "docs/WORKFLOW-MAP.md",
    "docs/workflows/engineering-request-workflow.md",
    "docs/workflows/engineering-package-workflow.md",
    "docs/workflows/security-review-workflow.md",
    "docs/workflows/validation-and-rollback-workflow.md",
    "docs/workflows/iac-generation-guardrails.md",
    "docs/workflows/adr-workflow.md",
    "docs/workflows/ci-validation-workflow.md",
    "prompts/system/daedalus-operating-rules.md",
    "prompts/workflows/engineering-request-review.md",
    "prompts/workflows/security-review.md",
    "prompts/workflows/validation-checklist.md",
    "prompts/workflows/rollback-plan.md",
    "prompts/workflows/iac-generation.md",
    "prompts/workflows/adr-generation.md",
    "prompts/output-contracts/engineering-package.md",
    "prompts/output-contracts/iac-package.md",
    "templates/engineering-package-template.md",
    "templates/security-review-template.md",
    "templates/validation-checklist-template.md",
    "templates/rollback-plan-template.md",
    "templates/iac-package-template.md",
    "templates/adr-template.md",
    "schemas/engineering-package.schema.json",
    "schemas/security-review.schema.json",
    "schemas/validation-checklist.schema.json",
    "schemas/rollback-plan.schema.json",
    "schemas/iac-package.schema.json",
    "schemas/adr.schema.json",
    "memory/README.md",
    "memory/architecture/current-lab-context.md",
    "memory/decisions/README.md",
    "memory/decisions/0001-project-memory.md",
    "memory/outputs/README.md",
    "memory/plans/README.md",
    "memory/rollback/README.md",
    "memory/threat-models/README.md",
    "memory/validation/README.md",
    ".github/ISSUE_TEMPLATE/engineering-request.md",
    ".github/ISSUE_TEMPLATE/bug-report.md",
    ".github/ISSUE_TEMPLATE/documentation-update.md",
    ".github/ISSUE_TEMPLATE/workflow-improvement.md",
    ".github/pull_request_template.md",
    ".github/workflows/validate-repo.yml",
    "examples/end-to-end/internal-docs-service/01-engineering-request.md",
    "examples/end-to-end/internal-docs-service/02-readiness-review.md",
    "examples/end-to-end/internal-docs-service/03-engineering-package.md",
    "examples/end-to-end/internal-docs-service/04-security-review.md",
    "examples/end-to-end/internal-docs-service/05-validation-checklist.md",
    "examples/end-to-end/internal-docs-service/06-rollback-plan.md",
    "examples/end-to-end/internal-docs-service/07-adr.md",
]


REQUIRED_DIRECTORIES = [
    ".github",
    ".github/ISSUE_TEMPLATE",
    ".github/workflows",
    "daedalus",
    "daedalus/generators",
    "docs",
    "docs/diagrams",
    "docs/workflows",
    "examples",
    "examples/cli",
    "examples/end-to-end",
    "memory",
    "memory/architecture",
    "memory/decisions",
    "memory/outputs",
    "memory/plans",
    "memory/rollback",
    "memory/threat-models",
    "memory/validation",
    "prompts",
    "prompts/output-contracts",
    "prompts/system",
    "prompts/workflows",
    "schemas",
    "scripts",
    "templates",
    "templates/ansible",
    "templates/kubernetes",
    "templates/scripts",
    "templates/terraform",
    "tests",
]


# Match real Git conflict marker lines only.
# Do not flag Markdown horizontal rules, YAML frontmatter, or table separators.
FORBIDDEN_PATTERNS = [
    re.compile(r"(?m)^<<<<<<< .+$"),
    re.compile(r"(?m)^=======$"),
    re.compile(r"(?m)^>>>>>>> .+$"),
]


SECRET_PATTERNS = [
    re.compile(r"(?i)api[_-]?key\s*=\s*['\"][A-Za-z0-9_\-]{16,}['\"]"),
    re.compile(r"(?i)token\s*=\s*['\"][A-Za-z0-9_\-]{16,}['\"]"),
    re.compile(r"(?i)password\s*=\s*['\"][^'\"]{8,}['\"]"),
    re.compile(r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]


MARKDOWN_HEADING_EXEMPTIONS = [
    ".github/ISSUE_TEMPLATE/",
]


def print_header(message: str) -> None:
    print(f"\n== {message} ==")


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)
    print(f"FAIL: {message}")


def pass_check(message: str) -> None:
    print(f"PASS: {message}")


def validate_required_directories(failures: list[str]) -> None:
    print_header("Required directories")
    for rel_path in REQUIRED_DIRECTORIES:
        path = REPO_ROOT / rel_path
        if path.is_dir():
            pass_check(rel_path)
        else:
            fail(f"Missing required directory: {rel_path}", failures)


def validate_required_paths(failures: list[str]) -> None:
    print_header("Required files")
    for rel_path in REQUIRED_PATHS:
        path = REPO_ROOT / rel_path
        if path.is_file():
            pass_check(rel_path)
        else:
            fail(f"Missing required file: {rel_path}", failures)


def validate_json_schemas(failures: list[str]) -> None:
    print_header("JSON schema validity")
    schema_dir = REPO_ROOT / "schemas"
    if not schema_dir.exists():
        fail("schemas directory does not exist", failures)
        return

    schema_files = sorted(schema_dir.glob("*.json"))
    if not schema_files:
        fail("No JSON schema files found", failures)
        return

    for schema_file in schema_files:
        try:
            with schema_file.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
        except json.JSONDecodeError as exc:
            fail(f"Invalid JSON in {schema_file.relative_to(REPO_ROOT)}: {exc}", failures)
            continue

        if "$schema" not in data:
            fail(f"Schema missing $schema field: {schema_file.relative_to(REPO_ROOT)}", failures)
        elif "title" not in data:
            fail(f"Schema missing title field: {schema_file.relative_to(REPO_ROOT)}", failures)
        else:
            pass_check(str(schema_file.relative_to(REPO_ROOT)))


def iter_text_files() -> list[Path]:
    allowed_suffixes = {
        ".md",
        ".json",
        ".yml",
        ".yaml",
        ".sh",
        ".ps1",
        ".tf",
        ".py",
        ".txt",
        ".toml",
        ".mmd",
    }

    ignored_dirs = {
        ".git",
        "__pycache__",
        ".pytest_cache",
        ".venv",
        "venv",
        "node_modules",
        "build",
        "dist",
    }

    files: list[Path] = []

    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue

        if any(part in ignored_dirs for part in path.parts):
            continue

        if path.suffix.lower() in allowed_suffixes:
            files.append(path)

    return files


def validate_no_merge_conflicts(failures: list[str]) -> None:
    print_header("Merge conflict markers")
    found = False

    for file_path in iter_text_files():
        text = file_path.read_text(encoding="utf-8", errors="ignore")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                found = True
                fail(f"Possible merge conflict marker in {file_path.relative_to(REPO_ROOT)}", failures)
                break

    if not found:
        pass_check("No merge conflict markers found")


def validate_no_obvious_secrets(failures: list[str]) -> None:
    print_header("Obvious plaintext secret patterns")
    found = False

    for file_path in iter_text_files():
        text = file_path.read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                found = True
                fail(f"Possible plaintext secret in {file_path.relative_to(REPO_ROOT)}", failures)
                break

    if not found:
        pass_check("No obvious plaintext secret patterns found")


def markdown_heading_exempt(file_path: Path) -> bool:
    rel = str(file_path.relative_to(REPO_ROOT)).replace("\\", "/")
    return any(rel.startswith(prefix) for prefix in MARKDOWN_HEADING_EXEMPTIONS)


def validate_markdown_headings(failures: list[str]) -> None:
    print_header("Markdown heading checks")
    markdown_files = sorted(REPO_ROOT.rglob("*.md"))

    if not markdown_files:
        fail("No Markdown files found", failures)
        return

    missing_heading = []

    for file_path in markdown_files:
        if any(part in {".git", "node_modules"} for part in file_path.parts):
            continue

        if markdown_heading_exempt(file_path):
            continue

        text = file_path.read_text(encoding="utf-8", errors="ignore")
        if not text.lstrip().startswith("# "):
            missing_heading.append(str(file_path.relative_to(REPO_ROOT)))

    if missing_heading:
        for rel_path in missing_heading:
            fail(f"Markdown file missing top-level heading: {rel_path}", failures)
    else:
        pass_check("Markdown files have top-level headings")


def main() -> int:
    print("Daedalus repository validation starting...")
    print(f"Repository root: {REPO_ROOT}")

    failures: list[str] = []

    validate_required_directories(failures)
    validate_required_paths(failures)
    validate_json_schemas(failures)
    validate_no_merge_conflicts(failures)
    validate_no_obvious_secrets(failures)
    validate_markdown_headings(failures)

    print_header("Validation result")

    if failures:
        print(f"Validation failed with {len(failures)} issue(s):")
        for item in failures:
            print(f"- {item}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
