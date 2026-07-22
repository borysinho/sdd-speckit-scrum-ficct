# Workflow De Equipo En Un Proyecto Real

Este documento muestra como un equipo aplica `github-sdd-scrum-ficct` en un proyecto real usando Spec Kit, Scrum FICCT, GitHub Issues, Pull Requests, GitHub Actions y evidencia trazable.

## Roles Obligatorios

| Rol | Responsabilidad principal | Evidencia que debe dejar |
| --- | --- | --- |
| Product Owner | Define alcance, prioridad y aceptacion del producto. | F3 actualizado, Issues de historia validados, criterios `CA` aceptados o rechazados. |
| Scrum Master | Coordina el Sprint, remueve bloqueos y cuida el proceso. | F1, F2, F5 actualizados, bloqueos registrados, seguimiento de Issues. |
| Analista SDD | Mantiene requisitos, reglas, criterios y trazabilidad. | `spec.md`, matriz de trazabilidad, relaciones `RF/RNF/RN -> CA -> HU`. |
| Equipo De Desarrollo | Implementa tareas y mantiene el codigo en ramas y PRs. | Commits, PRs, tareas `TASK`, pruebas ejecutadas y evidencias tecnicas. |
| QA O Validador | Verifica criterios de aceptacion y resultados. | Evidencias de prueba, Issues de evidencia, observaciones de rechazo o aprobacion. |
| Integrador | Revisa PRs, Actions y consistencia antes de merge. | Resultado de `ficct-pr-check`, checks de GitHub Actions y cierre del PR. |

Un integrante puede cubrir mas de un rol, pero todos los roles deben estar asignados y visibles en F5 o en los Issues.

## Compatibilidad De Entorno

El workflow aplica igual en Linux, macOS y Windows. Los comandos de IA son identicos; los scripts Python se ejecutan con `python3` en Linux/macOS y con `py -3` en Windows PowerShell. Consulte [Compatibilidad Windows y Linux](compatibilidad-windows-linux.md) antes de registrar evidencia o comandos de prueba.

## Flujo General

1. Preparar el repositorio y la extension.
2. Definir la feature con `specify`.
3. Completar `spec.md`, `plan.md` y `tasks.md`.
4. Construir Scrum FICCT con F1-F5.
5. Crear Issues de historia, tarea y evidencia.
6. Implementar en ramas de trabajo.
7. Abrir Pull Request completo.
8. Ejecutar `ficct-pr-check` y revisar GitHub Actions.
9. Validar evidencia y cerrar Issues.
10. Generar `ficct-report` y cerrar el Sprint.

## 1. Preparacion Del Proyecto

Responsables: Scrum Master e Integrador.

Linux/macOS:

```bash
git init
specify init --here --integration codex --force
specify extension add --dev ./github-sdd-scrum-ficct
python3 .specify/extensions/ficct/scripts/ficct_init.py --root . --project-name "agenda academica" --feature agenda-academica --validate --generate-report
```

Windows PowerShell:

```powershell
git init
specify init --here --integration codex --force
specify extension add --dev .\github-sdd-scrum-ficct
py -3 .\.specify\extensions\ficct\scripts\ficct_init.py --root . --project-name "agenda academica" --feature agenda-academica --validate --generate-report
```

`specify init` requiere destino. El comando documentado inicializa el directorio actual con integracion Codex y usa `--force` solo para evitar la confirmacion causada por `.git` en un repositorio recien creado.

Resultado esperado:

- `.github/ISSUE_TEMPLATE/feature.yml`
- `.github/ISSUE_TEMPLATE/task.yml`
- `.github/ISSUE_TEMPLATE/evidence.yml`
- `.github/pull_request_template.md`
- `.github/workflows/sdd-gate.yml`
- `specs/<feature>/spec.md`
- `specs/<feature>/plan.md`
- `specs/<feature>/tasks.md`
- `docs/scrum/f1-sprint-review.md` a `f5-sprint-backlog.md`
- `docs/sdd/traceability-matrix.md`
- `docs/evidencias/sdd-compliance-report.md`

## 2. Specify

Responsables: Product Owner y Analista SDD.

El Product Owner define el problema, usuarios afectados, prioridad y valor. El Analista SDD registra requisitos y criterios verificables en `specs/<feature>/spec.md`.

Minimo obligatorio:

- `RF-001`, `RNF-001` o `RN-001` segun corresponda.
- `CA-001` en formato verificable.
- `HU-001` enlazada al requisito y criterio.
- Issue principal de GitHub.
- Evidencia esperada por criterio.

La feature no debe pasar a implementacion si el criterio de aceptacion no se puede probar.

## 3. Plan

Responsables: Analista SDD, Equipo De Desarrollo y QA.

Complete `specs/<feature>/plan.md` antes de programar:

- alcance tecnico;
- componentes afectados;
- decisiones y justificacion;
- riesgos y mitigaciones;
- estrategia de pruebas;
- evidencia requerida por cada `CA`.

El QA confirma que cada criterio tiene una prueba posible. El Equipo De Desarrollo confirma que las tareas son implementables dentro del Sprint.

## 4. Tasks

Responsables: Scrum Master y Equipo De Desarrollo.

Complete `specs/<feature>/tasks.md` con tareas pequenas y verificables:

- `TASK-001` con descripcion clara;
- `HU`, `PB`, `CA` y requisito relacionado;
- responsable;
- comando o tipo de prueba;
- Issue y PR cuando existan;
- evidencia esperada.

Cada tarea debe poder cerrarse con una prueba o evidencia concreta.

## 5. FICCT Scrum

Responsables: Scrum Master y Product Owner.

Use los artefactos Scrum FICCT para sincronizar el trabajo:

- F3 Product Backlog: prioridad, valor y alcance aprobado por Product Owner.
- F4 User Stories: historias en formato claro, con `HU`, `RF/RNF/RN` y `CA`.
- F5 Sprint Backlog: tareas, responsables, estado, Sprint y evidencia.
- F1 Sprint Review: resultado presentado, criterios aceptados y pendientes.
- F2 Retrospective: mejora del proceso, bloqueos y acciones.

Cuando cambie el alcance, actualice primero F3/F4/F5 y luego refleje el cambio en `spec.md`, `plan.md`, `tasks.md` y matriz.

## 6. FICCT Issues

Responsables: Product Owner, Scrum Master, Equipo De Desarrollo y QA.

Instale o verifique los assets:

```bash
python3 .specify/extensions/ficct/scripts/install_github_assets.py --root .
```

Cree Issues desde los formularios:

- Historia o funcionalidad: Product Owner registra `HU`, `RF/RNF/RN`, `CA`, Sprint, responsable y evidencia esperada.
- Tarea tecnica: Equipo De Desarrollo registra `TASK`, `HU`, requisito, criterio, Sprint y prueba.
- Evidencia o validacion: QA registra prueba ejecutada, captura, reporte, bloqueo o validacion.

Cada Issue debe quedar enlazado al PR o a la evidencia que lo cierra.

## 7. Implement

Responsables: Equipo De Desarrollo.

Trabaje siempre en una rama por feature o tarea:

```bash
git switch -c feature/HU-001-nombre-corto
```

Durante la implementacion:

- mantenga commits relacionados con el Issue;
- actualice `tasks.md` cuando cambie el estado de `TASK`;
- agregue o actualice pruebas;
- guarde evidencia en `docs/evidencias/` cuando corresponda;
- no cierre el Issue antes de que exista PR y evidencia.

## 8. Pull Request

Responsables: Equipo De Desarrollo e Integrador.

Abra un Pull Request y complete toda la plantilla:

- Issue relacionado;
- tipo de cambio;
- `RF/RNF/RN`, `HU`, `TASK` y Sprint;
- criterios `CA` cubiertos;
- comandos de prueba y resultado;
- capturas, reportes o evidencias;
- decisiones afectadas o `N/A`;
- checklist de cierre.

Un PR incompleto no debe pasar a revision de merge.

## 9. FICCT PR Check Y GitHub Actions

Responsables: Integrador y Scrum Master.

Antes de solicitar revision:

```bash
python3 .specify/extensions/ficct/scripts/validate_structure.py --root . --strict
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
```

En GitHub, revise el workflow `SDD Gate`:

- `Verificar plan de assets GitHub`: confirma formularios, PR template y workflow.
- `Validar estructura SDD/Scrum`: confirma carpetas y artefactos obligatorios.
- `Validar trazabilidad minima`: confirma relaciones entre requisitos, criterios, historias y tareas.

Si Actions falla, el Integrador no fusiona el PR. El responsable corrige, sube commit y espera una nueva ejecucion.

## 10. Evidencia Y Cierre

Responsables: QA, Product Owner y Scrum Master.

QA verifica que la evidencia demuestre el criterio `CA`. El Product Owner acepta o rechaza la historia. El Scrum Master actualiza F1 y F2.

Genere el reporte final:

```bash
python3 .specify/extensions/ficct/scripts/generate_report.py --root . --strict
```

Revise `docs/evidencias/sdd-compliance-report.md`:

- resultado general;
- pendientes;
- fecha;
- estructura;
- trazabilidad.

El Sprint queda cerrado cuando el PR esta fusionado, los Issues estan cerrados, F1/F2/F5 estan actualizados y el reporte no oculta pendientes.

## Checklist De Demostracion Del Equipo

- Product Owner muestra F3, una historia y su Issue.
- Analista SDD muestra `spec.md` y la matriz de trazabilidad.
- Scrum Master muestra F5, estado del Sprint, F1 y F2.
- Equipo De Desarrollo muestra rama, commits, cambios y PR.
- QA muestra prueba ejecutada y evidencia.
- Integrador muestra `ficct-pr-check`, GitHub Actions y estado del merge.
- El equipo muestra `ficct-report` como cierre verificable.
