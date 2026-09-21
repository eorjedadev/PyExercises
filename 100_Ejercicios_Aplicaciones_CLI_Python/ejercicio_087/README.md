## Ejercicio 087 — Monitor de Quórum y Heartbeat en Clústeres de Alta Disponibilidad (`cluster-heartbeat`)

> [← Ejercicio 086](../ejercicio_086/README.md) · [Índice General](../README.md) · [Ejercicio 088 →](../ejercicio_088/README.md)

### Contexto profesional
En sistemas distribuidos de alta disponibilidad (clústeres de PostgreSQL con Patroni, clústeres de Kubernetes, etcd, Consul), los nodos del clúster intercambian señales periódicas de latido (Heartbeats) para elegir un líder mediante algoritmos de consenso (Raft/Paxos) y detectar caídas de nodos sin incurrir en el peligroso estado de cerebro dividido (Split-Brain).

### Problema
Construir una CLI que simule o monitoree el estado de quórum y latidos de un clúster distribuido de N nodos, registrando los heartbeats con marcas de tiempo en base de datos relacional (PostgreSQL como motor principal, o SQLite opcional), detectando caídas de nodos por timeout, evaluando si se mantiene el quórum mayoritario ($Q = \lfloor N/2 \rfloor + 1$) y disparando eventos de elección de nuevo líder.

### Usuario objetivo
Ingenieros de sistemas distribuidos, arquitectos de software y SREs.

### Objetivo
Crear un simulador y monitor de quórum y consenso en clústeres con detección de particiones de red y prevención de split-brain.

### Ejemplo conceptual de uso
```bash
# Monitorear el quórum de un clúster de 5 nodos en tiempo real
python cluster_heartbeat.py monitor --cluster-size 5 --heartbeat-timeout 3.0

# Simular la caída de 2 nodos y verificar si se mantiene el quórum
python cluster_heartbeat.py simulate-partition --failed-nodes "node-3,node-4"
```

### Requisitos funcionales
- Registro periódico de heartbeats por cada nodo con `node_id`, `term_election`, `is_leader`, `timestamp` y `health_status`.
- Detección de pérdida de latidos: si un nodo no envía heartbeat en `--heartbeat-timeout` segundos, marcarlo como `UNREACHABLE`.
- Cálculo de Quórum Mayoritario: evaluar si los nodos vivos representan estrictamente más del 50% de los nodos totales del clúster ($Vivos > N/2$). Si se pierde el quórum, el clúster debe pasar a modo de solo lectura (`READ_ONLY / NO_QUORUM`) para prevenir inconsistencias.
- Protocolo de Elección de Líder: si el nodo líder cae y hay quórum, los nodos vivos inician una elección y promueven al nodo con el término más reciente.
- Subcomando `monitor`: tablero TUI en vivo con el estado de cada nodo del clúster, rol (Líder / Seguidor), latencia del último heartbeat y estado de quórum.
- Persistencia de eventos de topología en PostgreSQL (o SQLite opcional).

### Requisitos de CLI
- Subcomandos: `monitor`, `simulate-partition`, `history`, `node-agent`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite`.
- Opción `--cluster-size <N>` (default 3).
- Opción `--heartbeat-timeout <SEG>` (default 3.0).
- Exit code 0 en quórum saludable, 1 si el clúster perdió el quórum (estado crítico), 2 en errores.

### Entradas
- Parámetros de clúster, identificadores de nodo y credenciales de BD.

### Salidas
- Tablero de estado de clúster en terminal y logs de consenso.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `cluster_nodes`, `heartbeat_log` y `election_events`.

### Validaciones
- El tamaño del clúster debe ser un número impar (3, 5, 7) para evitar empates en votaciones.
- Los timeouts de latido deben ser positivos.

### Casos límite
- Partición de red donde el clúster se divide en dos mitades (ej. 2 nodos en datacenter A y 1 nodo en datacenter B; solo el grupo mayoritario de 2 nodos puede operar).
- Reincorporación de un nodo antiguo que creía ser líder (debe ceder su liderazgo al detectar un término superior).
- Caída simultánea de la mayoría de nodos.

### Manejo de errores
- Excepciones de red y base de datos.
- Pérdida de conectividad con el almacén de estado.

### Fundamentos de Python relacionados
- Implementación de conceptos del algoritmo de consenso Raft (Términos, Elecciones, Heartbeats).
- Módulo `time` y `threading` para bucles de sondeo asíncronos.
- Persistencia relacional de estados y transacciones en PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Simulación y observabilidad de sistemas distribuidos y protocolos de consenso.
- Prevención de condiciones de Split-Brain.

### Herramientas o módulos para investigar
- `threading` y `time`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `inject-fencing <NODE_ID>` para forzar el aislamiento (STONITH / Fencing) de un nodo rebelde?

### Diseño de argumentos
¿Cómo nombrarías la opción para simular latencia de red variable entre nodos (`--jitter-ms 200`)?

### Diseño de variables
`cluster_total_nodes_count`, `active_quorum_threshold`, `current_leader_node_id`, `election_term_number`, `cluster_operational_state`.

### Antes de programar
1. ¿Por qué los clústeres distribuidos requieren siempre un número impar de nodos (3, 5, 7) para calcular la mayoría estricta $\lfloor N/2 \rfloor + 1$?
2. ¿Qué es el fenómeno de Split-Brain y por qué una partición de red puede provocar corrupción irrecuperable de datos si dos líderes aceptan escrituras al mismo tiempo?

### Arquitectura
Motor de consenso (`raft_simulator.py`), gestor de heartbeats (`heartbeat_manager.py`), repositorio de clúster (`cluster_repo.py`) y CLI.

### Pruebas mínimas
1. Iniciar clúster de 3 nodos, verificar que se elija un líder y el estado sea `HEALTHY_QUORUM`.
2. Simular la caída de 1 nodo (quedan 2/3 vivos) y verificar que el clúster mantenga quórum.
3. Simular la caída de un segundo nodo (queda 1/3 vivo) y verificar que el estado cambie inmediatamente a `NO_QUORUM / READ_ONLY` y retorne exit code 1.

### Pruebas de error
1. Configurar un tamaño de clúster par (ej. 4 nodos) sin desempate -> Emitir advertencia de riesgo de split-brain.

### Experiencia de usuario
Tablero visual en terminal con insignias de rol: `[LÍDER] node-1 (Heartbeat: hace 0.2s - OK)`, `[SEGUIDOR] node-2 (OK)`, `[DESCONECTADO] node-3` y estado global `QUÓRUM ACTIVO (2/3) - OPERACIONAL`.

### Explicación posterior
Explica el Teorema CAP (Consistencia, Disponibilidad, Tolerancia a Particiones) y por qué los sistemas basados en quórum priorizan la Consistencia sobre la Disponibilidad ante particiones de red.

### Aplicación profesional
Monitoreo de clústeres de PostgreSQL HA (Patroni/Stolon), supervisión de etcd en Kubernetes y sistemas de almacenamiento distribuido.

### Reto adicional
Implementar el protocolo de votación de Raft completo con intercambio de mensajes `RequestVote` y `AppendEntries` entre procesos independientes.

---
> [← Ejercicio 086](../ejercicio_086/README.md) · [Índice General](../README.md) · [Ejercicio 088 →](../ejercicio_088/README.md)
