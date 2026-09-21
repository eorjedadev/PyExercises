## Ejercicio 064 — Simulador de Colas de Mensajería FIFO con Persistencia (`queue-tool`)

> [← Ejercicio 063](../ejercicio_063/README.md) · [Índice General](../README.md) · [Ejercicio 065 →](../ejercicio_065/README.md)

### Contexto profesional
En sistemas distribuidos y arquitecturas orientadas a eventos (RabbitMQ, Amazon SQS, Apache Kafka), las colas de mensajes desacoplan productores y consumidores. Para depurar flujos de trabajo asíncronos y probar procesamiento por lotes localmente, los desarrolladores necesitan una herramienta CLI que opere como una cola de mensajería persistente con semántica FIFO, visibilidad de mensajes y colas de mensajes fallidos (Dead Letter Queue / DLQ).

### Problema
Construir una CLI que gestione colas de mensajería con persistencia en base de datos relacional (PostgreSQL como motor principal, o SQLite local opcional), permitiendo publicar mensajes (`publish`), consumir mensajes con confirmación explícita (`consume` / `ack`), reintentar mensajes no confirmados tras un tiempo de visibilidad (`visibility timeout`), mover mensajes agotados a una Dead Letter Queue (DLQ) y consultar estadísticas de la cola.

### Usuario objetivo
Desarrolladores backend, arquitectos de software e ingenieros de integración.

### Objetivo
Implementar un sistema de colas de mensajes con persistencia relacional, control de visibilidad (locks temporales), confirmaciones (ACK/NACK) y DLQ.

### Ejemplo conceptual de uso
```bash
# Publicar un mensaje en la cola 'orders'
python queue_tool.py publish orders --payload '{"order_id": 1042, "amount": 99.50}' --priority 1

# Consumir un mensaje bloqueándolo durante 30 segundos
python queue_tool.py consume orders --visibility-timeout 30

# Confirmar procesamiento exitoso (ACK) del mensaje consumido
python queue_tool.py ack orders --message-id "msg_88a3f"

# Ver estado y cantidad de mensajes encolados vs en proceso
python queue_tool.py stats orders
```

### Requisitos funcionales
- Subcomando `create-queue <NOMBRE>`: crea una cola con parámetros de configuración (tiempo de visibilidad por defecto, reintentos máximos antes de DLQ).
- Subcomando `publish <COLA>`: encola un mensaje con cuerpo JSON/texto, prioridad (opcional) y timestamp de encolado.
- Subcomando `consume <COLA>`: extrae el mensaje de mayor prioridad y más antiguo (FIFO) que esté disponible, actualiza su estado a `IN_FLIGHT` y establece un `visible_after` basado en el timeout.
- Subcomando `ack <COLA> --message-id <ID>`: confirma la finalización del procesamiento y elimina o marca el mensaje como completado.
- Subcomando `nack <COLA> --message-id <ID>`: rechaza el mensaje haciéndolo visible inmediatamente para otros consumidores o incrementando su contador de reintentos.
- Mecanismo Dead Letter Queue (DLQ): si un mensaje es consumido y falla N veces (`max_receive_count`), se mueve automáticamente a `<COLA>_dlq`.
- Subcomando `stats <COLA>`: muestra mensajes disponibles, en vuelo, completados y en DLQ.

### Requisitos de CLI
- Subcomandos: `create-queue`, `publish`, `consume`, `ack`, `nack`, `stats`, `purge`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Exit code 0 en éxito, 1 si la cola está vacía en `consume` o el mensaje no existe, 2 en errores.

### Entradas
- Nombres de cola, payloads de mensajes, IDs de mensaje y parámetros de timeout.

### Salidas
- Payload de mensaje en STDOUT (para que scripts consumidores procesen la salida) o tablas de estadísticas.

### Persistencia
PostgreSQL como motor principal (aprovechando `SELECT ... FOR UPDATE SKIP LOCKED` para concurrencia perfecta) o SQLite con bloqueo a nivel de archivo.

### Validaciones
- El nombre de la cola debe ser alfanumérico.
- El payload no debe estar vacío.
- Validar que el mensaje exista antes de ejecutar `ack` o `nack`.

### Casos límite
- Múltiples consumidores concurrentes ejecutando `consume` simultáneamente (evitar que dos consumidores reciban el mismo mensaje; race conditions).
- Consumidor que se cae a mitad del procesamiento (el mensaje debe volver a estar disponible automáticamente cuando expire `visible_after`).
- Colas vacías.

### Manejo de errores
- Excepciones de concurrencia y base de datos.
- Cola no encontrada.

### Fundamentos de Python relacionados
- Bloqueo de filas en bases de datos relacionales (`FOR UPDATE SKIP LOCKED` en PostgreSQL).
- Módulo `datetime` para cálculo de expiración de visibilidad.
- Dataclasses y serialización JSON.
- Patrón Repositorio para soporte de PostgreSQL y SQLite.

### Conceptos CLI relacionados
- Semántica de sistemas de mensajería (At-least-once delivery, Acknowledgements, Dead Letter Queues).
- Consumo concurrente de tareas en terminal.

### Herramientas o módulos para investigar
- `psycopg`.
- `sqlite3`.
- `datetime` y `json`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `worker <COLA> --exec "./process_order.sh"` para ejecutar un script externo por cada mensaje y hacer ACK/NACK según su exit code?

### Diseño de argumentos
¿Cómo nombrarías la opción para enviar un mensaje con retraso programado (Delayed Message) para que sea visible en N segundos (`--delay-seconds 60`)?

### Diseño de variables
`queue_name`, `message_payload_dto`, `message_visibility_lock_timestamp`, `receive_count_integer`, `dlq_queue_target`.

### Antes de programar
1. ¿Por qué la instrucción SQL `SELECT id, payload FROM queue_messages WHERE queue = '...' AND visible_after <= NOW() ORDER BY priority DESC, id ASC LIMIT 1 FOR UPDATE SKIP LOCKED` es el estándar de oro para colas de trabajo concurrentes en PostgreSQL?
2. ¿Cómo simular el comportamiento de visibilidad en SQLite sin `SKIP LOCKED` usando transacciones inmediatas?

### Arquitectura
Motor de colas (`queue_engine.py`), repositorio relacional (`queue_repository.py`), gestor de DLQ (`dlq_manager.py`) y CLI.

### Pruebas mínimas
1. Publicar 2 mensajes, consumir el primero, hacer `ack`, verificar que `consume` devuelva el segundo mensaje.
2. Consumir un mensaje sin hacer `ack`, simular la expiración del timeout de visibilidad y verificar que vuelva a ser entregado.

### Pruebas de error
1. Intentar hacer `ack` de un ID de mensaje inexistente -> Exit code 1.

### Experiencia de usuario
En `consume`, emitir exclusivamente el JSON puro del mensaje a STDOUT para facilitar pipes (`python queue_tool.py consume orders | jq .`), y mensajes de diagnóstico en STDERR.

### Explicación posterior
Explica la diferencia entre entrega al menos una vez (At-Least-Once Delivery) y entrega exactamente una vez (Exactly-Once Processing) en sistemas distribuidos.

### Aplicación profesional
Colas de procesamiento en segundo plano (Background Job Queues) para microservicios, sincronización asíncrona y procesamiento de tareas pesadas.

### Reto adicional
Implementar un subcomando `replay-dlq <COLA>` que reinyecte todos los mensajes de la Dead Letter Queue de vuelta a la cola principal tras corregir el error en el consumidor.

---
> [← Ejercicio 063](../ejercicio_063/README.md) · [Índice General](../README.md) · [Ejercicio 065 →](../ejercicio_065/README.md)
