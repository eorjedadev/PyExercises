## Ejercicio 071 — Scaffolder de Proyectos y CLI Profesionales en Python (`cli-scaffold`)

> [← Ejercicio 070](../ejercicio_070/README.md) · [Índice General](../README.md) · [Ejercicio 072 →](../ejercicio_072/README.md)

### Contexto profesional
En equipos de ingeniería, iniciar una nueva herramienta CLI desde cero sin una estructura estandarizada genera inconsistencias de arquitectura, configuración deficiente de dependencias y falta de pruebas automatizadas. Un generador de plantillas (scaffolder) asegura que todos los proyectos cumplan los estándares corporativos.

### Problema
Construir una CLI que genere la estructura completa y profesional de un nuevo proyecto de aplicación CLI en Python, incluyendo `pyproject.toml`, configuración de empaquetado y entry points (`[project.scripts]`), estructura `src/`, suite de pruebas con `pytest`, linters (`ruff`, `mypy`), Dockerfile y workflow de GitHub Actions.

### Usuario objetivo
Desarrolladores de software, tech leads y equipos de DevOps.

### Objetivo
Crear una herramienta de scaffolding de proyectos CLI con parametrización interactiva y no interactiva, sustitución de variables en plantillas y validación de nombres de paquete.

### Ejemplo conceptual de uso
```bash
# Crear un nuevo proyecto CLI con arquitectura modular y soporte de PostgreSQL
python cli_scaffold.py new "data-pipeline-cli" --author "DevOps Team" --email "devops@empresa.com" --framework argparse --db postgresql

# Crear proyecto interactivo con wizard guiado
python cli_scaffold.py new --interactive
```

### Requisitos funcionales
- Subcomando `new <NOMBRE_PROYECTO>`: genera el árbol de directorios y archivos completos del nuevo proyecto.
- Opciones de framework CLI a integrar en la plantilla: `argparse` estándar, `click` o `typer`.
- Opciones de persistencia a generar en la plantilla: `postgresql` (con módulo `psycopg`), `sqlite` o `none`.
- Estructura generada:
  - `pyproject.toml`: metadatos del paquete, dependencias y entry point ejecutable `[project.scripts]`.
  - `src/<package_name>/`: `__init__.py`, `cli.py`, `core.py`, `config.py`.
  - `tests/`: `conftest.py`, `test_cli.py` con pruebas unitarias de ejemplo.
  - `.gitignore`, `.env.example`, `README.md`, `Dockerfile`, `.github/workflows/ci.yml`.
- Sustitución de variables de plantilla (nombre, slug, autor, email, licencia, año, descripción).

### Requisitos de CLI
- Subcomando `new`.
- Opción `--author <NOMBRE>`.
- Opción `--email <EMAIL>`.
- Opción `--framework [argparse|click|typer]` (default `argparse`).
- Opción `--db [postgresql|sqlite|none]` (default `none`).
- Opción `--out-dir <RUTA>` (default directorio actual).
- Flag `--interactive / -i`.
- Exit code 0 en éxito, 1 si el directorio de destino ya existe sin `--force`, 2 en errores de argumentos.

### Entradas
- Parámetros de configuración del proyecto y plantillas de código.

### Salidas
- Árbol de archivos generado en disco y resumen de inicialización.

### Persistencia
Creación completa de directorios y archivos en el sistema de archivos.

### Validaciones
- El nombre del proyecto debe ser un identificador de paquete PEP 508 válido (letras minúsculas, números, guiones o guiones bajos).
- No permitir sobreescribir un directorio existente a menos que se use `--force`.

### Casos límite
- Nombres de proyecto con palabras reservadas de Python (ej. `test`, `os`, `sys`, `email`).
- Generación en rutas sin permisos de escritura.

### Manejo de errores
- `FileExistsError` si el directorio ya existe.
- `PermissionError`.

### Fundamentos de Python relacionados
- `pathlib.Path` para creación recursiva de directorios y archivos.
- Motor de sustitución de plantillas con `string.Template` o cadenas de formato.
- Estándar de empaquetado moderno PEP 517 / PEP 621 (`pyproject.toml`).

### Conceptos CLI relacionados
- Scaffolding y generación declarativa de proyectos.
- Estandarización de arquitecturas de software.

### Herramientas o módulos para investigar
- `string.Template`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `list-templates` para listar las plantillas de proyecto disponibles?

### Diseño de argumentos
¿Cómo nombrarías la opción para inicializar automáticamente un repositorio Git (`git init`) en el proyecto generado (`--git-init`)?

### Diseño de variables
`project_slug_name`, `python_package_identifier`, `template_variables_dictionary`, `scaffold_destination_path`, `project_license_type`.

### Antes de programar
1. ¿Cómo estructurar el archivo `pyproject.toml` según PEP 621 para definir `[project.scripts]` que apunte a `mi_paquete.cli:main`?
2. ¿Cómo diseñar la sustitución de plantillas para que los archivos generados no tengan problemas de codificación o saltos de línea incompatibles?

### Arquitectura
Motor de plantillas (`template_engine.py`), validador de identificadores (`validator.py`), asistente interactivo (`wizard.py`) y CLI.

### Pruebas mínimas
1. Generar un proyecto de prueba `test-cli-tool` y verificar que existan `pyproject.toml`, `src/test_cli_tool/cli.py` y `tests/test_cli.py`.
2. Ejecutar `pytest` dentro del proyecto generado y verificar que las pruebas pasen.

### Pruebas de error
1. Intentar crear un proyecto con nombre inválido `123-proyecto!` -> Exit code 2 con error de formato.

### Experiencia de usuario
Mensaje final inspirador con instrucciones claras de inicio rápido: `cd mi-proyecto && pip install -e . && pytest`.

### Explicación posterior
Explica la evolución del empaquetado en Python desde `setup.py` / `setup.cfg` hacia el estándar unificado `pyproject.toml` (PEP 517/518/621).

### Aplicación profesional
Aceleración del desarrollo de herramientas internas en organizaciones de tecnología y estandarización de repositorios.

### Reto adicional
Implementar un subcomando `add-command <NOMBRE>` dentro de un proyecto ya generado para añadir automáticamente un nuevo subcomando a la CLI existente.

---
> [← Ejercicio 070](../ejercicio_070/README.md) · [Índice General](../README.md) · [Ejercicio 072 →](../ejercicio_072/README.md)
