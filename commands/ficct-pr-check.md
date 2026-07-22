---
description: "Check a project or pull request workspace against FICCT SDD/Scrum gates"
---

# FICCT PR Check

Validate the current workspace before opening, reviewing or merging a pull request.

## Usage

```text
/speckit.ficct.pr-check Revisa el PR de HU-001 y corrige solo documentacion de trazabilidad si falta RF, CA, HU, TASK, prueba o evidencia.
```

The text after the command defines the branch, PR or correction scope.

## Fast Execution

Run the validators first and use their messages to decide what to inspect. Do not read every generated artifact unless a validator or PR check points to it.

## Cross-Platform Execution

Use `python3` on Linux/macOS. Use `py -3` and backslash paths on Windows PowerShell. `gh pr checks` works on both systems after GitHub CLI login.

## Agent Task

When this command is invoked, the agent must:

1. Run strict structure and traceability validators.
2. Inspect `.github/pull_request_template.md`.
3. Verify that the current PR or branch has evidence for:
   - related Issue;
   - `RF/RNF/RN`;
   - `CA`;
   - `HU`;
   - `TASK`;
   - Sprint;
   - tests executed;
   - evidence path or link;
   - decisions affected or `N/A`.
4. If validation fails, explain the exact missing relation and the file that should be fixed.
5. If the user asks for repair, update only the relevant documentation and rerun validators.
6. Do not approve merge while validators or GitHub Actions are failing.

## Execution

Run strict validators from the project root:

```bash
python3 .specify/extensions/ficct/scripts/validate_structure.py --root . --strict
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
```

If GitHub CLI is available, also inspect PR checks:

```bash
gh pr checks
```

## Required Evidence

- At least one `specs/<feature>/spec.md`.
- Matching `plan.md` and `tasks.md` for each feature in strict mode.
- Scrum F1-F5 documents.
- SDD traceability matrix.
- GitHub Issue Forms, PR template and `sdd-gate.yml` workflow.
- PR body filled with Issue, IDs, tests and evidence.

## Guardrails

- Do not hide pending items.
- Do not mark a PR as ready if tests or evidence are missing.
- Do not invent evidence paths; use files, URLs or command outputs that exist or are explicitly provided.
