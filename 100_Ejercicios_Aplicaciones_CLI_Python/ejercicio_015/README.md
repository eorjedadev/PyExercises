## Ejercicio 015 — Detector de Archivos Duplicados por Hash (`dedup-scan`)

> [← Ejercicio 014](../ejercicio_014/README.md) · [Índice General](../README.md) · [Ejercicio 016 →](../ejercicio_016/README.md)

### Contexto profesional
En servidores de archivos, repositorios de assets y respaldos locales, se acumulan gigabytes de archivos duplicados con nombres diferentes en carpetas distintas, desperdiciando espacio y complicando la gestión de backups.

### Problema
Construir una CLI que analice un árbol de directorios, identifique archivos duplicados comparando primero su tamaño en bytes y luego su hash SHA256 (para no calcular hashes innecesarios), reporte los duplicados agrupados y opcionalmente permita eliminarlos o moverlos de forma segura.

### Usuario objetivo
Administradores de sistemas, DevOps y usuarios avanzados.

### Objetivo
Implementar un escáner de duplicados de alto rendimiento con filtrado en dos fases (tamaño -> hash), soporte de `--dry-run` y reportes detallados.

### Ejemplo conceptual de uso
```bash
# Escanear directorio buscando duplicados
python dedup_scan.py /var/data

# Filtrar archivos de al menos 1 MB y generar reporte JSON
python dedup_scan.py /var/data --min-size 1M --json

# Simular eliminación de duplicados manteniendo el archivo más antiguo
python dedup_scan.py /var/data --delete --keep oldest --dry-run
```

### Requisitos funcionales
- Recorrer el directorio recursivamente recopilando tamaño de archivos.
- Fase 1: Agrupar por tamaño. Si un tamaño es único, descartar inmediatamente (no se calcula hash).
- Fase 2: Para archivos con tamaño idéntico, calcular hash SHA256 por bloques.
- Agrupar archivos con hash idéntico y calcular espacio total desperdiciado.
- Opciones de acción: solo listar, o borrar duplicados (`--delete`) preservando el más antiguo (`--keep oldest`) o más reciente (`--keep newest`).
- Flag obligatorio de seguridad `--dry-run` para simular acciones destructivas.

### Requisitos de CLI
- Argumento posicional: directorio a escanear.
- Opción `--min-size <SIZE>` (ej. `10k`, `1M`, `500M`).
- Opción `--keep [oldest|newest|first]`.
- Flag `--delete`.
- Flag `--dry-run`.
- Flag `--json`.
- Exit code 0 en éxito (incluso si hay duplicados), 1 si falló el borrado, 2 en argumentos inválidos.

### Entradas
- Ruta de directorio.
- Políticas de tamaño y conservación.

### Salidas
- Reporte en terminal con grupos de duplicados, rutas y espacio recuperable.
- Detalle de acciones realizadas o simuladas.

### Persistencia
Modificación del sistema de archivos únicamente cuando se invoca `--delete` sin `--dry-run`.

### Validaciones
- Si se usa `--delete`, exigir confirmación interactiva a menos que se use `--force`.
- Validar que la opción `--min-size` tenga un formato válido.

### Casos límite
- Archivos con 0 bytes (muchos archivos vacíos pueden tener hash idéntico; permitir ignorarlos con `--ignore-empty`).
- Enlaces duros (hard links): dos entradas apuntando al mismo inodo no deben contarse como duplicados que ocupan doble espacio.
- Archivos bloqueados o sin permisos de lectura.

### Manejo de errores
- `PermissionError` al leer archivos o intentar eliminarlos.
- `FileNotFoundError` si un archivo fue eliminado concurrentemente.

### Fundamentos de Python relacionados
- `pathlib.Path` y `os.stat` (inodos con `st_ino`, timestamps con `st_mtime`).
- Módulo `hashlib`.
- Diccionarios con estructuras `dict[int, list[Path]]` y `dict[str, list[Path]]`.

### Conceptos CLI relacionados
- Patrón de dos fases para optimización de I/O.
- Implementación rigurosa del patrón `--dry-run` para operaciones destructivas.

### Herramientas o módulos para investigar
- `pathlib` y `os`.
- `hashlib`.
- `argparse`.

### Diseño de comandos
¿Cómo permitirías exportar un script bash con los comandos `rm` para que el usuario revise manualmente antes de ejecutar?

### Diseño de argumentos
¿Cómo diseñarías el flag `--exclude-ext ".log,.tmp"`?

### Diseño de variables
`size_buckets`, `hash_buckets`, `duplicate_groups`, `wasted_bytes`, `original_file`, `redundant_files`.

### Antes de programar
1. ¿Por qué comparar tamaños primero reduce en más del 90% la necesidad de calcular hashes en discos con millones de archivos?
2. ¿Cómo asegurar que `--dry-run` nunca toque el disco pero imprima exactamente lo que haría?

### Arquitectura
Estructura en fases: `collector.py` -> `hasher.py` -> `reporter.py` -> `remediator.py`.

### Pruebas mínimas
1. Crear 3 archivos idénticos con nombres distintos y verificar que se agrupen en un solo grupo de duplicados.
2. Ejecutar con `--dry-run --delete` y verificar que los archivos continúen existiendo.

### Pruebas de error
1. Intentar borrar sin `--dry-run` y rechazar la confirmación interactiva -> Comprobar que no se borre nada.

### Experiencia de usuario
Mostrar una barra de progreso durante la fase de hashing si se procesan muchos archivos y un resumen claro del total de MB liberables.

### Explicación posterior
Explica la diferencia entre inodos, enlaces duros (hard links) y enlaces simbólicos (symlinks) en la detección de duplicados.

### Aplicación profesional
Limpieza de almacenamiento en servidores de producción, deduplicación de backups y optimización de repositorios de assets.

### Reto adicional
Implementar la opción de reemplazar los duplicados por enlaces duros (`--hardlink`) para ahorrar espacio sin alterar las rutas existentes.

---
> [← Ejercicio 014](../ejercicio_014/README.md) · [Índice General](../README.md) · [Ejercicio 016 →](../ejercicio_016/README.md)
