"""Daedalus CLI entry point."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from daedalus import __version__
from daedalus.generators.adr import create_adr
from daedalus.generators.engineering_package import create_engineering_package
from daedalus.generators.engineering_request import create_engineering_request
from daedalus.generators.rollback import create_rollback_plan
from daedalus.generators.validation import create_validation_checklist
from daedalus.paths import find_repo_root


def add_common_new_args(parser: argparse.ArgumentParser) -> None:
    """Add common generator arguments."""

    parser.add_argument("title", help="Artifact title")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the target file if it already exists",
    )


def cmd_init_check(_: argparse.Namespace) -> int:
    """Confirm that the CLI can locate the repository root."""

    root = find_repo_root()
    print(f"Daedalus repository detected: {root}")
    print("Init check passed.")
    return 0


def cmd_new_request(args: argparse.Namespace) -> int:
    root = find_repo_root()
    path = create_engineering_request(root, args.title, force=args.force)
    print(f"Created engineering request: {path.relative_to(root)}")
    return 0


def cmd_new_package(args: argparse.Namespace) -> int:
    root = find_repo_root()
    path = create_engineering_package(root, args.title, force=args.force)
    print(f"Created engineering package: {path.relative_to(root)}")
    return 0


def cmd_new_adr(args: argparse.Namespace) -> int:
    root = find_repo_root()
    path = create_adr(root, args.title, force=args.force)
    print(f"Created ADR: {path.relative_to(root)}")
    return 0


def cmd_new_validation(args: argparse.Namespace) -> int:
    root = find_repo_root()
    path = create_validation_checklist(root, args.title, force=args.force)
    print(f"Created validation checklist: {path.relative_to(root)}")
    return 0


def cmd_new_rollback(args: argparse.Namespace) -> int:
    root = find_repo_root()
    path = create_rollback_plan(root, args.title, force=args.force)
    print(f"Created rollback plan: {path.relative_to(root)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser."""

    parser = argparse.ArgumentParser(
        prog="daedalus",
        description="Local CLI helpers for the Daedalus engineering platform.",
    )
    parser.add_argument("--version", action="version", version=f"daedalus {__version__}")

    subparsers = parser.add_subparsers(dest="command", required=True)

    init_check = subparsers.add_parser(
        "init-check",
        help="Confirm the current directory is inside a Daedalus repository",
    )
    init_check.set_defaults(func=cmd_init_check)

    new_request = subparsers.add_parser(
        "new-request",
        help="Create a proposed engineering request under memory/plans",
    )
    add_common_new_args(new_request)
    new_request.set_defaults(func=cmd_new_request)

    new_package = subparsers.add_parser(
        "new-package",
        help="Create a proposed engineering package under memory/outputs",
    )
    add_common_new_args(new_package)
    new_package.set_defaults(func=cmd_new_package)

    new_adr = subparsers.add_parser(
        "new-adr",
        help="Create a proposed ADR under memory/decisions",
    )
    add_common_new_args(new_adr)
    new_adr.set_defaults(func=cmd_new_adr)

    new_validation = subparsers.add_parser(
        "new-validation",
        help="Create a proposed validation checklist under memory/validation",
    )
    add_common_new_args(new_validation)
    new_validation.set_defaults(func=cmd_new_validation)

    new_rollback = subparsers.add_parser(
        "new-rollback",
        help="Create a proposed rollback plan under memory/rollback",
    )
    add_common_new_args(new_rollback)
    new_rollback.set_defaults(func=cmd_new_rollback)

    return parser


def main(argv: list[str] | None = None) -> int:
    """Run Daedalus CLI."""

    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        return args.func(args)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
