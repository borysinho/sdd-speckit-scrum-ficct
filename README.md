# github-sdd-scrum-ficct

Extension local de GitHub Spec Kit para adaptar SDD al flujo academico Scrum de la FICCT. Integra especificacion, planificacion, tareas, Scrum F1-F5, GitHub Issues, Pull Requests, GitHub Actions y reporte de cumplimiento en un mismo flujo verificable.

## Para Que Sirve

- Preparar un proyecto Spec Kit con estructura SDD/Scrum FICCT.
- Materializar plantillas de `spec.md`, `plan.md`, `tasks.md`, Scrum F1-F5, matriz de trazabilidad y reporte.
- Instalar formularios de Issues, plantilla de Pull Request y workflow `sdd-gate.yml`.
- Validar estructura y trazabilidad antes de entregar o fusionar un PR.
- Generar `docs/evidencias/sdd-compliance-report.md` para revision docente.

## Instalacion Local

Desde la raiz del repositorio del proyecto en Linux/macOS:

```bash
git init
specify init --here --integration codex --force
specify extension add --dev ./github-sdd-scrum-ficct
python3 .specify/extensions/ficct/scripts/ficct_init.py --root . --validate --generate-report
```

Desde Windows PowerShell:

```powershell
git init
specify init --here --integration codex --force
specify extension add --dev .\github-sdd-scrum-ficct
py -3 .\.specify\extensions\ficct\scripts\ficct_init.py --root . --validate --generate-report
```

Para crear la carpeta inicial de la funcionalidad y registrar el nombre del proyecto sin pasos manuales, pase ambos datos al inicializador:

```bash
python3 .specify/extensions/ficct/scripts/ficct_init.py --root . --project-name "agenda academica" --feature agenda-academica --validate --generate-report
```

```powershell
py -3 .\.specify\extensions\ficct\scripts\ficct_init.py --root . --project-name "agenda academica" --feature agenda-academica --validate --generate-report
```

`specify init` requiere indicar destino. Use `--here` para inicializar el directorio actual. Se usa `--force` porque `git init` crea `.git` y Spec Kit considera que el directorio ya no esta vacio; en un proyecto con archivos propios, revise antes de usar `--force`. Si usa otro agente, cambie `codex` por la integracion correspondiente, por ejemplo `copilot`, `claude` o `generic`.

Si la extension se usa desde este repositorio durante desarrollo, ejecute los scripts indicando la raiz del proyecto destino y, si hace falta, el `--extension-root`.

Linux/macOS:

```bash
python3 github-sdd-scrum-ficct/scripts/ficct_init.py --root /ruta/proyecto-spec-kit --extension-root github-sdd-scrum-ficct --validate --generate-report
```

Windows PowerShell:

```powershell
py -3 github-sdd-scrum-ficct\scripts\ficct_init.py --root C:\ruta\proyecto-spec-kit --extension-root github-sdd-scrum-ficct --validate --generate-report
```

Use `--force` solo cuando quiera reemplazar archivos generados que ya existen y difieren.

## Flujo Completo

1. `/speckit.ficct.specify <descripcion>`: pedir a la IA que genere `specs/<feature>/spec.md` con la estructura FICCT obligatoria.
2. `/speckit.ficct.plan <restricciones>`: pedir a la IA que genere `specs/<feature>/plan.md` desde la especificacion.
3. `/speckit.ficct.tasks <detalle>`: pedir a la IA que genere `specs/<feature>/tasks.md` desde especificacion y plan.
4. `/speckit.ficct.scrum`: generar o actualizar F1-F5 desde `spec.md`, `plan.md` y `tasks.md`.
5. `/speckit.ficct.issues`: instalar formularios y preparar Issues trazables para GitHub.
6. `/speckit.ficct.implement <HU/TASK>`: pedir a la IA que implemente una HU/TASK en una rama con pruebas y evidencia.
7. `/speckit.ficct.pr-check`: validar estructura, trazabilidad, PR, pruebas y evidencia.
8. `/speckit.ficct.report`: generar y revisar el reporte de cumplimiento para entrega.

Comandos directos equivalentes en Linux/macOS:

```bash
python3 .specify/extensions/ficct/scripts/ficct_init.py --root . --validate
python3 .specify/extensions/ficct/scripts/install_github_assets.py --root .
python3 .specify/extensions/ficct/scripts/validate_structure.py --root . --strict
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
python3 .specify/extensions/ficct/scripts/generate_report.py --root . --strict
```

Comandos directos equivalentes en Windows PowerShell:

```powershell
py -3 .\.specify\extensions\ficct\scripts\ficct_init.py --root . --validate
py -3 .\.specify\extensions\ficct\scripts\install_github_assets.py --root .
py -3 .\.specify\extensions\ficct\scripts\validate_structure.py --root . --strict
py -3 .\.specify\extensions\ficct\scripts\validate_traceability.py --root . --strict
py -3 .\.specify\extensions\ficct\scripts\generate_report.py --root . --strict
```

## Comandos De La Extension

- `speckit.ficct.init` - Inicializa estructura, assets GitHub, plantillas y reporte base.
- `speckit.ficct.specify` - Genera `spec.md` desde una instruccion inline y respeta la estructura SDD/FICCT.
- `speckit.ficct.plan` - Genera `plan.md` desde la especificacion y restricciones inline.
- `speckit.ficct.tasks` - Genera `tasks.md` desde especificacion, plan y detalle inline.
- `speckit.ficct.scrum` - Genera o actualiza Scrum F1-F5 desde specs, plan y tasks.
- `speckit.ficct.issues` - Instala assets y prepara Issues desde HU, TASK y evidencia.
- `speckit.ficct.implement` - Implementa una HU/TASK con pruebas, evidencia y trazabilidad.
- `speckit.ficct.pr-check` - Valida estructura, trazabilidad, PR, pruebas y evidencia.
- `speckit.ficct.report` - Genera y resume el reporte Markdown de cumplimiento.

## Documentacion

- [Guia de estudiantes](docs/uso-estudiantes.md)
- [Guia docente](docs/guia-docente.md)
- [Compatibilidad Windows y Linux](docs/compatibilidad-windows-linux.md)
- [Workflow de equipo](docs/workflow-equipo.md)
- [Ejemplo de proyecto con dos casos de uso](docs/ejemplo-proyecto-dos-casos.md)
- [Decisiones y limitaciones](docs/decisiones.md)

## GitHub Issues, PRs Y Actions

`ficct-issues` instala tres formularios: historia o funcionalidad, tarea tecnica y evidencia. Cada Issue debe incluir IDs estables como `RF-001`, `CA-001`, `HU-001`, `TASK-001` y `Sprint-1`.

La plantilla de Pull Request exige Issue relacionado, trazabilidad RF/HU/TASK/Sprint, criterios de aceptacion, pruebas, evidencias y decisiones afectadas. El workflow `SDD Gate` se ejecuta en PR y push a `main` o `master`; si falla, revise el paso con `::error::` y corrija el archivo indicado antes de solicitar revision.

## Limitaciones De La Primera Version

- No crea Issues ni Pull Requests automaticamente en GitHub.
- No interpreta codigo fuente ni verifica cobertura real de pruebas; valida estructura y trazabilidad documental.
- La actualizacion de Scrum F1-F5 no infiere cambios desde commits.
- La evidencia visual o manual debe ser revisada por una persona.
- La integracion depende de que Spec Kit y la extension esten instalados en la ruta esperada.
