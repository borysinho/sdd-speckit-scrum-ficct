---
description: "Generate FICCT implementation tasks from the specification, plan and inline prompt"
---

# FICCT Tasks

Generate or update `specs/<feature>/tasks.md` from the current specification, plan and the text supplied after the command.

## Usage

```text
/speckit.ficct.tasks Divide el trabajo de agenda academica en tareas pequenas para registrar tarea, consultar pendientes, probar criterios y generar evidencia.
```

The text after the command describes task granularity, team assignment or Sprint constraints.

## Fast Execution

Read only the target `spec.md`, `plan.md`, existing `tasks.md` when present and the tasks template. Do not scan source code or run project tests while generating tasks. Run traceability validation once after writing.

## Cross-Platform Execution

Use `python3` on Linux/macOS. Use `py -3` and backslash paths on Windows PowerShell.

## Agent Task

When this command is invoked, the agent must:

1. Identify the target feature from the inline prompt or active feature directory.
2. Read `specs/<feature>/spec.md` and `specs/<feature>/plan.md`.
3. Create or update `specs/<feature>/tasks.md`.
4. Use `templates/tasks-template.md` as mandatory structure.
5. Fill every required section with useful first-draft content:
   - `Metadatos Obligatorios`
   - `Tareas`
   - `Detalle Obligatorio Por Tarea`
   - `Trazabilidad Y Evidencia`
   - `Checklist De Cierre`
6. Assign stable `TASK-*` IDs.
7. Link every task to `RF/RNF/RN`, `CA`, `HU`, `PB`, tests, Issue/PR placeholders and evidence.
8. Keep tasks small enough to be implemented and reviewed in a PR.
9. Preserve user-approved tasks when refining an existing file.
10. Run traceability validation and report pending items.

## Validation

```bash
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
```

## Guardrails

- Do not create tasks that cannot be traced to a requirement and acceptance criterion.
- Do not mark tasks as `done` unless implementation evidence exists.
- Do not remove user-assigned owners without explicit instruction.
