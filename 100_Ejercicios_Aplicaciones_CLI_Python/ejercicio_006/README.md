## Ejercicio 006 — Extractor y Validador de Enlaces Markdown (`md-links`)

> [← Ejercicio 005](../ejercicio_005/README.md) · [Índice General](../README.md) · [Ejercicio 007 →](../ejercicio_007/README.md)

### Contexto profesional
En documentación técnica, repositorios de código abierto y wikis de ingeniería, los enlaces rotos o mal formateados en archivos Markdown degradan la calidad del proyecto y generan frustración en los usuarios.

### Problema
Construir una CLI que analice uno o varios archivos Markdown, extraiga todos los enlaces HTTP/HTTPS y rutas relativas locales, y valide su formato y opcionalmente su disponibilidad de red.

### Usuario objetivo
Technical writers, desarrolladores y mantenedores de proyectos open source.

### Objetivo
Crear un extractor sintáctico y validador de enlaces en archivos Markdown con reportes tabulares y detección de hipervínculos rotos.

### Ejemplo conceptual de uso
```bash
# Extraer enlaces de un archivo
python md_links.py README.md

# Validar enlaces locales y comprobar que los archivos referenciados existan
python md_links.py README.md --validate-local

# Exportar reporte de enlaces en formato JSON
python md_links.py docs/ --recursive --json
```

### Requisitos funcionales
- Parsear sintaxis Markdown estándar: `[Texto del enlace](URL_o_Ruta)` e imágenes `![Alt text](URL_o_Ruta)`.
- Extraer texto ancla, URL/Ruta de destino y número de línea donde aparece.
- En modo `--validate-local`, comprobar que los archivos o secciones ancla (`#seccion`) referenciados existan en el sistema de archivos relativo.
- Permitir procesar un archivo individual o un directorio recursivo (`--recursive`).

### Requisitos de CLI
- Argumento posicional: archivo `.md` o directorio.
- Opción `--validate-local`: valida existencia de rutas relativas.
- Opción `--json`: emite la lista estructurada de enlaces en JSON.
- Opción `--recursive`: busca todos los `.md` en subdirectorios.
- Exit code 0 si todos los enlaces locales son válidos, 1 si hay enlaces rotos, 2 en error de argumentos.

### Entradas
- Ruta de archivo o directorio Markdown.

### Salidas
- Reporte en tabla en STDOUT o payload JSON con la lista de enlaces encontrados y su estado de validación.

### Persistencia
Sin persistencia.

### Validaciones
- Validar que el archivo objetivo tenga extensión `.md` o `.markdown`.
- Validar que el directorio exista si se usa `--recursive`.

### Casos límite
- Enlaces anidados o con caracteres especiales en la URL (paréntesis, query params).
- Enlaces dentro de bloques de código de bloque (triple comilla invertida) o en línea con comilla simple invertida que no deben parsearse.
- Enlaces con rutas relativas con `../` hacia niveles superiores.

### Manejo de errores
- Manejo de errores de lectura y permisos.
- Advertencias para enlaces sintácticamente mal formados.

### Fundamentos de Python relacionados
- Expresiones regulares (`re.compile`, `re.finditer`).
- Módulo `pathlib.Path` para resolución de rutas relativas y comprobación de `exists()`.
- Módulo `json` para serialización de resultados.

### Conceptos CLI relacionados
- Manejo de recursividad en el sistema de archivos.
- Modos de salida duales: amigable para humanos (tabla) vs máquina (`--json`).

### Herramientas o módulos para investigar
- `re`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo estructurarías el comando para filtrar solo enlaces externos (`--external-only`) o solo locales (`--local-only`)?

### Diseño de argumentos
¿Cómo llamarías a un flag para ignorar dominios específicos (`--ignore-domain localhost`)?

### Diseño de variables
`markdown_file`, `link_pattern`, `link_text`, `target_url`, `line_number`, `is_valid_target`.

### Antes de programar
1. ¿Cómo evitar falsos positivos de enlaces dentro de bloques de código Markdown?
2. ¿Cómo resolver la ruta relativa de un enlace `[guia](doc/guia.md)` con respecto al directorio donde reside el archivo `.md`?

### Arquitectura
Estructura sugerida con módulo de parsing (`parser.py`) y validador de rutas (`validator.py`).

### Pruebas mínimas
1. Crear archivo con 3 enlaces válidos y 1 local inexistente. Ejecutar con `--validate-local` -> Detectar el enlace roto y salir con código 1.

### Pruebas de error
1. Ejecutar sobre un archivo inexistente -> Exit code 2.

### Experiencia de usuario
Presentar una lista clara indicando archivo, línea, texto y URL, con marcas visuales de éxito o fallo.

### Explicación posterior
Explica la diferencia entre regex voraz (greedy) y no voraz (lazy/non-greedy) al capturar enlaces Markdown `\[(.*?)\]\((.*?)\)`.

### Aplicación profesional
Herramienta integrada en CI/CD (GitHub Actions / GitLab CI) para verificar documentación antes de publicar releases.

### Reto adicional
Incorporar verificación de enlaces web externos usando `urllib.request` con timeout corto (2s) y flag `--check-online`.

---
> [← Ejercicio 005](../ejercicio_005/README.md) · [Índice General](../README.md) · [Ejercicio 007 →](../ejercicio_007/README.md)
