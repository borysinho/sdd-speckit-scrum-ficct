#!/usr/bin/env python3
"""Validate minimal SDD/Scrum FICCT traceability across Markdown artifacts."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ValidationResult:
    ok: bool
    messages: tuple[str, ...]


ID_PATTERNS = {
    "requirement": re.compile(r"(?<![A-Z])(?:RF|RNF|RN)-\d{3}\b"),
    "criterion": re.compile(r"(?<![A-Z])CA-\d{3}\b"),
    "story": re.compile(r"(?<![A-Z])HU-\d{3}\b"),
    "task": re.compile(r"(?<![A-Z])TASK-\d{3}\b"),
}


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", type=Path, help="Project root to validate.")
    parser.add_argument("--strict", action="store_true", help="Fail when any required relation is missing.")
    return parser.parse_args(argv)


def iter_markdown_lines(root: Path) -> list[str]:
    search_roots = (root / "specs", root / "docs" / "sdd", root / "docs" / "scrum")
    lines: list[str] = []
    for search_root in search_roots:
        if not search_root.exists():
            continue
        for path in sorted(search_root.rglob("*.md")):
            text = path.read_text(encoding="utf-8", errors="ignore")
            lines.extend(text.splitlines())
    return lines


def ids_for(pattern_name: str, text: str) -> set[str]:
    return set(ID_PATTERNS[pattern_name].findall(text))


def has_relation(lines: list[str], left: str, right_pattern: re.Pattern[str]) -> bool:
    return any(left in line and right_pattern.search(line) for line in lines)


def has_task_relation(lines: list[str], task: str) -> bool:
    for line in lines:
        if task not in line:
            continue
        if ID_PATTERNS["story"].search(line) and ID_PATTERNS["requirement"].search(line):
            return True
    return False


def validate_traceability(root: Path, strict: bool = False) -> ValidationResult:
    root = root.resolve()
    if not root.exists():
        return ValidationResult(False, (f"root not found: {root}",))

    lines = iter_markdown_lines(root)
    text = "\n".join(lines)
    messages: list[str] = []

    requirements = ids_for("requirement", text)
    criteria = ids_for("criterion", text)
    stories = ids_for("story", text)
    tasks = ids_for("task", text)

    minimum_ids = {
        "requisito RF/RNF/RN": requirements,
        "criterio CA": criteria,
        "historia HU": stories,
        "tarea TASK": tasks,
    }
    for label, values in minimum_ids.items():
        if not values:
            messages.append(f"No se encontro trazabilidad minima para {label}.")

    for requirement in sorted(requirements):
        if not has_relation(lines, requirement, ID_PATTERNS["criterion"]):
            messages.append(f"{requirement} no tiene criterio de aceptacion vinculado.")

    for story in sorted(stories):
        if not has_relation(lines, story, ID_PATTERNS["requirement"]):
            messages.append(f"{story} no tiene requisito vinculado.")

    for task in sorted(tasks):
        if not has_task_relation(lines, task):
            messages.append(f"{task} no tiene HU y requisito vinculados en la misma traza.")

    if not strict:
        messages = [message for message in messages if message.startswith("No se encontro")]

    return ValidationResult(not messages, tuple(messages))


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    result = validate_traceability(args.root, strict=args.strict)

    if result.ok:
        print("Trazabilidad minima SDD/Scrum encontrada.")
        return 0

    for message in result.messages:
        print(f"::error::{message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
