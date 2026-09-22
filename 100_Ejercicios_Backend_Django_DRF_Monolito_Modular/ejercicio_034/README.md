# Ejercicio 034 — Transacciones Atómicas con transaction.atomic y Consistencia

[← Ejercicio 033](../ejercicio_033/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 035 →](../ejercicio_035/README.md)

---

### Contexto de negocio

Al crear un pedido con múltiples líneas, si ocurre un fallo al insertar la 5ta línea (ej. corte de red, error de validación, caída de proceso), la base de datos no puede quedar en un estado inconsistente con una cabecera huérfana y 4 líneas incompletas. Toda la operación de creación debe ser atómica (Todo o Nada).

### Estado actual del sistema

Servicio `create_order` básico en `apps/orders`.

### Nueva necesidad

Envolver la creación de la orden y sus ítems dentro de un bloque `transaction.atomic()` de Django, asegurando rollback automático ante cualquier excepción no controlada.

### Objetivo

Dominar el control de transacciones en PostgreSQL y Django (`django.db.transaction.atomic`), comprendiendo las propiedades ACID, puntos de guardado (savepoints) y la prevención de datos huérfanos.

### Actor

Sistema de Pedidos ejecutando procesos internos de dominio o tareas programadas de fondo.

### Módulo responsable

`apps/orders` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Order`, `OrderItem`, `transaction.atomic`.

### Reglas de negocio

1. La creación de la orden (`Order`) y todas sus líneas (`OrderItem`) deben ocurrir dentro de una única transacción de base de datos.
2. Si la creación de cualquier línea falla, la cabecera de la orden y las líneas previas deben deshacerse (`ROLLBACK`) inmediatamente.
3. Ningún registro parcial debe persistir en PostgreSQL si la operación no culmina exitosamente.

### Contrato esperado

Comportamiento transaccional estricto ante fallos: 0 registros guardados si ocurre un error.

### Persistencia

Transacción PostgreSQL `BEGIN; ... COMMIT;` o `ROLLBACK;`.

### Relaciones

`Order` y `OrderItem`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación integral antes y durante la persistencia.

### Transacciones

Uso explícito de `@transaction.atomic` en la función de servicio `create_order` o bloque `with transaction.atomic():`.

### Casos límite

Simulación de una excepción forzada a mitad de la inserción de ítems.

### Casos de error

Excepción capturada y relanzada como error de dominio, garantizando el rollback de la base de datos.

### Consideraciones de seguridad

Garantizar consistencia financiera: no pueden existir órdenes sin ítems ni ítems sin orden asociada.

### Consideraciones de rendimiento

Mantener los bloques transaccionales cortos; no realizar llamadas lentas a APIs externas de red dentro de `transaction.atomic()`.

### Fundamentos de Python relacionados

Context managers (`with`), decoradores de función.

### Conceptos Django relacionados

`django.db.transaction.atomic`, `transaction.on_commit` para efectos secundarios.

### Conceptos DRF relacionados

Manejo de excepciones dentro de vistas transaccionales.

### PostgreSQL

`BEGIN`, `SAVEPOINT`, `RELEASE SAVEPOINT`, `ROLLBACK`.

### Arquitectura

La demarcación transaccional pertenece a la Capa de Servicios (`apps/orders/services.py`), NUNCA a las vistas ni serializers.

### Dependencias entre módulos

Interno a `apps/orders` utilizando utilidades de base de datos de Django.

### Antes de programar

1. ¿Por qué es un error gravísimo hacer una llamada HTTP a una pasarela de pagos externa dentro de un bloque `transaction.atomic()`?
2. ¿Qué ocurre con las conexiones de base de datos en PostgreSQL si una transacción queda abierta indefinidamente?

### Pruebas mínimas

1. Ejecutar `create_order` con datos válidos y comprobar que tanto `Order` como todos los `OrderItem` existan en la base de datos tras el commit.
2. Usar un test con mock para forzar una excepción en la creación del segundo ítem y verificar que `Order.objects.count()` sea 0 (rollback total verificado).

### Pruebas negativas

1. Verificar que ante cualquier excepción de integridad, PostgreSQL no deje filas huérfanas en `orders_order`.

### Documentación

Documentar las reglas de demarcación transaccional y el uso de `on_commit` en la guía de arquitectura.

### Explicación posterior

Explica qué son las propiedades ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad) y por qué `transaction.on_commit` es el lugar correcto para enviar correos o encolar tareas tras confirmar la transacción.

### Aplicación profesional

Operaciones financieras, transferencias bancarias, emisión de pólizas y carritos de compra de alta concurrencia.

### Reto adicional

Integrar `transaction.on_commit(lambda: logger.info('Orden confirmada en DB'))` para registrar la confirmación solo tras el commit exitoso.
