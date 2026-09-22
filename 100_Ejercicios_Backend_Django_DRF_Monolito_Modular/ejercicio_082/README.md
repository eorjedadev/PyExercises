# Ejercicio 082 — Transferencias de Inventario entre Sucursales con Trazabilidad y Confirmación

[← Ejercicio 081](../ejercicio_081/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 083 →](../ejercicio_083/README.md)

---

### Contexto de negocio

Cuando la Sede A tiene exceso de stock de un producto y la Sede B se queda sin existencias, los operadores deben coordinar una Transferencia de Inventario entre Sucursales (`StockTransfer`). El stock no puede teletransportarse instantáneamente: 1) Se descuenta de Sede A y entra en estado `IN_TRANSIT` (no disponible para la venta en ninguna sede mientras viaja en el camión). 2) Cuando el camión llega a Sede B, el operador de destino confirma la recepción física y el stock se suma a Sede B.

### Estado actual del sistema

Módulo de sucursales e inventario multisede operativos.

### Nueva necesidad

Crear el modelo `StockTransfer` y `StockTransferItem` en `apps/inventory`, modelando el ciclo de vida `INITIATED` -> `IN_TRANSIT` -> `RECEIVED` (o `CANCELLED`), con endpoints para iniciar despacho y confirmar recepción en destino.

### Objetivo

Dominar el modelado de transferencias físicas de inventario en tránsito, aplicando transacciones atómicas dobles (origen y destino) y garantizando la trazabilidad total de mercancías.

### Actor

Operador de Sede Origen (Despachador) / Operador de Sede Destino (Receptor)

### Módulo responsable

`apps/inventory` colaborando con `apps/branches`

### Entidades involucradas

`StockTransfer` (`id` UUID, `transfer_number`, `source_branch` FK, `target_branch` FK, `status`, `shipped_at`, `received_at`), `StockTransferItem` (`id` UUID, `transfer` FK, `product_id` UUID, `quantity`), servicios `initiate_transfer`, `confirm_transfer_receipt`.

### Reglas de negocio

1. La sucursal de origen y destino no pueden ser la misma (`CheckConstraint(source_branch != target_branch)`).
2. Al despachar la transferencia (`INITIATED` -> `IN_TRANSIT`), se descuenta inmediatamente el stock físico de `source_branch` y se registra el movimiento `TRANSFER_OUT`.
3. Mientras está en tránsito, el stock NO está disponible para venta en ninguna de las dos sucursales.
4. Al confirmar la recepción en destino (`RECEIVED`), se suma el stock a `target_branch` y se registra el movimiento `TRANSFER_IN`.

### Contrato esperado

1. Despachar Transferencia (Sede Origen):
- `POST /api/v1/inventory/transfers/`
  Body: `{"source_branch_id": "uuid-sede-a", "target_branch_id": "uuid-sede-b", "items": [{"product_id": "uuid-prod", "quantity": 10}]}`
  Response: `201 Created` `{ "status": "IN_TRANSIT", ... }`

2. Confirmar Recepción (Sede Destino):
- `POST /api/v1/inventory/transfers/{id}/receive/`
  Response: `200 OK` `{ "status": "RECEIVED", "received_at": "2026-09-22T21:00:00Z" }`

### Persistencia

Tablas `inventory_stocktransfer`, `inventory_stocktransferitem` y movimientos `inventory_stockmovement` en PostgreSQL.

### Relaciones

`StockTransfer.source_branch` y `target_branch` -> `ForeignKey('branches.Branch')`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso basado en roles (RBAC). Requiere que el usuario autenticado cuente con permisos administrativos (`IsAdminUser` o `HasRole(['ADMIN', 'MANAGER'])`).

### Validaciones

Validar que la sede de origen tenga stock suficiente para transferir.

### Transacciones

Transacción atómica en el despacho y transacción atómica en la recepción.

### Casos límite

Cancelar una transferencia antes de que salga (`INITIATED` -> `CANCELLED`: el stock reservado en origen se devuelve a disponible).

### Casos de error

`400 Bad Request` si la sede origen no tiene suficiente stock o si origen y destino son idénticos.

### Consideraciones de seguridad

Trazabilidad inmutable de quién inició y quién recibió la mercancía.

### Consideraciones de rendimiento

Uso de `select_for_update()` en los registros de stock de ambas sucursales para evitar inconsistencias concurrentes.

### Fundamentos de Python relacionados

Modelado de flujos en dos fases (Two-Phase Commit conceptual a nivel de negocio).

### Conceptos Django relacionados

Restricciones `CheckConstraint(check=~Q(source_branch=models.F('target_branch')))`.

### Conceptos DRF relacionados

Endpoints de acción para confirmación de recepción.

### PostgreSQL

`ALTER TABLE inventory_stocktransfer ADD CONSTRAINT check_different_branches CHECK (source_branch_id <> target_branch_id);`.

### Arquitectura

`apps/inventory` gobierna las transferencias de existencias entre las entidades provistas por `apps/branches`.

### Dependencias entre módulos

`apps/inventory` depende de `apps/branches`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué el stock en tránsito NO debe sumarse a la sede destino hasta que el operador receptor confirme físicamente la llegada?
2. ¿Cómo protege el constraint `source_branch_id <> target_branch_id` contra errores humanos en la selección de sucursales?

### Pruebas mínimas

1. Sede A tiene 20 unidades, Sede B tiene 0. Iniciar transferencia de 10 unidades de A a B -> Verificar que Sede A quede en 10, Sede B en 0 y la transferencia en `IN_TRANSIT`.
2. Confirmar recepción en destino -> Verificar que Sede B quede en 10 unidades y la transferencia en `RECEIVED`.

### Pruebas negativas

1. Intentar crear una transferencia donde la sede de origen sea igual a la de destino -> Verificar que falle la validación / constraint de DB.

### Documentación

Documentar el flujo de transferencias entre almacenes en el manual de inventario.

### Explicación posterior

Explica el concepto de 'Inventario en Tránsito' en logística y cómo los sistemas ERP (SAP, Oracle) garantizan que ningún producto desaparezca del balance contable mientras viaja entre almacenes.

### Aplicación profesional

Logística de distribución de mercancías, reaprovisionamiento de tiendas, cadenas de farmacias y almacenes centrales.

### Reto adicional

Implementar recepción parcial con registro de mermas o artículos dañados durante el transporte.
