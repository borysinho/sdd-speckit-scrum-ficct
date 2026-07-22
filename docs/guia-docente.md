# Guia Docente

Esta guia enfoca la revision en evidencia verificable. La nota no debe depender solo de que existan archivos, sino de que la trazabilidad explique que se pidio, que se planifico, que se implemento, como se probo y donde esta la evidencia.

La revision debe aceptar evidencia generada en Linux, macOS o Windows. Los comandos pueden variar entre `python3` y `py -3`, pero deben apuntar a los mismos scripts y producir los mismos resultados. Use [Compatibilidad Windows y Linux](compatibilidad-windows-linux.md) como referencia.

## Evidencia Principal A Revisar

| Evidencia | Que confirma |
| --- | --- |
| `specs/<feature>/spec.md` | Requisitos, criterios de aceptacion e historias con IDs estables. |
| `specs/<feature>/plan.md` | Decisiones tecnicas, riesgos, pruebas y alcance de implementacion. |
| `specs/<feature>/tasks.md` | Trabajo ejecutable por tarea, responsable, prueba y evidencia. |
| `docs/scrum/f3-product-backlog.md` | Priorizacion del producto. |
| `docs/scrum/f4-user-stories.md` | Historias alineadas con requisitos. |
| `docs/scrum/f5-sprint-backlog.md` | Plan de Sprint con tareas y responsables. |
| `docs/sdd/traceability-matrix.md` | Cadena RF/RNF/RN -> CA -> HU -> TASK -> prueba -> evidencia. |
| Pull Request | Integracion de Issue, pruebas, evidencia y decisiones. |
| GitHub Actions | Validacion automatica de estructura y trazabilidad. |
| `docs/evidencias/sdd-compliance-report.md` | Resumen de cumplimiento y pendientes. |

## Criterios De Evaluacion

1. Coherencia SDD: cada requisito tiene criterio verificable y fuente clara.
2. Coherencia Scrum: F3, F4 y F5 reflejan el mismo alcance que `spec.md`, `plan.md` y `tasks.md`.
3. Trazabilidad: los IDs `RF/RNF/RN`, `CA`, `HU`, `TASK` y Sprint aparecen conectados.
4. Evidencia: las pruebas, capturas, demos o reportes demuestran los criterios declarados.
5. Uso de GitHub: Issues y PRs no son decorativos; deben contener informacion suficiente para auditar el trabajo.
6. Calidad de cierre: el PR queda revisable, Actions explican su resultado y el reporte final no oculta pendientes.

## Como Revisar GitHub Issues

Revise al menos una historia, una tarea y una evidencia por Sprint. En cada Issue verifique:

- ID correcto y estable.
- Relacion con requisito y criterio de aceptacion.
- Responsable y Sprint.
- Evidencia esperada o entregada.
- Enlace a PR, commit, captura, reporte o prueba.

Un Issue cerrado sin evidencia enlazada debe contarse como pendiente.

## Como Revisar Pull Requests

El PR debe llenar la plantilla instalada. La revision docente puede seguir este orden:

1. Confirmar que enlaza un Issue de GitHub.
2. Verificar IDs de requisito, historia, tarea y Sprint.
3. Leer criterios de aceptacion cubiertos.
4. Revisar comandos de prueba y resultado.
5. Abrir evidencia enlazada.
6. Revisar si hubo decisiones nuevas o cambios de alcance.
7. Confirmar que `SDD Gate` paso o que el fallo esta justificado y corregido.

## Como Interpretar GitHub Actions

El workflow `SDD Gate` se ejecuta en Pull Requests y pushes a `main` o `master`.

- Verde: los validadores no encontraron pendientes estructurales ni de trazabilidad minima.
- Rojo en assets: faltan Issue Forms, PR template o workflow.
- Rojo en estructura: falta carpeta, archivo Scrum, matriz o `spec/plan/tasks`.
- Rojo en trazabilidad: falta una relacion documental entre `RF/RNF/RN`, `CA`, `HU` o `TASK`.

Un workflow verde no reemplaza la evaluacion docente: solo prueba que la evidencia documental minima existe.

## Como Evaluar Evidencia

Evidencia fuerte:

- Comando reproducible con salida visible.
- Sistema operativo y terminal indicados cuando el comando depende del entorno.
- Captura o video con fecha, feature y resultado reconocible.
- PR que muestra cambios relacionados con la tarea.
- Matriz actualizada con la misma cadena de IDs.
- Reporte final sin pendientes o con pendientes declarados.

Evidencia debil:

- Captura sin relacion con `CA`.
- Texto que afirma "probado" sin comando ni resultado.
- Issue cerrado sin PR ni evidencia.
- IDs inconsistentes entre documentos.
- Actions rojas sin explicacion.

## Limitaciones De La Primera Version

- No mide calidad del codigo ni cobertura real.
- No crea ni sincroniza Issues automaticamente.
- No valida que una captura corresponda al sistema correcto.
- No reemplaza la revision docente de decisiones y evidencia.
- Puede aceptar trazabilidad superficial si los IDs aparecen conectados, aunque el contenido sea pobre.
