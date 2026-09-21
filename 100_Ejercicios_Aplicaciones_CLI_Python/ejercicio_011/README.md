## Ejercicio 011 — Analizador de Extensiones y Espacio en Directorios (`ext-stats`)

> [← Ejercicio 010](../ejercicio_010/README.md) · [Índice General](../README.md) · [Ejercicio 012 →](../ejercicio_012/README.md)

### Contexto profesional
En servidores de almacenamiento, estaciones de trabajo de desarrollo y sistemas de archivos compartidos, los administradores necesitan saber qué tipos de archivos están consumiendo la mayor cantidad de espacio en disco (ej. videos `.mp4`, volcados `.dump`, artefactos `.zip` o `.tar.gz`).

### Problema
Desarrollar una CLI que recorra recursivamente un directorio, agrupe todos los archivos por su extensión, calcule el conteo total de archivos, el tamaño acumulado en bytes (formateado en KB, MB, GB) y el porcentaje que representa cada extensión respecto al total.

### Usuario objetivo
Administradores de sistemas, desarrolladores y usuarios avanzados.

### Objetivo
Crear un analizador de uso de disco por tipo de archivo con cálculo de agregados, formateo de unidades binarias y ordenamiento flexible.

### Ejemplo conceptual de uso
```bash
# Analizar el directorio actual
python ext_stats.py .

# Analizar directorio ordenando por tamaño y mostrando top 10
python ext_stats.py /var/log --sort size --top 10
```

### Requisitos funcionales
- Recorrer el directorio especificado de forma recursiva.
- Manejar archivos sin extensión agrupándolos bajo `(sin extensión)`.
- Extraer dobles extensiones comunes (ej. `.tar.gz`, `.tar.bz2`).
- Calcular: Cantidad de archivos, Tamaño total acumulado, Tamaño promedio por archivo y Porcentaje del total.
- Formatear tamaños de forma legible (B, KB, MB, GB, TB) con 2 decimales.
- Opciones de ordenamiento: por tamaño (`size`), por cantidad de archivos (`count`) o por extensión alfabética (`name`).

### Requisitos de CLI
- Argumento posicional: ruta del directorio a analizar (default `.`).
- Opción `--sort [size|count|name]` (default `size`).
- Opción `--top <N>` (default muestra todas o top N).
- Flag `--human-readable / -H` (activado por defecto).
- Exit code 0 en éxito, 1 si el directorio no existe o no se puede leer, 2 en argumentos inválidos.

### Entradas
- Ruta de directorio.

### Salidas
- Tabla con columnas: `EXTENSIÓN`, `ARCHIVOS`, `TAMAÑO TOTAL`, `% ESPACIO`, `PROMEDIO`.

### Persistencia
Sin persistencia.

### Validaciones
- Comprobar que la ruta exista y sea un directorio.
- Manejar enlaces simbólicos (`symlinks`) para evitar bucles infinitos.

### Casos límite
- Directorio completamente vacío (debe reportar 0 archivos y 0 B sin fallar).
- Archivos con permisos denegados durante el recorrido (omitir y registrar advertencia sin abortar).
- Archivos ocultos que inician con punto (ej. `.gitignore` -> considerar si es extensión o archivo sin extensión).

### Manejo de errores
- `PermissionError`: Capturar al listar subdirectorios protegidos.
- `FileNotFoundError` si un archivo desaparece durante el escaneo.

### Fundamentos de Python relacionados
- Módulo estándar `pathlib` (`Path.rglob()`, `Path.stat()`, `is_file()`, `is_symlink()`).
- Módulo `os` (`os.scandir` para máxima velocidad).
- Algoritmos de ordenamiento con funciones lambda y `sorted()`.

### Conceptos CLI relacionados
- Formateo de números y unidades para humanos vs máquinas.
- Manejo elegante de permisos en exploraciones del sistema de archivos.

### Herramientas o módulos para investigar
- `pathlib` y `os.scandir`.
- `argparse`.

### Diseño de comandos
¿Cómo agregarías un flag `--include-hidden` para controlar si se analizan archivos y carpetas ocultas?

### Diseño de argumentos
¿Cómo permitirías ignorar ciertas extensiones o carpetas (ej. `--ignore-dir node_modules,.git`)?

### Diseño de variables
`target_dir`, `extension_stats`, `total_directory_size`, `total_file_count`, `human_formatted_size`, `sort_criterion`.

### Antes de programar
1. ¿Por qué `os.scandir()` es sustancialmente más rápido que `os.walk()` o `Path.rglob()` en directorios con decenas de miles de archivos?
2. ¿Cómo evitar contar dos veces un archivo accesible mediante enlaces simbólicos circulares?

### Arquitectura
Función `scan_directory(path)` con generador de estadísticas y formateador de tabla.

### Pruebas mínimas
1. Escanear un directorio con fixtures de prueba y comprobar que la suma de bytes por extensión coincida con el tamaño total del directorio.
2. Ordenar por `--sort count` y verificar el orden descendente.

### Pruebas de error
1. Pasar una ruta a un archivo regular en lugar de directorio -> Exit code 1.

### Experiencia de usuario
Salida visualmente agradable con alineación a la derecha para números y porcentajes, y barra de resumen al pie.

### Explicación posterior
Explica la diferencia entre tamaño de archivo (file size) y tamaño en disco (allocated disk blocks / cluster size).

### Aplicación profesional
Diagnóstico de almacenamiento en servidores, optimización de imágenes Docker y limpieza de entornos de compilación.

### Reto adicional
Agregar una barra visual en texto ASCII que represente la proporción de uso (ej. `[████████░░░░] 65.4%`).

---
> [← Ejercicio 010](../ejercicio_010/README.md) · [Índice General](../README.md) · [Ejercicio 012 →](../ejercicio_012/README.md)
