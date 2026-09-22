# Ejercicio 091 — Desafío de Dominio: Sistema de Subastas en Tiempo Real y Cierre Atómico

[← Ejercicio 090](../ejercicio_090/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 092 →](../ejercicio_092/README.md)

---

### Contexto de negocio

Una casa de subastas de arte y artículos de colección necesita digitalizar su operativa. En una subasta en vivo, cientos de usuarios pujan simultáneamente por el mismo lote en los últimos segundos. El backend debe procesar pujas concurrentes garantizando que cada puja supere a la anterior por al menos el incremento mínimo, rechazar pujas tardías o menores, retener el saldo del mejor postor y ejecutar el cierre atómico de la subasta al expirar el tiempo, adjudicando el lote al ganador y liberando los fondos retenidos de los demás.

### Estado actual del sistema

Monolito modular consolidado con usuarios, pagos y auditoría.

### Nueva necesidad

Diseñar desde cero la solución completa para el dominio de subastas (`apps/auctions`), definiendo autónomamente entidades, reglas de concurrencia pesimista, estados de lote, contratos REST y pruebas.

### Objetivo

Demostrar autonomía técnica para modelar un dominio de alta contención y concurrencia (Subastas en tiempo real), aplicando transacciones atómicas, bloqueos en PostgreSQL y cierre automatizado.

### Actor

Pujador Autenticado / Administrador de Subasta / Proceso de Cierre

### Módulo responsable

Determinación autónoma por el practicante (módulo `apps/auctions`)

### Entidades involucradas

El practicante debe identificar y modelar las entidades necesarias (ej. `AuctionItem`, `Bid`, `BidderHold`).

### Reglas de negocio

1. Un lote tiene precio base, incremento mínimo de puja y fecha/hora exacta de inicio y fin.
2. Toda nueva puja debe ser estrictamente mayor a: `puja_actual_mas_alta + incremento_minimo`.
3. Control estricto de concurrencia: si dos usuarios pujan por el mismo monto en el mismo milisegundo, solo la primera debe ser aceptada; la segunda debe rechazarse informando el nuevo monto mínimo.
4. Cierre atómico: al vencer el plazo, el lote pasa a adjudicado (`WON`), se cobra al ganador y se generan los registros contables y notificaciones.
5. Un usuario no puede pujar contra sí mismo si ya tiene la puja más alta.

### Contrato esperado

El practicante debe diseñar el contrato REST formal:
- Endpoint para emitir puja: `POST /api/v1/auctions/{id}/bids/` con validaciones y respuestas estructuradas.
- Endpoint de estado de subasta en tiempo real: `GET /api/v1/auctions/{id}/live/`.

### Persistencia

Tablas en PostgreSQL con restricciones `CHECK` y claves foráneas.

### Relaciones

Relaciones entre usuarios, lotes y ofertas.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

Bloqueo pesimista `select_for_update()` OBLIGATORIO al evaluar y registrar la puja más alta.

### Casos límite

Puja que llega 1 milisegundo después de que la subasta cerró; extensión automática de 2 minutos (Anti-Sniping) si entra una puja en el último minuto.

### Casos de error

`409 Conflict` si la puja fue superada concurrentemente; `400 Bad Request` si la subasta no está activa.

### Consideraciones de seguridad

Garantía de que ningún postor pueda pujar sin fondos o manipular el monto.

### Consideraciones de rendimiento

Uso de índices en PostgreSQL sobre `(auction_id, -amount)` para consultas instantáneas de la mejor oferta.

### Fundamentos de Python relacionados

Control de concurrencia, matemáticas financieras y fechas UTC.

### Conceptos Django relacionados

`select_for_update()`, `transaction.atomic()`, `models.CheckConstraint`.

### Conceptos DRF relacionados

Diseño limpio de serializers y endpoints de acción.

### PostgreSQL

`SELECT * FROM auctions_item WHERE id = ... FOR UPDATE;`.

### Arquitectura

Monolito Modular: `apps/auctions` colaborando con `apps/payments` y `apps/notifications`.

### Dependencias entre módulos

Diseñar dependencias unidireccionales limpias.

### Antes de programar

1. ¿Cómo se previene que dos postores registren la misma oferta de $500 al mismo tiempo?
2. ¿Cómo se implementa la regla anti-sniping (extender el tiempo si hay pujas al final) de forma atómica en PostgreSQL?

### Pruebas mínimas

1. Probar 10 hilos concurrentes intentando pujar sobre un lote y verificar que las ofertas queden estrictamente ordenadas y sin montos duplicados.
2. Probar el cierre de la subasta adjudicando al ganador correcto.

### Pruebas negativas

1. Intentar pujar un monto inferior al incremento mínimo -> Verificar rechazo inmediato.

### Documentación

Documentar el diseño del dominio y el grafo de estados de subasta en el README del módulo.

### Explicación posterior

Justifica tus decisiones de modelado, la estrategia de bloqueo de concurrencia elegida y cómo garantizaste la consistencia financiera del remate.

### Aplicación profesional

Casas de subastas de arte, remates judiciales electrónicos, plataformas de compraventa de vehículos y plataformas de trading.

### Reto adicional

Implementar el sistema de 'Auto-Puja' (Proxy Bidding) donde el usuario define su monto máximo y el sistema puja automáticamente por él en incrementos mínimos.
