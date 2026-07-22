# F3 - Product Backlog

> Instrucciones: registre items priorizados con IDs `PB-###`. Cada item debe enlazar requisitos, historias, criterios de aceptacion, tareas y evidencia.

## Metadatos Obligatorios

| Campo | Valor |
| --- | --- |
| Proyecto | `[PROJECT_NAME]` |
| Product Owner | `[PRODUCT_OWNER]` |
| Fecha de actualizacion | `[YYYY-MM-DD]` |
| Fuente principal | `[SPEC_OR_REPOSITORY_LINK]` |

## Items Del Product Backlog

| PB | Titulo | Descripcion | Prioridad | Valor | Estado | RF/RNF/RN | HU | CA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PB-001 | `[BACKLOG_ITEM_TITLE]` | `[BACKLOG_ITEM_DESCRIPTION]` | `[alta/media/baja]` | `[BUSINESS_OR_ACADEMIC_VALUE]` | `[todo/ready/in-progress/done]` | `RF-001, RN-001` | `HU-001` | `CA-001` |

## Criterios De Preparacion

| PB | Condicion de ready | Responsable | Evidencia |
| --- | --- | --- | --- |
| PB-001 | Tiene `RF/RNF/RN`, `HU`, `CA`, estimacion y prioridad. | `[OWNER]` | `[LINK_TO_SPEC_OR_REVIEW]` |

## Trazabilidad Y Evidencia

| PB | RF/RNF/RN | HU | CA | F5/Tarea | Prueba | Issue/PR | Evidencia |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PB-001 | `RF-001, RNF-001, RN-001` | `HU-001` | `CA-001` | `F5-001/TASK-001` | `[TEST_ID_OR_PATH]` | `[ISSUE_OR_PR_URL]` | `[EVIDENCE_LINK]` |

## Checklist F3

- [ ] Cada `PB` tiene prioridad y estado.
- [ ] Cada `PB` enlaza al menos una `HU`.
- [ ] Cada `PB` implementado tiene prueba y evidencia.
