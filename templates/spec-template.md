# Especificacion De Feature: `[FEATURE_NAME]`

> Instrucciones: reemplace placeholders, conserve IDs estables y no marque una seccion como completa si falta trazabilidad hacia Scrum, tareas, pruebas o evidencia.

## Metadatos Obligatorios

| Campo | Valor |
| --- | --- |
| Feature | `[FEATURE_NAME]` |
| Rama | `[BRANCH_NAME]` |
| Autor(es) | `[AUTHOR_NAMES]` |
| Fecha | `[YYYY-MM-DD]` |
| Estado | `[draft/review/approved/implemented]` |
| Issue principal | `[GITHUB_ISSUE_URL]` |

## Contexto

**Problema:** `[PROBLEM_STATEMENT]`

**Objetivo:** `[OUTCOME_EXPECTED]`

**Usuarios afectados:** `[USER_TYPES]`

**Fuera de alcance:** `[OUT_OF_SCOPE]`

## Requisitos Funcionales

| RF | Descripcion obligatoria | Prioridad | Fuente | CA vinculados |
| --- | --- | --- | --- | --- |
| RF-001 | `[SYSTEM_SHALL_BEHAVIOR]` | `[alta/media/baja]` | `[STAKEHOLDER_OR_DOC]` | `CA-001` |

## Requisitos No Funcionales

| RNF | Atributo | Condicion medible | Evidencia esperada |
| --- | --- | --- | --- |
| RNF-001 | `[performance/security/usability/etc]` | `[MEASURABLE_CONDITION]` | `[TEST_OR_REPORT_PATH]` |

## Reglas De Negocio

| RN | Regla | Impacto | Validacion |
| --- | --- | --- | --- |
| RN-001 | `[BUSINESS_RULE]` | `[WHO_OR_WHAT_IS_AFFECTED]` | `CA-001` |

## Criterios De Aceptacion

| CA | Dado/Cuando/Entonces | RF/RNF/RN cubiertos | Prueba requerida |
| --- | --- | --- | --- |
| CA-001 | `Dado [contexto], cuando [accion], entonces [resultado]` | `RF-001, RN-001` | `[TEST_ID_OR_PATH]` |

## Historias Relacionadas

| HU | Historia | PB | CA | Evidencia |
| --- | --- | --- | --- | --- |
| HU-001 | `Como [rol], quiero [capacidad], para [beneficio]` | `PB-001` | `CA-001` | `[EVIDENCE_LINK]` |

## Trazabilidad Y Evidencia

| RF/RNF/RN | CA | HU | PB | Tarea | Prueba | Issue/PR | Evidencia |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RF-001 | CA-001 | HU-001 | PB-001 | `[TASK_ID]` | `[TEST_ID_OR_PATH]` | `[ISSUE_OR_PR_URL]` | `[EVIDENCE_LINK]` |

## Checklist De Revision

- [ ] Todos los `RF`, `RNF`, `RN` y `CA` tienen IDs unicos.
- [ ] Cada `CA` tiene prueba verificable.
- [ ] Cada `HU` enlaza `PB`, tareas, Issue/PR y evidencia.
- [ ] La matriz de trazabilidad fue actualizada.
