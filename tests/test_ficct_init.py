from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml


EXTENSION_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = EXTENSION_ROOT / "scripts" / "ficct_init.py"


def make_project(tmp_path: Path) -> Path:
    project = tmp_path / "project"
    (project / ".specify" / "memory").mkdir(parents=True)
    (project / ".specify" / "extensions" / "ficct").mkdir(parents=True)
    (project / ".specify" / "memory" / "constitution.md").write_text(
        "# Project Constitution\n",
        encoding="utf-8",
    )
    return project


def run_ficct_init(project: Path, *extra_args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--root",
            str(project),
            *extra_args,
            "--validate",
            "--generate-report",
        ],
        text=True,
        capture_output=True,
        check=False,
    )


def test_manifest_command_files_exist() -> None:
    manifest = yaml.safe_load((EXTENSION_ROOT / "extension.yml").read_text(encoding="utf-8"))

    missing = [
        command["file"]
        for command in manifest["provides"]["commands"]
        if not (EXTENSION_ROOT / command["file"]).is_file()
    ]

    assert missing == []


def test_extension_docs_folder_only_contains_package_documentation() -> None:
    docs_root = EXTENSION_ROOT / "docs"
    if not docs_root.exists():
        return

    project_artifact_dirs = {"scrum", "sdd", "evidencias"}
    shipped_project_dirs = [
        path.name
        for path in docs_root.iterdir()
        if path.is_dir() and path.name in project_artifact_dirs
    ]

    assert shipped_project_dirs == [], (
        "The extension may ship package documentation in docs/, but project "
        "artifacts must remain templates so Spec Kit does not rewrite docs/* "
        "references as extension-internal paths."
    )


def test_ficct_init_materializes_project_and_passes_validators(tmp_path: Path) -> None:
    project = make_project(tmp_path)

    result = run_ficct_init(project)

    assert result.returncode == 0, result.stdout + result.stderr
    assert "validate structure: pass" in result.stdout
    assert "validate traceability: pass" in result.stdout
    assert "ficct-init completado" in result.stdout

    expected_files = [
        ".specify/extensions/ficct/github-sdd-scrum-ficct-config.yml",
        ".github/ISSUE_TEMPLATE/feature.yml",
        ".github/ISSUE_TEMPLATE/task.yml",
        ".github/ISSUE_TEMPLATE/evidence.yml",
        ".github/pull_request_template.md",
        ".github/workflows/sdd-gate.yml",
        "specs/ficct-demo/spec.md",
        "specs/ficct-demo/plan.md",
        "specs/ficct-demo/tasks.md",
        "docs/scrum/f1-sprint-review.md",
        "docs/scrum/f2-retrospective.md",
        "docs/scrum/f3-product-backlog.md",
        "docs/scrum/f4-user-stories.md",
        "docs/scrum/f5-sprint-backlog.md",
        "docs/sdd/traceability-matrix.md",
        "docs/evidencias/sdd-compliance-report.md",
    ]
    for relative in expected_files:
        assert (project / relative).is_file(), relative

    constitution = (project / ".specify" / "memory" / "constitution.md").read_text(encoding="utf-8")
    assert "BEGIN github-sdd-scrum-ficct constitution addendum" in constitution

    report = (project / "docs" / "evidencias" / "sdd-compliance-report.md").read_text(encoding="utf-8")
    assert "| Resultado | pass |" in report


def test_ficct_init_uses_project_name_as_feature_and_config(tmp_path: Path) -> None:
    project = make_project(tmp_path)

    result = run_ficct_init(project, "--project-name", "agenda academica")

    assert result.returncode == 0, result.stdout + result.stderr
    assert (project / "specs/agenda-academica/spec.md").is_file()
    assert not (project / "specs/ficct-demo").exists()

    config = (
        project / ".specify" / "extensions" / "ficct" / "github-sdd-scrum-ficct-config.yml"
    ).read_text(encoding="utf-8")
    assert 'project_name: "agenda academica"' in config


def test_ficct_init_is_reentrant_without_force(tmp_path: Path) -> None:
    project = make_project(tmp_path)

    first = run_ficct_init(project)
    second = run_ficct_init(project)

    assert first.returncode == 0, first.stdout + first.stderr
    assert second.returncode == 0, second.stdout + second.stderr
    assert "skip .github/ISSUE_TEMPLATE/feature.yml" in second.stdout
    assert "skip .specify/memory/constitution.md addendum" in second.stdout


def test_ficct_init_is_reentrant_with_project_name_without_force(tmp_path: Path) -> None:
    project = make_project(tmp_path)

    first = run_ficct_init(project, "--project-name", "agenda academica")
    second = run_ficct_init(project, "--project-name", "agenda academica")

    assert first.returncode == 0, first.stdout + first.stderr
    assert second.returncode == 0, second.stdout + second.stderr
    assert "conflict .specify/extensions/ficct/github-sdd-scrum-ficct-config.yml" not in second.stdout
    assert "skip .specify/extensions/ficct/github-sdd-scrum-ficct-config.yml project_name" in second.stdout
