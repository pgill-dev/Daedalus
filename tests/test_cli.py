"""CLI behavior tests for Daedalus."""

from __future__ import annotations

from pathlib import Path

from daedalus.cli import main


def create_minimal_repo(tmp_path: Path) -> Path:
    """Create the minimum files needed for Daedalus repo detection."""

    (tmp_path / "docs").mkdir()
    (tmp_path / "memory").mkdir()
    (tmp_path / "README.md").write_text("# Daedalus\n", encoding="utf-8")
    (tmp_path / "docs" / "DAEDALUS-OPERATING-MANUAL.md").write_text(
        "# Daedalus Operating Manual\n",
        encoding="utf-8",
    )
    (tmp_path / "memory" / "README.md").write_text(
        "# Daedalus Project Memory\n",
        encoding="utf-8",
    )
    return tmp_path


def test_cli_init_check_passes_in_repo(tmp_path: Path, monkeypatch) -> None:
    """init-check should pass when run inside a Daedalus repository."""

    repo = create_minimal_repo(tmp_path)
    monkeypatch.chdir(repo)

    assert main(["init-check"]) == 0


def test_cli_help_exits_successfully() -> None:
    """--help should exit successfully through argparse."""

    try:
        main(["--help"])
    except SystemExit as exc:
        assert exc.code == 0


def test_cli_new_request_creates_file(tmp_path: Path, monkeypatch) -> None:
    """new-request should create an engineering request artifact."""

    repo = create_minimal_repo(tmp_path)
    monkeypatch.chdir(repo)

    assert main(["new-request", "Deploy Internal Docs"]) == 0

    generated = list((repo / "memory" / "plans").glob("*deploy-internal-docs-engineering-request.md"))
    assert len(generated) == 1
    assert generated[0].read_text(encoding="utf-8").startswith(
        "# Engineering Request: Deploy Internal Docs"
    )


def test_cli_new_package_creates_file(tmp_path: Path, monkeypatch) -> None:
    """new-package should create an engineering package artifact."""

    repo = create_minimal_repo(tmp_path)
    monkeypatch.chdir(repo)

    assert main(["new-package", "Deploy Internal Docs"]) == 0

    generated = list((repo / "memory" / "outputs").glob("*deploy-internal-docs-engineering-package.md"))
    assert len(generated) == 1
    assert generated[0].read_text(encoding="utf-8").startswith(
        "# Engineering Package: Deploy Internal Docs"
    )


def test_cli_new_adr_creates_file(tmp_path: Path, monkeypatch) -> None:
    """new-adr should create an ADR artifact."""

    repo = create_minimal_repo(tmp_path)
    (repo / "memory" / "decisions").mkdir(parents=True)
    (repo / "memory" / "decisions" / "0001-project-memory.md").write_text(
        "# ADR-0001: Establish Project Memory\n",
        encoding="utf-8",
    )
    monkeypatch.chdir(repo)

    assert main(["new-adr", "Use Identity Aware Access"]) == 0

    generated = repo / "memory" / "decisions" / "0002-use-identity-aware-access.md"
    assert generated.exists()
    assert generated.read_text(encoding="utf-8").startswith(
        "# ADR-0002: Use Identity Aware Access"
    )


def test_cli_new_validation_creates_file(tmp_path: Path, monkeypatch) -> None:
    """new-validation should create a validation checklist artifact."""

    repo = create_minimal_repo(tmp_path)
    monkeypatch.chdir(repo)

    assert main(["new-validation", "Deploy Internal Docs"]) == 0

    generated = list((repo / "memory" / "validation").glob("*deploy-internal-docs-validation-checklist.md"))
    assert len(generated) == 1
    assert generated[0].read_text(encoding="utf-8").startswith(
        "# Validation Checklist: Deploy Internal Docs"
    )


def test_cli_new_rollback_creates_file(tmp_path: Path, monkeypatch) -> None:
    """new-rollback should create a rollback plan artifact."""

    repo = create_minimal_repo(tmp_path)
    monkeypatch.chdir(repo)

    assert main(["new-rollback", "Deploy Internal Docs"]) == 0

    generated = list((repo / "memory" / "rollback").glob("*deploy-internal-docs-rollback-plan.md"))
    assert len(generated) == 1
    assert generated[0].read_text(encoding="utf-8").startswith(
        "# Rollback Plan: Deploy Internal Docs"
    )
