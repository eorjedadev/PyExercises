# Ejercicio 081 — Sistema Multisede / Sucursales (apps/branches) y Stock Distribuido

[← Ejercicio 080](../ejercicio_080/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 082 →](../ejercicio_082/README.md)

---

### Contexto de negocio

La empresa pasa de operar en una sola bodega central a un modelo de negocio omnicanal con múltiples sucursales físicas y almacenes regionales (ej. 'Sucursal Centro', 'Almacén Norte', 'Tienda Miraflores'). El inventario ya no es global; cada sucursal tiene su propio stock físico independiente para cada producto. El backend debe soportar gestión multisede y asignación inteligente de pedidos por cercanía.

### Estado actual del sistema

Módulo de inventario con stock centralizado. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Crear el módulo `apps/branches`, modelar `Branch` (con coordenadas GPS `latitude`/`longitude` y dirección) y evolucionar el modelo de inventario a `BranchStockItem` en `apps/inventory`, permitiendo consultar stock distribuido por sede.

### Objetivo

Evolucionar la arquitectura de inventario de un modelo monosede a un modelo multisede distribuido, gestionando existencias por ubicación y calculando distancias geográficas para despacho.

### Actor

Operador de Tienda / Cliente que consulta stock en tienda

### Módulo responsable

`apps/branches` y `apps/inventory` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Branch` (`id` UUID, `name`, `code`, `address`, `latitude`, `longitude`, `is_active`), `BranchStockItem` (`id` UUID, `branch` FK, `product_id` UUID, `quantity_on_hand`, `quantity_reserved`), selector `get_stock_by_branch`.

### Reglas de negocio

1. Cada sucursal tiene un código único alfanumérico (ej. `BR-CENTRO-01`).
2. El inventario de un producto se desglosa por sucursal (`BranchStockItem`).
3. La suma del stock disponible de todas las sucursales representa el stock global de la empresa.
4. El cliente puede consultar la disponibilidad de un producto en todas las sucursales activas mediante `GET /api/v1/branches/stock/?product_id=UUID`.

### Contrato esperado

Consultar Disponibilidad Multisede:
- `GET /api/v1/branches/stock/?product_id=uuid-prod-1`
  Response: `200 OK`
  ```json
  [
    {
      "branch_id": "uuid-branch-1",
      "branch_name": "Sucursal Centro",
      "address": "Av. Principal 123",
      "available_stock": 15
    },
    {
      "branch_id": "uuid-branch-2",
      "branch_name": "Almacén Norte",
      "address": "Parque Industrial Lote 8",
      "available_stock": 0
    }
  ]
  ```

### Persistencia

Tablas `branches_branch` e `inventory_branchstockitem` en PostgreSQL con restricción única `(branch_id, product_id)`.

### Relaciones

`BranchStockItem.branch` -> `ForeignKey(Branch, on_delete=models.PROTECT)`.

### Autenticación

Público para consulta de stock por tienda; `IsAuthenticated` para gestión.

### Autorización

Control de acceso basado en roles (RBAC). Requiere que el usuario autenticado cuente con permisos administrativos (`IsAdminUser` o `HasRole(['ADMIN', 'MANAGER'])`).

### Validaciones

Validar coordenadas de latitud (-90 a +90) y longitud (-180 a +180).

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Consultar disponibilidad de un producto que nunca ha sido asignado a una sucursal (debe retornar 0 existencias limpiamente).

### Casos de error

`404 Not Found` si el producto no existe en el catálogo.

### Consideraciones de seguridad

Protección de endpoints de ajuste de stock por sucursal según el rol del operador asignado a esa sede.

### Consideraciones de rendimiento

Índice compuesto en PostgreSQL sobre `(product_id, branch_id)`.

### Fundamentos de Python relacionados

Fórmula de Haversine para cálculo de distancia entre coordenadas geográficas.

### Conceptos Django relacionados

`models.UniqueConstraint(fields=['branch', 'product_id'])`, migraciones de datos para asignar el stock previo a la sucursal central.

### Conceptos DRF relacionados

Diseño de contratos REST con `serializers.Serializer` / `ModelSerializer`, vistas delegadoras `APIView` o `GenericAPIView`, normalización de respuestas JSON y documentación declarativa con `@extend_schema`.

### PostgreSQL

`CREATE TABLE branches_branch (id UUID PRIMARY KEY, name VARCHAR(100) NOT NULL, latitude NUMERIC(9,6), longitude NUMERIC(9,6), ...);`.

### Arquitectura

`apps/branches` define la entidad geográfica/organizacional; `apps/inventory` gestiona el stock físico asignado.

### Dependencias entre módulos

`apps.inventory` referencia `apps.branches.models.Branch` mediante clave foránea.

### Antes de programar

1. ¿Cómo evoluciona una base de datos de producción de inventario centralizado a inventario multisede mediante una migración de datos con `RunPython` sin perder los datos históricos?
2. ¿Por qué es vital el constraint `UniqueConstraint(fields=['branch', 'product_id'])` para evitar filas duplicadas de stock en la misma tienda?

### Pruebas mínimas

1. Crear 2 sucursales (Sede A y Sede B), asignar 10 unidades del producto a Sede A y 5 a Sede B -> Verificar que el endpoint de stock por sucursal devuelva las cantidades exactas por sede.
2. Verificar que el total consolidado sea 15.

### Pruebas negativas

1. Intentar registrar dos veces el mismo producto en la misma sucursal -> Verificar que PostgreSQL lance `IntegrityError` por el UniqueConstraint.

### Documentación

Documentar el modelo de datos multisede y la migración de inventario en `MAPA_ARQUITECTURA.md`.

### Explicación posterior

Explica el desafío arquitectónico de la evolución de dominios: cómo pasar de un modelo 1 a 1 a un modelo 1 a N sin romper el código cliente existente mediante la actualización de los selectores centrales.

### Aplicación profesional

Sistemas de retail omnicanal, cadenas de farmacias, supermercados, bodegas distribuidas y click-and-collect (retiro en tienda).

### Reto adicional

Implementar un selector que ordene las sucursales con stock disponible de menor a mayor distancia respecto a las coordenadas GPS del cliente.
