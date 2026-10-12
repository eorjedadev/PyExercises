## Ejercicio 098 — Mesa de Ayuda y Ticketing Corporativo con Niveles de SLA (`CorporateHelpdeskSlaApp`)

> [Índice General](../README.md) · [← Ejercicio 097](../ejercicio_097/README.md) · [Ejercicio 099 →](../ejercicio_099/README.md)

### Contexto profesional
En departamentos de TI corporativos y mesas de ayuda de telecomunicaciones, los ingenieros atienden tickets de soporte técnico bajo acuerdos de nivel de servicio (SLA) que imponen tiempos máximos de respuesta y resolución según la prioridad.

### Usuario objetivo
Analista de soporte de TI, despachador de tickets o gerente de servicio.

### Problema
La falta de visibilidad del tiempo restante de SLA provoca que tickets críticos venzan sin atención oportuna, acarreando penalizaciones contractuales a la empresa.

### Objetivo
Desarrollar autónomamente una plataforma integral de gestión de tickets de soporte con control dinámico de SLA en SQLite. La aplicación debe calcular en tiempo real el tiempo restante de SLA para cada ticket, actualizar la urgencia con colores dinámicos mediante temporizadores no bloqueantes, permitir asignación a técnicos y generar reportes de cumplimiento de nivel de servicio.

### Flujo principal
El analista ve la cola de tickets clasificados por urgencia. Cada ticket muestra una cuenta regresiva de SLA (ej. '02:45 restantes'). Si el ticket está a menos de 30 minutos de vencer, se torna amarillo; si vence, se marca como 'SLA Incumplido' en rojo parpadeante. El técnico toma el ticket, documenta las acciones de soporte y lo marca como 'Resuelto', registrando si cumplió o no el SLA contractual.

### Requisitos funcionales
- Esquema de base de datos SQLite con tablas de tickets, técnicos, categorías y bitácora de acciones.
- Cálculo automático de fecha y hora límite de SLA al crear el ticket según la prioridad: Crítica (2 horas), Alta (4 horas), Media (8 horas), Baja (24 horas).
- Temporizador no bloqueante en la interfaz que recalcula periódicamente los tiempos restantes de SLA para todos los tickets visibles.
- Clasificación visual por semáforo de SLA: Verde (>50% de tiempo restante), Amarillo (<50%), Rojo (<10% o Vencido).
- Flujo de estados: Abierto, Asignado, En Progreso, Resuelto, Cerrado.
- Asignación de técnicos y registro de notas de avance en el expediente del ticket.
- Métrica consolidada: Porcentaje de Cumplimiento de SLA institucional (%) del periodo.

### Requisitos de interfaz
- Tablero principal con tabla o tarjetas de tickets ordenados por urgencia de SLA.
- Panel de detalle de ticket seleccionado con historial de notas y acciones.
- Indicador visual prominente de la cuenta regresiva del SLA del ticket activo.

### Datos
- Ticket: id, folio, titulo, prioridad, categoria, estado, tecnico_id, fecha_creacion, fecha_limite_sla, fecha_resolucion, sla_cumplido.

### Estado
- Cola de tickets en memoria con tiempos restantes actualizados dinámicamente.
- Ticket en inspección activa.

### Persistencia
Base de datos relacional SQLite (`datos/helpdesk.db`).

### Validaciones
- Título y descripción obligatorios.
- No permitir resolver un ticket sin registrar la nota técnica de resolución.

### Casos límite
- Tickets creados fuera del horario laboral o en fin de semana (computar SLA continuo o de horario laboral según diseño).
- Resolver un ticket exactamente en el minuto límite del SLA.

### Manejo de errores
- Manejar la persistencia de cambios de estado y notas asegurando integridad transaccional.

### Fundamentos de Python relacionados
- Aritmética de fechas y cálculo de deltas de tiempo (`datetime.timedelta`).
- Modelado de acuerdos de servicio y métricas porcentuales.

### Conceptos Tkinter relacionados
- Uso coordinado de `.after()` para refrescar cuentas regresivas en tiempo real sin saturar la GUI.
- Tags dinámicos en `ttk.Treeview` según tiempos calculados en memoria.

### Herramientas para investigar
- Concepto de SLA (Service Level Agreement) y mejores prácticas ITIL en mesas de ayuda.
- Manejo de diferencias temporales en Python.

### Diseño de interfaz
El estudiante diseña la jerarquía visual priorizando la atención de los tickets más próximos a vencer.

### Diseño de variables
Nombres profesionales en toda la base de código del proyecto.

### Antes de programar
1. ¿Cómo calcularás la fecha límite exacta sumando horas de SLA a la fecha de creación con `datetime`?
2. ¿Cómo diseñarás el callback con `after()` para refrescar el tiempo restante en pantalla cada 60 segundos sin reconstruir toda la tabla?

### Arquitectura
Arquitectura modular profesional en tres capas con repositorio de datos SQLite desacoplado.

### Pruebas mínimas
1. Crear ticket con prioridad Crítica (2h) -> La cuenta regresiva debe iniciar en ~02:00:00 y marcarse en verde.
2. Resolver el ticket antes del vencimiento -> Debe registrarse formalmente con `sla_cumplido = 1` en la base de datos.

### Pruebas de error
1. Simular un ticket con fecha límite en el pasado -> Debe marcarse inmediatamente como 'SLA Incumplido' en rojo.

### Experiencia de usuario
Experiencia de sala de control ágil, clara y que minimice el estrés operativo del analista de soporte.

### Explicación posterior
El estudiante debe explicar cómo estructuró el cálculo dinámico de tiempos restantes y cómo garantizó que el refresco periódico no congelara la ventana.

### Aplicación profesional
Mesas de ayuda corporativas (Service Desk), soporte técnico de operadores de telecomunicaciones y centros de atención a clientes con garantías contractuales.

### Reto adicional
Añade un filtro para excluir sábados y domingos del cómputo de horas de SLA si la prioridad del ticket es 'Baja' o 'Media'.

---
> [Índice General](../README.md) · [← Ejercicio 097](../ejercicio_097/README.md) · [Ejercicio 099 →](../ejercicio_099/README.md)
