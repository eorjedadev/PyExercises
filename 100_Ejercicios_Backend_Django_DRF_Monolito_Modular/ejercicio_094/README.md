# Ejercicio 094 — Desafío de Dominio: Gestión de Flotas y Logística de Envíos en Rutas Multiparada

[← Ejercicio 093](../ejercicio_093/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 095 →](../ejercicio_095/README.md)

---

### Contexto de negocio

Una empresa de transporte logístico gestiona una flota de camiones y camionetas de reparto. Cada vehículo tiene una capacidad máxima de peso (kg) y volumen (m3). Un viaje logístico (`DeliveryRoute`) agrupa múltiples entregas (`DeliveryStop`) ordenadas por secuencia de parada (Parada 1 -> Parada 2 -> ... -> Parada N). El backend debe validar que la carga total de paquetes asignada no supere la capacidad del vehículo y registrar el progreso de cada parada con geolocalización y firmas de entrega.

### Estado actual del sistema

Monolito modular con módulos de órdenes, catálogo y clientes.

### Nueva necesidad

Diseñar de forma autónoma el módulo de gestión de flotas y rutas (`apps/fleet`), modelando vehículos, conductores, rutas multiparada y paradas de entrega con control de capacidad máxima y trazabilidad en tiempo real.

### Objetivo

Diseñar un sistema de logística avanzada y gestión de flotas en Django/DRF, controlando restricciones de peso/volumen e implementando el ciclo de vida de rutas multiparada.

### Actor

Planificador Logístico / Conductor de Reparto

### Módulo responsable

Determinación autónoma por el practicante (`apps/fleet`)

### Entidades involucradas

El practicante debe modelar las entidades necesarias (`Vehicle`, `Driver`, `DeliveryRoute`, `DeliveryStop`, `StopProofOfDelivery`).

### Reglas de negocio

1. Un vehículo tiene `max_weight_kg` y `max_volume_m3` inmutables.
2. Al planificar una ruta (`DeliveryRoute`), la suma del peso y volumen de todas las paradas no puede exceder la capacidad del vehículo asignado.
3. Cada parada tiene un número de secuencia entero (`sequence_order`: 1, 2, 3...) y coordenadas de destino.
4. El conductor debe completar las paradas en orden: al entregar en una parada (`POST .../complete/`), se registra la firma digital o foto de entrega y se actualiza el estado de la orden asociada a `DELIVERED`.
5. Los estados de la ruta son: `PLANNED`, `IN_PROGRESS`, `COMPLETED`, `ABORTED`.

### Contrato esperado

El practicante debe diseñar los endpoints REST:
- `POST /api/v1/fleet/routes/` (Crear ruta y asignar paradas con validación de capacidad)
- `POST /api/v1/fleet/routes/{id}/start/` (Iniciar recorrido)
- `POST /api/v1/fleet/stops/{id}/complete/` (Confirmar entrega en parada)

### Persistencia

Tablas relacionales en PostgreSQL con restricciones `CHECK (current_weight <= max_weight)`.

### Relaciones

Vehículos, Conductores, Rutas, Paradas y Envíos.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Planificadores asignan rutas; conductores solo pueden actualizar paradas de sus rutas asignadas.

### Validaciones

Validación matemática de suma de pesos y volúmenes contra capacidad del vehículo.

### Transacciones

Transacción atómica al crear la ruta y sus paradas.

### Casos límite

El conductor intenta saltarse una parada obligatoria o registrar una entrega como fallida (motivo: 'Dirección no encontrada').

### Casos de error

`400 Bad Request` si la carga total excede la capacidad del vehículo.

### Consideraciones de seguridad

Verificación de permisos de conductor sobre su ruta asignada.

### Consideraciones de rendimiento

Índices sobre `(route_id, sequence_order)` para consultas ordenadas de paradas.

### Fundamentos de Python relacionados

Cálculo de sumatorias de atributos de objetos y validaciones complejas de agregación.

### Conceptos Django relacionados

`models.CheckConstraint`, `models.UniqueConstraint(fields=['route', 'sequence_order'])`.

### Conceptos DRF relacionados

Serializadores anidados con validación cruzada entre capacidad del vehículo y suma de ítems.

### PostgreSQL

`CREATE TABLE fleet_deliveryroute (id UUID PRIMARY KEY, vehicle_id UUID NOT NULL, driver_id UUID NOT NULL, ...);`.

### Arquitectura

`apps/fleet` como módulo logístico avanzado en el monolito.

### Dependencias entre módulos

`apps/fleet` interactúa con `apps/orders` y `apps/shipping`.

### Antes de programar

1. ¿Cómo se valida en el backend que la suma de peso de 10 paquetes diferentes no sobrepase los 1,500 kg de un camión antes de confirmar la ruta?
2. ¿Por qué el `UniqueConstraint(fields=['route', 'sequence_order'])` garantiza que no existan dos paradas con el mismo número de orden en una ruta?

### Pruebas mínimas

1. Asignar 3 paradas con peso total 800 kg a un vehículo de 1000 kg -> Creación exitosa de la ruta con status `PLANNED`.
2. Iniciar la ruta y completar la parada 1 -> Verificar que la parada quede `DELIVERED` y la ruta continúe `IN_PROGRESS`.
3. Completar todas las paradas -> Verificar que la ruta pase automáticamente a `COMPLETED`.

### Pruebas negativas

1. Intentar asignar 1200 kg a un vehículo de 1000 kg -> Verificar rechazo `400 Bad Request` por exceso de capacidad.

### Documentación

Documentar el flujo de gestión de flotas y entregas multiparada en `docs/FLEET_MANAGEMENT.md`.

### Explicación posterior

Explica el modelado de problemas de ruteo de vehículos (VRP - Vehicle Routing Problem) a nivel de backend y la sincronización con el estado de las órdenes del cliente.

### Aplicación profesional

Empresas de logística y transporte (FedEx, DHL), plataformas de distribución urbana y flotas de última milla.

### Reto adicional

Calcular el porcentaje de utilización de capacidad del camión (`capacity_utilization_percentage`) como campo calculado de la ruta.
