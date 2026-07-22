#!/usr/bin/env python3
"""Install GitHub assets for github-sdd-scrum-ficct without silent overwrites."""

from __future__ import annotations

import argparse
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Asset:
    source_name: str
    target: str


ASSETS = (
    Asset("github-issue-feature.yml", ".github/ISSUE_TEMPLATE/feature.yml"),
    Asset("github-issue-task.yml", ".github/ISSUE_TEMPLATE/task.yml"),
    Asset("github-issue-evidence.yml", ".github/ISSUE_TEMPLATE/evidence.yml"),
    Asset("pull_request_template.md", ".github/pull_request_template.md"),
    Asset("sdd-gate.yml", ".github/workflows/sdd-gate.yml"),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    default_templates = Path(__file__).resolve().parent.parent / "templates"
    parser = argparse.ArgumentParser(
        description="Copy github-sdd-scrum-ficct assets into a project's .github directory."
    )
    parser.add_argument(
        "--root",
        default=".",
        type=Path,
        help="Destination project root. Defaults to current directory.",
    )
    parser.add_argument(
        "--templates",
        default=default_templates,
        type=Path,
        help="Directory containing extension templates.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show files that would be copied without modifying the project.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing target files when their content differs.",
    )
    return parser.parse_args(argv)


def relative_to_root(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def read_bytes(path: Path) -> bytes:
    return path.read_bytes()


def plan_asset(asset: Asset, templates: Path, root: Path, force: bool) -> tuple[str, Path, Path]:
    source = templates / asset.source_name
    target = root / asset.target

    if not source.is_file():
        return "missing-source", source, target
    if not target.exists():
        return "create", source, target
    if not target.is_file():
        return "conflict", source, target
    if read_bytes(source) == read_bytes(target):
        return "skip", source, target
    if force:
        return "overwrite", source, target
    return "conflict", source, target


def copy_asset(action: str, source: Path, target: Path, dry_run: bool) -> None:
    if dry_run or action not in {"create", "overwrite"}:
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    root = args.root.resolve()
    templates = args.templates.resolve()

    prefix = "DRY-RUN " if args.dry_run else ""
    exit_code = 0

    if not root.exists():
        if args.dry_run:
            print(f"{prefix}root-missing {root} (no changes will be made)")
        else:
            print(f"error: destination root not found: {root}", file=sys.stderr)
            return 1
    elif not root.is_dir():
        print(f"error: destination root is not a directory: {root}", file=sys.stderr)
        return 1

    if not templates.is_dir():
        print(f"error: templates directory not found: {templates}", file=sys.stderr)
        return 1

    for asset in ASSETS:
        action, source, target = plan_asset(asset, templates, root, args.force)
        target_label = relative_to_root(target, root)

        if action == "missing-source":
            print(f"{prefix}missing-source {asset.source_name} -> {target_label}")
            exit_code = 1
            continue

        if action == "conflict":
            print(
                f"{prefix}conflict {target_label} "
                f"(existing file differs; rerun with --force to overwrite)"
            )
            exit_code = 1
            continue

        print(f"{prefix}{action} {target_label}")
        copy_asset(action, source, target, args.dry_run)

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
