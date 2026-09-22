# Ejercicio 043 — Django Admin Operativo para Gestión de Pedidos e Inventario

[← Ejercicio 042](../ejercicio_042/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 044 →](../ejercicio_044/README.md)

---

### Contexto de negocio

El equipo interno de operaciones y atención al cliente necesita una interfaz administrativa rápida y segura para inspeccionar pedidos, visualizar el historial de líneas de compra, verificar el stock disponible y ejecutar acciones operativas. El Django Admin debe configurarse profesionalmente como panel de control interno, sin confundirlo con la API pública de clientes.

### Estado actual del sistema

Modelos de órdenes, ítems, catálogo e inventario registrados en el sistema.

### Nueva necesidad

Personalizar `apps/orders/admin.py` y `apps/inventory/admin.py` con `ModelAdmin`, `TabularInline` para `OrderItem`, `list_display`, filtros avanzados, búsquedas por número de orden o email, y acciones administrativas personalizadas.

### Objetivo

Dominar la personalización avanzada del Django Admin para uso operativo profesional, protegiendo campos inmutables (`readonly_fields`), optimizando consultas con `list_select_related` y agregando acciones de lote seguras.

### Actor

Operador de Soporte / Administrador de Operaciones

### Módulo responsable

`apps/orders` y `apps/inventory` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`OrderAdmin`, `OrderItemInline`, `StockItemAdmin`, `StockMovementInline`.

### Reglas de negocio

1. En el detalle de una orden en el Admin, los campos financieros (`total_amount`, `subtotal_amount`, `order_number`) y los ítems deben ser de solo lectura para evitar alteraciones manuales de registros contables.
2. La vista de lista de órdenes debe mostrar: `order_number`, `customer_email`, `status`, `total_amount`, `created_at`.
3. Se debe poder buscar órdenes por `order_number` y por el `email` del usuario asociado.
4. Se debe agregar una acción administrativa de lote 'Exportar pedidos seleccionados a CSV'.

### Contrato esperado

Panel accesible en `/admin/` con navegación fluida, filtros por estado y sin consultas lentas.

### Persistencia

Consultas al ORM para renderizado del Django Admin.

### Relaciones

`Order`, `OrderItem`, `CustomerProfile`, `User`, `StockItem`.

### Autenticación

Autenticación de sesión de Django (`is_staff=True`).

### Autorización

Solo usuarios con privilegios de staff/admin.

### Validaciones

Protección contra edición en campos de auditoría y dinero.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Listar 50 órdenes con sus usuarios e ítems (debe usar `list_select_related = ['customer__user']` para evitar N+1 queries al cargar el listado del admin).

### Casos de error

`PermissionDenied` si un usuario no staff intenta acceder a `/admin/`.

### Consideraciones de seguridad

Restringir permisos de edición y eliminación en el Admin para tablas transaccionales.

### Consideraciones de rendimiento

Uso obligatorio de `list_select_related` en todos los `ModelAdmin` que muestren relaciones foráneas.

### Fundamentos de Python relacionados

Métodos de formateo de texto, generación de respuestas HTTP de descarga de archivos (`HttpResponse(content_type='text/csv')`).

### Conceptos Django relacionados

`admin.ModelAdmin`, `admin.TabularInline`, `readonly_fields`, `list_display`, `list_filter`, `search_fields`, `actions`.

### Conceptos DRF relacionados

No aplica directamente (panel web interno de Django).

### PostgreSQL

Consultas eficientes con `INNER JOIN` optimizadas por el admin.

### Arquitectura

Los archivos `admin.py` residen dentro de cada módulo respectivo (`apps/orders/admin.py`, `apps/inventory/admin.py`).

### Dependencias entre módulos

`admin.py` interactúa con los modelos locales de cada módulo.

### Antes de programar

1. ¿Por qué dejar campos de dinero editables en el Django Admin es un peligro operativo gigantesco en empresas reales?
2. ¿Cómo evita `list_select_related` que el listado del Django Admin ejecute cientos de consultas individuales para mostrar el email del cliente?

### Pruebas mínimas

1. Iniciar sesión como superusuario en `/admin/`, acceder a Pedidos y verificar que las órdenes se listen con sus columnas y que las líneas aparezcan en el inline de solo lectura.
2. Probar la búsqueda por email y verificar que filtre correctamente.

### Pruebas negativas

1. Intentar acceder a `/admin/` con un usuario estándar (`is_staff=False`) y comprobar que el acceso sea denegado.

### Documentación

Documentar las capacidades del panel administrativo y las acciones disponibles en la guía de operaciones.

### Explicación posterior

Explica por qué el Django Admin es una herramienta de productividad excepcional para backoffice y soporte, y cómo mantenerlo limpio y rápido mediante inlines y `readonly_fields`.

### Aplicación profesional

Herramientas de backoffice interno (Customer Support Dashboard, Ops Portal) sin necesidad de construir un frontend administrativo desde cero.

### Reto adicional

Agregar un método coloreado con HTML seguro (`format_html`) en `list_display` que pinte el estado del pedido (verde para `PAID`, amarillo para `PENDING`, rojo para `CANCELLED`).
