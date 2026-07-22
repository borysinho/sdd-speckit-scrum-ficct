---
description: "Prepare or create GitHub Issues from FICCT stories, tasks and evidence"
scripts:
  sh: scripts/install_github_assets.py
---

# FICCT Issues

Install GitHub Issue Forms and help the agent prepare traceable Issues from the current SDD/Scrum artifacts.

## Usage

```text
/speckit.ficct.issues Prepara Issues para HU-001, HU-002, TASK-001, TASK-003 y evidencia del Sprint-1. No los crees hasta que confirme.
```

The text after the command controls which Issues to prepare, whether to only draft commands or create them after confirmation.

## Fast Execution

Install or verify GitHub assets with the provided script, then read only the feature, Scrum and traceability files needed for the requested Issues. Do not scan source code or run tests. Validate once after updates.

## Cross-Platform Execution

Use `python3` on Linux/macOS. Use `py -3` and backslash paths on Windows PowerShell. `gh` commands work on both systems; prefer one-line commands when sharing them with students.

## Agent Task

When this command is invoked, the agent must:

1. Install or verify GitHub assets:
   - `.github/ISSUE_TEMPLATE/feature.yml`
   - `.github/ISSUE_TEMPLATE/task.yml`
   - `.github/ISSUE_TEMPLATE/evidence.yml`
   - `.github/pull_request_template.md`
   - `.github/workflows/sdd-gate.yml`
2. Read `specs/<feature>/spec.md`, `tasks.md`, `docs/scrum/f4-user-stories.md`, `docs/scrum/f5-sprint-backlog.md` and `docs/sdd/traceability-matrix.md`.
3. Prepare one Issue body for each required item:
   - feature/story Issues for each `HU-*`;
   - task Issues for implementable `TASK-*`;
   - evidence Issues for tests, validation, screenshots, reports or blockers.
4. Include required IDs in every Issue: `RF/RNF/RN`, `CA`, `HU`, `TASK` when applicable, Sprint, owner and evidence.
5. If GitHub CLI is available and the user asks to create Issues, run `gh issue create` commands.
6. If Issues are created, update specs, Scrum artifacts and traceability matrix with real Issue numbers.
7. Validate traceability after updates.

## Execution

Preview asset changes first:

```bash
python3 .specify/extensions/ficct/scripts/install_github_assets.py --root . --dry-run
```

Apply missing assets:

```bash
python3 .specify/extensions/ficct/scripts/install_github_assets.py --root .
```

Use `--force` only if the user wants to replace differing existing GitHub assets.

## Issue Creation Pattern

Use `gh issue create` only after the body has been reviewed:

```bash
gh issue create --title "[HU/RF]: HU-001 ..." --label feature,user-story,sdd --body "..."
gh issue create --title "[TASK]: TASK-001 ..." --label task,sdd --body "..."
gh issue create --title "[EVIDENCIA]: CA-001 ..." --label evidence,sdd --body "..."
```

## Guardrails

- Do not create GitHub Issues without user approval.
- Do not omit required traceability IDs from Issue bodies.
- Do not close Issues in this command.
- Do not create Issues for scope that is not present in `spec.md`, F4 or F5.
