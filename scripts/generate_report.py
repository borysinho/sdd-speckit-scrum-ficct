#!/usr/bin/env python3
"""Generate a Markdown SDD/Scrum FICCT compliance report."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from validate_structure import validate_structure
from validate_traceability import validate_traceability


@dataclass(frozen=True)
class ReportResult:
    ok: bool
    output: Path
    pending: tuple[str, ...]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", type=Path, help="Project root to validate.")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Report path. Defaults to docs/evidencias/sdd-compliance-report.md inside root.",
    )
    parser.add_argument("--strict", action="store_true", help="Use strict validators.")
    return parser.parse_args(argv)


def render_report(structure_messages: tuple[str, ...], traceability_messages: tuple[str, ...]) -> str:
    pending = [*structure_messages, *traceability_messages]
    result = "pass" if not pending else "fail"
    pending_rows = "\n".join(
        f"| PEND-{index:03d} | {message} | high | Pendiente de correccion |"
        for index, message in enumerate(pending, start=1)
    )
    if not pending_rows:
        pending_rows = "| - | Sin pendientes | - | - |"

    return "\n".join(
        (
            "# Reporte De Cumplimiento SDD/Scrum",
            "",
            "## Metadatos",
            "",
            "| Campo | Valor |",
            "| --- | --- |",
            f"| Fecha | {date.today().isoformat()} |",
            f"| Resultado | {result} |",
            "",
            "## Resumen",
            "",
            f"- Estructura: {'pass' if not structure_messages else 'fail'}",
            f"- Trazabilidad: {'pass' if not traceability_messages else 'fail'}",
            "",
            "## Pendientes",
            "",
            "| ID | Descripcion | Severidad | Accion |",
            "| --- | --- | --- | --- |",
            pending_rows,
            "",
        )
    )


def generate_report(root: Path, output: Path | None = None, strict: bool = False) -> ReportResult:
    root = root.resolve()
    output = (root / "docs/evidencias/sdd-compliance-report.md") if output is None else output
    if not output.is_absolute():
        output = root / output

    structure = validate_structure(root, strict=strict)
    traceability = validate_traceability(root, strict=strict)
    pending = (*structure.messages, *traceability.messages)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_report(structure.messages, traceability.messages), encoding="utf-8")
    return ReportResult(not pending, output, pending)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    result = generate_report(args.root, output=args.output, strict=args.strict)
    print(f"Reporte generado: {result.output}")
    if result.pending:
        print(f"Pendientes: {len(result.pending)}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
