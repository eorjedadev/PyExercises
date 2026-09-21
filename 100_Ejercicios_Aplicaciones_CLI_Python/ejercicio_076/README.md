## Ejercicio 076 — Gestor y Ejecutor de Git Pre-Commit Hooks (`pre-commit-lite`)

> [← Ejercicio 075](../ejercicio_075/README.md) · [Índice General](../README.md) · [Ejercicio 077 →](../ejercicio_077/README.md)

### Contexto profesional
Para asegurar que ningún desarrollador suba código con errores de sintaxis, secretos expuestos, formateo inconsistente o pruebas unitarias rotas, los equipos configuran Git Hooks locales que se ejecutan automáticamente antes de cada `git commit` o `git push`.

### Problema
Construir una CLI que actúe como gestor de hooks de Git ligero (similar a la herramienta `pre-commit`), configurado mediante un archivo declarativo `.hooks.yaml` o `.hooks.json`, que instale el script ejecutable en `.git/hooks/pre-commit`, filtre únicamente los archivos preparados en el staging de Git (`staged files`), ejecute una lista de herramientas en paralelo o secuencia y aborte el commit si alguna verificación falla.

### Usuario objetivo
Desarrolladores de software, DevOps y líderes de equipo.

### Objetivo
Crear un gestor y orquestador de hooks de Git con filtrado de staged files, ejecución de checkers configurables e instalación desatendida.

### Ejemplo conceptual de uso
```bash
# Instalar el hook en el repositorio Git actual
python pre_commit_lite.py install

# Ejecutar manualmente todos los hooks sobre todos los archivos del repo
python pre_commit_lite.py run --all-files

# Ejecutar hooks únicamente sobre los archivos staged para el commit
python pre_commit_lite.py run
```

### Requisitos funcionales
- Archivo de configuración `.hooks.json` con lista de tareas:
  - `id`: identificador de la tarea (ej. `check-yaml`, `ruff-format`, `no-secrets`, `pytest`).
  - `name`: nombre descriptivo.
  - `command`: comando ejecutable del sistema.
  - `files_regex`: patrón de archivos a los que aplica (ej. `\.py$`, `\.json$`).
  - `pass_filenames`: booleano (si es true, pasa los archivos staged como argumentos al comando).
- Subcomando `install`: escribe el script interceptor en `.git/hooks/pre-commit` con permisos ejecutables.
- Subcomando `uninstall`: remueve el hook de Git de forma segura.
- Subcomando `run`: obtiene la lista de archivos modificados en el staging de Git (`git diff --cached --name-only --diff-filter=ACM`), evalúa qué hooks aplican, los ejecuta y muestra el resultado de cada uno (`PASSED` / `FAILED`).
- Si cualquier hook retorna un código de salida diferente de 0, abortar el proceso con exit code 1 para cancelar el `git commit`.

### Requisitos de CLI
- Subcomandos: `install`, `uninstall`, `run`.
- Opción `--config <RUTA>` (default `.hooks.json`).
- Flag `--all-files` en `run`: ejecuta sobre todo el repositorio, no solo staged.
- Flag `-v / --verbose`: muestra la salida completa de los comandos que fallan.
- Exit code 0 si todos los hooks pasan, 1 si al menos un hook falla (bloqueando el commit), 2 en errores.

### Entradas
- Archivo de configuración de hooks y estado del staging de Git.

### Salidas
- Resumen visual de ejecución de hooks en STDOUT y detalles de fallos en STDERR.

### Persistencia
Creación del hook ejecutable en `.git/hooks/pre-commit`.

### Validaciones
- Comprobar que el directorio actual sea un repositorio Git.
- Validar que los comandos configurados existan en el sistema antes de ejecutar.

### Casos límite
- Commit sin ningún archivo que coincida con las expresiones regulares (debe pasar exitosamente sin ejecutar comandos innecesarios).
- Commits con archivos con nombres con espacios.
- Archivos eliminados en el staging (no pasarlos a herramientas que esperan que el archivo exista).

### Manejo de errores
- `subprocess.CalledProcessError`.
- `FileNotFoundError` si `.git` no existe.

### Fundamentos de Python relacionados
- Invocación y control de subprocesos con `subprocess.run`.
- Manipulación de archivos y permisos ejecutables (`os.chmod` en Unix para `0o755`).
- Expresiones regulares para filtrado de extensiones de archivo.
- Módulo `json` para configuración.

### Conceptos CLI relacionados
- Integración profunda con el flujo de trabajo de Git.
- Gating de calidad local antes de compartir código con el equipo.

### Herramientas o módulos para investigar
- `subprocess`.
- `pathlib` y `os`.
- `re` y `json`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para que el hook de pre-push ejecute pruebas más pesadas que el pre-commit (`install --hook-type pre-push`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para ejecutar únicamente un hook específico por ID (`--hook-id ruff-format`)?

### Diseño de variables
`staged_files_list`, `configured_hooks_list`, `matching_files_chunk`, `hook_process_result`, `all_hooks_passed_boolean`.

### Antes de programar
1. ¿Cómo obtener la lista exacta de archivos agregados, copiados o modificados en el staging de Git usando `git diff --cached --name-only --diff-filter=ACM`?
2. ¿Cómo estructurar el script Bash/Python que se coloca en `.git/hooks/pre-commit` para que invoque a `pre_commit_lite.py run`?

### Arquitectura
Gestor de hooks de Git (`hook_manager.py`), ejecutor de comandos (`hook_runner.py`), parser de configuración (`config_parser.py`) y CLI.

### Pruebas mínimas
1. Configurar un hook de prueba simple (ej. validador de sintaxis JSON), crear un archivo JSON staged roto, ejecutar `run` y verificar que reporte `FAILED` y retorne exit code 1.
2. Corregir el JSON, ejecutar `run` y verificar que reporte `PASSED` y retorne exit code 0.

### Pruebas de error
1. Ejecutar `install` fuera de un repositorio Git -> Exit code 2 con error claro.

### Experiencia de usuario
Salida elegante en terminal: `Check Python Syntax (flake8)................[PASSED]`, `Check Trailing Whitespace...................[FAILED] (3 archivos corregibles)`.

### Explicación posterior
Explica la importancia de la retroalimentación rápida (Shift-Left Testing) al detectar errores en la máquina local del desarrollador antes de que lleguen a CI.

### Aplicación profesional
Estandarización de calidad en equipos de desarrollo, prevención de subida de secretos y formateo automático de código.

### Reto adicional
Implementar soporte para auto-formateo y auto-stage automático (si un formateador modifica un archivo, volver a agregarlo a Git con `git add`).

---
> [← Ejercicio 075](../ejercicio_075/README.md) · [Índice General](../README.md) · [Ejercicio 077 →](../ejercicio_077/README.md)
