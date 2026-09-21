## Ejercicio 027 — Bóveda de Snippets de Código (`snip-vault`)

> [← Ejercicio 026](../ejercicio_026/README.md) · [Índice General](../README.md) · [Ejercicio 028 →](../ejercicio_028/README.md)

### Contexto profesional
Los ingenieros de software y administradores de sistemas manejan comandos complejos de `kubectl`, pipelines de `awk`, queries SQL analíticas o configuraciones de Docker que necesitan guardar, buscar por lenguaje y copiar al portapapeles rápidamente.

### Problema
Construir una CLI para almacenar y gestionar fragmentos de código (snippets) multilínea, categorizados por lenguaje y etiquetas, con soporte para importar desde archivo, recibir código por STDIN y copiar el snippet seleccionado al portapapeles del sistema.

### Usuario objetivo
Desarrolladores de software, DevOps y sysadmins.

### Objetivo
Crear un gestor de fragmentos de código con almacenamiento estructurado, soporte multilínea, resaltado de sintaxis básico y exportación.

### Ejemplo conceptual de uso
```bash
# Guardar un snippet desde un archivo
python snip_vault.py save "docker-clean" --lang bash --file ./scripts/clean.sh --tags "docker,ops"

# Guardar un snippet pasando el código directamente o por pipe
cat query.sql | python snip_vault.py save "active-users" --lang sql --tags "db,report"

# Ver el contenido de un snippet
python snip_vault.py get "docker-clean"
```

### Requisitos funcionales
- Subcomando `save <NOMBRE>`: guarda snippet con lenguaje, descripción, tags y cuerpo de código (leído de argumento, archivo o STDIN).
- Subcomando `get <NOMBRE>`: muestra el código del snippet en texto plano limpio.
- Subcomando `list`: lista snippets con nombre, lenguaje, tags y fecha de actualización.
- Subcomando `find <QUERY>`: busca por término en nombre, descripción o contenido del código.
- Subcomando `delete <NOMBRE>`: elimina un snippet previa confirmación.
- Subcomando `run <NOMBRE>` (opcional/modo seguro): muestra el comando y solicita confirmación antes de ejecutarlo en el shell.

### Requisitos de CLI
- Subcomandos: `save`, `get`, `list`, `find`, `delete`.
- Opción `--lang <LENGUAJE>`.
- Opción `--tags <TAGS>`.
- Opción `-f / --file <RUTA>`.
- Exit code 0 en éxito, 1 si el snippet no existe, 2 en argumentos inválidos.

### Entradas
- Código fuente, nombres de snippets y etiquetas.

### Salidas
- Snippets en STDOUT (sin cabeceras decorativas en `get` para permitir redirección directa a archivos o ejecución `$(snip_vault get ...)`).

### Persistencia
Directorio de archivos individuales (un archivo por snippet en `~/.snip_vault/snippets/`) con metadatos en encabezado YAML/JSON o archivo `metadata.json` central.

### Validaciones
- El nombre del snippet debe ser alfanumérico con guiones (slug válido, ej. `k8s-pod-restart`).
- No permitir sobrescribir un snippet existente en `save` a menos que se pase `--force`.

### Casos límite
- Snippets de miles de líneas de código.
- Snippets con caracteres de control o saltos de línea especiales (CRLF vs LF).
- Nombres de snippet duplicados.

### Manejo de errores
- Snippet no encontrado.
- Errores de lectura de STDIN si la entrada está vacía.

### Fundamentos de Python relacionados
- `pathlib.Path` para gestión de carpetas y archivos.
- Módulos `json` y `re`.
- Lectura polimórfica (argumentos vs archivos vs `sys.stdin`).

### Conceptos CLI relacionados
- Diseño de salida 'composable': `get` emite exclusivamente el código puro para permitir pipes.

### Herramientas o módulos para investigar
- `pathlib`.
- `sys.stdin`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `edit <NOMBRE>` para abrir el snippet en el editor predeterminado del sistema (`$EDITOR` o `notepad`/`nano`)?

### Diseño de argumentos
¿Cómo permitirías copiar el snippet directamente al portapapeles (`--copy / -c`)?

### Diseño de variables
`snippet_name`, `snippet_language`, `snippet_body`, `snippet_metadata`, `vault_directory_path`.

### Antes de programar
1. ¿Por qué almacenar cada snippet en su propio archivo en disco es más escalable que guardar todos los fragmentos gigantescos dentro de un solo archivo JSON monolítico?
2. ¿Cómo invocar el editor del sistema configurado en la variable de entorno `os.environ.get('EDITOR', 'nano')` usando `subprocess.run`?

### Arquitectura
Estructura:
```
ejercicio_027/
├── snip_vault.py
├── storage_engine.py
└── snippet_model.py
```

### Pruebas mínimas
1. Guardar un snippet por pipe `echo "SELECT 1;" | python snip_vault.py save test-sql --lang sql`.
2. Recuperar con `python snip_vault.py get test-sql` y comprobar que la salida sea exactamente `SELECT 1;`.

### Pruebas de error
1. Intentar guardar con el mismo nombre sin `--force` -> Exit code 1 informando que ya existe.

### Experiencia de usuario
En `list` y `find`, mostrar tablas formateadas. En `get`, emitir solo el código crudo.

### Explicación posterior
Explica la diferencia de experiencia de usuario entre comandos informativos y comandos diseñados para composición en tuberías Unix.

### Aplicación profesional
Gestión de playbooks de respuesta a incidentes, catálogo de consultas SQL frecuentes y comandos de infraestructura.

### Reto adicional
Implementar integración con el portapapeles del sistema operativo mediante librerías nativas o comandos del sistema (`pbcopy` en macOS, `xclip`/`wl-copy` en Linux, `clip` en Windows).

---
> [← Ejercicio 026](../ejercicio_026/README.md) · [Índice General](../README.md) · [Ejercicio 028 →](../ejercicio_028/README.md)
