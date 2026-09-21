## Ejercicio 051 — Sincronizador Unidireccional con Storage Mock (`s3-sync-sim`)

> [← Ejercicio 050](../ejercicio_050/README.md) · [Índice General](../README.md) · [Ejercicio 052 →](../ejercicio_052/README.md)

### Contexto profesional
En arquitecturas cloud, los scripts de backup y despliegue sincronizan carpetas locales con buckets de almacenamiento de objetos (Amazon S3, Google Cloud Storage, Azure Blob). Para probar la lógica de sincronización (subidas incrementales, borrado de archivos remotos huérfanos, detección de cambios por MD5/ETag) sin incurrir en costos de nube, se utilizan simuladores de almacenamiento de objetos.

### Problema
Construir una CLI que sincronice un directorio local hacia un almacenamiento de objetos simulado (o base de datos relacional de metadatos en PostgreSQL/SQLite), aplicando sincronización incremental (solo transferir archivos nuevos o modificados por hash/timestamp), soportando `--dry-run`, flag `--delete` para remover objetos remotos eliminados en local y generación de reportes de transferencia.

### Usuario objetivo
Ingenieros de DevOps, arquitectos cloud y desarrolladores backend.

### Objetivo
Crear un motor de sincronización incremental unidireccional con cálculo de diferencias, simulación de almacenamiento y persistencia de metadatos.

### Ejemplo conceptual de uso
```bash
# Sincronizar carpeta local hacia un bucket simulado
python s3_sync_sim.py sync ./dist/ s3://mi-bucket-app/

# Simular sincronización con borrado de remotos huérfanos
python s3_sync_sim.py sync ./dist/ s3://mi-bucket-app/ --delete --dry-run

# Listar objetos almacenados en el bucket simulado
python s3_sync_sim.py ls s3://mi-bucket-app/
```

### Requisitos funcionales
- Subcomando `sync <ORIGEN_LOCAL> <DESTINO_BUCKET>`: analiza archivos locales y objetos remotos, calcula diferencias por hash MD5/SHA256 y tamaño, y transfiere únicamente los archivos modificados o nuevos.
- Flag `--delete`: elimina del bucket remoto los objetos que ya no existan en el directorio local de origen.
- Subcomando `ls <BUCKET>`: lista objetos en el bucket con tamaño, fecha de última modificación y ETag.
- Subcomando `mb <BUCKET>`: crea un nuevo bucket simulado.
- Subcomando `rb <BUCKET>`: elimina un bucket vacío.
- Subcomando `stat <OBJETO>`: muestra metadatos detallados de un objeto.
- Flag `--dry-run`: muestra las operaciones de subida, actualización y borrado que se realizarían sin modificar el almacenamiento.

### Requisitos de CLI
- Subcomandos: `sync`, `ls`, `mb`, `rb`, `stat`.
- Opciones de persistencia de metadatos: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Flag `--delete`.
- Flag `--dry-run`.
- Exit code 0 en éxito, 1 si falló la transferencia de algún archivo, 2 en errores.

### Entradas
- Rutas locales y URIs de bucket (`s3://nombre-bucket/prefijo/`).

### Salidas
- Progreso de subida, estadísticas de bytes transferidos y resumen de sincronización en STDOUT.

### Persistencia
Directorio mock en disco para los objetos binarios y PostgreSQL/SQLite para el catálogo de metadatos (`buckets`, `objects`, `sync_logs`).

### Validaciones
- Validar sintaxis de URI de bucket (`s3://<bucket-name>/...`).
- El directorio de origen local debe existir.

### Casos límite
- Sincronización de carpetas vacías.
- Archivos locales con nombres que contienen caracteres especiales o espacios.
- Archivos locales modificados que tienen exactamente el mismo tamaño pero distinto contenido (detección obligatoria por hash).

### Manejo de errores
- Errores de lectura de archivos locales.
- Bucket no encontrado.

### Fundamentos de Python relacionados
- Módulo `hashlib` para cálculo de sumas MD5 (ETags).
- `pathlib.Path` para recorrido recursivo del sistema de archivos.
- Persistencia de metadatos con PostgreSQL o SQLite.
- Subparsers de `argparse`.

### Conceptos CLI relacionados
- Implementación del algoritmo de reconciliación de dos vías para sincronización incremental.
- Operaciones seguras con simulación `--dry-run`.

### Herramientas o módulos para investigar
- `hashlib`.
- `pathlib` y `shutil`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo permitirías excluir ciertos archivos o patrones de la sincronización (`--exclude "*.tmp" --include "*.png"`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para limitar el ancho de banda o concurrencia de transferencia simulada (`--concurrency 4`)?

### Diseño de variables
`local_files_inventory_map`, `remote_objects_inventory_map`, `files_to_upload_list`, `objects_to_delete_list`, `transferred_bytes_total`.

### Antes de programar
1. ¿Cómo construir la clave relativa de objeto (object key) en S3 a partir de la ruta del archivo relativo al directorio base local?
2. ¿Por qué comparar tamaño y ETag/MD5 es más confiable que comparar marcas de tiempo (`mtime`) en transferencias cloud?

### Arquitectura
Motor de reconciliación (`sync_engine.py`), adaptador de almacenamiento mock (`storage_adapter.py`), repositorio de metadatos (`metadata_repo.py`) y CLI.

### Pruebas mínimas
1. Sincronizar un directorio con 3 archivos hacia un bucket nuevo y verificar que se suban los 3.
2. Ejecutar `sync` nuevamente sin cambios y verificar que reporte `0 archivos transferidos (al día)`.
3. Modificar 1 archivo local, ejecutar `sync` y verificar que solo transfiera ese archivo.

### Pruebas de error
1. Intentar sincronizar hacia un bucket inexistente sin haberlo creado -> Exit code 1.

### Experiencia de usuario
Salida detallada indicando `upload: ./dist/app.js -> s3://mi-bucket/app.js` y resumen final de archivos añadidos, actualizados y eliminados.

### Explicación posterior
Explica la diferencia de arquitectura entre sistemas de archivos jerárquicos POSIX y el modelo plano de claves de los almacenamientos de objetos (Object Storage).

### Aplicación profesional
Despliegue de sitios estáticos a AWS S3 / CloudFront, pipelines de backup automatizados y distribución de artefactos.

### Reto adicional
Implementar soporte para compresión Gzip automática en la subida y configuración de cabeceras de metadatos HTTP (`Content-Type`, `Cache-Control`).

---
> [← Ejercicio 050](../ejercicio_050/README.md) · [Índice General](../README.md) · [Ejercicio 052 →](../ejercicio_052/README.md)
