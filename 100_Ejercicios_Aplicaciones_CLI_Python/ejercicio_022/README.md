## Ejercicio 022 — Divisor y Reensamblador de Archivos en Chunks (`chunk-split`)

> [← Ejercicio 021](../ejercicio_021/README.md) · [Índice General](../README.md) · [Ejercicio 023 →](../ejercicio_023/README.md)

### Contexto profesional
Al transferir archivos gigantescos (imágenes de disco de 50 GB, volcados de base de datos) a través de medios con límites de tamaño por archivo (sistemas FAT32, cuotas de subida en S3, adjuntos o límites de red), es necesario dividir los archivos en fragmentos de tamaño fijo y reensamblarlos posteriormente verificando su integridad absoluta.

### Problema
Construir una CLI con dos subcomandos: `split` (divide un archivo en partes numeradas de N megabytes y genera un manifiesto de integridad con hashes SHA256) y `merge` (reconstruye el archivo original a partir de los chunks y valida el hash contra el manifiesto).

### Usuario objetivo
Administradores de sistemas, ingenieros de datos y especialistas en DevOps.

### Objetivo
Desarrollar una herramienta de particionado y reensamblado de archivos binarios con verificación criptográfica y streaming por bloques.

### Ejemplo conceptual de uso
```bash
# Dividir un archivo en partes de 100 MB
python chunk_split.py split backup.tar.gz --size 100M --out-dir ./chunks

# Reensamblar las partes y verificar integridad
python chunk_split.py merge ./chunks/backup.tar.gz.manifest.json -o ./restored_backup.tar.gz
```

### Requisitos funcionales
- Subcomando `split`: lee archivo origen en bloques y escribe partes con nombres secuenciales (ej. `archivo.part.001`, `archivo.part.002`).
- Generar un archivo manifiesto JSON (`.manifest.json`) que contenga: nombre original, tamaño total, algoritmo de hash, hash SHA256 del archivo completo y lista de hashes individuales de cada chunk.
- Subcomando `merge`: lee el manifiesto, verifica que todas las partes existan, las une secuencialmente en el archivo de destino y comprueba que el hash del archivo final coincida exactamente con el manifiesto.
- Soportar unidades de tamaño: `K` (Kilobytes), `M` (Megabytes), `G` (Gigabytes).

### Requisitos de CLI
- Subcomandos: `split` y `merge`.
- En `split`: archivo de entrada, opción `-s / --size` (default `10M`), opción `--out-dir`.
- En `merge`: manifiesto JSON, opción `-o / --output`.
- Exit code 0 en éxito, 1 en fallo de verificación de integridad (hash mismatch), 2 en errores de archivo.

### Entradas
- Archivo a dividir o manifiesto a reensamblar.

### Salidas
- Chunks y manifiesto en disco, o archivo restaurado.
- Reporte de progreso en terminal.

### Persistencia
Creación y lectura de múltiples archivos en el sistema de archivos.

### Validaciones
- Validar que el tamaño de chunk sea menor al tamaño total del archivo en `split`.
- Validar que no falte ningún chunk intermedio al hacer `merge`.

### Casos límite
- Archivo cuyo tamaño es múltiplo exacto del tamaño de chunk.
- Interrupción a mitad del proceso (limpiar archivos temporales parciales si falla).
- Nombres de archivos con caracteres especiales.

### Manejo de errores
- `FileNotFoundError` si falta una parte.
- Error de integridad si un chunk fue alterado o corrompido.

### Fundamentos de Python relacionados
- Manejo de archivos binarios (`'rb'`, `'wb'`).
- Módulo `hashlib` para cálculo acumulativo y por chunk.
- Módulo `json` para el archivo de manifiesto.
- Subparsers en `argparse`.

### Conceptos CLI relacionados
- Diseño de arquitecturas split/merge simétricas.
- Verificación criptográfica obligatoria post-operación.

### Herramientas o módulos para investigar
- `hashlib`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías una opción para borrar automáticamente los chunks después de un merge exitoso (`--delete-chunks`)?

### Diseño de argumentos
¿Cómo permitirías especificar el prefijo de numeración de partes (ej. `.part001` vs `.001.bin`)?

### Diseño de variables
`source_file_path`, `chunk_size_bytes`, `total_parts_count`, `manifest_data`, `restored_hasher`.

### Antes de programar
1. ¿Cómo procesar la división sin cargar un chunk completo de 1 GB en memoria RAM a la vez?
2. ¿Cómo estructurar el JSON del manifiesto para garantizar compatibilidad entre sistemas operativos?

### Arquitectura
Módulo de particionado (`splitter.py`), módulo de reensamblado (`merger.py`) y CLI.

### Pruebas mínimas
1. Dividir un archivo de 25 MB en chunks de 10 MB (debe generar 3 partes: 10MB, 10MB y 5MB).
2. Reensamblar y verificar que el hash del archivo restaurado sea idéntico al original.

### Pruebas de error
1. Alterar 1 byte en uno de los chunks y ejecutar `merge` -> Debe abortar con error de hash mismatch y exit code 1.

### Experiencia de usuario
Mostrar el progreso de escritura de cada parte y un mensaje final de confirmación de integridad.

### Explicación posterior
Explica la importancia de los manifiestos criptográficos en sistemas de almacenamiento distribuido como BitTorrent o HDFS.

### Aplicación profesional
Gestión de backups en almacenamiento en frío, transferencia de datasets masivos y superación de límites de tamaño en repositorios.

### Reto adicional
Añadir compresión opcional GZIP por chunk (`--compress`) para reducir el espacio de almacenamiento de las partes.

---
> [← Ejercicio 021](../ejercicio_021/README.md) · [Índice General](../README.md) · [Ejercicio 023 →](../ejercicio_023/README.md)
