# Ejercicio 074 — Monitoreo de Rendimiento y Medición de Consultas SQL en Tests

[← Ejercicio 073](../ejercicio_073/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 075 →](../ejercicio_075/README.md)

---

### Contexto de negocio

Para evitar que futuros cambios de código introduzcan regresiones silenciosas de rendimiento (ej. que alguien agregue un campo a un serializer y vuelva a provocar un N+1 sin darse cuenta), el pipeline de integración continua (CI) debe medir y limitar de forma automática el número exacto de consultas SQL y el tiempo máximo de ejecución de cada endpoint crítico del sistema.

### Estado actual del sistema

Endpoints optimizados en todos los módulos. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Crear un decorador de pruebas `@assert_max_queries(N)` y `@assert_max_duration_ms(ms)` en `tests/utils.py` y aplicarlo a los tests de integración de los 10 endpoints más críticos del monolito (catálogo, login, órdenes, inventario).

### Objetivo

Implementar pruebas automatizadas de regresión de rendimiento en Django, garantizando que el presupuesto de consultas SQL (SQL Query Budget) y la latencia máxima se cumplan estrictamente en cada Pull Request.

### Actor

Ingeniero de Calidad / Desarrollador Backend

### Módulo responsable

`tests/` y transversal en todos los módulos

### Entidades involucradas

`CaptureQueriesContext`, `django.test.utils`, decoradores de prueba en `tests/utils.py`.

### Reglas de negocio

1. Ningún endpoint de listado paginado (catálogo, órdenes, clientes) puede ejecutar más de 4 consultas SQL en total.
2. Ningún endpoint de detalle o acción individual puede ejecutar más de 3 consultas SQL.
3. Si un desarrollador agrega una relación perezosa que aumente las consultas, el test debe fallar con un mensaje explícito: `QueryBudgetExceeded: Expected max 4 queries, but executed 12 queries`.
4. Los tests de presupuesto de queries deben ejecutarse en cada corrida de `pytest`.

### Contrato esperado

Suite de pruebas de rendimiento ejecutándose dentro de `pytest` con reporte de consultas por endpoint.

### Persistencia

Base de datos de pruebas en PostgreSQL. Persistencia física garantizada mediante tablas relacionales en PostgreSQL, con tipos de datos nativos e integridad referencial protegida.

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Consultas disparadas por configuración de sesiones o middleware de autenticación (deben contabilizarse dentro del presupuesto establecido).

### Casos de error

Fallo del test con volcado de las consultas SQL capturadas para facilitar el diagnóstico inmediato.

### Consideraciones de seguridad

Garantizar la estabilidad y previsibilidad del consumo de recursos del backend.

### Consideraciones de rendimiento

Garantía de rendimiento O(1) en consultas a base de datos.

### Fundamentos de Python relacionados

Creación de context managers y decoradores de prueba en Python con `functools.wraps`.

### Conceptos Django relacionados

`django.test.utils.CaptureQueriesContext`, `django.db.connection`.

### Conceptos DRF relacionados

Diseño de contratos REST con `serializers.Serializer` / `ModelSerializer`, vistas delegadoras `APIView` o `GenericAPIView`, normalización de respuestas JSON y documentación declarativa con `@extend_schema`.

### PostgreSQL

Captura e inspección del SQL exacto ejecutado por Django en PostgreSQL.

### Arquitectura

Infraestructura de testing de calidad en `tests/utils.py`.

### Dependencias entre módulos

`tests/` importa utilidades de infraestructura.

### Antes de programar

1. ¿Por qué el monitoreo de rendimiento no debe ser solo reactivo en producción, sino preventivo mediante tests de presupuesto de queries en CI?
2. ¿Cómo ayuda imprimir la lista de queries SQL capturadas cuando falla un test a que el desarrollador identifique exactamente qué relación faltó optimizar?

### Pruebas mínimas

1. Aplicar `@assert_max_queries(3)` al test de listado de productos con 50 registros y comprobar que el test pase en verde.
2. Forzar intencionalmente una consulta no optimizada en una prueba y verificar que el test falle con el mensaje descriptivo `QueryBudgetExceeded`.

### Pruebas negativas

1. Verificar que ante una regresión en el código, el pipeline de CI bloquee el merge automáticamente.

### Documentación

Documentar la tabla de presupuestos de consultas SQL por endpoint en la guía de testing.

### Explicación posterior

Explica el concepto de Performance Budget (Presupuesto de Rendimiento) en ingeniería de software y cómo aplicarlo a bases de datos relacionales en arquitecturas backend.

### Aplicación profesional

Cultura de ingeniería en empresas de tecnología de alto impacto (Spotify, Netflix, Meta) para prevenir degradación de microservicios y monolitos.

### Reto adicional

Imprimir una tabla formateada en consola con el tiempo de ejecución y lista de queries de cada endpoint probado al finalizar la suite con `pytest`.
