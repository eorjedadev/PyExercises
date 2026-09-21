## Ejercicio 026 — Gestor Local de Marcadores Web (`bm-cli`)

> [← Ejercicio 025](../ejercicio_025/README.md) · [Índice General](../README.md) · [Ejercicio 027 →](../ejercicio_027/README.md)

### Contexto profesional
Los desarrolladores y profesionales de IT consultan cientos de recursos web técnicos (documentación de librerías, tableros de Grafana, repositorios de GitHub, tickets de Jira). Mantener una base de marcadores categorizada y accesible instantáneamente desde la terminal acelera la productividad diaria.

### Problema
Construir una aplicación CLI con subcomandos completos (`add`, `list`, `search`, `delete`, `open`, `export`) para gestionar marcadores web con títulos, URLs, etiquetas (tags) y fecha de creación, persistiendo los datos de forma atómica en un archivo JSON local.

### Usuario objetivo
Desarrolladores, investigadores y administradores de sistemas.

### Objetivo
Diseñar una arquitectura CLI completa con subcomandos, persistencia transaccional en JSON, validación de URLs y búsqueda por tags.

### Ejemplo conceptual de uso
```bash
# Agregar un nuevo marcador con etiquetas
python bm_cli.py add "https://docs.python.org/3/" --title "Python Docs" --tags "python,docs,oficial"

# Listar marcadores filtrando por etiqueta
python bm_cli.py list --tag "docs"

# Abrir el marcador en el navegador predeterminado del sistema
python bm_cli.py open 1
```

### Requisitos funcionales
- Subcomando `add <URL>`: almacena URL, título (opcional o autodetectado), etiquetas separadas por comas y timestamp ISO.
- Subcomando `list`: muestra tabla con ID autoincremental, título, URL y tags.
- Subcomando `search <QUERY>`: busca por coincidencia en título, URL o etiquetas.
- Subcomando `delete <ID>`: elimina un marcador por su identificador.
- Subcomando `open <ID>`: abre la URL en el navegador web del sistema operativo (`webbrowser`).
- Subcomando `export`: exporta los marcadores en formato HTML estándar compatible con navegadores (Netscape Bookmark File).

### Requisitos de CLI
- Subcomandos: `add`, `list`, `search`, `delete`, `open`, `export`.
- Opciones globales: `--db <RUTA>` para especificar un archivo JSON personalizado.
- Exit code 0 en éxito, 1 si el ID no existe o falla la operación, 2 en error de sintaxis.

### Entradas
- URLs, títulos, tags y comandos de terminal.

### Salidas
- Tablas formateadas en terminal, confirmaciones de guardado y mensajes en STDERR.

### Persistencia
Archivo JSON transaccional (ej. `~/.bookmarks.json` o local). Escritura atómica usando archivo temporal + renombramiento.

### Validaciones
- Validar que la URL tenga formato válido con protocolo `http://` o `https://`.
- Validar que el ID ingresado en `delete` y `open` sea un entero positivo existente.

### Casos límite
- Base de datos JSON inexistente (debe inicializarse automáticamente en la primera ejecución).
- Eliminación del último marcador restante.
- Búsquedas que no arrojan resultados.

### Manejo de errores
- `json.JSONDecodeError` si el archivo de datos fue corrompido manualmente.
- Captura de errores al abrir el navegador.

### Fundamentos de Python relacionados
- Módulos `json`, `webbrowser`, `urllib.parse`.
- Escritura atómica de archivos con `tempfile` y `os.replace`.
- Subparsers en `argparse` con funciones asociadas (`set_defaults(func=...)`).

### Conceptos CLI relacionados
- Patrón arquitectónico de Subcomandos (`app action resource`).
- Persistencia local segura contra caídas de energía o fallos de escritura.

### Herramientas o módulos para investigar
- `argparse`.
- `webbrowser`.
- `urllib.parse`.
- `tempfile` y `os.replace`.

### Diseño de comandos
Diseña la distribución de subcomandos para que cada acción tenga su propio subconjunto de flags.

### Diseño de argumentos
¿Cómo nombrarías la opción para ordenar los marcadores por fecha de creación o por frecuencia de uso (`--sort-by date|clicks`)?

### Diseño de variables
`bookmark_records`, `new_bookmark_item`, `search_query_term`, `tag_filter_list`, `storage_file_path`.

### Antes de programar
1. ¿Por qué escribir directamente en `bookmarks.json` con `open('w')` es riesgoso si el programa se interrumpe a mitad de escritura, y por qué `os.replace()` garantiza atomicidad?
2. ¿Cómo desacoplar la lógica de almacenamiento (Storage) de la lógica de presentación CLI?

### Arquitectura
Estructura modular:
```
ejercicio_026/
├── bm_cli.py        # Punto de entrada y configuración de subparsers
├── storage.py       # Capa de persistencia JSON atómica
├── models.py        # Entidad Bookmark y validaciones
└── views.py         # Renderizado de tablas y mensajes
```

### Pruebas mínimas
1. Agregar 2 marcadores, listar y verificar que se asignen IDs 1 y 2.
2. Buscar por etiqueta y verificar que solo retorne el marcador correspondiente.
3. Eliminar el marcador 1 y verificar que `list` solo contenga el marcador 2.

### Pruebas de error
1. Intentar borrar un ID inexistente `python bm_cli.py delete 999` -> Exit code 1 con mensaje claro.

### Experiencia de usuario
Tabla limpia con bordes, resumen de marcadores encontrados y confirmación visual al agregar o borrar.

### Explicación posterior
Explica el concepto de escritura atómica (atomic write) en sistemas de archivos POSIX y Windows.

### Aplicación profesional
Base para construir gestores de snippets, administradores de recursos de nube y herramientas CLI personales de productividad.

### Reto adicional
Implementar autocompletado de título haciendo un `HTTP GET` rápido (con timeout de 2 segundos) para extraer el tag `<title>` de la página web si no se proporciona `--title`.

---
> [← Ejercicio 025](../ejercicio_025/README.md) · [Índice General](../README.md) · [Ejercicio 027 →](../ejercicio_027/README.md)
