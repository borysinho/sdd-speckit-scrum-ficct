# Guia Operativa Para Estudiantes

Use esta guia como checklist corto de trabajo. Mantenga los IDs iguales en todos los archivos: `RF-001`, `CA-001`, `HU-001`, `TASK-001`, `Sprint-1`.

## 1. Instalar

Linux/macOS:

```bash
git init
specify init --here --integration codex --force
specify extension add --dev ./github-sdd-scrum-ficct
python3 .specify/extensions/ficct/scripts/ficct_init.py --root . --validate --generate-report
```

Windows PowerShell:

```powershell
git init
specify init --here --integration codex --force
specify extension add --dev .\github-sdd-scrum-ficct
py -3 .\.specify\extensions\ficct\scripts\ficct_init.py --root . --validate --generate-report
```

Si ya conoce el nombre del proyecto, use el comando parametrizado para evitar renombrar carpetas despues:

```bash
python3 .specify/extensions/ficct/scripts/ficct_init.py --root . --project-name "agenda academica" --feature agenda-academica --validate --generate-report
```

```powershell
py -3 .\.specify\extensions\ficct\scripts\ficct_init.py --root . --project-name "agenda academica" --feature agenda-academica --validate --generate-report
```

`specify init` no debe ejecutarse solo: indique un proyecto, use `.` o use `--here`. En esta guia se usa `--here --force` porque el flujo inicia con `git init`; `.git` hace que el directorio no este vacio y Spec Kit pide confirmacion. Si ya existen archivos propios y quiere conservar su avance, no use `--force` sin revisar primero.

Para equivalencias de comandos consulte [Compatibilidad Windows y Linux](compatibilidad-windows-linux.md).

## 2. Flujo De Trabajo

1. `/speckit.ficct.specify <descripcion>`: pida a la IA generar `specs/<feature>/spec.md` con problema, requisitos, criterios y HU.
2. `/speckit.ficct.plan <restricciones>`: pida a la IA generar `specs/<feature>/plan.md` con decisiones tecnicas, riesgos, pruebas y evidencia esperada.
3. `/speckit.ficct.tasks <detalle>`: pida a la IA generar `specs/<feature>/tasks.md` con tareas pequenas, responsables, comandos de prueba y enlaces.
4. `/speckit.ficct.scrum`: pida a la IA actualizar `docs/scrum/f3-product-backlog.md`, `f4-user-stories.md` y `f5-sprint-backlog.md`.
5. `/speckit.ficct.issues`: instale assets GitHub y prepare Issues para historia, tarea y evidencia.
6. `/speckit.ficct.implement <HU/TASK>`: pida a la IA implementar una HU/TASK en una rama, con pruebas y evidencia.
7. `/speckit.ficct.pr-check`: valide antes de abrir el Pull Request.
8. `/speckit.ficct.report`: genere el reporte final.

## 3. Comandos Utiles

Linux/macOS:

```bash
python3 .specify/extensions/ficct/scripts/install_github_assets.py --root .
python3 .specify/extensions/ficct/scripts/validate_structure.py --root . --strict
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
python3 .specify/extensions/ficct/scripts/generate_report.py --root . --strict
```

Windows PowerShell:

```powershell
py -3 .\.specify\extensions\ficct\scripts\install_github_assets.py --root .
py -3 .\.specify\extensions\ficct\scripts\validate_structure.py --root . --strict
py -3 .\.specify\extensions\ficct\scripts\validate_traceability.py --root . --strict
py -3 .\.specify\extensions\ficct\scripts\generate_report.py --root . --strict
```

## 4. GitHub Issues

Cree Issues desde las plantillas instaladas:

- Historia o funcionalidad: use `HU-001`, `RF-001`, `CA-001`, Sprint, responsable y evidencia esperada.
- Tarea tecnica: use `TASK-001`, historia, requisito, criterio, Sprint, responsable y tipo de tarea.
- Evidencia: registre prueba ejecutada, captura, demo, reporte, validacion docente o bloqueo.

No cierre un Issue si el PR, la prueba y la evidencia no estan enlazados.

## 5. Pull Request

Complete todos los campos de `.github/pull_request_template.md`:

- Issue relacionado.
- IDs `RF/RNF/RN`, `HU`, `TASK` y Sprint.
- Criterios `CA` cubiertos.
- Comandos de prueba y resultado.
- Ruta o enlace de evidencia.
- Decisiones afectadas o `N/A`.

Abra el PR solo cuando `ficct-pr-check` pase o cuando el pendiente este justificado en el mismo PR.

## 6. GitHub Actions

En el PR abra la pestana `Checks`. El workflow `SDD Gate` debe quedar en verde. Si falla, revise el paso con error:

- `Verificar plan de assets GitHub`: faltan formularios, PR template o workflow.
- `Validar estructura SDD/Scrum`: falta un archivo o carpeta obligatoria.
- `Validar trazabilidad minima`: falta relacion entre requisito, criterio, historia o tarea.

Corrija el archivo indicado, haga commit y espere la nueva ejecucion.

## 7. Entrega Minima

- `specs/<feature>/spec.md`, `plan.md`, `tasks.md`.
- `docs/scrum/f1` a `f5`.
- `docs/sdd/traceability-matrix.md`.
- PR completo.
- `docs/evidencias/sdd-compliance-report.md`.
