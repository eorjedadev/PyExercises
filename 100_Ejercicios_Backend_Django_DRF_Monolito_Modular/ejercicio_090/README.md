# Ejercicio 090 — Refactorización Arquitectónica Mayor: Desacoplamiento con Eventos de Dominio Internos

[← Ejercicio 089](../ejercicio_089/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 091 →](../ejercicio_091/README.md)

---

### Contexto de negocio

El servicio `create_order` en `apps/orders` se ha vuelto un orquestador sobrecargado: llama directamente a inventario, cupones, facturación, notificaciones, auditoría y analítica. Cada vez que un nuevo módulo necesita reaccionar a una orden creada, se debe modificar el código de `orders/services.py`, violando el principio Abierto/Cerrado (Open/Closed Principle). Se requiere implementar un Bus de Eventos de Dominio Interno (Internal Domain Events Dispatcher) en memoria.

### Estado actual del sistema

Acoplamiento de servicios directos en el flujo de órdenes.

### Nueva necesidad

Diseñar un despachador de eventos de dominio ligero en `apps/core/events.py`, definir el evento inmutable `OrderCreatedEvent` y hacer que los módulos (`inventory`, `notifications`, `audit`) se suscriban como escuchadores (Listeners / Handlers) desacoplados.

### Objetivo

Implementar Arquitectura Dirigida por Eventos (EDA - Event-Driven Architecture) interna dentro del Monolito Modular, logrando que los módulos reaccionen a cambios de estado del negocio sin que el módulo emisor conozca a sus suscriptores.

### Actor

Sistema de Dominio ejecutando procesos internos de dominio o tareas programadas de fondo.

### Módulo responsable

`apps/core` (Event Bus) y todos los módulos suscriptores

### Entidades involucradas

`DomainEvent` (Base Dataclass), `OrderCreatedEvent`, `EventDispatcher`, handlers en `apps/inventory`, `apps/notifications`, `apps/audit`.

### Reglas de negocio

1. Un Evento de Dominio es un objeto inmutable que representa un hecho que ya ocurrió en el negocio (nombre en pasado: `OrderCreatedEvent`, `PaymentCapturedEvent`).
2. El módulo `apps/orders` solo emite el evento: `events.dispatch(OrderCreatedEvent(order_id=..., customer_id=...))` y NO importa ni conoce qué módulos lo están escuchando.
3. Los módulos interesados (`notifications`, `audit`) registran sus handlers de forma declarativa.
4. Los eventos transaccionales deben despacharse tras la confirmación de la base de datos (`transaction.on_commit`).
5. Si un handler secundario (ej. analítica) falla, no debe romper la operación principal del usuario.

### Contrato esperado

Flujo de creación de orden completamente desacoplado donde nuevos módulos pueden suscribirse sin tocar una sola línea de código de `apps/orders`.

### Persistencia

Persistencia en cada módulo según su responsabilidad.

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Validación de tipos en los payloads de eventos.

### Transacciones

Coordinación con `transaction.on_commit` para eventos con efectos secundarios externos.

### Casos límite

Múltiples suscriptores para el mismo evento ejecutándose en orden determinista.

### Casos de error

Manejo resiliente de excepciones en handlers individuales para evitar caídas en cascada.

### Consideraciones de seguridad

Garantizar que los eventos no contengan datos sensibles no autorizados.

### Consideraciones de rendimiento

Despacho en memoria ultrarrápido en Python (microsegundos).

### Fundamentos de Python relacionados

Patrón Observer / PubSub en Python, dataclasses inmutables (`@dataclass(frozen=True)`), tipado con `Generic`.

### Conceptos Django relacionados

Alternativa limpia y tipada frente a los Django Signals implícitos.

### Conceptos DRF relacionados

Diseño de contratos REST con `serializers.Serializer` / `ModelSerializer`, vistas delegadoras `APIView` o `GenericAPIView`, normalización de respuestas JSON y documentación declarativa con `@extend_schema`.

### PostgreSQL

Alineación con el motor relacional PostgreSQL 16: tipos de datos nativos (`UUID`, `NUMERIC`, `TIMESTAMPTZ`, `JSONB`), índices B-Tree compuestos y garantías transaccionales ACID en nivel de aislamiento `READ COMMITTED`.

### Arquitectura

Monolito Modular con Event-Driven Architecture interna (Bajo Acoplamiento Extremo y Principio Open/Closed cumplido).

### Dependencias entre módulos

`apps/orders` solo depende de `apps/core/events.py`. Los demás módulos dependen del evento público `OrderCreatedEvent`.

### Antes de programar

1. ¿Por qué el patrón de Eventos de Dominio explícitos es muy superior a las 'Django Signals' desordenadas (que introducen dependencias invisibles, difíciles de rastrear y depurar)?
2. ¿Cómo permite este patrón agregar un nuevo módulo de 'Puntos de Fidelización' en el futuro sin modificar ni una sola línea de código del módulo de pedidos?

### Pruebas mínimas

1. Emitir un `OrderCreatedEvent` en una prueba unitaria y verificar que todos los handlers registrados (notificaciones, inventario, auditoría) sean invocados con los parámetros exactos.
2. Verificar que `apps/orders/services.py` ya no contenga imports de `apps.notifications` ni `apps.audit`.

### Pruebas negativas

1. Simular una excepción en el handler de notificaciones y verificar que la creación de la orden se complete con éxito sin abortar el proceso.

### Documentación

Documentar el catálogo de eventos de dominio del sistema y la guía para registrar nuevos suscriptores en `MAPA_ARQUITECTURA.md`.

### Explicación posterior

Explica cómo los Eventos de Dominio dentro del Monolito Modular preparan a la aplicación para una eventual separación a microservicios en el futuro (si alguna vez fuera necesario) simplemente cambiando el despachador en memoria por RabbitMQ o Kafka, sin reescribir la lógica del dominio.

### Aplicación profesional

Arquitectura de software empresarial, Domain-Driven Design (DDD), sistemas financieros y plataformas escalables de alto desacoplamiento.

### Reto adicional

Implementar un despachador asíncrono que ejecute automáticamente los handlers no críticos en hilos secundarios o tareas en background.
