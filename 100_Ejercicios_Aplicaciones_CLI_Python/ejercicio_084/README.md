## Ejercicio 084 — Visualizador de Mapas de Dependencias entre Microservicios (`service-map`)

> [← Ejercicio 083](../ejercicio_083/README.md) · [Índice General](../README.md) · [Ejercicio 085 →](../ejercicio_085/README.md)

### Contexto profesional
En arquitecturas complejas de microservicios distribuidos, comprender qué servicios se comunican entre sí, qué bases de datos (PostgreSQL, Redis, RabbitMQ) consumen y qué dependencias aguas abajo (downstream) se verán afectadas si un servicio falla es un desafío crítico de observabilidad y arquitectura.

### Problema
Construir una CLI que analice archivos de trazas distribuidas (OpenTelemetry / Jaeger JSON) o manifiestos de infraestructura (Docker Compose / Kubernetes), construya el grafo dirigido de dependencias entre servicios, calcule métricas de centralidad y puntos únicos de fallo (SPOF), genere diagramas visuales en formato DOT (Graphviz) o Mermaid y permita consultar el radio de impacto ante la caída de un nodo.

### Usuario objetivo
Arquitectos de software, ingenieros de SRE y desarrolladores de microservicios.

### Objetivo
Crear un generador y analizador de mapas de topología de microservicios con análisis de impacto de caídas y exportación de diagramas.

### Ejemplo conceptual de uso
```bash
# Construir mapa de dependencias a partir de trazas o manifiestos
python service_map.py build --from-compose docker-compose.yml --format mermaid -o topology.mmd

# Analizar el radio de impacto de fallo del servicio 'auth-service'
python service_map.py blast-radius "auth-service" --graph topology.json

# Identificar puntos únicos de fallo (SPOF) en la arquitectura
python service_map.py audit-spof --graph topology.json
```

### Requisitos funcionales
- Ingestión de topologías desde múltiples fuentes:
  - Manifiestos `docker-compose.yml` o manifiestos de Kubernetes.
  - Archivos de trazas distribuidas JSON (extrayendo llamadas cliente -> servidor).
  - Archivo de definición de grafo JSON personalizado.
- Construir el grafo dirigido de dependencias ($G = (V, E)$ donde los vértices son servicios/bases de datos y las aristas son llamadas RPC/HTTP/mensajería).
- Subcomando `blast-radius <SERVICIO>`: ejecuta un recorrido en profundidad (DFS) inverso para identificar todos los servicios aguas arriba que colapsarían si el servicio objetivo se cae.
- Subcomando `audit-spof`: detecta puntos únicos de fallo (nodos con alto grado de entrada/centralidad sin redundancia declarada).
- Subcomando `export`: genera el diagrama visual de la arquitectura en sintaxis Mermaid (`graph TD`) o Graphviz DOT (`digraph`).
- Persistencia del grafo topológico en PostgreSQL o SQLite opcional.

### Requisitos de CLI
- Subcomandos: `build`, `blast-radius`, `audit-spof`, `export`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite`.
- Opción `--format [mermaid|dot|table|json]` (default `mermaid`).
- Opción `-o / --output <RUTA>`.
- Exit code 0 en éxito, 1 si se detectan puntos críticos de fallo sin redundancia en `audit-spof`, 2 en errores.

### Entradas
- Manifiestos de servicios, archivos de trazas y nombres de nodos.

### Salidas
- Código de diagrama (Mermaid/DOT), tablas de análisis de impacto y JSON en STDOUT.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `services`, `service_dependencies` y `topology_snapshots`.

### Validaciones
- Comprobar que el archivo de entrada exista y tenga sintaxis válida.
- Validar que el servicio consultado en `blast-radius` exista en el grafo.

### Casos límite
- Arquitecturas con dependencias circulares entre microservicios.
- Grafos gigantes con cientos de servicios y bases de datos.
- Servicios aislados sin conexiones entrantes ni salientes.

### Manejo de errores
- Errores de parsing de archivos YAML/JSON.
- Nodo no encontrado en el grafo.

### Fundamentos de Python relacionados
- Teoría de grafos con estructuras de datos nativas (`dict[str, set[str]]` para listas de adyacencia).
- Algoritmos de recorrido de grafos: DFS (Depth-First Search) y BFS (Breadth-First Search).
- Serialización de sintaxis de diagramas Mermaid y Graphviz DOT.
- Persistencia de relaciones de grafo en PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Modelado y análisis de topologías distribuidas en terminal.
- Análisis de radio de impacto (Blast Radius Analysis) en ingeniería de resiliencia.

### Herramientas o módulos para investigar
- `json`.
- `pathlib`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `shortest-path <ORIGEN> <DESTINO>` para mostrar la cadena exacta de llamadas entre dos microservicios distantes?

### Diseño de argumentos
¿Cómo nombrarías la opción para filtrar por tipo de comunicación (ej. solo dependencias síncronas HTTP vs asíncronas de colas con `--comm-type sync|async`)?

### Diseño de variables
`services_adjacency_graph`, `reverse_dependency_graph`, `affected_upstream_nodes_set`, `spof_vulnerable_nodes_list`, `mermaid_diagram_output`.

### Antes de programar
1. ¿Cómo construir el grafo invertido (donde las aristas apuntan de los proveedores a los consumidores) para calcular el radio de impacto hacia atrás con DFS?
2. ¿Cómo formatear la sintaxis Mermaid: `graph TD; A[API Gateway] --> B[Auth Service]; B --> C[(PostgreSQL DB)];`?

### Arquitectura
Parser de topologías (`compose_parser.py`), motor de grafos (`graph_engine.py`), calculador de radio de impacto (`blast_radius_calc.py`) y CLI.

### Pruebas mínimas
1. Construir un grafo de prueba con 4 servicios (`Gateway -> Auth -> Postgres` y `Gateway -> Orders -> Postgres`), ejecutar `blast-radius Postgres` y verificar que reporte que todos los servicios se ven afectados.
2. Ejecutar `export --format mermaid` y validar la sintaxis generada.

### Pruebas de error
1. Solicitar `blast-radius` de un servicio inexistente -> Exit code 1 con error claro.

### Experiencia de usuario
Salida limpia en STDOUT que pueda pegarse directamente en Notion, GitHub Markdown o visualizadores Mermaid, y resumen de impacto con porcentajes de afectación de la plataforma.

### Explicación posterior
Explica el concepto de dependencias duras (Hard Dependencies) vs dependencias blandas (Soft Dependencies con fallbacks) en arquitecturas de microservicios.

### Aplicación profesional
Planificación de mantenimientos de infraestructura, análisis de riesgos de cambio y arquitectura de software.

### Reto adicional
Calcular la métrica de centralidad de intermediación (Betweenness Centrality) de cada nodo para rankear los microservicios más neurálgicos de la empresa.

---
> [← Ejercicio 083](../ejercicio_083/README.md) · [Índice General](../README.md) · [Ejercicio 085 →](../ejercicio_085/README.md)
