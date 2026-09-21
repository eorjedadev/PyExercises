## Ejercicio 060 — Generador Automatizado de Release Notes desde Git (`rel-notes-gen`)

> [← Ejercicio 059](../ejercicio_059/README.md) · [Índice General](../README.md) · [Ejercicio 061 →](../ejercicio_061/README.md)

### Contexto profesional
En el ciclo de entrega continua de software, preparar las notas de lanzamiento (Release Notes) para una nueva versión requiere analizar todos los commits realizados desde el último tag de versión, categorizarlos según Conventional Commits, extraer autores colaboradores y renderizar una plantilla elegante en Markdown para publicar en GitHub Releases o enviar a clientes.

### Problema
Construir una CLI que inspeccione el repositorio Git local, compare el rango de commits entre dos tags o referencias (ej. `v1.2.0..HEAD`), agrupe los cambios por categoría (`Features`, `Bug Fixes`, `Performance`, `Documentation`, `Breaking Changes`), extraiga referencias a Pull Requests y tickets (ej. `#123`, `JIRA-456`), identifique nuevos contribuidores y renderice el documento Markdown final usando plantillas personalizables.

### Usuario objetivo
Release managers, líderes técnicos y mantenedores de código abierto.

### Objetivo
Crear un generador de notas de versión automatizado basado en el historial de Git con motor de plantillas y categorización inteligente.

### Ejemplo conceptual de uso
```bash
# Generar notas de versión desde el último tag hasta HEAD
python rel_notes_gen.py generate --version "v1.3.0"

# Generar notas entre dos tags específicos usando plantilla personalizada
python rel_notes_gen.py generate --from-tag "v1.2.0" --to-tag "v1.3.0" --template ./templates/release.md.j2 -o RELEASE_v1.3.0.md
```

### Requisitos funcionales
- Detectar automáticamente el tag de versión anterior si no se especifica `--from-tag`.
- Extraer el historial de commits mediante `git log --format=...` en el rango especificado.
- Parsear mensajes de commit clasificándolos según su tipo Conventional Commit:
  - `feat` -> `🚀 Nuevas Características`
  - `fix` -> `🐛 Corrección de Errores`
  - `perf` -> `⚡ Mejoras de Rendimiento`
  - `docs` -> `📚 Documentación`
  - `refactor` -> `♻️ Refactorizaciones`
  - `BREAKING CHANGE` -> `⚠️ Cambios Rupturistas` (destacados al inicio).
- Extraer números de Pull Requests (`#123`) y nombres/correos de autores.
- Listar sección de nuevos contribuidores (autores cuyo primer commit en el repositorio ocurrió en este rango de versiones).
- Renderizar plantilla Markdown por defecto o plantilla personalizada.

### Requisitos de CLI
- Subcomando `generate`.
- Opción `--version <VERSION>`: nombre de la versión que se publicará.
- Opción `--from-tag <TAG>` (default último tag).
- Opción `--to-tag <TAG>` (default `HEAD`).
- Opción `--template <RUTA>`.
- Opción `-o / --output <RUTA>` (default STDOUT).
- Exit code 0 en éxito, 1 si no hay commits en el rango especificado, 2 en errores de Git.

### Entradas
- Repositorio Git y parámetros de versionado.

### Salidas
- Documento Markdown con las notas de versión en STDOUT o archivo.

### Persistencia
Escritura del archivo Markdown si se especifica `-o`.

### Validaciones
- Comprobar que el directorio actual sea un repositorio Git válido.
- Validar que los tags de origen y destino existan en el historial.

### Casos límite
- Repositorio sin tags previos (generar notas desde el commit inicial).
- Commits que no siguen la convención Conventional Commits (agruparlos bajo una sección `Otras Mejoras`).
- Commits de merge (ignorar o procesar según flag `--include-merges`).

### Manejo de errores
- `subprocess.CalledProcessError` al invocar comandos de Git.
- Errores de lectura de plantillas.

### Fundamentos de Python relacionados
- Invocación y parsing de salida de `git log` con `subprocess`.
- Expresiones regulares para extracción de tipos, scopes, PRs y breaking changes.
- Motor de plantillas simple con cadenas de formato o librería `jinja2` (si se investiga).
- Manejo de conjuntos para detección de nuevos contribuidores.

### Conceptos CLI relacionados
- Automatización de procesos de ingeniería de software y release management.
- Extracción y transformación de grafos de commits de Git.

### Herramientas o módulos para investigar
- `subprocess`.
- `re`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para publicar automáticamente las notas generadas en GitHub Releases mediante la API de GitHub o CLI de `gh`?

### Diseño de argumentos
¿Cómo nombrarías la opción para ocultar commits marcados como `chore` o `ci` en el reporte público (`--exclude-internal`)?

### Diseño de variables
`git_commit_records_list`, `categorized_changes_dict`, `breaking_changes_list`, `pull_request_links_set`, `new_contributors_list`.

### Antes de programar
1. ¿Cómo formatear la llamada a `git log` para obtener hash, autor, correo, fecha y mensaje completo separados por delimitadores unívocos (ej. `git log --format="%H%x1f%an%x1f%ae%x1f%s%x1f%b%x1e"`)?
2. ¿Cómo determinar si un autor es nuevo comparando sus commits previos con `git log <from-tag> --author=...`?

### Arquitectura
Extractor de Git (`git_extractor.py`), parser de commits (`commit_categorizer.py`), renderizador de plantillas (`template_renderer.py`) y CLI.

### Pruebas mínimas
1. Generar notas sobre un repo de prueba con 3 commits (`feat`, `fix`, `docs`) y verificar que el Markdown resultante contenga las 3 secciones correspondientes.
2. Verificar que un commit con `BREAKING CHANGE:` aparezca en la sección de advertencia.

### Pruebas de error
1. Ejecutar fuera de un repositorio Git -> Exit code 2 con mensaje claro.

### Experiencia de usuario
Documento Markdown perfectamente formateado listo para ser publicado en portales de release, sin requerir edición manual.

### Explicación posterior
Explica cómo la combinación de Conventional Commits y generadores de Release Notes elimina la fricción en los despliegues ágiles.

### Aplicación profesional
Herramienta integrada en GitHub Actions / GitLab CI para automatizar publicaciones de versiones en repositorios open source y corporativos.

### Reto adicional
Generar automáticamente los enlaces de hipervínculo a los commits y perfiles de usuario en GitHub/GitLab a partir de la URL del repositorio remoto.

---
> [← Ejercicio 059](../ejercicio_059/README.md) · [Índice General](../README.md) · [Ejercicio 061 →](../ejercicio_061/README.md)
