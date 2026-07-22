# Especificacion Login

## Requisitos Funcionales

| RF | Descripcion | CA vinculados |
| --- | --- | --- |
| RF-001 | El sistema permite iniciar sesion. | CA-001 |

## Requisitos No Funcionales

| RNF | Condicion | CA vinculados |
| --- | --- | --- |
| RNF-001 | La respuesta ocurre en menos de dos segundos. | CA-001 |

## Reglas De Negocio

| RN | Regla | CA vinculados |
| --- | --- | --- |
| RN-001 | Solo usuarios activos pueden iniciar sesion. | CA-001 |

## Criterios De Aceptacion

| CA | Dado/Cuando/Entonces | RF/RNF/RN cubiertos |
| --- | --- | --- |
| CA-001 | Dado un usuario activo, cuando envia credenciales validas, entonces ingresa al sistema. | RF-001, RNF-001, RN-001 |

## Historias Relacionadas

| HU | Historia | CA |
| --- | --- | --- |
| HU-001 | Como estudiante, quiero iniciar sesion para usar el sistema. | CA-001 |

## Trazabilidad Y Evidencia

| RF/RNF/RN | CA | HU | Tarea |
| --- | --- | --- | --- |
| RF-001, RNF-001, RN-001 | CA-001 | HU-001 | TASK-001 |
