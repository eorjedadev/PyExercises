# Ejercicio 093 — Desafío de Dominio: Sistema de Citas Médicas y Quirófanos con Control de Solapamientos

[← Ejercicio 092](../ejercicio_092/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 094 →](../ejercicio_094/README.md)

---

### Contexto de negocio

Una red de clínicas médicas necesita gestionar la programación de consultas médicas y cirugías en quirófanos. El dominio exige una regla de consistencia temporal absoluta: un médico no puede estar en dos citas simultáneas, un paciente no puede tener dos citas solapadas y un quirófano no puede albergar dos cirugías en el mismo horario. El backend debe garantizar que no exista solapamiento temporal (`Time Overlapping Prevention`) utilizando rangos de tiempo nativos de PostgreSQL (`TSRANGE` / `TSTZRANGE`).

### Estado actual del sistema

Monolito modular con usuarios y notificaciones.

### Nueva necesidad

Diseñar de forma autónoma el módulo de agendamiento clínico (`apps/appointments`), modelando médicos, especialidades, salas/quirófanos, citas y agendas, aplicando restricciones de exclusión de rangos temporales en PostgreSQL (`ExclusionConstraint`).

### Objetivo

Dominar el control estricto de intervalos de tiempo y reservas sin solapamiento utilizando tipos de rango nativos de PostgreSQL (`tstzrange`) y `ExclusionConstraint` en Django.

### Actor

Paciente / Recepcionista / Médico Especialista

### Módulo responsable

Determinación autónoma por el practicante (`apps/appointments`)

### Entidades involucradas

El practicante debe modelar las entidades necesarias (`Doctor`, `Specialty`, `Room`, `Appointment`, `DoctorSchedule`).

### Reglas de negocio

1. Una cita médica se define por: médico, paciente, sala/consultorio y rango de tiempo `[start_datetime, end_datetime)`.
2. No se permite solapamiento temporal para el mismo médico (`Doctor + TimeRange`).
3. No se permite solapamiento temporal para la misma sala/quirófano (`Room + TimeRange`).
4. Las citas deben respetar el horario de atención configurado del médico (`DoctorSchedule`).
5. Los estados de una cita son: `SCHEDULED`, `CONFIRMED`, `IN_PROGRESS`, `COMPLETED`, `CANCELLED`, `NO_SHOW`.

### Contrato esperado

El practicante debe diseñar el contrato REST:
- `POST /api/v1/appointments/` (Agendar cita con verificación de disponibilidad)
- `GET /api/v1/appointments/available-slots/?doctor_id=...&date=...` (Consultar huecos libres)
- `POST /api/v1/appointments/{id}/cancel/` (Cancelar con liberación inmediata del slot)

### Persistencia

Tablas en PostgreSQL con extensiones `btree_gist` y restricciones `ExclusionConstraint`.

### Relaciones

Médicos, Especialidades, Pacientes, Consultorios y Citas.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Pacientes gestionan sus citas; médicos gestionan su agenda; recepcionistas gestionan citas generales.

### Validaciones

Validar que `end_datetime > start_datetime` y que la duración mínima sea de 15 minutos.

### Transacciones

Operación atómica obligatoria mediante `transaction.atomic()`. Garantiza que todas las mutaciones en la base de datos se confirmen de forma íntegra o se reviertan totalmente (Rollback) ante fallos.

### Casos límite

Dos pacientes intentan reservar exactamente el mismo turno médico en el mismo segundo (PostgreSQL debe bloquear el solapamiento a nivel de motor físico con `ExclusionConstraint`).

### Casos de error

`409 Conflict` si el médico o la sala ya están ocupados en ese rango horario.

### Consideraciones de seguridad

Protección de datos médicos sensibles (cumplimiento HIPAA / normativas de salud).

### Consideraciones de rendimiento

Índices GiST en PostgreSQL sobre columnas de tipo `tstzrange`.

### Fundamentos de Python relacionados

Manejo avanzado de zonas horarias y rangos de fechas con `datetime` y `zoneinfo`.

### Conceptos Django relacionados

`django.contrib.postgres.constraints.ExclusionConstraint`, `django.contrib.postgres.fields.DateTimeRangeField`, `Op(range='&&')`.

### Conceptos DRF relacionados

Serializadores de validación de disponibilidad horaria.

### PostgreSQL

`CREATE EXTENSION IF NOT EXISTS btree_gist; ALTER TABLE appointments_appointment ADD CONSTRAINT no_doctor_overlap EXCLUDE USING gist (doctor_id WITH =, time_range WITH &&) WHERE (status NOT IN ('CANCELLED'));`.

### Arquitectura

`apps/appointments` como módulo clínico autónomo.

### Dependencias entre módulos

Diseñar integración con `apps/users` y `apps/notifications`.

### Antes de programar

1. ¿Por qué validar solapamientos únicamente con `if Appointment.objects.filter(start__lt=end, end__gt=start).exists()` en Python es vulnerable a condiciones de carrera en reservas simultáneas?
2. ¿Cómo funciona `ExclusionConstraint` con la extensión `btree_gist` en PostgreSQL para garantizar a nivel de motor físico que nunca existan citas solapadas?

### Pruebas mínimas

1. Crear una cita para el Doctor 1 de 10:00 a 10:30 -> Creación exitosa.
2. Intentar agendar otra cita para el Doctor 1 de 10:15 a 10:45 -> Verificar que PostgreSQL rechace el solapamiento y devuelva `409 Conflict`.
3. Probar agendar de 10:30 a 11:00 (contigua, sin solapamiento) -> Creación exitosa.

### Pruebas negativas

1. Intentar agendar una cita con fecha de fin anterior a la fecha de inicio -> Verificar rechazo `400`.

### Documentación

Documentar la configuración de `ExclusionConstraint` y la extensión `btree_gist` en el manual de instalación de PostgreSQL.

### Explicación posterior

Explica el funcionamiento de los tipos de rango (Range Types) y los índices GiST en PostgreSQL para la resolución matemática de solapamientos temporales y espaciales.

### Aplicación profesional

Sistemas de agendamiento médico, reserva de salas de conferencias, alquiler de canchas deportivas y reservas de vuelos.

### Reto adicional

Implementar un selector que devuelva la lista de 'slots libres' de 30 minutos disponibles de un médico para un día específico restando los intervalos ocupados de su horario de trabajo.
