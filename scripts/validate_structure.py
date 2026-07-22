#!/usr/bin/env python3
"""Validate the minimal SDD/Scrum FICCT project structure."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ValidationResult:
    ok: bool
    messages: tuple[str, ...]


REQUIRED_PATHS = (
    ".github/ISSUE_TEMPLATE/feature.yml",
    ".github/ISSUE_TEMPLATE/task.yml",
    ".github/ISSUE_TEMPLATE/evidence.yml",
    ".github/pull_request_template.md",
    ".github/workflows/sdd-gate.yml",
    "specs",
    "docs/sdd",
    "docs/scrum",
    "docs/evidencias",
)

STRICT_FILES = (
    "docs/sdd/traceability-matrix.md",
    "docs/scrum/f1-sprint-review.md",
    "docs/scrum/f2-retrospective.md",
    "docs/scrum/f3-product-backlog.md",
    "docs/scrum/f4-user-stories.md",
    "docs/scrum/f5-sprint-backlog.md",
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", type=Path, help="Project root to validate.")
    parser.add_argument("--strict", action="store_true", help="Require Scrum and traceability artifacts.")
    return parser.parse_args(argv)


def validate_structure(root: Path, strict: bool = False) -> ValidationResult:
    root = root.resolve()
    messages: list[str] = []

    if not root.exists():
        return ValidationResult(False, (f"root not found: {root}",))
    if not root.is_dir():
        return ValidationResult(False, (f"root is not a directory: {root}",))

    for relative in REQUIRED_PATHS:
        if not (root / relative).exists():
            messages.append(f"Falta estructura requerida: {relative}")

    spec_files = sorted((root / "specs").glob("*/spec.md")) if (root / "specs").is_dir() else []
    if not spec_files:
        messages.append("Falta al menos una especificacion en specs/<feature>/spec.md")

    if strict:
        for relative in STRICT_FILES:
            if not (root / relative).is_file():
                messages.append(f"Falta artefacto requerido en modo strict: {relative}")

        for spec_file in spec_files:
            feature_dir = spec_file.parent
            for filename in ("plan.md", "tasks.md"):
                if not (feature_dir / filename).is_file():
                    messages.append(
                        f"Falta artefacto de feature: {feature_dir.relative_to(root).as_posix()}/{filename}"
                    )

    return ValidationResult(not messages, tuple(messages))


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    result = validate_structure(args.root, strict=args.strict)

    if result.ok:
        print("Estructura SDD/Scrum minima encontrada.")
        return 0

    for message in result.messages:
        print(f"::error::{message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
