# Compatibilidad Windows Y Linux

La extension esta pensada para equipos que trabajan en Linux, macOS o Windows. Los comandos de IA son iguales en todos los sistemas; lo que cambia es la terminal usada para ejecutar scripts y algunas rutas.

## Requisitos

| Herramienta | Linux/macOS | Windows |
| --- | --- | --- |
| Git | `git --version` | `git --version` en PowerShell o Git Bash |
| Python 3 | `python3 --version` | `py -3 --version` |
| Spec Kit | `specify --help` | `specify --help` |
| GitHub CLI | `gh --version` | `gh --version` |
| Node.js, si el proyecto lo usa | `npm --version` | `npm --version` |

## Terminal Recomendada

| Sistema | Terminal recomendada | Nota |
| --- | --- | --- |
| Linux | Bash | Use `python3`. |
| macOS | Zsh o Bash | Use `python3`. |
| Windows | PowerShell 7 o Git Bash | En PowerShell use `py -3`; en Git Bash puede usar `python3` si esta disponible. |

## Inicializacion De Spec Kit

Si ya creo la carpeta del proyecto, entro con `cd` y ejecuto `git init`, inicialice Spec Kit en el directorio actual con:

```bash
specify init --here --integration codex --force
```

El comando `specify init` sin argumentos falla porque Spec Kit exige un nombre de proyecto, `.` o `--here`. El flag `--force` evita la confirmacion que aparece porque `git init` ya creo `.git`; no lo use en un proyecto con archivos propios sin revisar antes.

## Comandos De IA

Los comandos de la extension no cambian por sistema operativo:

```text
/speckit.ficct.init Inicializa agenda academica.
/speckit.ficct.specify Agenda academica para estudiantes...
/speckit.ficct.plan Implementar como web simple...
/speckit.ficct.tasks Dividir en tareas pequenas...
/speckit.ficct.scrum
/speckit.ficct.issues
/speckit.ficct.implement HU-001 ...
/speckit.ficct.pr-check
/speckit.ficct.report
```

## Equivalencias De Python

| Accion | Linux/macOS | Windows PowerShell |
| --- | --- | --- |
| Inicializar FICCT | `python3 .specify/extensions/ficct/scripts/ficct_init.py --root . --project-name "agenda academica" --feature agenda-academica --validate --generate-report` | `py -3 .\.specify\extensions\ficct\scripts\ficct_init.py --root . --project-name "agenda academica" --feature agenda-academica --validate --generate-report` |
| Instalar assets GitHub | `python3 .specify/extensions/ficct/scripts/install_github_assets.py --root .` | `py -3 .\.specify\extensions\ficct\scripts\install_github_assets.py --root .` |
| Validar estructura | `python3 .specify/extensions/ficct/scripts/validate_structure.py --root . --strict` | `py -3 .\.specify\extensions\ficct\scripts\validate_structure.py --root . --strict` |
| Validar trazabilidad | `python3 .specify/extensions/ficct/scripts/validate_traceability.py --root . --strict` | `py -3 .\.specify\extensions\ficct\scripts\validate_traceability.py --root . --strict` |
| Generar reporte | `python3 .specify/extensions/ficct/scripts/generate_report.py --root . --strict` | `py -3 .\.specify\extensions\ficct\scripts\generate_report.py --root . --strict` |

## Rutas

En documentos y GitHub use rutas con `/`, por ejemplo:

```text
docs/evidencias/sprint-1/HU-001.png
specs/agenda-academica/spec.md
```

En PowerShell puede ejecutar scripts con `\`:

```powershell
py -3 .\.specify\extensions\ficct\scripts\validate_structure.py --root . --strict
```

No mezcle rutas absolutas personales en evidencias o PRs. Use rutas relativas del repositorio.

## GitHub CLI

Los comandos `gh` funcionan en Linux, macOS y Windows. Para evitar diferencias entre Bash y PowerShell, prefiera comandos de una sola linea o deje que la IA genere el comando adecuado para su terminal.

Ejemplo portable:

```bash
gh issue list --label sdd --state open
gh pr checks
```

## Evidencia

Cuando registre pruebas, indique siempre:

- sistema operativo usado;
- terminal usada;
- comando ejecutado;
- resultado;
- ruta de evidencia.

Ejemplo:

```text
SO: Windows 11
Terminal: PowerShell 7
Comando: py -3 .\.specify\extensions\ficct\scripts\validate_traceability.py --root . --strict
Resultado: Trazabilidad minima SDD/Scrum encontrada.
```
