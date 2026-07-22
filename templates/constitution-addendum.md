# Addendum de Constitucion SDD/Scrum FICCT

> Instrucciones: complete todos los campos marcados como obligatorio, mantenga los identificadores estables y actualice la trazabilidad cada vez que cambien requisitos, Scrum, tareas, pruebas o evidencias.

## Metadatos Obligatorios

| Campo | Valor |
| --- | --- |
| Proyecto | `[PROJECT_NAME]` |
| Facultad | `[FACULTY]` |
| Carrera | `[DEGREE]` |
| Materia | `[SUBJECT]` |
| Equipo | `[TEAM_NAME]` |
| Repositorio | `[GITHUB_REPOSITORY_URL]` |
| Fecha de adopcion | `[YYYY-MM-DD]` |

## Reglas Obligatorias

- Todo requisito funcional debe usar ID `RF-###`.
- Todo requisito no funcional debe usar ID `RNF-###`.
- Toda regla de negocio debe usar ID `RN-###`.
- Todo criterio de aceptacion debe usar ID `CA-###`.
- Toda historia de usuario debe usar ID `HU-###`.
- Todo item de Product Backlog debe usar ID `PB-###`.
- Todo artefacto Scrum FICCT debe identificar `F1`, `F2`, `F3`, `F4` o `F5`.
- Ningun Pull Request puede cerrarse sin pruebas y evidencia enlazadas.

## Politicas De Trazabilidad

| ID | Politica obligatoria | Evidencia minima |
| --- | --- | --- |
| RN-001 | Cada `RF`, `RNF` y `RN` debe aparecer en la matriz de trazabilidad. | `[TRACEABILITY_MATRIX_PATH]` |
| RN-002 | Cada `HU` debe enlazar al menos un `PB`, un `CA` y una prueba. | `[F4_PATH]`, `[TEST_REPORT_PATH]` |
| RN-003 | Cada tarea implementada debe enlazar especificacion, historia, prueba, Issue y PR. | `[TASKS_PATH]`, `[GITHUB_PR_URL]` |
| RN-004 | Cada sprint debe producir evidencia `F1` y `F2`. | `[F1_PATH]`, `[F2_PATH]` |

## Criterios De Cumplimiento

| CA | Condicion verificable | Responsable | Evidencia |
| --- | --- | --- | --- |
| CA-001 | La especificacion contiene `RF`, `RNF`, `RN`, `CA` y trazabilidad. | `[ROLE]` | `[SPEC_PATH]` |
| CA-002 | F3, F4 y F5 estan sincronizados con tareas y pruebas. | `[ROLE]` | `[SCRUM_DOCS_PATH]` |
| CA-003 | El reporte SDD no contiene incumplimientos bloqueantes. | `[ROLE]` | `[COMPLIANCE_REPORT_PATH]` |

## Aprobacion

| Rol | Nombre | Fecha | Evidencia |
| --- | --- | --- | --- |
| Product Owner | `[NAME]` | `[YYYY-MM-DD]` | `[APPROVAL_LINK]` |
| Scrum Master | `[NAME]` | `[YYYY-MM-DD]` | `[APPROVAL_LINK]` |
| Equipo de desarrollo | `[NAME_OR_TEAM]` | `[YYYY-MM-DD]` | `[APPROVAL_LINK]` |
