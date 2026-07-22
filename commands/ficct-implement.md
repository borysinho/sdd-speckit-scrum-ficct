---
description: "Implement a FICCT story or task with tests, evidence and traceability updates"
---

# FICCT Implement

Implement a specific `HU-*` or `TASK-*` using the current SDD/Scrum artifacts as source.

## Usage

```text
/speckit.ficct.implement HU-001 Implementa registrar tarea academica con prueba test_registrar_tarea y evidencia en docs/evidencias/sprint-1/.
```

The text after the command defines the target story/task and any implementation constraints.

## Fast Execution

Read only the artifacts linked to the requested `HU-*` or `TASK-*` plus the files needed for the implementation. Avoid broad repository scans after the target files are known. Run the project tests relevant to the implemented scope and traceability validation once.

## Cross-Platform Execution

Use the project's native test command for the student's operating system. Use `python3` on Linux/macOS and `py -3` on Windows PowerShell for FICCT validators.

## Agent Task

When this command is invoked, the agent must:

1. Identify the target `HU-*` or `TASK-*` from the inline text.
2. Read `specs/<feature>/spec.md`, `plan.md`, `tasks.md`, F5 and the traceability matrix.
3. Determine the exact scope from linked `RF/RNF/RN`, `CA`, `HU`, `TASK`, tests and evidence.
4. Implement only the requested story or task.
5. Add or update tests required by the linked `CA-*`.
6. Record evidence under `docs/evidencias/` when the project workflow supports it.
7. Update `tasks.md`, F5 and traceability only for the implemented scope.
8. Run project tests and strict traceability validation.
9. Prepare PR evidence if the user asks for a Pull Request.

## Validation

Run the project test command, then:

```bash
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
```

## Guardrails

- Do not implement scope outside the requested `HU-*` or `TASK-*`.
- Do not mark tasks as `done` unless tests or manual evidence exist.
- Do not fabricate test results or evidence files.
- Do not change requirements to fit the implementation without explicit user approval.
