---
description: "Materialize FICCT SDD/Scrum structure, configuration, GitHub assets and validators"
scripts:
  sh: scripts/ficct_init.py --validate --generate-report
---

# FICCT Init

Prepare the current Spec Kit project for the FICCT SDD/Scrum workflow.

## Usage

```text
/speckit.ficct.init Inicializa agenda academica como proyecto FICCT SDD/Scrum para estudiantes de la facultad.
```

The text after the command can define project name, course context, initial feature name or setup constraints.

## Cross-Platform Execution

Use `python3` on Linux/macOS. Use `py -3` and backslash paths on Windows PowerShell.

## Fast Agent Contract

When this command is invoked, the agent must:

1. Infer only the project name and feature slug from the inline text.
2. Run `ficct_init.py` once with `--project-name`, `--feature`, `--validate` and `--generate-report`.
3. Report the script result from stdout.

Do not inspect the repository before running the initializer unless the command fails. Do not manually rename `specs/ficct-demo`; pass the desired slug with `--feature`. Do not run package tests, broad searches, file-by-file reviews or extra validators after a successful init. If repository policy requires a commit, run only the minimum Git status/add/commit steps needed for the generated files.

## Execution

Run this command from the project root:

```bash
python3 .specify/extensions/ficct/scripts/ficct_init.py --root . --project-name "agenda academica" --feature agenda-academica --validate --generate-report
```

Use `--force` only when the user explicitly wants to overwrite differing generated files:

```bash
python3 .specify/extensions/ficct/scripts/ficct_init.py --root . --project-name "agenda academica" --feature agenda-academica --force --validate --generate-report
```

## What It Materializes

- `.specify/extensions/ficct/github-sdd-scrum-ficct-config.yml`
- `.github/ISSUE_TEMPLATE/{feature,task,evidence}.yml`
- `.github/pull_request_template.md`
- `.github/workflows/sdd-gate.yml`
- `specs/<feature>/{spec,plan,tasks}.md`
- `docs/scrum/f1-sprint-review.md`
- `docs/scrum/f2-retrospective.md`
- `docs/scrum/f3-product-backlog.md`
- `docs/scrum/f4-user-stories.md`
- `docs/scrum/f5-sprint-backlog.md`
- `docs/sdd/traceability-matrix.md`
- `docs/evidencias/sdd-compliance-report.md`
- FICCT addendum appended to `.specify/memory/constitution.md`

## Guardrails

- Do not use real credentials or real private URLs while initializing academic test projects.
- Do not overwrite differing existing files unless the user requested `--force`.
- If validation fails, report the exact pending item and the file that should be adjusted.
