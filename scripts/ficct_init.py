#!/usr/bin/env python3
"""Materialize FICCT SDD/Scrum assets in a Spec Kit project."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from unicodedata import normalize

from generate_report import generate_report
from install_github_assets import ASSETS, plan_asset
from validate_structure import validate_structure
from validate_traceability import validate_traceability


EXTENSION_ID = "ficct"
CONFIG_TEMPLATE = "github-sdd-scrum-ficct-config.template.yml"
CONFIG_FILE = "github-sdd-scrum-ficct-config.yml"
ADDENDUM_BEGIN = "<!-- BEGIN github-sdd-scrum-ficct constitution addendum -->"
ADDENDUM_END = "<!-- END github-sdd-scrum-ficct constitution addendum -->"


@dataclass(frozen=True)
class Materialization:
    template: str
    target: str


MATERIALIZATIONS = (
    Materialization("spec-template.md", "specs/{feature}/spec.md"),
    Materialization("plan-template.md", "specs/{feature}/plan.md"),
    Materialization("tasks-template.md", "specs/{feature}/tasks.md"),
    Materialization("f3-product-backlog-template.md", "docs/scrum/f3-product-backlog.md"),
    Materialization("f4-user-stories-template.md", "docs/scrum/f4-user-stories.md"),
    Materialization("f5-sprint-backlog-template.md", "docs/scrum/f5-sprint-backlog.md"),
    Materialization("sprint-review-f1-template.md", "docs/scrum/f1-sprint-review.md"),
    Materialization("retrospective-f2-template.md", "docs/scrum/f2-retrospective.md"),
    Materialization("traceability-matrix-template.md", "docs/sdd/traceability-matrix.md"),
    Materialization("sdd-compliance-report-template.md", "docs/evidencias/sdd-compliance-report.md"),
)


@dataclass
class InitResult:
    ok: bool
    messages: list[str]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", type=Path, help="Spec Kit project root.")
    parser.add_argument(
        "--extension-root",
        default=Path(__file__).resolve().parent.parent,
        type=Path,
        help="Installed extension root. Defaults to this script's parent extension directory.",
    )
    parser.add_argument(
        "--feature",
        default=None,
        help="Feature directory name used for specs/<feature>/ artifacts.",
    )
    parser.add_argument(
        "--project-name",
        default=None,
        help="Project name written to the FICCT config. Also used to derive --feature when omitted.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing differing files.")
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Run strict structure and traceability validators after materialization.",
    )
    parser.add_argument(
        "--generate-report",
        action="store_true",
        help="Generate docs/evidencias/sdd-compliance-report.md after materialization.",
    )
    return parser.parse_args(argv)


def slugify(value: str | None) -> str:
    if not value:
        return ""
    ascii_value = normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_value.lower()).strip("-")
    return slug or ""


def copy_file(source: Path, target: Path, force: bool, label: str, messages: list[str]) -> bool:
    if not source.is_file():
        messages.append(f"missing-source {source}")
        return False

    if target.exists():
        if not target.is_file():
            messages.append(f"conflict {target} (target exists and is not a file)")
            return False
        if source.read_bytes() == target.read_bytes():
            messages.append(f"skip {label}")
            return True
        if not force:
            messages.append(f"conflict {label} (existing file differs; use --force to overwrite)")
            return False
        action = "overwrite"
    else:
        action = "create"

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    messages.append(f"{action} {label}")
    return True


def ensure_config(root: Path, extension_root: Path, force: bool, messages: list[str]) -> bool:
    source = extension_root / CONFIG_TEMPLATE
    target = root / ".specify" / "extensions" / EXTENSION_ID / CONFIG_FILE
    label = f".specify/extensions/{EXTENSION_ID}/{CONFIG_FILE}"
    if not source.is_file():
        messages.append(f"missing-source {source}")
        return False
    if target.exists():
        if not target.is_file():
            messages.append(f"conflict {target} (target exists and is not a file)")
            return False
        if not force:
            messages.append(f"skip {label}")
            return True
        action = "overwrite"
    else:
        action = "create"

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    messages.append(f"{action} {label}")
    return True


def yaml_string(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def read_simple_yaml_value(line: str) -> str:
    raw_value = line.split(":", 1)[1].strip()
    if len(raw_value) >= 2 and raw_value[0] == raw_value[-1] and raw_value[0] in {"'", '"'}:
        return raw_value[1:-1]
    return raw_value


def update_project_name(root: Path, project_name: str | None, force: bool, messages: list[str]) -> bool:
    if not project_name:
        return True

    target = root / ".specify" / "extensions" / EXTENSION_ID / CONFIG_FILE
    label = f".specify/extensions/{EXTENSION_ID}/{CONFIG_FILE} project_name"
    if not target.is_file():
        messages.append(f"conflict {label} (config file is missing)")
        return False

    lines = target.read_text(encoding="utf-8").splitlines()
    next_line = f"project_name: {yaml_string(project_name)}"
    updated = False

    for index, line in enumerate(lines):
        if not line.startswith("project_name:"):
            continue
        current = read_simple_yaml_value(line)
        if current == project_name:
            messages.append(f"skip {label}")
            return True
        if current and not force:
            messages.append(f"skip {label} (already set: {current})")
            return True
        lines[index] = next_line
        updated = True
        break

    if not updated:
        lines.insert(0, next_line)

    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    messages.append(f"update {label}")
    return True


def install_assets(root: Path, extension_root: Path, force: bool, messages: list[str]) -> bool:
    ok = True
    templates = extension_root / "templates"
    for asset in ASSETS:
        action, source, target = plan_asset(asset, templates, root, force)
        target_label = asset.target
        if action == "missing-source":
            messages.append(f"missing-source {asset.source_name} -> {target_label}")
            ok = False
            continue
        if action == "conflict":
            messages.append(f"conflict {target_label} (existing file differs; use --force to overwrite)")
            ok = False
            continue
        if action in {"create", "overwrite"}:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        messages.append(f"{action} {target_label}")
    return ok


def materialize_templates(
    root: Path,
    extension_root: Path,
    feature: str,
    force: bool,
    skip_report_template: bool,
    messages: list[str],
) -> bool:
    ok = True
    templates = extension_root / "templates"
    for item in MATERIALIZATIONS:
        if skip_report_template and item.template == "sdd-compliance-report-template.md":
            messages.append("skip docs/evidencias/sdd-compliance-report.md template (generated report requested)")
            continue
        target_rel = item.target.format(feature=feature)
        ok = copy_file(templates / item.template, root / target_rel, force, target_rel, messages) and ok
    return ok


def ensure_constitution_addendum(root: Path, extension_root: Path, force: bool, messages: list[str]) -> bool:
    source = extension_root / "templates" / "constitution-addendum.md"
    target = root / ".specify" / "memory" / "constitution.md"
    if not source.is_file():
        messages.append(f"missing-source {source}")
        return False

    addendum = source.read_text(encoding="utf-8")
    block = f"{ADDENDUM_BEGIN}\n\n{addendum.rstrip()}\n\n{ADDENDUM_END}\n"

    if target.exists():
        if not target.is_file():
            messages.append(f"conflict .specify/memory/constitution.md (target exists and is not a file)")
            return False
        current = target.read_text(encoding="utf-8")
        if ADDENDUM_BEGIN in current and ADDENDUM_END in current:
            if not force:
                messages.append("skip .specify/memory/constitution.md addendum")
                return True
            before = current.split(ADDENDUM_BEGIN, 1)[0].rstrip()
            after = current.split(ADDENDUM_END, 1)[1].lstrip()
            next_text = f"{before}\n\n{block}"
            if after:
                next_text += f"\n{after}"
            target.write_text(next_text, encoding="utf-8")
            messages.append("overwrite .specify/memory/constitution.md addendum")
            return True
        target.write_text(f"{current.rstrip()}\n\n{block}", encoding="utf-8")
        messages.append("append .specify/memory/constitution.md addendum")
        return True

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(block, encoding="utf-8")
    messages.append("create .specify/memory/constitution.md")
    return True


def run_validators(root: Path, strict: bool, messages: list[str]) -> bool:
    structure = validate_structure(root, strict=strict)
    traceability = validate_traceability(root, strict=strict)
    if structure.ok:
        messages.append("validate structure: pass")
    else:
        messages.extend(f"validate structure: {message}" for message in structure.messages)
    if traceability.ok:
        messages.append("validate traceability: pass")
    else:
        messages.extend(f"validate traceability: {message}" for message in traceability.messages)
    return structure.ok and traceability.ok


def ficct_init(
    root: Path,
    extension_root: Path,
    feature: str = "ficct-demo",
    project_name: str | None = None,
    force: bool = False,
    validate: bool = False,
    generate_report_file: bool = False,
) -> InitResult:
    root = root.resolve()
    extension_root = extension_root.resolve()
    messages: list[str] = []

    if not root.exists():
        return InitResult(False, [f"root not found: {root}"])
    if not root.is_dir():
        return InitResult(False, [f"root is not a directory: {root}"])
    if not (extension_root / "extension.yml").is_file():
        return InitResult(False, [f"extension root not found: {extension_root}"])

    ok = True
    ok = ensure_config(root, extension_root, force, messages) and ok
    ok = update_project_name(root, project_name, force, messages) and ok
    ok = install_assets(root, extension_root, force, messages) and ok
    ok = materialize_templates(
        root,
        extension_root,
        feature,
        force,
        skip_report_template=generate_report_file,
        messages=messages,
    ) and ok
    ok = ensure_constitution_addendum(root, extension_root, force, messages) and ok

    if generate_report_file:
        (root / "docs" / "evidencias").mkdir(parents=True, exist_ok=True)
        report = generate_report(root, strict=True)
        messages.append(f"generate report: {report.output}")
        if report.pending:
            messages.append(f"generate report pending: {len(report.pending)}")
            ok = False

    if validate:
        ok = run_validators(root, strict=True, messages=messages) and ok

    return InitResult(ok, messages)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    feature = args.feature or slugify(args.project_name) or "ficct-demo"
    result = ficct_init(
        args.root,
        args.extension_root,
        feature=feature,
        project_name=args.project_name,
        force=args.force,
        validate=args.validate,
        generate_report_file=args.generate_report,
    )
    for message in result.messages:
        print(message)
    if result.ok:
        print("ficct-init completado.")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
