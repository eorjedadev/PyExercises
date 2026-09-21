## Ejercicio 057 — Extractor Concurrente de Metadatos de Archivos Multimedia (`media-meta`)

> [← Ejercicio 056](../ejercicio_056/README.md) · [Índice General](../README.md) · [Ejercicio 058 →](../ejercicio_058/README.md)

### Contexto profesional
En plataformas de gestión de contenido digital (DAM), procesamiento de catálogos de comercio electrónico y aplicaciones de medios, se requiere inspeccionar decenas de miles de archivos de imágenes y videos para extraer metadatos técnicos (dimensiones, resolución, espacio de color, duración, tasa de bits, cámara EXIF) exportándolos en formatos estructurados.

### Problema
Construir una CLI concurrente que recorra directorios de medios masivos, distribuya la extracción de metadatos entre múltiples núcleos de CPU mediante `multiprocessing` o `ThreadPoolExecutor`, y genere un catálogo estructurado en CSV, JSON o base de datos relacional (PostgreSQL/SQLite).

### Usuario objetivo
Ingenieros de datos, fotógrafos técnicos y desarrolladores de plataformas de medios.

### Objetivo
Desarrollar un extractor de metadatos concurrente de alto rendimiento con balanceo de carga entre procesos y salida estructurada.

### Ejemplo conceptual de uso
```bash
# Extraer metadatos de imágenes en paralelo usando 8 procesos
python media_meta.py /var/media/photos --workers 8 --format csv -o catalog.csv

# Filtrar imágenes con resolución mayor a 4K y guardar en base de datos
python media_meta.py /var/media/ --min-width 3840 --min-height 2160 --db-url "postgresql://user:pass@localhost:5432/media_db"
```

### Requisitos funcionales
- Recorrer recursivamente directorios buscando formatos multimedia (`.jpg`, `.jpeg`, `.png`, `.webp`, `.mp4`, `.mov`, `.mkv`).
- Extraer metadatos técnicos sin cargar el contenido completo de los archivos: dimensiones (ancho, alto), formato MIME, espacio de color, tamaño en bytes, fecha de creación/captura y datos EXIF (modelo de cámara, lente, coordenadas GPS si están presentes).
- Procesamiento paralelo/concurrente configurable mediante `--workers N` (default número de CPUs del sistema).
- Opciones de exportación: archivo CSV, archivo JSON o inserción en base de datos relacional PostgreSQL / SQLite.
- Filtros avanzados: `--min-width`, `--min-height`, `--has-gps`.

### Requisitos de CLI
- Argumento posicional: directorio de medios a escanear.
- Opción `-w / --workers <N>`: número de workers concurrentes.
- Opción `--format [csv|json|table]`.
- Opción `-o / --output <RUTA>`.
- Opciones de persistencia: `--db-url` o `--driver sqlite`.
- Exit code 0 en éxito, 1 si no se encontraron archivos multimedia válidos, 2 en errores.

### Entradas
- Directorio de archivos multimedia y parámetros de concurrencia.

### Salidas
- Catálogo estructurado en STDOUT, archivo o base de datos.

### Persistencia
Escritura de catálogo en CSV/JSON o persistencia relacional en PostgreSQL/SQLite.

### Validaciones
- Comprobar que el directorio exista.
- Validar que el número de workers sea un entero positivo mayor a 0.

### Casos límite
- Archivos de imagen corruptos o truncados (capturar error sin abortar el procesamiento de los demás archivos).
- Archivos de video gigantescos de varios gigabytes (solo leer cabeceras de metadatos).
- Archivos sin metadatos EXIF.

### Manejo de errores
- `PermissionError` en archivos inaccesibles.
- Errores de decodificación de cabeceras de imagen.

### Fundamentos de Python relacionados
- Concurrencia con `concurrent.futures.ProcessPoolExecutor` o `ThreadPoolExecutor`.
- Extracción de cabeceras binarias o uso de librerías estándar/Pillow/struct.
- Módulo `multiprocessing` y serialización de tareas.
- Manejo de barras de progreso seguras para multihilo.

### Conceptos CLI relacionados
- Paralelización de tareas de E/S y cómputo en línea de comandos.
- Control de saturación de recursos de CPU y disco.

### Herramientas o módulos para investigar
- `concurrent.futures`.
- `multiprocessing.cpu_count`.
- `struct` y `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para mostrar una barra de progreso concurrente precisa mientras los workers procesan?

### Diseño de argumentos
¿Cómo nombrarías la opción para omitir la extracción de coordenadas GPS por motivos de privacidad (`--strip-gps`)?

### Diseño de variables
`media_file_tasks_queue`, `worker_process_pool`, `extracted_metadata_dto`, `catalog_results_collector`, `failed_files_counter`.

### Antes de programar
1. ¿Por qué usar `ProcessPoolExecutor` para tareas limitadas por CPU (CPU-bound) como decodificación de imágenes y `ThreadPoolExecutor` para tareas de E/S (I/O-bound)?
2. ¿Cómo leer únicamente los primeros bytes de cabecera de un archivo PNG/JPEG con `struct` para obtener el ancho y alto sin descomprimir la imagen completa?

### Arquitectura
Estructura:
```
ejercicio_057/
├── media_meta.py
├── concurrent_scanner.py
├── extractors/
│   ├── image_extractor.py
│   └── video_extractor.py
└── exporters/
    ├── csv_exporter.py
    └── db_exporter.py
```

### Pruebas mínimas
1. Escanear un directorio de prueba con 20 imágenes con `--workers 4` y verificar que el catálogo contenga exactamente los 20 registros con sus dimensiones.
2. Probar `--min-width 1000` y verificar el filtrado.

### Pruebas de error
1. Pasar un directorio que no existe -> Exit code 2 con error descriptivo.

### Experiencia de usuario
Progreso en tiempo real en STDERR (ej. `[=========>   ] 75% (150/200 archivos) - 45 arch/seg`) y resultado final en el formato solicitado.

### Explicación posterior
Explica el impacto del GIL (Global Interpreter Lock) de Python y cuándo es imperativo usar procesos en lugar de hilos para procesamiento paralelo.

### Aplicación profesional
Indexación masiva en plataformas de medios, auditorías de calidad de assets en videojuegos y preparación de datasets de visión por computadora.

### Reto adicional
Calcular el hash perceptual (pHash / dHash) de cada imagen para permitir búsquedas de imágenes visualmente similares.

---
> [← Ejercicio 056](../ejercicio_056/README.md) · [Índice General](../README.md) · [Ejercicio 058 →](../ejercicio_058/README.md)
