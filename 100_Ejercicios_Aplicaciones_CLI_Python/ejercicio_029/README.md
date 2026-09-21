## Ejercicio 029 — Gestor y Generador de Changelogs KeepAChangelog (`chg-log`)

> [← Ejercicio 028](../ejercicio_028/README.md) · [Índice General](../README.md) · [Ejercicio 030 →](../ejercicio_030/README.md)

### Contexto profesional
En el desarrollo ágil y mantenimiento de software, mantener un historial de cambios (`CHANGELOG.md`) ordenado y legible según el estándar internacional *Keep a Changelog* (con categorías: Added, Changed, Deprecated, Removed, Fixed, Security) es fundamental para comunicar actualizaciones a clientes y desarrolladores.

### Problema
Construir una CLI que permita registrar nuevas entradas de cambio sin editar el archivo Markdown manualmente, agruparlas por categoría bajo una sección `[Unreleased]`, incrementar la versión del proyecto según Semantic Versioning (`major`, `minor`, `patch`) y compilar el archivo final.

### Usuario objetivo
Desarrolladores, release managers y mantenedores de librerías.

### Objetivo
Crear un gestor automatizado de registros de cambio que garantice el cumplimiento del estándar Keep a Changelog y SemVer.

### Ejemplo conceptual de uso
```bash
# Registrar una nueva característica añadida
python chg_log.py add "Soporte para exportación en formato Excel" --type added --issue 142

# Registrar un bugfix
python chg_log.py add "Corrección de fuga de memoria en parsing" --type fixed

# Publicar una nueva versión (bump version) cerrando Unreleased
python chg_log.py bump minor --release-date "2026-06-15"
```

### Requisitos funcionales
- Subcomando `add <MENSAJE>`: añade un ítem bajo `[Unreleased]` en la categoría correspondiente (`added`, `changed`, `deprecated`, `removed`, `fixed`, `security`).
- Opción `--issue <ID>` para incluir enlace o referencia a ticket.
- Subcomando `bump [major|minor|patch]`: extrae la última versión semántica (ej. `1.2.4`), calcula la siguiente (ej. minor -> `1.3.0`), convierte la sección `[Unreleased]` en la nueva versión con la fecha actual y crea una nueva sección `[Unreleased]` vacía.
- Subcomando `validate`: comprueba que el archivo `CHANGELOG.md` existente cumpla con el formato estricto.
- Subcomando `export`: exporta el contenido de una versión específica para usarlo como Release Note en GitHub/GitLab.

### Requisitos de CLI
- Subcomandos: `add`, `bump`, `validate`, `export`.
- Opciones específicas según subcomando.
- Exit code 0 en éxito, 1 si la validación falla o la versión no existe, 2 en errores de sintaxis.

### Entradas
- Mensajes de cambio, tipos de categoría y acciones de versionado.

### Salidas
- Modificación directa en `CHANGELOG.md` o fragmento de release note en STDOUT.

### Persistencia
Lectura y escritura estructurada de `CHANGELOG.md`.

### Validaciones
- El tipo de cambio en `add` debe ser uno de los 6 permitidos por Keep a Changelog.
- El cálculo de versión SemVer debe respetar la jerarquía de 3 dígitos numéricos `X.Y.Z`.

### Casos límite
- `CHANGELOG.md` inexistente (crearlo con plantilla base).
- Intentar hacer `bump` cuando `[Unreleased]` no contiene ningún cambio registrado (advertir o requerir `--allow-empty`).
- Múltiples versiones pre-release o con sufijos (ej. `1.0.0-rc.1`).

### Manejo de errores
- Errores de parseo del archivo Markdown existente si alguien lo editó rompiendo la estructura.

### Fundamentos de Python relacionados
- Expresiones regulares para parsing y manipulación de texto Markdown.
- Manejo de fechas con `datetime.date`.
- Manipulación segura de archivos de texto con backups temporales.

### Conceptos CLI relacionados
- Automatización de flujos de trabajo de ingeniería de software.
- Mantenimiento determinista de documentación.

### Herramientas o módulos para investigar
- `re`.
- `pathlib`.
- `datetime`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `export --version 1.2.0` para que emita exclusivamente las notas de esa versión?

### Diseño de argumentos
¿Cómo permitirías especificar un archivo de changelog personalizado (`--file docs/HISTORY.md`)?

### Diseño de variables
`changelog_path`, `change_category`, `change_description`, `current_semver`, `next_semver`, `unreleased_entries`.

### Antes de programar
1. ¿Cómo estructurar el parser Markdown para leer y modificar secciones sin destruir comentarios o enlaces al final del documento?
2. ¿Cómo calcular el incremento de versión SemVer (ej. `bump minor` sobre `1.4.9` debe producir `1.5.0`, no `1.5.9`)?

### Arquitectura
Parser (`changelog_parser.py`), motor SemVer (`semver.py`) y CLI (`chg_log.py`).

### Pruebas mínimas
1. Crear changelog nuevo, hacer `add` de 2 items en diferentes categorías y verificar que aparezcan bajo `## [Unreleased]`.
2. Ejecutar `bump patch` y verificar que la sección pase a llamarse `## [0.0.1] - YYYY-MM-DD`.

### Pruebas de error
1. Pasar `--type categoria_invalida` -> Exit code 2 listando los tipos permitidos.

### Experiencia de usuario
Confirmación concisa de cada acción: `[OK] Añadido cambio a [Added]` o `[BUMP] Versión incrementada a 2.1.0`.

### Explicación posterior
Explica la filosofía de *Semantic Versioning 2.0.0* y la regla de breaking changes en versiones `0.X.Y` vs `1.0.0+`.

### Aplicación profesional
Automatización en pipelines de release (GitHub Actions, semantic-release) y estandarización de equipos de ingeniería.

### Reto adicional
Generar automáticamente los enlaces de comparación de diferencias de Git al final del archivo (ej. `[Unreleased]: https://github.com/org/repo/compare/v1.2.0...HEAD`).

---
> [← Ejercicio 028](../ejercicio_028/README.md) · [Índice General](../README.md) · [Ejercicio 030 →](../ejercicio_030/README.md)
