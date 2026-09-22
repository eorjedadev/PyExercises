# Ejercicio 070 — Versionado de APIs y Evolución de Contratos (/api/v1/ vs /api/v2/)

[← Ejercicio 069](../ejercicio_069/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 071 →](../ejercicio_071/README.md)

---

### Contexto de negocio

El negocio necesita rediseñar la estructura de respuestas de los productos y clientes para soportar una nueva aplicación móvil, cambiando nombres de campos y estructuras anidadas. Sin embargo, existen miles de usuarios utilizando la versión anterior de la app móvil que no se actualizará de inmediato. Modificar la API actual rompería a los clientes antiguos (Breaking Change). Se requiere implementar versionado de API.

### Estado actual del sistema

Endpoints expuestos bajo `/api/v1/`. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Configurar el esquema de versionado por URL en Django/DRF (`URLPathVersioning`), crear los endpoints `/api/v2/catalog/products/` con el nuevo contrato de datos, manteniendo `/api/v1/` completamente operativo sobre los mismos modelos de base de datos.

### Objetivo

Dominar las estrategias de versionado de APIs en Django REST Framework, aprendiendo a evolucionar contratos públicos sin duplicar modelos de base de datos ni romper clientes existentes.

### Actor

Clientes Antiguos (v1) y Clientes Nuevos (v2)

### Módulo responsable

`config/urls.py` y `apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`URLPathVersioning`, `ProductOutputV1Serializer`, `ProductOutputV2Serializer`, vistas versionadas.

### Reglas de negocio

1. `/api/v1/catalog/products/` debe mantener su contrato original intacto: campos `price_amount`, `weight_grams`.
2. `/api/v2/catalog/products/` expone el nuevo contrato: agrupa precios e impuestos en un objeto `pricing: { "amount": ..., "currency": ..., "formatted": "$199.99 USD" }` y dimensiones en `dimensions`.
3. Ambas versiones leen y escriben sobre la MISMA tabla `catalog_products` en PostgreSQL; no se duplican modelos de base de datos.
4. Las versiones se despachan dinámicamente según la URL solicitada.

### Contrato esperado

1. Contrato V1:
- `GET /api/v1/catalog/products/{id}/` -> `{ "id": "...", "price_amount": "49.90", "currency": "USD" }`

2. Contrato V2:
- `GET /api/v2/catalog/products/{id}/` -> `{ "id": "...", "pricing": { "amount": "49.90", "currency": "USD", "formatted": "$49.90 USD" } }`

### Persistencia

Misma tabla `catalog_products` en PostgreSQL.

### Relaciones

`Product`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validaciones adaptadas a cada versión de serializer.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Cliente que solicita una versión inexistente `/api/v3/...` (debe responder `404 Not Found`).

### Casos de error

- `400 Bad Request`: Payload JSON malformado o campos requeridos ausentes.
- `401 Unauthorized`: Token JWT expirado, revocado o ausente.
- `403 Forbidden`: Usuario sin permisos suficientes para la acción.
- `404 Not Found`: Identificador de recurso inexistente.
- `409 Conflict` / `422 Unprocessable`: Violación de invariantes de negocio o concurrencia.
- `500 Internal Server Error`: Errores no controlados capturados por el exception handler global.

### Consideraciones de seguridad

Garantizar que las correcciones de seguridad se apliquen a todas las versiones activas de la API.

### Consideraciones de rendimiento

Uso de los mismos selectores optimizados subyacentes.

### Fundamentos de Python relacionados

Herencia y polimorfismo de serializers. Tipado estricto con `typing` (`Optional`, `Dict`, `List`), decoradores, dataclasses, manejo estructurado de excepciones y programación modular.

### Conceptos Django relacionados

Enrutamiento modular de URLs por versión (`path('api/v1/', include(...))`, `path('api/v2/', include(...))`).

### Conceptos DRF relacionados

`versioning.URLPathVersioning`, `request.versión`, selección dinámica de serializer en `get_serializer_class()`.

### PostgreSQL

Alineación con el motor relacional PostgreSQL 16: tipos de datos nativos (`UUID`, `NUMERIC`, `TIMESTAMPTZ`, `JSONB`), índices B-Tree compuestos y garantías transaccionales ACID en nivel de aislamiento `READ COMMITTED`.

### Arquitectura

El versionado se resuelve en la Capa de Entrega / Presentación (Serializers y Vistas), preservando intacta la Capa de Dominio.

### Dependencias entre módulos

Interno a `apps/catalog`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué cambiar el nombre de un campo JSON en una API en producción sin versionado es una falta grave en ingeniería de software?
2. ¿Cuáles son las ventajas y desventajas del versionado por URL (`/api/v1/`) frente al versionado por cabecera HTTP (`Accept: application/vnd.app.v1+json`)?

### Pruebas mínimas

1. Consultar `GET /api/v1/catalog/products/{id}/` y verificar que la respuesta tenga el formato plano de la versión 1.
2. Consultar `GET /api/v2/catalog/products/{id}/` sobre el mismo producto y verificar que devuelva el objeto anidado `pricing` de la versión 2.

### Pruebas negativas

1. Crear un producto mediante V1 y comprobar que sea visible inmediatamente en V2 (misma base de datos).

### Documentación

Documentar la política de versionado y ciclo de vida de versiones (Deprecation Policy) en la guía de la API.

### Explicación posterior

Explica cómo gestionar el ciclo de vida de versiones de API (Active, Deprecated, Sunset/EOL) y por qué mantener más de 2 o 3 versiones simultáneas genera sobrecosto de mantenimiento.

### Aplicación profesional

Evolución de plataformas móviles (iOS/Android), APIs públicas para desarrolladores (Stripe, GitHub, Twitter) y microservicios.

### Reto adicional

Configurar `drf-spectacular` para generar dos esquemas OpenAPI independientes: uno para la V1 y otro para la V2.
