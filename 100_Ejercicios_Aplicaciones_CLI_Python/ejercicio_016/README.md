## Ejercicio 016 — Limpiador Seguro de Archivos Temporales (`clean-tmp`)

> [← Ejercicio 015](../ejercicio_015/README.md) · [Índice General](../README.md) · [Ejercicio 017 →](../ejercicio_017/README.md)

### Contexto profesional
Los servidores de compilación, proxies y sistemas de procesamiento de medios acumulan constantemente archivos temporales (`.tmp`, `.cache`, `.log`, `.pid`) que llenan los discos si no se depuran periódicamente según políticas de antigüedad.

### Problema
Construir una CLI que limpie directorios de archivos temporales según reglas de antigüedad (ej. archivos con más de 7 días sin modificarse), patrones de extensión o tamaño, ofreciendo modo interactivo de confirmación, modo desatendido para cron (`--force`) y simulación (`--dry-run`).

### Usuario objetivo
Administradores de sistemas y DevOps.

### Objetivo
Crear una herramienta de saneamiento de almacenamiento segura, parametrizable y automatizable.

### Ejemplo conceptual de uso
```bash
# Simular limpieza de archivos temporales con más de 14 días
python clean_tmp.py /tmp/builds --days 14 --dry-run

# Ejecutar limpieza real forzando sin preguntar (para cron)
python clean_tmp.py /var/cache/app --days 30 --extensions ".tmp,.bak,.log" --force
```

### Requisitos funcionales
- Escanear el directorio indicado en busca de archivos que cumplan los criterios.
- Filtrar por antigüedad en días (`--days N`) o en horas (`--hours N`) según la fecha de última modificación (`mtime`) o acceso (`atime`).
- Filtrar por extensiones permitidas para borrado (ej. `--extensions ".tmp,.old"`).
- Contar total de archivos eliminados y espacio total liberado en bytes/MB.
- Soportar `--dry-run` para listar lo que se borraría sin ejecutar.
- Solicitar confirmación `[y/N]` antes de borrar a menos que se use `--force`.

### Requisitos de CLI
- Argumento posicional: directorio a limpiar.
- Opción `--days <N>` o `--hours <N>`.
- Opción `--extensions <EXTS>`.
- Flag `--dry-run`.
- Flag `-f / --force`.
- Flag `--recursive / -r`.
- Exit code 0 en éxito, 1 si el usuario cancela la confirmación, 2 en errores.

### Entradas
- Ruta de directorio.
- Parámetros de antigüedad y tipos de archivo.

### Salidas
- Resumen de archivos procesados y espacio liberado en STDOUT.

### Persistencia
Eliminación en el sistema de archivos.

### Validaciones
- No permitir ejecutar sobre directorios del sistema raíz (`/`, `/bin`, `C:\Windows`) como medida de seguridad activa.
- Validar que `--days` o `--hours` sean números positivos.

### Casos límite
- Directorios protegidos contra escritura.
- Archivos en uso o bloqueados por otros procesos.
- Directorios vacíos que quedan tras borrar archivos (opción `--remove-empty-dirs`).

### Manejo de errores
- `PermissionError` al intentar borrar archivos protegidos.
- Interrupción por `Ctrl+C` (manejo limpio).

### Fundamentos de Python relacionados
- `pathlib.Path` (`Path.unlink()`, `Path.rmdir()`).
- `time` y `datetime` (`time.time()`, `datetime.fromtimestamp()`).
- `sys.exit` y función `input()` para confirmaciones.

### Conceptos CLI relacionados
- Seguridad en herramientas destructivas: confirmaciones vs flags de automatización (`--force`).
- Lista de exclusión de rutas protegidas del sistema operativo.

### Herramientas o módulos para investigar
- `pathlib`.
- `datetime`.
- `argparse`.

### Diseño de comandos
¿Cómo agregarías una opción para mover los archivos a una papelera de reciclaje o carpeta de cuarentena en vez de eliminarlos definitivamente (`--quarantine /tmp/quarantine`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para filtrar por tamaño mínimo antes de borrar (ej. `--min-size 100M`)?

### Diseño de variables
`target_directory`, `max_age_seconds`, `allowed_extensions`, `candidate_files`, `freed_bytes`, `is_dry_run`.

### Antes de programar
1. ¿Cómo prevenir que un usuario ejecute accidentalmente `clean_tmp.py /` o `clean_tmp.py C:\`?
2. ¿Cuál es la diferencia entre `st_mtime` (modificación) y `st_atime` (acceso)?

### Arquitectura
Módulo de escaneo y filtro (`scanner.py`), módulo de seguridad (`safety_guard.py`) y CLI (`clean_tmp.py`).

### Pruebas mínimas
1. Crear archivos temporales de prueba, simular con `--dry-run` y verificar que no se borren.
2. Ejecutar con `--force` y verificar que los archivos caducados se eliminen y el espacio se reporte con precisión.

### Pruebas de error
1. Intentar ejecutar sobre `/` o `C:\` -> Debe bloquearse inmediatamente con error crítico y exit code 2.

### Experiencia de usuario
Mensajes claros que indiquen exactamente cuántos archivos y cuántos megabytes se van a eliminar.

### Explicación posterior
Explica la diferencia entre un borrado suave (quarantine) y un borrado definitivo (`unlink()`).

### Aplicación profesional
Automatización mediante cron / systemd timers en servidores de producción para control de disco.

### Reto adicional
Añadir soporte para eliminar carpetas vacías residuales que queden después de la limpieza (`--clean-empty-dirs`).

---
> [← Ejercicio 015](../ejercicio_015/README.md) · [Índice General](../README.md) · [Ejercicio 017 →](../ejercicio_017/README.md)
