# Decisiones Del Paquete

Este documento registra decisiones de documentacion y uso para la primera version de `github-sdd-scrum-ficct`.

## DEC-001 - Mantener La Extension Local

Decision: la primera version se instala como extension local de Spec Kit con `specify extension add --dev`.

Motivo: permite usarla en laboratorio sin publicar paquetes ni depender de infraestructura externa. Tambien facilita revisar plantillas y scripts en clase.

Impacto: cada equipo debe tener la extension en una ruta accesible o recibirla dentro del repositorio base del curso.

## DEC-002 - Validar Documentacion Antes Que Codigo

Decision: `validate_structure.py` y `validate_traceability.py` revisan archivos, carpetas e IDs documentales.

Motivo: el objetivo academico inicial es ensenar trazabilidad SDD/Scrum, no reemplazar herramientas de calidad de codigo.

Impacto: un resultado verde indica cumplimiento documental minimo, pero no garantiza calidad funcional ni cobertura real.

## DEC-003 - Usar IDs Estables

Decision: la cadena de evidencia usa IDs como `RF-001`, `RNF-001`, `RN-001`, `CA-001`, `HU-001`, `TASK-001` y `Sprint-1`.

Motivo: los IDs facilitan auditar la misma decision desde especificacion, Scrum, Issue, PR, prueba y reporte.

Impacto: los estudiantes deben evitar renombrar IDs a mitad del Sprint sin actualizar toda la matriz.

## DEC-004 - No Automatizar Creacion De Issues En La Primera Version

Decision: la extension instala formularios de Issues, pero no crea Issues ni PRs automaticamente.

Motivo: evita requerir tokens, permisos de repositorio y manejo de errores de API durante la etapa inicial.

Impacto: los estudiantes completan Issues y PRs manualmente; el docente evalua la calidad de esos registros.

## DEC-005 - Compatibilidad Linux Y Windows

Decision: la documentacion debe mostrar equivalencias para Linux/macOS y Windows PowerShell cuando se ejecuten scripts locales.

Motivo: los equipos trabajan desde sus hogares y pueden usar distintos sistemas operativos.

Impacto: los comandos de IA se mantienen iguales, pero las guias deben indicar `python3` para Linux/macOS y `py -3` para Windows PowerShell.

## Limitaciones De La Primera Version

- No crea Issues, PRs ni comentarios automaticos en GitHub.
- No sincroniza cambios entre `spec.md`, Scrum F1-F5 y matriz de trazabilidad.
- No calcula cobertura de pruebas ni ejecuta test suites del proyecto.
- No valida semanticamente que una evidencia demuestre un criterio de aceptacion.
- No gestiona multiples equipos, roles o rubricas de calificacion dentro del workflow.
- No reemplaza la revision docente de alcance, decisiones y evidencia.

## Mejoras Futuras

- Comando que genere borradores de Issues desde F4/F5.
- Reporte con resumen por Sprint, equipo y responsable.
- Validacion configurable de nombres de ramas y commits.
- Integracion opcional con GitHub CLI para crear Issues y PRs.
- Rubrica docente parametrizable por materia.
