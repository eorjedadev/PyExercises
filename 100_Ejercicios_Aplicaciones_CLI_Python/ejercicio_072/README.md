## Ejercicio 072 — Motor de Ejecución de Tareas Basado en Plugins (`task-runner`)

> [← Ejercicio 071](../ejercicio_071/README.md) · [Índice General](../README.md) · [Ejercicio 073 →](../ejercicio_073/README.md)

### Contexto profesional
En plataformas de automatización y sistemas de orquestación de tareas, se requiere un ejecutor de comandos central que sea extensible mediante plugins dinámicos (módulos externos de Python cargados en tiempo de ejecución desde una carpeta `plugins/` o entry points) sin necesidad de modificar el código fuente de la herramienta principal.

### Problema
Construir una CLI modular que descubra dinámicamente plugins de tareas instalados en un directorio o mediante `importlib.metadata.entry_points`, valide que cumplan con una interfaz abstracta (`BaseTaskPlugin`), resuelva dependencias y orden de ejecución entre tareas mediante un grafo acíclico dirigido (DAG) y ejecute el pipeline reportando tiempos y resultados.

### Usuario objetivo
Ingenieros de automatización, DevOps y desarrolladores backend.

### Objetivo
Diseñar una arquitectura extensible basada en plugins dinámicos (`importlib`), resolución de dependencias mediante Topological Sort y ejecución secuencial/paralela.

### Ejemplo conceptual de uso
```bash
# Listar todos los plugins de tareas descubiertos
python task_runner.py plugins list

# Ejecutar una tarea específica con sus argumentos
python task_runner.py run backup-db --env production

# Ejecutar un pipeline de tareas encadenadas resolviendo dependencias
python task_runner.py pipeline deploy-pipeline --dry-run
```

### Requisitos funcionales
- Descubrimiento dinámico de plugins: carga de módulos `.py` desde la carpeta `~/.task_runner/plugins/` o `./plugins/` usando `importlib.util` y detección de entry points en `pyproject.toml`.
- Interfaz base estricta `BaseTaskPlugin`: cada plugin debe definir `name`, `description`, `dependencies` (lista de tareas previas requeridas) y el método `execute(context)`.
- Subcomando `plugins list`: muestra los plugins descubiertos, versión, autor y tareas que expone.
- Subcomando `run <TASK_NAME>`: ejecuta una tarea individual validando sus dependencias previas.
- Subcomando `pipeline <PIPELINE_FILE>`: lee una lista de tareas de un archivo YAML/JSON, construye un grafo acíclico dirigido (DAG), detecta ciclos infinitos y ejecuta las tareas en el orden topológico correcto.
- Subcomando `plugins install <URL/FILE>`: descarga o copia un nuevo plugin al directorio de plugins.

### Requisitos de CLI
- Subcomandos: `plugins`, `run`, `pipeline`.
- Opciones de `plugins`: `list`, `install`, `info`.
- Flag `--dry-run` en `pipeline`.
- Opción `--plugin-dir <RUTA>`.
- Exit code 0 en éxito, 1 si una tarea falla en su ejecución o hay ciclos en el DAG, 2 en errores de sintaxis.

### Entradas
- Nombres de tareas, parámetros de ejecución y archivos de pipeline.

### Salidas
- Logs de ejecución de tareas, reportes de estado y tiempos en STDOUT.

### Persistencia
Directorio de plugins en disco y registro de ejecuciones en PostgreSQL/SQLite opcional.

### Validaciones
- Validar que los plugins implementen todos los métodos requeridos de `BaseTaskPlugin`.
- Detección estricta de dependencias circulares (ej. Tarea A depende de B y B depende de A) antes de ejecutar.

### Casos límite
- Plugin con errores de sintaxis en su código (no debe colapsar la CLI principal; omitir con advertencia).
- Fallo de una tarea intermedia en un pipeline (abortar las tareas dependientes posteriores y ejecutar tareas de rollback si existen).

### Manejo de errores
- `ImportError` / `AttributeError` al cargar módulos dinámicos.
- Excepciones no controladas dentro de los plugins.

### Fundamentos de Python relacionados
- Carga dinámica de módulos con `importlib.util.spec_from_file_location` y `importlib.util.module_from_spec`.
- Clases abstractas y protocolos con `abc.ABC` y `abc.abstractmethod`.
- Algoritmo de ordenamiento topológico (Topological Sort / Kahn's Algorithm) con diccionarios y conjuntos.
- Subparsers de `argparse`.

### Conceptos CLI relacionados
- Arquitecturas extensibles mediante sistemas de plugins y entry points.
- Resolución y ejecución de grafos de dependencia (DAGs).

### Herramientas o módulos para investigar
- `importlib` e `importlib.metadata`.
- `abc` e `inspect`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para pasar variables de contexto compartidas entre tareas durante la ejecución de un pipeline (`--context "env=prod,version=1.2"`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para continuar la ejecución de tareas independientes si una tarea no crítica falla (`--continue-on-error`)?

### Diseño de variables
`loaded_plugins_registry`, `task_dependency_graph`, `topological_sorted_tasks_list`, `task_execution_context`, `task_run_result_dto`.

### Antes de programar
1. ¿Cómo cargar un archivo Python arbitrario desde una ruta en disco como módulo ejecutable usando `importlib.util`?
2. ¿Cómo implementar el algoritmo de ordenamiento topológico para detectar dependencias circulares y determinar el orden lineal de ejecución?

### Arquitectura
Estructura:
```
ejercicio_072/
├── task_runner.py
├── plugin_loader.py
├── base_plugin.py
├── dag_resolver.py
└── plugins/
    ├── backup_plugin.py
    └── notify_plugin.py
```

### Pruebas mínimas
1. Cargar 2 plugins de prueba (uno de compilación y otro de despliegue con dependencia), ejecutar el pipeline y verificar que se ejecute primero la compilación.
2. Probar detección de dependencia circular A -> B -> A y verificar que aborte con error.

### Pruebas de error
1. Intentar ejecutar una tarea que no existe -> Exit code 1.

### Experiencia de usuario
Salida clara indicando el árbol de ejecución de tareas: `[1/3] Ejecutando: build-assets... OK (1.2s)`, `[2/3] Ejecutando: test-suite... OK (4.5s)`.

### Explicación posterior
Explica la diferencia entre extender una aplicación mediante herencia/subclases directas vs mediante plugins dinámicos desacoplados en tiempo de ejecución.

### Aplicación profesional
Motores de tareas estilo Ansible/Fabric, herramientas de CI/CD locales y frameworks de automatización corporativos.

### Reto adicional
Implementar ejecución paralela de tareas independientes que residan en el mismo nivel jerárquico del grafo mediante `ThreadPoolExecutor`.

---
> [← Ejercicio 071](../ejercicio_071/README.md) · [Índice General](../README.md) · [Ejercicio 073 →](../ejercicio_073/README.md)
