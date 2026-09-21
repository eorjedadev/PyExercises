## Ejercicio 047 — Despachador y Gestor de Tickets de Soporte Técnico (`ticket-cli`)

> [← Ejercicio 046](../ejercicio_046/README.md) · [Índice General](../README.md) · [Ejercicio 048 →](../ejercicio_048/README.md)

### Contexto profesional
En centros de soporte técnico y operaciones de TI, los operadores reciben cientos de incidencias diarias que deben clasificarse por prioridad (Baja, Media, Alta, Crítica), asignarse a ingenieros según su especialidad, transicionar a través de una máquina de estados finita y auditar tiempos de resolución.

### Problema
Construir una CLI conectada a una base de datos relacional (PostgreSQL o SQLite opcional) para la gestión completa de tickets de soporte, con máquina de estados estricta (`NEW` -> `ASSIGNED` -> `IN_PROGRESS` -> `RESOLVED` -> `CLOSED`), asignación de colas, comentarios internos y generación de reportes de tiempos de atención.

### Usuario objetivo
Ingenieros de soporte, coordinadores de mesa de ayuda (Helpdesk) y administradores de sistemas.

### Objetivo
Implementar un sistema de gestión de tickets con máquina de estados finita, control de concurrencia y persistencia relacional.

### Ejemplo conceptual de uso
```bash
# Crear un nuevo ticket de soporte
python ticket_cli.py create "Fallo en conexión VPN sucursal norte" --priority high --category "Redes" --requester "carlos.ruiz"

# Asignar ticket a un ingeniero y cambiar estado
python ticket_cli.py assign 1042 --to "laura.sre"

# Transicionar estado del ticket agregando comentario de resolución
python ticket_cli.py transition 1042 --to RESOLVED --comment "Reinicio de túnel IPsec completado"
```

### Requisitos funcionales
- Subcomando `create`: crea un ticket con título, descripción, prioridad (`LOW`, `MEDIUM`, `HIGH`, `CRITICAL`), categoría y solicitante.
- Subcomando `list`: consulta de tickets con filtros por estado, prioridad, técnico asignado y ordenamiento por fecha o prioridad.
- Subcomando `assign <ID>`: asigna el ticket a un técnico y transiciona el estado automáticamente a `ASSIGNED`.
- Subcomando `transition <ID>`: cambia el estado validando que la transición sea permitida por la máquina de estados. Exigir comentario si se transiciona a `RESOLVED` o `CLOSED`.
- Subcomando `comment <ID> <TEXTO>`: añade una nota interna al historial del ticket.
- Subcomando `show <ID>`: muestra la ficha completa del ticket con todo su historial de comentarios y transiciones.
- Subcomando `metrics`: calcula tiempo medio de primera respuesta (MTTA) y tiempo medio de resolución (MTTR).

### Requisitos de CLI
- Subcomandos: `create`, `list`, `assign`, `transition`, `comment`, `show`, `metrics`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Exit code 0 en éxito, 1 si el ticket no existe o la transición de estado es inválida, 2 en errores.

### Entradas
- Datos de tickets, estados, comentarios y parámetros de conexión.

### Salidas
- Fichas técnicas, tablas de colas de soporte y reportes de métricas en STDOUT.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `tickets`, `ticket_comments` y `ticket_audit`.

### Validaciones
- Validar la máquina de estados: prohibir transiciones ilegales (ej. de `NEW` directo a `CLOSED` sin pasar por `RESOLVED`, o reabrir un ticket cerrado sin permiso).
- La prioridad debe pertenecer al catálogo permitido.

### Casos límite
- Cierre de tickets con comentarios de longitud considerable.
- Reasignación de tickets ya en progreso.
- Manejo de tickets duplicados.

### Manejo de errores
- `ValueError` en transiciones no válidas.
- Errores de acceso a base de datos.

### Fundamentos de Python relacionados
- Implementación del patrón Máquina de Estados Finita (FSM - Finite State Machine) con `Enum`.
- Patrón Repositorio y control transaccional con PostgreSQL / SQLite.
- `dataclasses` para modelado de entidades.

### Conceptos CLI relacionados
- Validación estricta de lógica de negocio y transiciones de estado en terminal.
- Gestión de trazabilidad y auditoría de eventos.

### Herramientas o módulos para investigar
- `enum.Enum`.
- `dataclasses`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `export --format json` para migrar tickets a plataformas externas como Jira o ServiceNow?

### Diseño de argumentos
¿Cómo nombrarías la opción para filtrar tickets que han superado el tiempo máximo de SLA sin respuesta (`--breached-sla`)?

### Diseño de variables
`ticket_state_machine`, `current_ticket_status`, `target_transition_status`, `ticket_audit_entry`, `mtta_average_seconds`.

### Antes de programar
1. ¿Cómo estructurar la matriz de transiciones válidas en un diccionario `ALLOWED_TRANSITIONS = {Status.NEW: [Status.ASSIGNED, Status.CANCELLED], ...}`?
2. ¿Cómo registrar automáticamente en la tabla de auditoría el usuario, timestamp, estado anterior y estado nuevo en cada transición?

### Arquitectura
Máquina de estados (`state_machine.py`), repositorio (`ticket_repository.py`), servicio de métricas (`sla_metrics.py`) y CLI.

### Pruebas mínimas
1. Crear un ticket, asignarlo, transicionarlo a `RESOLVED` con comentario y verificar que `show` muestre el historial completo.
2. Probar `metrics` y verificar el cálculo de tiempos.

### Pruebas de error
1. Intentar pasar un ticket de `NEW` a `RESOLVED` directamente -> Exit code 1 informando que la transición viola la máquina de estados.

### Experiencia de usuario
Ficha detallada con colores: Rojo para tickets Críticos, Verde para Resueltos, y línea de tiempo visual de comentarios.

### Explicación posterior
Explica por qué forzar transiciones a través de una máquina de estados previene inconsistencias de datos y estados huérfanos en sistemas transaccionales.

### Aplicación profesional
Mesas de ayuda internas, sistemas de gestión de incidencias de guardia (on-call incident management) y soporte técnico.

### Reto adicional
Implementar asignación automática de tickets basada en algoritmo Round-Robin o menor carga de trabajo activa entre los técnicos disponibles.

---
> [← Ejercicio 046](../ejercicio_046/README.md) · [Índice General](../README.md) · [Ejercicio 048 →](../ejercicio_048/README.md)
