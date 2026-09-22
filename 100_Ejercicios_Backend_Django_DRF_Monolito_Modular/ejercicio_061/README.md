# Ejercicio 061 — Detección y Diagnóstico del Problema N+1 en Listados de Pedidos

[← Ejercicio 060](../ejercicio_060/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 062 →](../ejercicio_062/README.md)

---

### Contexto de negocio

Al consultar el listado de órdenes en el panel de administración (`GET /api/v1/orders/`), la respuesta tarda más de 4 segundos para solo 50 pedidos. Al inspeccionar la consola de depuración o los logs de PostgreSQL, se observa que el servidor ejecuta 1 consulta para traer las 50 órdenes, y luego 50 consultas individuales para traer el perfil del cliente, 50 consultas para el usuario, y 50 consultas para los ítems: ¡más de 151 consultas SQL para una sola petición!

### Estado actual del sistema

Endpoint de listado de órdenes operando con serializador anidado ingenuo.

### Nueva necesidad

Reproducir intencionalmente el problema N+1 en un test de rendimiento, medir el número exacto de consultas SQL ejecutadas con `django.test.utils.CaptureQueriesContext` (o `django-silk` / `django-debug-toolbar`) y diagnosticar la causa raíz.

### Objetivo

Comprender qué es el problema N+1 en los ORMs relacionales, cómo medirlo de forma automatizada en Django y por qué los serializadores anidados de DRF son la principal fuente de este cuello de botella.

### Actor

Desarrollador Backend / Ingeniero de Rendimiento

### Módulo responsable

`apps/orders` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Order`, `CustomerProfile`, `User`, `OrderItem`, `OrderDetailOutputSerializer`.

### Reglas de negocio

1. La consulta de listado de órdenes no debe degradarse linealmente con el número de registros en la base de datos (O(N) queries es inaceptable; debe ser O(1)).
2. El desarrollador debe documentar el diagnóstico: por qué `order.customer.user.email` y `order.items.all()` disparan queries perezosas individuales por cada iteración del serializador.
3. Se debe escribir una prueba automatizada que falle si el número de queries SQL ejecutadas supera un umbral máximo.

### Contrato esperado

Diagnóstico técnico documentado y prueba de conteo de queries.

### Persistencia

Consultas `SELECT` repetitivas e ineficientes en PostgreSQL.

### Relaciones

`Order` -> `CustomerProfile` -> `User`, `Order` -> `OrderItem`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Listar 200 órdenes con 5 ítems cada una (provocaría más de 1,000 queries SQL colapsando la base de datos si no se optimiza).

### Casos de error

Timeout de base de datos o latencia inaceptable.

### Consideraciones de seguridad

Ataques de denegación de servicio por agotamiento de conexiones en el pool de PostgreSQL debido a queries masivas.

### Consideraciones de rendimiento

Identificación de sobrecarga de CPU en base de datos y latencia de red innecesaria (Network Roundtrips).

### Fundamentos de Python relacionados

Medición de tiempos de ejecución con `time.perf_counter()`, contexto managers.

### Conceptos Django relacionados

`django.db.connection.queries`, `CaptureQueriesContext`, comportamiento de evaluación perezosa (Lazy Loading) del ORM.

### Conceptos DRF relacionados

Cómo los serializers anidados evalúan propiedades relacionales en bucle.

### PostgreSQL

Inspección de logs de queries en PostgreSQL (`log_statement = 'all'`).

### Arquitectura

El problema de N+1 debe resolverse en la Capa de Selectores (`apps/orders/selectors.py`), manteniendo el serializador intacto.

### Dependencias entre módulos

Interno a `apps/orders`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué el ORM de Django no hace joins automáticos para todas las relaciones foráneas de manera predeterminada?
2. ¿Cuál es el impacto en la latencia de red de ejecutar 150 consultas pequeñas individuales versus ejecutar 2 consultas optimizadas?

### Pruebas mínimas

1. Crear 20 órdenes con 3 ítems cada una en la base de datos de prueba.
2. Ejecutar la vista de listado dentro de un bloque `with CaptureQueriesContext(connection) as ctx:` y verificar que la implementación ingenua ejecute más de 60 consultas.

### Pruebas negativas

1. Verificar que el tiempo de respuesta crezca proporcionalmente con el número de pedidos en el escenario no optimizado.

### Documentación

Documentar el informe de diagnóstico de N+1 en la carpeta `análisis/` de `apps/orders`.

### Explicación posterior

Explica detalladamente la diferencia mecánica entre una relación 1 a 1 / ForeignKey (donde la clave está en la misma tabla o tabla padre) y una relación 1 a N / ManyToMany (donde hay múltiples filas hijas), y por qué requieren estrategias de optimización diferentes.

### Aplicación profesional

Auditoría de rendimiento y optimización de APIs que experimentan lentitud bajo tráfico real en producción.

### Reto adicional

Configurar una herramienta de profiling como `django-silk` o logging de consultas SQL lentas en el entorno local.
