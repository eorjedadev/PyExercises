# Ejercicio 005 — Vistas Explícitas con APIView y Semántica de Verbos HTTP

[← Ejercicio 004](../ejercicio_004/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 006 →](../ejercicio_006/README.md)

---

### Contexto de negocio

El equipo backend necesita implementar los endpoints de listado y creación de productos utilizando vistas explícitas de bajo nivel (`APIView`) para comprender el flujo completo de una petición HTTP antes de usar abstracciones mágicas de alto nivel.

### Estado actual del sistema

Modelos y Serializers de `Product` listos en `apps/catalog`.

### Nueva necesidad

Crear la vista `ProductListCreateAPIView` heredando de `rest_framework.views.APIView`, manejando manualmente `GET` y `POST` con sus status codes HTTP correctos.

### Objetivo

Dominar el ciclo de vida de `APIView`, `request.data`, `request.query_params`, instanciación de serializers, `serializer.is_valid(raise_exception=True)` y respuestas con `Response`.

### Actor

Cliente de API autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Product`, `ProductListCreateAPIView`, `ProductOutputSerializer`, `ProductCreateInputSerializer`.

### Reglas de negocio

1. `GET /api/v1/catalog/products/` debe devolver la lista de todos los productos activos con status `200 OK`.
2. `POST /api/v1/catalog/products/` debe validar el payload, crear el producto y devolver status `201 Created` con la representación del recurso creado.
3. Métodos no permitidos (ej. `DELETE` en la raíz) deben responder `405 Method Not Allowed` automáticamente.

### Contrato esperado

Listado:
- `GET /api/v1/catalog/products/` -> `200 OK` `[ { "id": "...", "name": "..." } ]`

Creación:
- `POST /api/v1/catalog/products/` -> `201 Created` `{ "id": "...", "sku": "..." }`

### Persistencia

Consulta ORM `Product.objects.filter(is_active=True)` e inserción `serializer.save()`.

### Relaciones

Colección de `Product`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

Ejecución de validación de serializer en el método `post`.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Base de datos vacía al consultar `GET` (debe devolver `200 OK` con lista vacía `[]`, nunca `404 Not Found`).

### Casos de error

`400 Bad Request` en caso de datos inválidos en `POST`.

### Consideraciones de seguridad

No exponer stack traces en respuestas de error; devolver solo errores estructurados.

### Consideraciones de rendimiento

Filtrar solo registros activos en la consulta `GET`.

### Fundamentos de Python relacionados

Métodos de instancia, herencia de clases, manejo de parámetros HTTP.

### Conceptos Django relacionados

`urls.py` modular (`apps/catalog/urls.py`), inclusión en `config/urls.py` con `path('api/v1/catalog/', include('apps.catalog.urls'))`.

### Conceptos DRF relacionados

`APIView`, `Response`, `status`, `request.data`, `request.query_params`, `serializer.save()`.

### PostgreSQL

`SELECT ... FROM catalog_products WHERE is_active = true` e `INSERT INTO ...`.

### Arquitectura

Las vistas en `apps/catalog/views.py` actúan exclusivamente como adaptadores HTTP: reciben la petición, delegan validación/persistencia y retornan la respuesta.

### Dependencias entre módulos

`config/urls.py` incluye las URLs de `apps/catalog`.

### Antes de programar

1. ¿Por qué `GET` a una lista vacía debe responder `200 OK` con `[]` y no `404 Not Found`?
2. ¿Qué diferencia hay entre `request.data` de DRF y `request.POST` de Django estándar?

### Pruebas mínimas

1. Enviar `GET /api/v1/catalog/products/` y verificar status code `200` y tipo lista.
2. Enviar `POST` con datos válidos y verificar status code `201` y presencia del ID generado.

### Pruebas negativas

1. Enviar `POST` con cuerpo vacío `{}` y verificar status code `400`.
2. Enviar `DELETE /api/v1/catalog/products/` y verificar status `405 Method Not Allowed`.

### Documentación

Documentar la ruta URL y los métodos HTTP soportados en el módulo.

### Explicación posterior

Explica qué hace `APIView` internamente: parseo de contenido, autenticación previa, chequeo de permisos y manejo de excepciones.

### Aplicación profesional

Creación de endpoints personalizados cuando la lógica no encaja en un CRUD genérico estándar.

### Reto adicional

Implementar en la misma vista un parámetro query `?is_active=false` para que administradores puedan listar productos inactivos.
