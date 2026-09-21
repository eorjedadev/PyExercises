## Ejercicio 031 — Auditor y Limpiador de Ramas Git Obsoletas (`git-prune-helper`)

> [← Ejercicio 030](../ejercicio_030/README.md) · [Índice General](../README.md) · [Ejercicio 032 →](../ejercicio_032/README.md)

### Contexto profesional
En equipos de desarrollo que utilizan metodologías de ramas por característica (feature branches), los desarrolladores acumulan decenas de ramas locales que ya fueron mergeadas en `main` o eliminadas del repositorio remoto, saturando el entorno local.

### Problema
Construir una CLI que interactúe con el repositorio Git local mediante subprocesos, identifique ramas locales ya fusionadas (merged), ramas cuyo tracking remoto ha desaparecido (stale/gone), y ofrezca eliminarlas de forma segura con protección para ramas principales (`main`, `master`, `develop`, `release/*`).

### Usuario objetivo
Desarrolladores de software y DevOps.

### Objetivo
Desarrollar una herramienta de automatización sobre Git con invocación segura de subprocesos, análisis de estado y borrado controlado.

### Ejemplo conceptual de uso
```bash
# Listar ramas locales obsoletas ya fusionadas
python git_prune_helper.py list --merged-into main

# Simular eliminación de ramas obsoletas
python git_prune_helper.py clean --dry-run

# Eliminar ramas obsoletas con confirmación o forzado
python git_prune_helper.py clean --force
```

### Requisitos funcionales
- Verificar que el directorio actual sea un repositorio Git válido.
- Subcomando `list`: lista ramas locales indicando: nombre, último commit, fecha, si está mergeada en la rama base y si su remoto existe.
- Subcomando `clean`: elimina ramas locales que ya fueron integradas o cuyo remoto fue eliminado (`[gone]`).
- Proteger estrictamente ramas críticas (nunca permitir borrar `main`, `master`, `develop`, `staging` ni la rama actual activa).
- Soportar `--dry-run` para previsualizar las ramas que se eliminarían.
- Flag `--force` para saltarse la confirmación interactiva `[y/N]`.

### Requisitos de CLI
- Subcomandos: `list`, `clean`.
- Opción `--base <RAMA>`: rama principal de comparación (default detecta `main` o `master`).
- Flag `--dry-run`.
- Flag `-f / --force`.
- Exit code 0 en éxito, 1 si no se está en un repo git o no hay ramas que limpiar, 2 en errores.

### Entradas
- Repositorio Git local y opciones de comando.

### Salidas
- Listado de ramas y resumen de ramas eliminadas en STDOUT.

### Persistencia
Modificación del estado del repositorio Git local mediante comandos `git branch -d`.

### Validaciones
- Comprobar la presencia del binario `git` en el PATH del sistema.
- Validar que la rama base especificada exista en el repositorio.

### Casos límite
- Repositorios con cientos de ramas.
- Repositorio recién inicializado sin commits.
- Ramas con nombres que contienen caracteres especiales o barras (ej. `feature/PROJ-123/login-fix`).

### Manejo de errores
- `subprocess.CalledProcessError` al invocar Git.
- Manejo de ramas no fusionadas completamente (usar borrado seguro `-d` en lugar de forzado `-D` a menos que se indique).

### Fundamentos de Python relacionados
- Módulo estándar `subprocess` (`subprocess.run`, `capture_output=True`, `text=True`, `check=True`).
- Expresiones regulares para parsear la salida de comandos Git (`git branch -vv`).
- Manejo de listas y filtros.

### Conceptos CLI relacionados
- Orquestación e integración con herramientas externas del sistema operativo.
- Mecanismos de seguridad contra borrado accidental de código.

### Herramientas o módulos para investigar
- `subprocess`.
- `shutil.which`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías una opción para hacer `git fetch --prune` automáticamente antes de auditar las ramas?

### Diseño de argumentos
¿Cómo permitirías especificar una lista blanca de ramas protegidas adicionales (`--protect "staging,release/*"`)?

### Diseño de variables
`current_git_branch`, `merged_branches_list`, `stale_branches_list`, `protected_branches_set`, `git_command_output`.

### Antes de programar
1. ¿Por qué es fundamental usar `git branch -d` (minúscula) para que Git rechace el borrado si la rama tiene cambios no integrados?
2. ¿Cómo parsear la salida de `git branch -vv` para detectar el indicador `[gone]` que señala que la rama remota fue borrada?

### Arquitectura
Wrapper de Git (`git_client.py`), evaluador de ramas (`branch_evaluator.py`) y CLI (`git_prune_helper.py`).

### Pruebas mínimas
1. Crear un repo git temporal, crear una rama secundaria, mergearla en main y verificar que la herramienta la identifique como candidata para borrado.
2. Probar con `--dry-run` y verificar que la rama no se borre.

### Pruebas de error
1. Ejecutar fuera de un repositorio Git -> Exit code 1 con mensaje de error claro.

### Experiencia de usuario
Mostrar una lista clara de las ramas detectadas y el motivo de su eliminación (`[MERGED]` o `[REMOTO BORRADO]`), solicitando confirmación explícita antes de ejecutar cualquier acción.

### Explicación posterior
Explica la diferencia entre ramas locales, referencias remotas (`origin/branch`) y el comando `git remote prune origin`.

### Aplicación profesional
Mantenimiento diario de estaciones de trabajo de desarrolladores y scripts de saneamiento en servidores de CI.

### Reto adicional
Calcular y mostrar la fecha del último commit de cada rama para identificar ramas inactivas con más de 90 días de antigüedad.

---
> [← Ejercicio 030](../ejercicio_030/README.md) · [Índice General](../README.md) · [Ejercicio 032 →](../ejercicio_032/README.md)
