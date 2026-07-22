# F4 - Historias De Usuario

> Instrucciones: escriba historias con IDs `HU-###`. Cada historia debe estar conectada con Product Backlog, requisitos, criterios de aceptacion, tareas, pruebas y evidencia.

## Metadatos Obligatorios

| Campo | Valor |
| --- | --- |
| Proyecto | `[PROJECT_NAME]` |
| Sprint o release | `[SPRINT_OR_RELEASE]` |
| Responsable | `[OWNER]` |
| Fecha | `[YYYY-MM-DD]` |

## Historias

### HU-001 - `[STORY_TITLE]`

**Historia:** Como `[ROLE]`, quiero `[CAPABILITY]`, para `[BENEFIT]`.

| Campo | Valor |
| --- | --- |
| PB | `PB-001` |
| Prioridad | `[alta/media/baja]` |
| Estimacion | `[STORY_POINTS_OR_SIZE]` |
| Estado | `[draft/ready/in-progress/done]` |
| Issue GitHub | `[GITHUB_ISSUE_URL]` |

## Criterios De Aceptacion

| CA | Dado/Cuando/Entonces | RF/RNF/RN | Prueba |
| --- | --- | --- | --- |
| CA-001 | `Dado [contexto], cuando [accion], entonces [resultado]` | `RF-001, RN-001` | `[TEST_ID_OR_PATH]` |

## Trazabilidad Y Evidencia

| HU | PB | RF/RNF/RN | CA | F5/Tarea | Prueba | Issue/PR | Evidencia |
| --- | --- | --- | --- | --- | --- | --- | --- |
| HU-001 | PB-001 | `RF-001, RNF-001, RN-001` | CA-001 | `F5-001/TASK-001` | `[TEST_ID_OR_PATH]` | `[ISSUE_OR_PR_URL]` | `[EVIDENCE_LINK]` |

## Checklist F4

- [ ] Cada `HU` tiene formato rol-capacidad-beneficio.
- [ ] Cada `HU` enlaza `PB` y al menos un `CA`.
- [ ] Cada `CA` tiene prueba y evidencia.
