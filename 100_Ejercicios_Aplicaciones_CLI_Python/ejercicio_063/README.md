## Ejercicio 063 — Empaquetador y Minificador de Assets Estáticos (`asset-bundler`)

> [← Ejercicio 062](../ejercicio_062/README.md) · [Índice General](../README.md) · [Ejercicio 064 →](../ejercicio_064/README.md)

### Contexto profesional
En la compilación de sitios web y aplicaciones frontend modernas sin dependencias pesadas de Node.js, los desarrolladores necesitan empaquetar, concatenar y minificar archivos CSS y JavaScript, generar hashes de contenido (cache busting, ej. `styles.a3f5b8.min.css`) y actualizar automáticamente las referencias en los archivos HTML.

### Problema
Construir una CLI que procese un directorio de assets estáticos (archivos `.css`, `.js`, `.html`), concatene módulos según un manifiesto de entrada, minifique código eliminando espacios/comentarios innecesarios mediante reglas léxicas eficientes, calcule el hash de contenido de cada archivo resultante para cache-busting y genere un manifiesto de assets `manifest.json`.

### Usuario objetivo
Desarrolladores web, creadores de herramientas ligeras y DevOps.

### Objetivo
Crear un empaquetador de assets estáticos con minificación nativa, generación de hashes criptográficos para cache-busting y actualización de HTML.

### Ejemplo conceptual de uso
```bash
# Empaquetar y minificar directorio de assets hacia carpeta de distribución
python asset_bundler.py build --src ./src --dist ./dist --hash

# Modo observador para reconstruir automáticamente ante cambios
python asset_bundler.py watch --src ./src --dist ./dist
```

### Requisitos funcionales
- Subcomando `build`: recorre la carpeta de origen, procesa archivos CSS y JS:
  - Minificación CSS: remueve comentarios `/* ... */`, saltos de línea y espacios en blanco redundantes alrededor de `{`, `}`, `:`, `;`.
  - Minificación JS básica: remueve comentarios de línea `//` y bloque `/* */`, espacios colapsables y líneas vacías (respetando strings).
- Modo `--hash`: renombra los archivos de salida agregando un hash corto SHA256 de su contenido (ej. `app.8b3a1c.min.js`).
- Generar archivo `manifest.json` que mapee el archivo original a su versión empaquetada (ej. `{"app.js": "app.8b3a1c.min.js"}`).
- Actualizar automáticamente las etiquetas `<link rel="stylesheet" ...>` y `<script src="...">` en los archivos HTML copiados a la carpeta de distribución.
- Subcomando `watch`: monitorea el directorio de origen y ejecuta `build` automáticamente cuando se modifican archivos.

### Requisitos de CLI
- Subcomandos: `build`, `watch`.
- Opción `--src <DIR>` (default `./src`).
- Opción `--dist <DIR>` (default `./dist`).
- Flag `--hash`.
- Flag `--sourcemap` (genera mapa básico de archivos concatenados).
- Exit code 0 en compilación exitosa, 1 en errores de sintaxis de assets, 2 en errores de argumentos.

### Entradas
- Directorio de archivos fuente CSS, JS y HTML.

### Salidas
- Archivos minificados y manifiesto en el directorio de distribución.

### Persistencia
Creación y actualización de archivos en el sistema de archivos.

### Validaciones
- Comprobar que el directorio `--src` exista y contenga archivos.
- Limpiar el directorio `--dist` antes de compilar para no acumular archivos huérfanos.

### Casos límite
- Comentarios dentro de cadenas de texto literales (ej. `var url = "http://sitio.com//test";` no debe truncarse como comentario `//`).
- Código CSS con data-URIs Base64 incrustadas.
- Archivos ya minificados (evitar romper sintaxis al re-minificar).

### Manejo de errores
- `PermissionError` al escribir en `--dist`.
- Manejo de interrupción en modo `watch`.

### Fundamentos de Python relacionados
- Expresiones regulares y tokenizadores léxicos para stripping seguro de comentarios.
- Módulo `hashlib` para cálculo de hashes de contenido.
- `pathlib.Path` y `shutil.copy2` para manipulación de árboles de archivos.
- Detección de cambios de archivos mediante polling de `st_mtime` en modo `watch`.

### Conceptos CLI relacionados
- Construcción de pipelines de build y compilación en terminal.
- Implementación del patrón Watcher para desarrollo continuo.

### Herramientas o módulos para investigar
- `re`.
- `hashlib`.
- `pathlib` y `shutil`.
- `time` y `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para soportar compresión pre-generada Gzip / Brotli (`--gzip`) para servir directamente desde Nginx?

### Diseño de argumentos
¿Cómo nombrarías la opción para definir el orden de concatenación de módulos JS mediante un archivo de configuración (`--bundle-config bundle.json`)?

### Diseño de variables
`source_assets_tree`, `minified_content_buffer`, `content_sha256_hash`, `asset_manifest_dictionary`, `dist_output_directory`.

### Antes de programar
1. ¿Cómo diseñar la expresión regular de limpieza de comentarios JS para que no borre partes de cadenas de texto entre comillas o expresiones regulares literales `/pattern/`?
2. ¿Cómo implementar un bucle de observación de archivos en `watch` comparando timestamps de modificación (`mtime`) cada 500ms sin consumir 100% de CPU?

### Arquitectura
Minificador CSS (`css_minifier.py`), minificador JS (`js_minifier.py`), inyector HTML (`html_injector.py`), observador (`watcher.py`) y CLI.

### Pruebas mínimas
1. Compilar un proyecto con 1 CSS y 1 JS con comentarios, verificar que los archivos resultantes en `--dist` no tengan comentarios y su tamaño sea menor.
2. Verificar que el `index.html` en `--dist` tenga las rutas actualizadas con los hashes.

### Pruebas de error
1. Pasar un directorio fuente que no existe -> Exit code 2 con error descriptivo.

### Experiencia de usuario
Resumen claro en terminal con tabla de assets compilados, reducción de tamaño en KB y porcentaje de ahorro de peso.

### Explicación posterior
Explica el concepto de *Cache Busting* mediante hashes de contenido inmutables y cabeceras HTTP `Cache-Control: max-age=31536000, immutable`.

### Aplicación profesional
Compilación de assets en frameworks web ligeros, empaquetado de extensiones de navegador y optimización de sitios web estáticos.

### Reto adicional
Implementar inyección en línea (inlining) de CSS crítico directamente dentro de la etiqueta `<style>` del HTML para optimizar el First Contentful Paint (FCP).

---
> [← Ejercicio 062](../ejercicio_062/README.md) · [Índice General](../README.md) · [Ejercicio 064 →](../ejercicio_064/README.md)
