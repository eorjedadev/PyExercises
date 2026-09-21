## Ejercicio 040 — Bóveda de Notas Markdown con Búsqueda por Etiquetas (`note-cli`)

> [← Ejercicio 039](../ejercicio_039/README.md) · [Índice General](../README.md) · [Ejercicio 041 →](../ejercicio_041/README.md)

### Contexto profesional
Los ingenieros y arquitectos de software redactan continuamente notas de diseño técnico, registros de decisiones arquitectónicas (ADR), minutas de reuniones y guías de resolución de problemas. Disponer de una bóveda local basada en archivos Markdown puros en el sistema de archivos con gestión de metadatos (frontmatter YAML) permite mantener la información versionable en Git y consultable desde terminal.

### Problema
Construir una CLI para crear, editar, buscar y exportar notas Markdown, gestionando metadatos en formato frontmatter YAML (`title`, `date`, `tags`, `author`, `status`), permitiendo abrir el editor del sistema, buscar por texto completo o etiquetas y generar índices automáticos.

### Usuario objetivo
Desarrolladores, arquitectos de software e investigadores.

### Objetivo
Desarrollar un sistema de gestión de notas en Markdown puro con parsing de YAML frontmatter, indexación y búsqueda.

### Ejemplo conceptual de uso
```bash
# Crear una nueva nota interactiva o por argumento
python note_cli.py new "Arquitectura de Microservicios" --tags "arch,backend,adr"

# Buscar notas que contengan una etiqueta específica
python note_cli.py search --tag "adr"

# Buscar texto dentro de las notas (full-text search)
python note_cli.py find "event-driven"

# Abrir una nota en el editor configurado
python note_cli.py edit "arquitectura-de-microservicios"
```

### Requisitos funcionales
- Subcomando `new <TITULO>`: crea un archivo `.md` con nombre basado en slug (ej. `2026-06-15-arquitectura-de-microservicios.md`), inserta encabezado frontmatter YAML estructurado y abre el editor si se indica `--edit`.
- Subcomando `list`: lista notas mostrando fecha, título, tags y tamaño.
- Subcomando `search`: filtra por etiquetas (`--tag`) o estado (`--status draft|published`).
- Subcomando `find <TEXTO>`: busca ocurrencias de texto completo dentro del cuerpo de todas las notas.
- Subcomando `edit <SLUG/TITULO>`: busca la nota e invoca el editor del sistema (`$EDITOR`).
- Subcomando `index`: genera un archivo `README.md` índice con tabla de contenidos y enlaces a todas las notas de la bóveda.

### Requisitos de CLI
- Subcomandos: `new`, `list`, `search`, `find`, `edit`, `index`.
- Opción `--vault-dir <RUTA>`: carpeta de la bóveda (default `~/.notes_vault/`).
- Exit code 0 en éxito, 1 si la nota no se encuentra, 2 en errores.

### Entradas
- Títulos, tags, contenidos de notas y parámetros de búsqueda.

### Salidas
- Tablas de notas en terminal, contenido de notas o archivos generados.

### Persistencia
Directorio de archivos individuales Markdown (`.md`) en disco.

### Validaciones
- El título de la nota no debe estar vacío.
- Sanitizar el nombre del archivo para generar slugs seguros para el sistema de archivos.

### Casos límite
- Notas sin frontmatter YAML (manejo tolerante como texto Markdown puro).
- Títulos con caracteres especiales o acentos (generación de slug con normalización Unicode).
- Notas duplicadas con el mismo título en el mismo día.

### Manejo de errores
- `FileNotFoundError` al editar una nota inexistente.
- Manejo de fallos al invocar el editor externo.

### Fundamentos de Python relacionados
- `pathlib.Path` para manipulación de archivos y carpetas.
- Parsing de frontmatter YAML (usando lógica nativa con delimitadores `---` o parser).
- `subprocess.run` para invocar el editor configurado (`$EDITOR`).
- `unicodedata.normalize` para generación de slugs.

### Conceptos CLI relacionados
- Integración con editores externos del sistema operativo.
- Bóvedas de conocimiento basadas en archivos planos.

### Herramientas o módulos para investigar
- `pathlib`.
- `subprocess`.
- `unicodedata`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `export --format html` para compilar las notas a un sitio web estático básico?

### Diseño de argumentos
¿Cómo nombrarías la opción para añadir contenido a una nota existente directamente desde la línea de comandos sin abrir el editor (`--append "Nuevo punto..."`)?

### Diseño de variables
`vault_path`, `note_slug`, `yaml_frontmatter_dict`, `note_body_markdown`, `search_results_list`.

### Antes de programar
1. ¿Cómo parsear el bloque frontmatter delimitado por `---` al inicio del archivo sin romper el cuerpo de la nota si este contiene guiones?
2. ¿Cómo generar un slug seguro a partir de un título en español como `"Diseño de la API & Autenticación v2!"` -> `"diseno-de-la-api-autenticacion-v2"`?

### Arquitectura
Gestor de bóveda (`vault_manager.py`), parser de frontmatter (`frontmatter.py`), slugifier (`slug_util.py`) y CLI.

### Pruebas mínimas
1. Crear una nota nueva con tags y validar que el archivo físico contenga el frontmatter YAML y la fecha actual.
2. Ejecutar `search --tag` y verificar que la nota recién creada aparezca en los resultados.

### Pruebas de error
1. Intentar editar una nota inexistente -> Exit code 1 con sugerencias de nombres similares.

### Experiencia de usuario
Interacción ágil y rápida, abriendo el editor instantáneamente y mostrando tablas claras al listar.

### Explicación posterior
Explica el concepto de sistemas de notas basadas en texto plano (Plain Text Accounting / Zettelkasten / Obsidian-compatible) y la ventaja de la soberanía de datos sobre soluciones SaaS propietarias.

### Aplicación profesional
Gestión de Architecture Decision Records (ADRs) en repositorios Git y sistemas de documentación técnica personal.

### Reto adicional
Implementar detección y resolución de enlaces cruzados tipo WikiLinks `[[Nombre de Otra Nota]]` dentro del cuerpo de las notas.

---
> [← Ejercicio 039](../ejercicio_039/README.md) · [Índice General](../README.md) · [Ejercicio 041 →](../ejercicio_041/README.md)
