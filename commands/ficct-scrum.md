---
description: "Generate or update FICCT Scrum F1-F5 artifacts from Spec Kit specs, plans and tasks"
---

# FICCT Scrum

Generate or refresh the FICCT Scrum artifacts in `docs/scrum` using the current Spec Kit feature artifacts as source.

## Usage

```text
/speckit.ficct.scrum Genera F3, F4 y F5 para agenda academica Sprint-1. Ana es PO, Luis Scrum Master, Diego y Marco desarrollo, Sofia QA.
```

The text after the command provides Sprint context, roles, priorities or closure notes. Use it together with `spec.md`, `plan.md` and `tasks.md`.

## Fast Execution

Read only `specs/*/{spec,plan,tasks}.md`, the existing Scrum files and the required templates. Do not inspect source code, Git history or unrelated documentation. Run each validator once after writing.

## Cross-Platform Execution

Use `python3` on Linux/macOS. Use `py -3` and backslash paths on Windows PowerShell.

## Agent Task

When this command is invoked, the agent must:

1. Ensure the project was initialized with `speckit.ficct.init`.
2. Read all available `specs/<feature>/spec.md`, `plan.md` and `tasks.md` files.
3. Extract stable IDs: `RF-*`, `RNF-*`, `RN-*`, `CA-*`, `HU-*`, `PB-*`, `TASK-*` and Sprint IDs.
4. Create missing Scrum files from templates without overwriting existing work.
5. Update Scrum FICCT artifacts with concrete project data:
   - F3 Product Backlog from requirements, product backlog items and priorities.
   - F4 User Stories from `HU-*`, linked requirements and acceptance criteria.
   - F5 Sprint Backlog from `TASK-*`, owners, state, tests and evidence.
   - F1 Sprint Review when delivery evidence or accepted criteria exist.
   - F2 Retrospective when Sprint closure, blockers or improvements are provided.
6. Preserve existing valid content and merge new data instead of replacing unrelated sections.
7. Run strict structure and traceability validation.
8. Report exactly which files changed and which pending traceability items remain.

## Execution

If Scrum artifacts are missing, materialize them first:

```bash
python3 .specify/extensions/ficct/scripts/ficct_init.py --root . --validate
```

Use `--force` only when the user explicitly wants to reset generated Scrum templates:

```bash
python3 .specify/extensions/ficct/scripts/ficct_init.py --root . --force --validate
```

Validate after generation or update:

```bash
python3 .specify/extensions/ficct/scripts/validate_structure.py --root . --strict
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
```

## Required Inputs

- `specs/<feature>/spec.md`
- `specs/<feature>/plan.md`
- `specs/<feature>/tasks.md`

If an input is missing, stop and ask the user to run the corresponding FICCT command first: `/speckit.ficct.specify`, `/speckit.ficct.plan` or `/speckit.ficct.tasks`.

## Expected Artifacts

- `docs/scrum/f1-sprint-review.md`
- `docs/scrum/f2-retrospective.md`
- `docs/scrum/f3-product-backlog.md`
- `docs/scrum/f4-user-stories.md`
- `docs/scrum/f5-sprint-backlog.md`

## Guardrails

- Do not invent extra features or cases of use.
- Do not create orphan `HU-*`, `CA-*` or `TASK-*` IDs.
- Every F5 task must link to a story, requirement, criterion, owner, test or evidence.
- If the user provides Sprint status, reflect it in F1/F2/F5.
