---
description: "Generate a FICCT SDD feature specification from an inline prompt"
---

# FICCT Specify

Generate or update `specs/<feature>/spec.md` from the text supplied after the command.

## Usage

```text
/speckit.ficct.specify Agenda academica para estudiantes de la facultad. Sera una web simple con 2 casos de uso: registrar tarea y consultar tareas pendientes.
```

The text after the command is the product brief. Use it as the main source of truth unless the user later refines it.

## Fast Execution

Read only the target `spec.md` when it already exists and the template needed for this command. Do not scan the whole repository, run tests or inspect unrelated docs before drafting the specification. Run traceability validation once after writing.

## Cross-Platform Execution

Use `python3` on Linux/macOS. Use `py -3` and backslash paths on Windows PowerShell.

## Agent Task

When this command is invoked, the agent must:

1. Parse the inline prompt and derive a feature slug, for example `agenda-academica`.
2. Create or update `specs/<feature>/spec.md`.
3. Use `templates/spec-template.md` as mandatory structure.
4. Fill every required section with useful first-draft content:
   - `Metadatos Obligatorios`
   - `Contexto`
   - `Requisitos Funcionales`
   - `Requisitos No Funcionales`
   - `Reglas De Negocio`
   - `Criterios De Aceptacion`
   - `Historias Relacionadas`
   - `Trazabilidad Y Evidencia`
   - `Checklist De Revision`
5. Assign stable IDs starting at `RF-001`, `RNF-001`, `RN-001`, `CA-001`, `HU-001` and `PB-001`.
6. Create acceptance criteria that are objectively testable.
7. Link every `HU-*` to `PB-*`, `CA-*`, evidence and future task placeholders.
8. Preserve user-approved content when the command is used to refine an existing spec.
9. Run traceability validation and report pending items.

## Validation

```bash
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
```

## Guardrails

- Do not leave template placeholders such as `[FEATURE_NAME]` when enough information exists.
- Do not invent extra cases of use beyond the inline prompt.
- If the prompt is ambiguous, make a conservative first draft and mark assumptions in the document.
- Do not mark checklist items as complete unless the traceability exists.
