# Matriz De Trazabilidad SDD/Scrum/GitHub

> Instrucciones: use esta matriz como fuente de verificacion cruzada. No deje filas implementadas sin prueba, PR y evidencia.

## Metadatos Obligatorios

| Campo | Valor |
| --- | --- |
| Proyecto | `[PROJECT_NAME]` |
| Fecha de actualizacion | `[YYYY-MM-DD]` |
| Responsable | `[OWNER]` |
| Repositorio | `[GITHUB_REPOSITORY_URL]` |
| Estado | `[draft/review/approved]` |

## Matriz Principal

| RF/RNF/RN | Descripcion corta | CA | HU | PB | F5 | Tarea | Prueba | Issue | PR | Evidencia | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RF-001 | `[SHORT_REQUIREMENT]` | CA-001 | HU-001 | PB-001 | F5-001 | TASK-001 | `[TEST_ID_OR_PATH]` | `[ISSUE_URL]` | `[PR_URL]` | `[EVIDENCE_LINK]` | `[covered/missing/risk]` |
| RNF-001 | `[SHORT_NFR]` | CA-001 | HU-001 | PB-001 | F5-001 | TASK-001 | `[TEST_ID_OR_PATH]` | `[ISSUE_URL]` | `[PR_URL]` | `[EVIDENCE_LINK]` | `[covered/missing/risk]` |
| RN-001 | `[SHORT_RULE]` | CA-001 | HU-001 | PB-001 | F5-001 | TASK-001 | `[TEST_ID_OR_PATH]` | `[ISSUE_URL]` | `[PR_URL]` | `[EVIDENCE_LINK]` | `[covered/missing/risk]` |

## Cobertura Scrum

| Artefacto | Ruta | IDs cubiertos | Evidencia |
| --- | --- | --- | --- |
| F1 | `[F1_PATH]` | `PB-001, HU-001, CA-001` | `[EVIDENCE_LINK]` |
| F2 | `[F2_PATH]` | `RN-001` | `[EVIDENCE_LINK]` |
| F3 | `[F3_PATH]` | `PB-001` | `[EVIDENCE_LINK]` |
| F4 | `[F4_PATH]` | `HU-001` | `[EVIDENCE_LINK]` |
| F5 | `[F5_PATH]` | `F5-001, TASK-001` | `[EVIDENCE_LINK]` |

## Hallazgos

| ID | Hallazgo | Severidad | Accion | Responsable |
| --- | --- | --- | --- | --- |
| HALL-001 | `[TRACEABILITY_GAP]` | `[blocker/high/medium/low]` | `[ACTION]` | `[OWNER]` |
