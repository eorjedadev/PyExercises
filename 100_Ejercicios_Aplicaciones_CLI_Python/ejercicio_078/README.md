## Ejercicio 078 — Recolector de Basura y Limpiador de Artefactos CI/CD (`ci-cleaner`)

> [← Ejercicio 077](../ejercicio_077/README.md) · [Índice General](../README.md) · [Ejercicio 079 →](../ejercicio_079/README.md)

### Contexto profesional
Los servidores de integración continua y repositorios de artefactos (GitHub Actions caches, Nexus, Artifactory, Docker registries, carpetas locales de build `/tmp/ci`) acumulan terabytes de imágenes antiguas, ruedas de dependencias y reportes temporales que saturan el almacenamiento si no se depuran mediante políticas de retención inteligentes.

### Problema
Construir una CLI que actúe como recolector de basura (Garbage Collector) para artefactos de compilación y pruebas, evaluando reglas de retención basadas en antigüedad, espacio consumido, número máximo de versiones por rama y estado de aprobación en base de datos relacional (PostgreSQL o SQLite opcional), con soporte de simulación segura (`--dry-run`).

### Usuario objetivo
Ingenieros de DevOps, administradores de CI/CD y SREs.

### Objetivo
Desarrollar un recolector de basura automatizado de artefactos con evaluación de políticas complejas, soporte `--dry-run` y auditoría relacional.

### Ejemplo conceptual de uso
```bash
# Simular limpieza de artefactos en el directorio de builds
python ci_cleaner.py clean /var/ci/artifacts --policy retention_policy.json --dry-run

# Ejecutar limpieza real liberando al menos 50 GB de espacio y registrando en PostgreSQL
python ci_cleaner.py clean /var/ci/artifacts --policy retention_policy.json --target-free 50G --force
```

### Requisitos funcionales
- Analizar el directorio de artefactos o consultar el inventario de artefactos en PostgreSQL / SQLite.
- Reglas de retención configurables en `retention_policy.json`:
  - `keep_latest_per_branch`: conservar siempre las últimas N compilaciones por rama de Git (ej. 3 builds de feature branches, 10 de main).
  - `max_age_days`: eliminar artefactos con más de N días sin acceso o modificación.
  - `protect_tagged_releases`: nunca eliminar artefactos asociados a tags de release de producción.
  - `disk_threshold_percent`: disparar limpieza agresiva si el disco supera el 85% de uso.
- Subcomando `clean`: evalúa las reglas, identifica los artefactos huérfanos/caducados y los elimina físicamente del disco y de la base de datos.
- Subcomando `analyze`: genera un reporte del espacio consumido por rama, proyecto y antigüedad.
- Flag `--dry-run`: muestra exactamente qué archivos se eliminarían y cuántos gigabytes se liberarían sin borrar nada.

### Requisitos de CLI
- Subcomandos: `clean`, `analyze`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Opción `--policy <RUTA>` (default `retention_policy.json`).
- Opción `--target-free <SIZE>` (ej. `20G`, `500M`).
- Flag `--dry-run`.
- Flag `-f / --force`.
- Exit code 0 en éxito, 1 si no se pudo alcanzar el objetivo de espacio libre, 2 en errores.

### Entradas
- Directorio de artefactos, archivo de políticas y credenciales de base de datos.

### Salidas
- Reporte de análisis de almacenamiento y resumen de espacio liberado en STDOUT.

### Persistencia
Eliminación de archivos en disco y actualización del catálogo en PostgreSQL / SQLite.

### Validaciones
- Prohibir la ejecución si la política intenta eliminar artefactos marcados como protegidos (`PROTECTED_RELEASE`).
- Exigir confirmación interactiva `[y/N]` en operaciones destructivas a menos que se use `--force`.

### Casos límite
- Artefactos bloqueados o en uso por compilaciones activas en ese instante.
- Directorios con millones de archivos pequeños.
- Simulación `--dry-run` sobre discos completamente llenos (0 bytes libres).

### Manejo de errores
- `PermissionError` al intentar borrar archivos protegidos.
- Errores de acceso a base de datos.

### Fundamentos de Python relacionados
- Módulos `pathlib` y `shutil` (`shutil.rmtree`, `os.stat`).
- Módulo `datetime` para cálculo de antigüedad de archivos.
- Persistencia y transacciones en PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Diseño de motores de recolección de basura (Garbage Collection) para sistemas de almacenamiento.
- Manejo de umbrales de seguridad y simulación de impacto.

### Herramientas o módulos para investigar
- `pathlib` y `shutil`.
- `datetime`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `archive <DESTINO>` para mover los artefactos antiguos a almacenamiento en frío (Glacier / S3) en lugar de eliminarlos definitivamente?

### Diseño de argumentos
¿Cómo nombrarías la opción para ordenar los candidatos a borrado por antigüedad o por tamaño (`--eviction-policy lru|lfu|largest-first`)?

### Diseño de variables
`artifacts_inventory_list`, `retention_policy_config`, `candidates_for_deletion_list`, `freed_storage_bytes_total`, `disk_usage_stats`.

### Antes de programar
1. ¿Cómo calcular el tamaño acumulado total de un subdirectorio recursivo antes de eliminarlo para reportar exactamente cuántos megabytes se liberarán?
2. ¿Cómo asegurar que los artefactos asociados a la rama `main` o a tags de versión tengan una regla de retención mucho más longeva que los de ramas temporales?

### Arquitectura
Analizador de inventario (`artifact_scanner.py`), evaluador de políticas (`eviction_engine.py`), ejecutor de limpieza (`remover.py`) y CLI.

### Pruebas mínimas
1. Crear una estructura de 5 carpetas de build simuladas (3 antiguas y 2 recientes), ejecutar `clean --dry-run` con política de 30 días y verificar que identifique las 3 carpetas antiguas sin borrarlas.
2. Ejecutar con `--force` y verificar que solo queden las 2 carpetas recientes y el espacio se reporte con precisión.

### Pruebas de error
1. Intentar limpiar un directorio inexistente -> Exit code 2 con error claro.

### Experiencia de usuario
Reporte claro con gráficos de uso antes y después: `Espacio antes: 88.5 GB usado -> Espacio después: 32.1 GB usado (56.4 GB liberados)`.

### Explicación posterior
Explica las estrategias de desalojo de caché (Cache Eviction Policies) más comunes: LRU (Least Recently Used), LFU (Least Frequently Used) y FIFO.

### Aplicación profesional
Mantenimiento automatizado de agentes de compilación de CI/CD (Jenkins, GitLab Runners, GitHub self-hosted runners) y servidores de paquetes.

### Reto adicional
Implementar compresión automática de artefactos que están en periodo de gracia antes de su eliminación definitiva.

---
> [← Ejercicio 077](../ejercicio_077/README.md) · [Índice General](../README.md) · [Ejercicio 079 →](../ejercicio_079/README.md)
