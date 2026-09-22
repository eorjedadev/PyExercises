# Ejercicio 010 — Vistas Genéricas de DRF y Selección Consciente de Abstracciones

[← Ejercicio 009](../ejercicio_009/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 011 →](../ejercicio_011/README.md)

---

### Contexto de negocio

El módulo de catálogo necesita endpoints CRUD completos para gestionar productos individuales (obtener detalle, actualizar parcialmente con PATCH, eliminar lógicamente). El equipo debe migrar de `APIView` a vistas genéricas (`generics.RetrieveUpdateDestroyAPIView`), comprendiendo exactamente qué métodos sobreescribir sin depender ciegamente de `ModelViewSet`.

### Estado actual del sistema

Endpoints de listado y creación implementados en `apps/catalog`.

### Nueva necesidad

Implementar endpoints de detalle, actualización (`PUT`/`PATCH`) y eliminación (`DELETE`) usando `generics.RetrieveUpdateDestroyAPIView`, personalizando `get_queryset()` y `get_serializer_class()`.

### Objetivo

Aprender a elegir la abstracción correcta de DRF (`generics.*` vs `APIView` vs `ViewSet`), controlando el queryset dinámicamente y aplicando diferentes serializers según la acción HTTP.

### Actor

Operador de Catálogo en el contexto de las operaciones comerciales de la plataforma.

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Product`, `ProductDetailOutputSerializer`, `ProductUpdateInputSerializer`, `ProductRetrieveUpdateDestroyAPIView`.

### Reglas de negocio

1. `GET /api/v1/catalog/products/{id}/`: Retorna el detalle completo del producto activo.
2. `PATCH /api/v1/catalog/products/{id}/`: Permite actualizar parcialmente campos permitidos (`name`, `description`, `price_amount`, `weight_grams`).
3. El campo `sku` no puede ser modificado una vez creado el producto (inmutable).
4. `DELETE /api/v1/catalog/products/{id}/`: Marca `is_active = False` (desactivación) y responde `204 No Content`.

### Contrato esperado

Detalle:
- `GET /api/v1/catalog/products/{id}/` -> `200 OK` `{ "id": "...", "name": "..." }`

Actualización Parcial:
- `PATCH /api/v1/catalog/products/{id}/`
  Request: `{"price_amount": "59.99"}`
  Response: `200 OK` `{ ... "price_amount": "59.99" }`

Eliminación:
- `DELETE /api/v1/catalog/products/{id}/` -> `204 No Content`

### Persistencia

Actualización en tabla `catalog_products` con `UPDATE catalog_products SET ...`.

### Relaciones

`Product`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

Validaciones de serializer sobre los campos actualizados.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Intentar enviar `PATCH` con un `sku` nuevo (el serializer debe ignorar el campo o rechazarlo).

### Casos de error

`404 Not Found` si el ID de producto no existe o está inactivo.

### Consideraciones de seguridad

Garantizar que `perform_destroy` ejecute soft-delete en lugar de `instance.delete()` físico si esa es la regla.

### Consideraciones de rendimiento

Optimizar el queryset base usando `select_related('category')`.

### Fundamentos de Python relacionados

Sobreescritura de métodos polimórficos (`get_serializer_class`, `perform_destroy`).

### Conceptos Django relacionados

`get_object_or_404`, ciclo de vida de actualización en el ORM.

### Conceptos DRF relacionados

`generics.GenericAPIView`, `generics.RetrieveUpdateDestroyAPIView`, `lookup_field='id'`, `perform_update`, `perform_destroy`.

### PostgreSQL

`UPDATE catalog_products SET is_active = false, updated_at = NOW() WHERE id = ...`.

### Arquitectura

Uso de vistas genéricas en `apps/catalog/views.py` manteniendo el código conciso pero explícito.

### Dependencias entre módulos

Interno a `apps/catalog`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Cuándo es preferible usar `generics.RetrieveUpdateDestroyAPIView` en lugar de un `ModelViewSet` completo con router?
2. ¿Por qué `lookup_field` debe configurarse explícitamente a `'id'` cuando se usan UUIDs?

### Pruebas mínimas

1. Consultar `GET /api/v1/catalog/products/{id}/` de un producto existente y verificar `200 OK`.
2. Enviar `PATCH` modificando el precio y comprobar que en base de datos el precio cambie y el SKU permanezca igual.
3. Enviar `DELETE` y verificar que el producto quede con `is_active = False`.

### Pruebas negativas

1. Consultar un UUID inexistente y comprobar respuesta `404 Not Found`.

### Documentación

Documentar los endpoints de detalle y modificación en el contrato de API.

### Explicación posterior

Explica el flujo interno de `RetrieveUpdateDestroyAPIView`: cómo `get_object()` obtiene la instancia, verifica permisos y delega a `retrieve()`, `update()` o `destroy()`.

### Aplicación profesional

Implementación de interfaces RESTful limpias y mantenibles sin código boilerplate redundante.

### Reto adicional

Sobreescribir `get_serializer_class()` para usar un serializer con menos campos en el `GET` de detalle que en el `PATCH`.
