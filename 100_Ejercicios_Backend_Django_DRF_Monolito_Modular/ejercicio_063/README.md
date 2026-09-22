# Ejercicio 063 — Consultas Agregadas, Anotaciones y Subqueries con el ORM

[← Ejercicio 062](../ejercicio_062/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 064 →](../ejercicio_064/README.md)

---

### Contexto de negocio

La gerencia comercial requiere un endpoint de estadísticas de clientes (`GET /api/v1/customers/stats/`) que devuelva cada cliente junto con métricas calculadas en tiempo real: total de pedidos completados, monto total gastado históricamente (Customer Lifetime Value - LTV), fecha del último pedido y si tiene pedidos pendientes de pago (`has_pending_orders`). Calcular esto en Python iterando en bucles sería ineficiente y consumiría gigabytes de RAM; debe ser calculado directamente por el motor de PostgreSQL.

### Estado actual del sistema

Módulos de clientes y órdenes operativos. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Diseñar una consulta en `apps/customers/selectors.py` utilizando `annotate()`, `Count()`, `Sum()`, `Max()`, `Subquery()`, `OuterRef()` y `Exists()` para calcular todas las métricas en una única consulta SQL analítica en PostgreSQL.

### Objetivo

Dominar las capacidades analíticas avanzadas del ORM de Django (`annotate`, `aggregate`, `Coalesce`, `Subquery`, `Exists`), delegando cálculos matemáticos y agrupaciones al motor relacional de PostgreSQL.

### Actor

Gerente Comercial / Administrador con permisos administrativos y credenciales de acceso seguras.

### Módulo responsable

`apps/customers` y `apps/orders` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`CustomerProfile`, `Order`, `Count`, `Sum`, `Max`, `Subquery`, `Exists`, `OuterRef`, `Coalesce`.

### Reglas de negocio

1. `total_orders`: Conteo de órdenes del cliente en cualquier estado.
2. `total_spent`: Suma de `total_amount` únicamente de órdenes con estado `PAID` o `DELIVERED`. Si el cliente no tiene compras, debe devolver `0.00` (usando `Coalesce` para evitar `null`).
3. `last_order_date`: Fecha máxima (`Max`) de creación de sus pedidos.
4. `has_pending_orders`: Booleano calculado mediante `Exists(Order.objects.filter(customer=OuterRef('pk'), status='PENDING'))`.

### Contrato esperado

Estadísticas de Clientes:
- `GET /api/v1/customers/stats/`
  Response: `200 OK`
  ```json
  [
    {
      "id": "uuid-cliente-1",
      "email": "carlos@empresa.com",
      "total_orders": 12,
      "total_spent": "1450.50",
      "last_order_date": "2026-09-20T14:30:00Z",
      "has_pending_orders": true
    }
  ]
  ```

### Persistencia

Consulta analítica única en PostgreSQL con cláusulas `LEFT JOIN`, `GROUP BY`, `COALESCE(SUM(...), 0)` y subqueries correlacionadas.

### Relaciones

`CustomerProfile` y `Order`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Clientes registrados que nunca han realizado ningún pedido (deben devolver `total_orders: 0`, `total_spent: "0.00"`, `last_order_date: null`, `has_pending_orders: false`).

### Casos de error

`403 Forbidden` a usuarios sin privilegios administrativos.

### Consideraciones de seguridad

Protección de datos agregados comerciales. Prevención de vulnerabilidades OWASP API Top 10: validación estricta contra Mass Assignment, control de Ownership para evitar BOLA/IDOR y parametrización de consultas contra SQLi.

### Consideraciones de rendimiento

Asegurar índices en PostgreSQL sobre `orders_order(customer_id, status)` para que el `GROUP BY` y los filtros sean instantáneos.

### Fundamentos de Python relacionados

Manejo de expresiones complejas y tipos numéricos.

### Conceptos Django relacionados

`django.db.models.functions.Coalesce`, `django.db.models.Subquery`, `django.db.models.OuterRef`, `django.db.models.Exists`, `filter` condicional en agregaciones (`filter=Q(orders__status='PAID')`).

### Conceptos DRF relacionados

Serializadores que exponen campos anotados del QuerySet.

### PostgreSQL

`SELECT customer.*, COALESCE(SUM(CASE WHEN orders.status = 'PAID' THEN total_amount ELSE 0 END), 0) AS total_spent, ... GROUP BY customer.id;`.

### Arquitectura

Los selectores analíticos residen en `apps/customers/selectors.py`.

### Dependencias entre módulos

`apps/customers` analiza datos de `apps/orders`.

### Antes de programar

1. ¿Por qué traer todos los pedidos a Python para calcular la suma con un bucle `sum(o.total_amount for o in orders)` es un antipatrón en bases de datos con millones de registros?
2. ¿Cómo funciona `Coalesce` para reemplazar valores `NULL` por `0` cuando una suma en SQL no encuentra filas coincidentes?

### Pruebas mínimas

1. Crear 1 cliente con 2 pedidos pagados ($50 y $30) y 1 pedido cancelado ($20) -> Verificar que `total_spent` sea exactamente `80.00` y `total_orders` sea 3.
2. Crear un cliente sin pedidos y verificar que `total_spent` sea `0.00` y `has_pending_orders` sea `False`.

### Pruebas negativas

1. Verificar que la consulta SQL completa se ejecute en 1 sola consulta sin N+1.

### Documentación

Documentar los campos anotados y su significado comercial en el catálogo de métricas del proyecto.

### Explicación posterior

Explica el funcionamiento de `Subquery` y `OuterRef` en Django y cuándo es preferible una subconsulta correlacionada frente a un `JOIN` con `GROUP BY` masivo.

### Aplicación profesional

Dashboards analíticos, paneles ejecutivos de métricas, reportes de retención de clientes y segmentación de usuarios por valor comercial.

### Reto adicional

Permitir ordenar el endpoint por el campo anotado `?ordering=-total_spent` para identificar inmediatamente a los mejores clientes de la empresa.
