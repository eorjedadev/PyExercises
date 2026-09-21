## Ejercicio 021 — Generador de Árbol de Directorios ASCII (`dir-tree`)

> [← Ejercicio 020](../ejercicio_020/README.md) · [Índice General](../README.md) · [Ejercicio 022 →](../ejercicio_022/README.md)

### Contexto profesional
Al documentar la estructura de repositorios de software, crear especificaciones de proyectos en archivos README o auditar jerarquías de carpetas complejas, los desarrolladores necesitan visualizar la estructura en forma de árbol visual idéntica al comando `tree` de Unix.

### Problema
Construir una CLI que recorra directorios y dibuje un árbol visual con caracteres ASCII/Unicode (`├──`, `└──`, `│   `), permitiendo limitar la profundidad, ignorar carpetas específicas (como `.git`, `node_modules`, `__pycache__`), mostrar tamaños de archivo y ordenar por diferentes criterios.

### Usuario objetivo
Desarrolladores de software, technical writers y administradores de sistemas.

### Objetivo
Implementar un generador de árbol de directorios con recursividad controlada, formateo de conectores gráficos y filtros avanzados.

### Ejemplo conceptual de uso
```bash
# Generar árbol del proyecto limitando a 2 niveles de profundidad
python dir_tree.py . --max-depth 2

# Mostrar solo directorios e ignorar carpetas comunes
python dir_tree.py /var/www --dirs-only --ignore ".git,node_modules,venv"

# Incluir tamaño de archivos y exportar en Markdown
python dir_tree.py src/ --sizes --format markdown
```

### Requisitos funcionales
- Recorrer el sistema de archivos dibujando conectores jerárquicos precisos (`├── `, `└── `, `│   `).
- Controlar profundidad máxima de exploración (`-L / --max-depth`).
- Filtrar solo directorios (`-d / --dirs-only`).
- Ignorar nombres o patrones de carpetas/archivos (`-I / --ignore`).
- Mostrar tamaño de archivos formateado junto al nombre (`-s / --sizes`).
- Mostrar conteo total de directorios y archivos al final del árbol.
- Salida en texto plano Unicode o bloque de código Markdown (`--format markdown`).

### Requisitos de CLI
- Argumento posicional: directorio raíz (default `.`).
- Opción `-L / --max-depth <N>`: profundidad máxima.
- Opción `-I / --ignore <PATRONES>`: lista separada por comas.
- Flag `-d / --dirs-only`.
- Flag `-s / --sizes`.
- Flag `-a / --all`: incluye archivos y carpetas ocultas.
- Exit code 0 en éxito, 1 si la ruta no es válida, 2 en argumentos inválidos.

### Entradas
- Ruta de directorio.
- Opciones de filtrado y visualización.

### Salidas
- Representación en árbol en STDOUT.

### Persistencia
Sin persistencia.

### Validaciones
- Comprobar que la ruta raíz exista y sea un directorio.
- Validar que `--max-depth` sea un entero positivo mayor o igual a 1.

### Casos límite
- Directorios con cientos de miles de archivos (respetar estrictamente el límite de profundidad para no saturar memoria).
- Enlaces simbólicos a carpetas (evitar ciclos infinitos).
- Directorios vacíos.

### Manejo de errores
- `PermissionError` en carpetas sin permiso de lectura (mostrar indicador `[Acceso Denegado]`).

### Fundamentos de Python relacionados
- `pathlib.Path` (`Path.iterdir()`, `Path.is_dir()`, `Path.name`).
- Algoritmos recursivos o iterativos basados en pila (`stack`).
- Gestión de prefijos de indentación en árboles.

### Conceptos CLI relacionados
- Dibujo de jerarquías con caracteres gráficos de terminal.
- Control de recursión y rendimiento en exploración de disco.

### Herramientas o módulos para investigar
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para exportar la jerarquía en formato JSON estructurado (`--json`)?

### Diseño de argumentos
¿Cómo permitirías filtrar por patrón de extensión de archivo (ej. `--pattern "*.py"`)?

### Diseño de variables
`root_path`, `current_depth`, `max_depth_limit`, `prefix_connector`, `dir_counter`, `file_counter`.

### Antes de programar
1. ¿Cómo determinar si un elemento es el último de su directorio para decidir si usar `└──` o `├──`?
2. ¿Cómo propagar correctamente la cadena de prefijos (`│   ` vs `    `) a los niveles inferiores?

### Arquitectura
Motor de recorrido de árbol (`tree_walker.py`) y formateador de conectores.

### Pruebas mínimas
1. Ejecutar sobre una estructura conocida con 2 niveles y validar que los conectores `├──` y `└──` estén alineados.
2. Probar `--dirs-only` y verificar que ningún archivo regular aparezca en la salida.

### Pruebas de error
1. Pasar una ruta a un archivo de texto en vez de carpeta -> Exit code 1.

### Experiencia de usuario
Salida limpia que pueda copiarse y pegarse directamente en documentación técnica.

### Explicación posterior
Explica la diferencia entre recorrido en profundidad (DFS) y recorrido en anchura (BFS) y cuál es el apropiado para dibujar árboles jerárquicos.

### Aplicación profesional
Documentación técnica de proyectos, linters de estructura de repositorios y auditoría de proyectos.

### Reto adicional
Calcular y mostrar el tamaño acumulado total de cada subdirectorio junto a su nombre.

---
> [← Ejercicio 020](../ejercicio_020/README.md) · [Índice General](../README.md) · [Ejercicio 022 →](../ejercicio_022/README.md)
