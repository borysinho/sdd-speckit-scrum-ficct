---
description: "Generate a FICCT SDD/Scrum compliance report"
scripts:
  sh: scripts/generate_report.py --strict
---

# FICCT Report

Generate and summarize the compliance report for the current FICCT SDD/Scrum project.

## Usage

```text
/speckit.ficct.report Genera el reporte final de Sprint-1 para agenda academica y lista pendientes si existen.
```

The text after the command defines delivery scope, Sprint, feature or pending repair expectations.

## Fast Execution

Run the report generator once and summarize its output. Read the generated report only when stdout indicates pending items or the user asks for the detailed report.

## Cross-Platform Execution

Use `python3` on Linux/macOS. Use `py -3` and backslash paths on Windows PowerShell.

## Agent Task

When this command is invoked, the agent must:

1. Run the strict compliance report generator.
2. Read `docs/evidencias/sdd-compliance-report.md`.
3. Summarize the result as `pass` or `fail`.
4. If there are pending items, list each pending item and the artifact that should be corrected.
5. If the user asks for repair, update only the relevant SDD/Scrum documents and rerun the report.
6. Confirm whether the report is ready for delivery.

## Execution

Run from the project root:

```bash
python3 .specify/extensions/ficct/scripts/generate_report.py --root . --strict
```

The report is written to:

```text
docs/evidencias/sdd-compliance-report.md
```

If the command exits with a non-zero status, the report was still generated and contains pending items under `## Pendientes`.

## Guardrails

- Do not edit the generated report manually to hide failures.
- Fix source artifacts first, then regenerate the report.
- Keep pending items visible until the validator passes.
