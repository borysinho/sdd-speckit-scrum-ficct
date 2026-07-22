# Ejemplo Guiado Por IA: Proyecto Con Dos Casos De Uso

Este ejemplo muestra el uso esperado de `github-sdd-scrum-ficct`: el equipo guia a la IA con comandos Spec Kit y comandos de la extension, revisa los artefactos generados y valida trazabilidad con scripts.

Proyecto: `agenda-academica`

Objetivo: permitir que un estudiante registre tareas academicas y consulte tareas pendientes.

Casos de uso:

| Caso de uso | Nombre | Actor | Resultado |
| --- | --- | --- | --- |
| `CU-001` | Registrar tarea academica | Estudiante | La tarea queda guardada con titulo, materia y fecha limite. |
| `CU-002` | Consultar tareas pendientes | Estudiante | El estudiante ve tareas no completadas ordenadas por fecha limite. |

## Roles

| Rol | Integrante ejemplo | Responsabilidad |
| --- | --- | --- |
| Product Owner | Ana | Define alcance, prioridad y acepta `HU-001` y `HU-002`. |
| Scrum Master | Luis | Supervisa Sprint, F1, F2 y F5. |
| Analista SDD | Carla | Revisa `spec.md` y matriz de trazabilidad. |
| Equipo De Desarrollo | Diego y Marco | Implementa con IA, prueba y prepara PRs. |
| QA O Validador | Sofia | Valida criterios y registra evidencia. |
| Integrador | Elena | Ejecuta checks, revisa Actions y fusiona PRs. |

## Secuencia De Comandos

Use esta secuencia como columna vertebral del trabajo:

```text
/speckit.ficct.init
/speckit.ficct.specify Agenda academica para estudiantes de la facultad. Web simple con 2 casos de uso: registrar tarea y consultar tareas pendientes.
/speckit.ficct.plan Implementar como web simple con persistencia local o en memoria, pruebas por criterio y evidencia por Sprint.
/speckit.ficct.tasks Dividir el trabajo en tareas pequenas para registrar tarea, consultar pendientes, probar criterios y generar evidencia.
/speckit.ficct.scrum
/speckit.ficct.issues
/speckit.ficct.implement HU-001 Implementa registrar tarea academica con test_registrar_tarea y evidencia en docs/evidencias/sprint-1/
/speckit.ficct.implement HU-002 Implementa consultar tareas pendientes con test_listar_pendientes y evidencia en docs/evidencias/sprint-1/
/speckit.ficct.pr-check
/speckit.ficct.report
```

Cada etapa debe seguir este patron:

1. Ejecutar el comando IA.
2. Dar contexto en el prompt de entrada.
3. Revisar los archivos generados.
4. Ejecutar validadores o pruebas.
5. Hacer commit y PR solo si la evidencia es consistente.

## Compatibilidad De Entorno

Los comandos `/speckit.ficct.*` son iguales en Linux, macOS y Windows. Para scripts Python use:

| Sistema | Comando |
| --- | --- |
| Linux/macOS | `python3 .specify/extensions/ficct/scripts/<script>.py ...` |
| Windows PowerShell | `py -3 .\.specify\extensions\ficct\scripts\<script>.py ...` |

En este ejemplo los bloques `bash` muestran Linux/macOS. En Windows use las equivalencias de [Compatibilidad Windows y Linux](compatibilidad-windows-linux.md).

## 1. Inicializar Proyecto

Responsables: Scrum Master e Integrador.

Terminal:

Linux/macOS:

```bash
mkdir agenda-academica
cd agenda-academica
git init
specify init --here --integration codex --force
specify extension add --dev ../github-sdd-scrum-ficct
```

Windows PowerShell:

```powershell
mkdir agenda-academica
cd agenda-academica
git init
specify init --here --integration codex --force
specify extension add --dev ..\github-sdd-scrum-ficct
```

Nota: no ejecute `specify init` sin argumentos. Despues de `git init`, el directorio contiene `.git`; por eso el ejemplo usa `--here --force` para que Spec Kit inicialice el directorio actual sin pedir confirmacion interactiva.

Comando IA completo:

```text
/speckit.ficct.init Inicializa la estructura FICCT SDD/Scrum para agenda-academica.
Materializa configuracion, assets GitHub, plantillas, validadores y reporte base.
No completes contenido funcional todavia.
```

Validacion:

```bash
git status --short
python3 .specify/extensions/ficct/scripts/ficct_init.py --root . --project-name "agenda academica" --feature agenda-academica --validate --generate-report
```

Commit:

```bash
git add .specify .github specs docs
git commit -m "chore(project): inicializar agenda academica con sdd scrum"
```

## 2. Specify

Responsables: Product Owner y Analista SDD.

Comando IA completo:

```text
/speckit.ficct.specify Agenda academica para estudiantes de la facultad. Web simple con 2 casos de uso: registrar tarea y consultar tareas pendientes.

Producto: gestor web simple de tareas academicas.
Usuario principal: estudiante.
Alcance exacto:
- CU-001: registrar tarea academica con titulo, materia y fecha limite.
- CU-002: consultar tareas pendientes, mostrando solo tareas no completadas ordenadas por fecha limite.

Fuera de alcance:
- autenticacion;
- notificaciones;
- colaboracion entre usuarios;
- edicion avanzada;
- roles administrativos.

IDs obligatorios:
- RF-001 cubre CU-001.
- RF-002 cubre CU-002.
- CA-001 valida RF-001 con test_registrar_tarea.
- CA-002 valida RF-002 con test_listar_pendientes.
- HU-001 enlaza RF-001, CA-001 y PB-001.
- HU-002 enlaza RF-002, CA-002 y PB-002.

Completa trazabilidad RF -> CA -> HU -> PB -> TASK -> prueba -> Issue/PR -> evidencia.
No agregues mas casos de uso.
```

Validacion:

```bash
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
git diff -- specs/agenda-academica/spec.md
```

Contenido minimo que debe existir:

```markdown
| RF-001 | El sistema debe permitir registrar una tarea con titulo, materia y fecha limite. | alta | CU-001 | CA-001 |
| RF-002 | El sistema debe mostrar tareas pendientes ordenadas por fecha limite ascendente. | alta | CU-002 | CA-002 |
| CA-001 | Dado un formulario valido, cuando el estudiante guarda la tarea, entonces la tarea aparece como pendiente. | RF-001 | test_registrar_tarea |
| CA-002 | Dadas varias tareas, cuando el estudiante abre pendientes, entonces solo ve tareas no completadas ordenadas por fecha limite. | RF-002 | test_listar_pendientes |
| HU-001 | Como estudiante, quiero registrar tareas academicas, para recordar mis entregas. | PB-001 | CA-001 | docs/evidencias/sprint-1/HU-001.png |
| HU-002 | Como estudiante, quiero consultar tareas pendientes, para priorizar mis entregas. | PB-002 | CA-002 | docs/evidencias/sprint-1/HU-002.png |
```

Commit:

```bash
git add specs/agenda-academica/spec.md
git commit -m "docs(spec): definir agenda academica con dos casos de uso"
```

## 3. Plan

Responsables: Analista SDD, Desarrollo y QA.

Comando IA completo:

```text
/speckit.ficct.plan Implementar agenda academica como web simple con persistencia local o en memoria, pruebas automatizadas y evidencia por criterio.

Restricciones:
- mantener solo CU-001 y CU-002;
- aplicacion web simple;
- persistencia local o en memoria para el prototipo;
- sin autenticacion.

Incluye:
- alcance tecnico;
- componentes afectados;
- decision RN-001 para persistencia local o en memoria;
- riesgos y mitigaciones;
- estrategia de pruebas;
- test_registrar_tarea cubre CA-001;
- test_listar_pendientes cubre CA-002;
- evidencia esperada en docs/evidencias/sprint-1/.

Mantiene conectados RF-001, RF-002, CA-001, CA-002, HU-001 y HU-002.
```

Validacion:

```bash
git diff -- specs/agenda-academica/plan.md
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
```

Prompt de revision:

```text
Revisa specs/agenda-academica/plan.md contra spec.md.
Corrige si algun CA no tiene prueba, si alguna decision no enlaza RF/RNF/RN o si el plan agrega alcance fuera de CU-001 y CU-002.
```

Commit:

```bash
git add specs/agenda-academica/plan.md
git commit -m "docs(plan): planificar implementacion de agenda academica"
```

## 4. Tasks

Responsables: Scrum Master y Desarrollo.

Comando IA completo:

```text
/speckit.ficct.tasks Divide agenda academica en tareas pequenas para registrar tarea, consultar pendientes, probar criterios y generar evidencia.

Genera solo estas tareas:
- TASK-001: modelo y persistencia de tarea academica para HU-001 / RF-001 / CA-001.
- TASK-002: formulario de registro para HU-001 / RF-001 / CA-001.
- TASK-003: listado filtrado y ordenado de pendientes para HU-002 / RF-002 / CA-002.
- TASK-004: pruebas y evidencias para HU-001 y HU-002.

Cada tarea debe incluir responsable, HU, PB, CA, RF, prueba, evidencia esperada, Issue pendiente y PR pendiente.
No agregues tareas fuera de CU-001 y CU-002.
```

Validacion:

```bash
git diff -- specs/agenda-academica/tasks.md
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
```

Commit:

```bash
git add specs/agenda-academica/tasks.md
git commit -m "docs(tasks): definir tareas trazables de agenda academica"
```

## 5. FICCT Scrum

Responsables: Product Owner y Scrum Master.

Comando IA:

```text
/speckit.ficct.scrum
```

Texto inline de ejemplo:

```text
Genera o actualiza Scrum FICCT usando spec.md, plan.md y tasks.md.

Archivos:
- docs/scrum/f3-product-backlog.md
- docs/scrum/f4-user-stories.md
- docs/scrum/f5-sprint-backlog.md

Contenido obligatorio:
- PB-001 relacionado con CU-001, RF-001, HU-001 y CA-001.
- PB-002 relacionado con CU-002, RF-002, HU-002 y CA-002.
- F4 contiene HU-001 y HU-002.
- F5 contiene TASK-001, TASK-002, TASK-003 y TASK-004 con responsable, Sprint-1, estado y evidencia.
```

Validacion:

```bash
python3 .specify/extensions/ficct/scripts/validate_structure.py --root . --strict
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
```

Commit:

```bash
git add docs/scrum/f3-product-backlog.md docs/scrum/f4-user-stories.md docs/scrum/f5-sprint-backlog.md
git commit -m "docs(scrum): sincronizar backlog e historias de agenda academica"
```

## 6. FICCT Issues

Responsables: Product Owner, Desarrollo y QA.

Comando IA:

```text
/speckit.ficct.issues
```

Texto inline de ejemplo:

```text
Instala o verifica assets GitHub.
Prepara comandos gh issue create para:
1. HU-001 relacionada con RF-001, CA-001, Sprint-1 y evidencia docs/evidencias/sprint-1/HU-001.png.
2. HU-002 relacionada con RF-002, CA-002, Sprint-1 y evidencia docs/evidencias/sprint-1/HU-002.png.
3. TASK-001 relacionada con HU-001, RF-001 y CA-001.
4. TASK-003 relacionada con HU-002, RF-002 y CA-002.
5. Evidencia Sprint-1 para CA-001 y CA-002.

Devuelve comandos listos para ejecutar y no crees Issues sin confirmacion.
```

Instalar assets:

```bash
python3 .specify/extensions/ficct/scripts/install_github_assets.py --root . --dry-run
python3 .specify/extensions/ficct/scripts/install_github_assets.py --root .
```

Ejemplo de comandos que la IA debe generar:

```bash
gh issue create --title "[HU/RF]: HU-001 registrar tarea academica" --label feature,user-story,sdd --body "HU-001
RF-001
CA-001
Sprint-1
Responsable: Ana
Evidencia: docs/evidencias/sprint-1/HU-001.png"

gh issue create --title "[HU/RF]: HU-002 consultar tareas pendientes" --label feature,user-story,sdd --body "HU-002
RF-002
CA-002
Sprint-1
Responsable: Ana
Evidencia: docs/evidencias/sprint-1/HU-002.png"

gh issue create --title "[TASK]: TASK-001 persistencia de tarea" --label task,sdd --body "TASK-001
HU-001
RF-001
CA-001
Sprint-1
Responsable: Diego
Evidencia: test_registrar_tarea"

gh issue create --title "[TASK]: TASK-003 listado de pendientes" --label task,sdd --body "TASK-003
HU-002
RF-002
CA-002
Sprint-1
Responsable: Marco
Evidencia: test_listar_pendientes"

gh issue create --title "[EVIDENCIA]: CA-001 y CA-002 pruebas sprint 1" --label evidence,sdd --body "HU-001, HU-002
RF-001, RF-002
CA-001, CA-002
Sprint-1
Responsable: Sofia"
```

Despues de crear Issues:

```bash
gh issue list --label sdd --state open
```

Comando IA para enlazar numeros reales:

```text
/speckit.ficct.issues
```

Texto inline de ejemplo:

```text
Actualiza spec.md, tasks.md, F5 y matriz con los numeros reales:
- HU-001: #<numero>
- HU-002: #<numero>
- TASK-001: #<numero>
- TASK-003: #<numero>
- Evidencia Sprint-1: #<numero>
```

Commit:

```bash
git add .github specs/agenda-academica docs/scrum docs/sdd
git commit -m "docs(github): enlazar issues de agenda academica"
```

## 7. Implement CU-001

Responsable: Diego.

Terminal:

```bash
git switch -c feature/HU-001-registrar-tarea
```

Comando IA:

```text
/speckit.ficct.implement HU-001 Implementa registrar tarea academica con test_registrar_tarea y evidencia en docs/evidencias/sprint-1/
```

Texto inline de ejemplo:

```text
Implementa CU-001 usando spec.md, plan.md y tasks.md.

Alcance:
- HU-001;
- RF-001;
- CA-001;
- TASK-001;
- TASK-002.

Debe:
- registrar tarea con titulo, materia y fecha limite;
- dejar la tarea como pendiente al guardar;
- agregar test_registrar_tarea;
- guardar evidencia en docs/evidencias/sprint-1/test_registrar_tarea.txt si aplica;
- actualizar tasks.md y F5 solo si la prueba existe;
- no implementar CU-002.
```

Validacion:

```bash
npm test
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
git status --short
```

Commit:

```bash
git add .
git commit -m "feat(tasks): registrar tarea academica"
```

Comando IA para PR:

```text
/speckit.ficct.pr-check
```

Texto inline de ejemplo:

```text
Prepara el cuerpo del PR usando .github/pull_request_template.md.
Guarda el cuerpo en docs/evidencias/sprint-1/pr-hu-001.md.
Debe enlazar Issue HU-001, Issue TASK-001, RF-001, CA-001, HU-001, TASK-001, TASK-002, test_registrar_tarea y evidencia.
```

Crear PR:

```bash
gh pr create --title "feat(tasks): registrar tarea academica" --body-file docs/evidencias/sprint-1/pr-hu-001.md --base main --head feature/HU-001-registrar-tarea
```

## 8. Implement CU-002

Responsable: Marco.

Terminal:

```bash
git switch main
git pull
git switch -c feature/HU-002-consultar-pendientes
```

Comando IA:

```text
/speckit.ficct.implement HU-002 Implementa consultar tareas pendientes con test_listar_pendientes y evidencia en docs/evidencias/sprint-1/
```

Texto inline de ejemplo:

```text
Implementa CU-002 usando spec.md, plan.md y tasks.md.

Alcance:
- HU-002;
- RF-002;
- CA-002;
- TASK-003.

Debe:
- mostrar solo tareas no completadas;
- ordenar por fecha limite ascendente;
- agregar test_listar_pendientes;
- guardar evidencia en docs/evidencias/sprint-1/test_listar_pendientes.txt si aplica;
- actualizar tasks.md y F5 solo si la prueba existe;
- no agregar casos de uso nuevos.
```

Validacion:

```bash
npm test
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
git status --short
```

Commit:

```bash
git add .
git commit -m "feat(tasks): listar tareas pendientes"
```

Comando IA para PR:

```text
/speckit.ficct.pr-check
```

Texto inline de ejemplo:

```text
Prepara el cuerpo del PR usando .github/pull_request_template.md.
Guarda el cuerpo en docs/evidencias/sprint-1/pr-hu-002.md.
Debe enlazar Issue HU-002, Issue TASK-003, RF-002, CA-002, HU-002, TASK-003, test_listar_pendientes y evidencia.
```

Crear PR:

```bash
gh pr create --title "feat(tasks): listar tareas pendientes" --body-file docs/evidencias/sprint-1/pr-hu-002.md --base main --head feature/HU-002-consultar-pendientes
```

## 9. FICCT PR Check

Responsable: Integrador.

Comando IA:

```text
/speckit.ficct.pr-check
```

Texto inline de ejemplo:

```text
Valida el PR actual contra estructura, trazabilidad, plantilla de PR, pruebas y evidencia.
Si hay errores, corrige solo documentos relacionados y vuelve a ejecutar validadores.
No apruebes merge si falta Issue, RF, CA, HU, TASK, prueba o evidencia.
```

Terminal:

```bash
python3 .specify/extensions/ficct/scripts/validate_structure.py --root . --strict
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
gh pr checks
```

Regla de merge:

- validadores en verde;
- GitHub Actions `SDD Gate` en verde;
- PR completo;
- evidencia revisada por QA.

## 10. FICCT Report

Responsables: Scrum Master e Integrador.

Comando IA:

```text
/speckit.ficct.report
```

Texto inline de ejemplo:

```text
Genera el reporte final de cumplimiento.
Antes de generarlo, revisa spec.md, plan.md, tasks.md, F1-F5, matriz y docs/evidencias.
Corrige inconsistencias de IDs entre RF-001, RF-002, CA-001, CA-002, HU-001, HU-002, TASK-001, TASK-002, TASK-003 y TASK-004.
No agregues nuevos casos de uso.
```

Terminal:

```bash
python3 .specify/extensions/ficct/scripts/generate_report.py --root . --strict
cat docs/evidencias/sdd-compliance-report.md
```

Resultado esperado:

```markdown
| Resultado | pass |
```

Commit:

```bash
git add docs/evidencias/sdd-compliance-report.md docs/scrum docs/sdd specs/agenda-academica
git commit -m "docs(report): cerrar cumplimiento sdd scrum de agenda academica"
```

## 11. Cierre Del Sprint

Responsables: todos los roles.

Comando IA:

```text
/speckit.ficct.scrum
```

Texto inline de ejemplo:

```text
Genera el cierre de Sprint-1 en F1 y F2.

Datos:
- CU-001 implementado y validado con CA-001.
- CU-002 implementado y validado con CA-002.
- PR de HU-001 fusionado.
- PR de HU-002 fusionado.
- Issues de historia, tarea y evidencia cerrados.
- GitHub Actions SDD Gate en verde.
- Reporte final generado.

Incluye entregado, criterios aceptados, evidencias, pendientes si existen y mejora de proceso para el siguiente Sprint.
```

Validacion final:

```bash
python3 .specify/extensions/ficct/scripts/validate_structure.py --root . --strict
python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict
python3 .specify/extensions/ficct/scripts/generate_report.py --root . --strict
git status --short
```

Commit:

```bash
git add docs/scrum/f1-sprint-review.md docs/scrum/f2-retrospective.md docs/evidencias/sdd-compliance-report.md
git commit -m "docs(scrum): cerrar sprint de agenda academica"
```

## Checklist Final

- Product Owner: `HU-001` y `HU-002` aceptadas en GitHub.
- Scrum Master: F1, F2 y F5 actualizados.
- Analista SDD: `spec.md` y matriz sincronizados.
- Desarrollo: PRs fusionados para CU-001 y CU-002.
- QA: evidencias de `CA-001` y `CA-002` registradas.
- Integrador: `ficct-pr-check`, GitHub Actions y `ficct-report` en verde.

El proyecto queda completo cuando la IA genero o actualizo los artefactos, el equipo reviso el contenido y los validadores confirmaron estructura y trazabilidad.
