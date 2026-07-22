---
description: "Generate a FICCT implementation plan from the specification and an inline prompt"
---

# FICCT Plan

Generate or update `specs/<feature>/plan.md` from the current specification and the text supplied after the command.

## Usage

```text
/speckit.ficct.plan Implementar agenda academica como web simple con almacenamiento local, pruebas automatizadas y evidencia por criterio de aceptacion.
```

The text after the command describes implementation constraints, technology, risks or preferences.

## Fast Execution

Read only the target `spec.md`, existing `plan.md` when present and the plan template. Do not scan the whole repository or run project tests while planning. Run traceability validation once after writing.

## Cross-Platform Execution

Use `python3` on Linux/macOS. Use `py -3` and backslash paths on Windows PowerShell.

## Agent Task

When this command is invoked, the agent must:

1. Identify the target feature from the inline prompt or the active `specs/<feature>/spec.md`.
2. Read `specs/<feature>/spec.md` before writing the plan.
3. Create or update `specs/<feature>/plan.md`.
4. Use `templates/plan-template.md` as mandatory structure.
5. Fill every required section with useful first-draft content:
   - `Metadatos Obligatorios`
   - `Alcance Tecnico`
   - `Decisiones`
   - `Riesgos Y Mitigaciones`
   - `Estrategia De Pruebas`
   - `Trazabilidad Del Plan`
   - `Gate De Aprobacion`
6. Carry forward all `RF-*`, `RNF-*`, `RN-*`, `CA-*`, `HU-*` and `PB-*` from `spec.md`.
7. Define tests for every `CA-*`.
8. Define evidence paths under `docs/evidencias/`.
9. Preserve user-approved plan content when refining an existing plan.
10. Run traceability validation and report pending items.

## Validation

```bash
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
```

## Guardrails

- Do not add implementation scope not present in `spec.md` unless the inline prompt explicitly requests a scope change.
- Do not remove IDs from the specification.
- Do not mark the gate as approved until tests and evidence are mapped.
