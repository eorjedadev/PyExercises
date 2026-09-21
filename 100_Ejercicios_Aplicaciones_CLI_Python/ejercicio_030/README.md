## Ejercicio 030 — Navegador y Conmutador Rápido de Workspaces (`ws-jump`)

> [← Ejercicio 029](../ejercicio_029/README.md) · [Índice General](../README.md) · [Ejercicio 031 →](../ejercicio_031/README.md)

### Contexto profesional
Los ingenieros de software trabajan simultáneamente en decenas de proyectos repartidos en rutas profundas del sistema de archivos (ej. `/home/user/work/clients/acme/backend-api`, `/home/user/personal/oss/tool`). Navegar manualmente con `cd` repetitivo reduce la agilidad.

### Problema
Construir una CLI que gestione alias y accesos rápidos a directorios de trabajo (workspaces), permita registrar rutas con alias cortos, liste proyectos por tags, elimine rutas huérfanas (carpetas que fueron borradas del disco) y genere el comando de salto compatible con el shell del usuario (Bash, Zsh, PowerShell).

### Usuario objetivo
Desarrolladores, administradores de sistemas y usuarios intensivos de terminal.

### Objetivo
Crear un gestor de directorios frecuentes con persistencia JSON, validación de existencia en disco y generación de wrappers para shell.

### Ejemplo conceptual de uso
```bash
# Registrar el directorio actual con un alias y tags
python ws_jump.py add api-core --tags "work,backend"

# Listar todos los workspaces registrados
python ws_jump.py list

# Obtener la ruta para que el shell ejecute cd
python ws_jump.py path api-core

# Limpiar registros huérfanos cuyas carpetas ya no existan en disco
python ws_jump.py prune
```

### Requisitos funcionales
- Subcomando `add <ALIAS> [RUTA]`: registra un directorio (por defecto el directorio actual de trabajo `Path.cwd()`) con un alias único y tags opcionales.
- Subcomando `path <ALIAS>`: emite únicamente la ruta absoluta en STDOUT para permitir su uso con alias de shell (ej. `jump() { cd "$(python ws_jump.py path $1)"; }`).
- Subcomando `list`: tabla formateada con alias, ruta absoluta, tags y estado de existencia en disco.
- Subcomando `remove <ALIAS>`: elimina el registro del alias.
- Subcomando `prune`: busca todas las rutas registradas y elimina automáticamente los alias cuyos directorios ya no existan en el sistema.
- Subcomando `init [bash|zsh|powershell]`: imprime el script de función wrapper para integrar en el `.bashrc` o `profile.ps1`.

### Requisitos de CLI
- Subcomandos: `add`, `path`, `list`, `remove`, `prune`, `init`.
- Opciones según subcomando.
- Exit code 0 en éxito, 1 si el alias no existe, 2 en errores.

### Entradas
- Nombres de alias, rutas y etiquetas.

### Salidas
- Rutas puras en STDOUT para `path`, tablas en `list`, código shell en `init`.

### Persistencia
Archivo JSON en el directorio de usuario (`~/.ws_jump.json`).

### Validaciones
- El alias no debe contener espacios ni caracteres reservados.
- La ruta a registrar debe ser un directorio existente al momento de añadir.

### Casos límite
- Rutas con espacios en blanco o caracteres Unicode.
- Intentar registrar un alias ya existente (requerir confirmación o `--force`).
- Directorios que fueron renombrados o eliminados externamente.

### Manejo de errores
- `FileNotFoundError`.
- Alias no encontrado en el catálogo.

### Fundamentos de Python relacionados
- `pathlib.Path` (`Path.resolve()`, `Path.exists()`, `Path.is_dir()`, `Path.home()`).
- Persistencia atómica en JSON.
- Módulo `argparse`.

### Conceptos CLI relacionados
- Integración entre herramientas Python y el entorno del shell (un script Python no puede cambiar el directorio de la terminal padre directamente; debe emitir la ruta para que la función wrapper ejecute `cd`).

### Herramientas o módulos para investigar
- `pathlib.Path`.
- `json`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `init` para que el usuario solo tenga que añadir `eval "$(python ws_jump.py init bash)"` a su configuración?

### Diseño de argumentos
¿Cómo agregarías un flag para registrar la última fecha en que se accedió al workspace para ordenar por uso reciente (`--recent`)?

### Diseño de variables
`alias_name`, `workspace_resolved_path`, `workspaces_registry_dict`, `shell_type`, `stale_aliases_list`.

### Antes de programar
1. ¿Por qué un programa de Python ejecutado en un proceso hijo no puede hacer `os.chdir()` y afectar la terminal interactiva del usuario?
2. ¿Cómo estructurar la función shell generada en `init` para que capture la salida de `ws-jump path`?

### Arquitectura
Módulo de gestión de workspaces (`workspace_manager.py`), generador de scripts shell (`shell_integrations.py`) y CLI.

### Pruebas mínimas
1. Registrar una carpeta temporal con alias `test-dir`.
2. Ejecutar `python ws_jump.py path test-dir` y comprobar que devuelva la ruta exacta.
3. Borrar la carpeta física, ejecutar `prune` y verificar que el alias sea eliminado.

### Pruebas de error
1. Solicitar `path` de un alias que no existe -> Exit code 1 e imprimir error en STDERR.

### Experiencia de usuario
Salida limpia en STDOUT para no romper las funciones del shell, y tablas informativas detalladas en modo interactivo.

### Explicación posterior
Explica el modelo de procesos de los sistemas operativos y la herencia de variables de entorno / directorio de trabajo entre procesos padre e hijo.

### Aplicación profesional
Herramientas de productividad de desarrollador inspiradas en utilidades como `z`, `autojump` o `fasd`.

### Reto adicional
Implementar autocompletado dinámico de alias para Bash/Zsh exportando la función de completion correspondiente.

---
> [← Ejercicio 029](../ejercicio_029/README.md) · [Índice General](../README.md) · [Ejercicio 031 →](../ejercicio_031/README.md)
