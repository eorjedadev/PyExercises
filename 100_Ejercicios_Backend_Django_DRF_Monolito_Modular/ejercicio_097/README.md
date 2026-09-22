# Ejercicio 097 — Desafío de Dominio: Alquiler de Propiedades/Vehículos con Depósito en Custodia (Escrow)

[← Ejercicio 096](../ejercicio_096/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 098 →](../ejercicio_098/README.md)

---

### Contexto de negocio

Una plataforma de alquiler de vehículos y propiedades vacacionales (tipo Airbnb / Turo) gestiona reservas por días. El flujo exige: 1) Bloquear las fechas en el calendario sin solapamiento. 2) Retener un Depósito de Garantía (Security Deposit / Escrow) en la tarjeta del cliente durante el periodo de alquiler. 3) Al finalizar el alquiler, un inspector registra el informe de entrega/devolución con kilometraje y daños. Si no hay daños, el depósito en garantía se libera automáticamente; si hay daños, se descuenta el costo de reparación y se devuelve el remanente.

### Estado actual del sistema

Monolito modular con pagos, usuarios y notificaciones.

### Nueva necesidad

Diseñar de forma autónoma el módulo de alquileres (`apps/rentals`), modelando recursos alquilables (`RentalAsset`), reservas con calendario (`RentalBooking`), depósitos en custodia (`EscrowDeposit`) e informes de inspección (`InspectionReport`).

### Objetivo

Diseñar un sistema de reservas de alquiler y retención de depósitos en garantía (Escrow), implementando bloqueos temporales, autorizaciones previas de pago y liquidaciones basadas en inspecciones.

### Actor

Arrendatario (Cliente) / Propietario / Inspector de Devolución

### Módulo responsable

Determinación autónoma por el practicante (`apps/rentals`)

### Entidades involucradas

El practicante debe modelar las entidades necesarias (`RentalAsset`, `RentalBooking`, `EscrowDeposit`, `InspectionReport`).

### Reglas de negocio

1. Las reservas se definen por rango de fechas `[check_in_date, check_out_date]` y no pueden solaparse para el mismo recurso.
2. El pago se compone del costo de alquiler + el monto de garantía en custodia (`escrow_amount`).
3. El depósito de garantía permanece en estado `HELD` durante todo el alquiler.
4. Al devolver el vehículo/propiedad, el inspector completa el `InspectionReport`. Si `damage_detected = False`, el depósito pasa a `RELEASED` y se desbloquea el dinero.
5. Si hay daños (`damage_detected = True`), se cobra el monto de reparación (`claimed_amount`) y se reembolsa el sobrante.

### Contrato esperado

El practicante debe diseñar los endpoints REST:
- `POST /api/v1/rentals/bookings/` (Crear reserva con retención de garantía)
- `POST /api/v1/rentals/bookings/{id}/inspect/` (Registrar inspección de devolución y liquidar garantía)
- `GET /api/v1/rentals/assets/{id}/availability/` (Consultar calendario de disponibilidad)

### Persistencia

Tablas relacionales en PostgreSQL con exclusión de fechas solapadas.

### Relaciones

Recursos, Reservas, Depósitos en Custodia e Inspecciones.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Cliente gestiona su reserva; inspectores autorizados registran informes de daños.

### Validaciones

Validar que `check_out_date > check_in_date` y que el recurso esté disponible.

### Transacciones

Transacciones atómicas en la creación de la reserva y en la liquidación del depósito.

### Casos límite

El monto de daños declarados por el inspector es mayor al monto total de la garantía (se captura el 100% de la garantía y se genera una deuda por el saldo restante).

### Casos de error

`409 Conflict` si las fechas seleccionadas ya están ocupadas por otra reserva.

### Consideraciones de seguridad

Protección contra fraudes en la retención y liberación de fondos en custodia.

### Consideraciones de rendimiento

Índices de fechas para consultas de disponibilidad de calendario.

### Fundamentos de Python relacionados

Cálculo de tarifas por día (`(check_out - check_in).days * daily_rate`).

### Conceptos Django relacionados

Exclusión de rangos de fechas, integración con servicios de pago.

### Conceptos DRF relacionados

Serializadores de reservas complejas e inspecciones.

### PostgreSQL

`CREATE TABLE rentals_rentalbooking (id UUID PRIMARY KEY, asset_id UUID NOT NULL, check_in DATE NOT NULL, check_out DATE NOT NULL, ...);`.

### Arquitectura

`apps/rentals` como módulo de reservas y alquileres en el monolito.

### Dependencias entre módulos

`apps/rentals` interactúa con `apps/payments` y `apps/notifications`.

### Antes de programar

1. ¿Cómo funciona la retención de depósitos (Pre-Authorization / Hold) en pasarelas de pago y por qué es diferente a un cobro definitivo?
2. ¿Cómo se diseñan las tablas para registrar el estado del vehículo antes de la entrega (Check-in) y después de la devolución (Check-out)?

### Pruebas mínimas

1. Crear una reserva de 5 días con $200 de depósito de garantía -> Verificar que el depósito quede en estado `HELD`.
2. Registrar una inspección sin daños -> Verificar que el depósito pase a `RELEASED` y se liberen los $200.
3. Probar una reserva con daños de $50 -> Verificar que se capturen $50 y se reembolsen $150.

### Pruebas negativas

1. Intentar reservar un vehículo en fechas que se solapen con una reserva existente confirmada -> Verificar rechazo `409 Conflict`.

### Documentación

Documentar el flujo de custodia (Escrow) y el protocolo de inspección en `docs/RENTALS_DOMAIN.md`.

### Explicación posterior

Explica el patrón Escrow (Custodia de Fondos) en plataformas peer-to-peer y cómo coordinar la autorización previa de pagos con inspecciones físicas en el mundo real.

### Aplicación profesional

Plataformas de alquiler de autos (Hertz, Turo), alquiler vacacional (Airbnb), arriendo de maquinaria pesada y depósitos de garantía inmobiliarios.

### Reto adicional

Implementar penalizaciones automáticas por entrega tardía (Late Return Fee) calculadas por hora de retraso.
