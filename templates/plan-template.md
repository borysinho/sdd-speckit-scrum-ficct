# Plan De Implementacion: `[FEATURE_NAME]`

> Instrucciones: complete decisiones tecnicas, riesgos, tareas y evidencia antes de iniciar desarrollo. Mantenga sincronizado este plan con `spec.md`, `tasks.md`, F3, F4 y F5.

## Metadatos Obligatorios

| Campo | Valor |
| --- | --- |
| Feature | `[FEATURE_NAME]` |
| Spec | `[SPEC_PATH]` |
| Responsable tecnico | `[OWNER]` |
| Sprint | `[SPRINT_ID]` |
| Fecha | `[YYYY-MM-DD]` |
| Estado | `[draft/approved/in-progress/done]` |

## Alcance Tecnico

| Elemento | Descripcion |
| --- | --- |
| Objetivo de implementacion | `[IMPLEMENTATION_GOAL]` |
| Componentes afectados | `[MODULES_OR_SERVICES]` |
| Dependencias | `[DEPENDENCIES]` |
| Migraciones o datos | `[DATA_OR_MIGRATION_NOTES]` |
| Restricciones | `[TECHNICAL_CONSTRAINTS]` |

## Decisiones

| ID | Decision | Justificacion | RF/RNF/RN relacionados |
| --- | --- | --- | --- |
| RN-001 | `[TECHNICAL_OR_PRODUCT_DECISION]` | `[RATIONALE]` | `RF-001, RNF-001` |

## Riesgos Y Mitigaciones

| ID | Riesgo | Impacto | Mitigacion | Evidencia requerida |
| --- | --- | --- | --- | --- |
| RISK-001 | `[RISK_DESCRIPTION]` | `[high/medium/low]` | `[MITIGATION]` | `[EVIDENCE_LINK]` |

## Estrategia De Pruebas

| Prueba | Tipo | CA cubiertos | Responsable | Evidencia |
| --- | --- | --- | --- | --- |
| `[TEST_ID_OR_PATH]` | `[unit/integration/e2e/manual]` | `CA-001` | `[OWNER]` | `[TEST_REPORT_OR_SCREENSHOT]` |

## Trazabilidad Del Plan

| RF/RNF/RN | CA | HU | PB | Tarea planificada | Prueba | Evidencia |
| --- | --- | --- | --- | --- | --- | --- |
| RF-001 | CA-001 | HU-001 | PB-001 | `[TASK_ID]` | `[TEST_ID_OR_PATH]` | `[EVIDENCE_LINK]` |

## Gate De Aprobacion

- [ ] Las decisiones cubren los requisitos afectados.
- [ ] Las pruebas cubren todos los `CA`.
- [ ] Los riesgos tienen mitigacion y evidencia.
- [ ] El plan esta enlazado desde F5 y desde el PR.
