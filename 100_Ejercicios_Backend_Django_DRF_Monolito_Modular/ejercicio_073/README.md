# Ejercicio 073 — Control de Concurrencia Optimista mediante version_id / Timestamps

[← Ejercicio 072](../ejercicio_072/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 074 →](../ejercicio_074/README.md)

---

### Contexto de negocio

En el panel administrativo, dos operadores abren simultáneamente la ficha del mismo producto. El Operador A modifica la descripción y guarda su cambio. Cinco segundos después, el Operador B, que tenía la pantalla abierta con el precio antiguo, modifica solo el stock y presiona Guardar. El guardado del Operador B sobrescribe silenciosamente los cambios del Operador A (Lost Update Problem). Se requiere implementar Control de Concurrencia Optimista (OCC) mediante `version_id`.

### Estado actual del sistema

Actualización estándar de productos en `apps/catalog`.

### Nueva necesidad

Agregar el campo `versión = models.IntegerField(default=1)` al modelo `Product`, requerir que las peticiones de actualización envíen la versión esperada (o cabecera `If-Match`), y ejecutar una actualización condicional `Product.objects.filter(id=id, versión=current_version).update(..., versión=F('versión') + 1)`.

### Objetivo

Dominar el Control de Concurrencia Optimista (OCC) en Django y PostgreSQL, comprendiendo la prevención de sobrescrituras accidentales (Lost Updates) sin bloquear la base de datos.

### Actor

Múltiples Operadores concurrentes en el contexto de las operaciones comerciales de la plataforma.

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Product` (campo `versión`), `OptimisticLockError`, servicio `update_product_optimistic`.

### Reglas de negocio

1. Cada vez que un producto se actualiza con éxito, su campo `versión` se incrementa en 1 (`versión = F('versión') + 1`).
2. El cliente debe enviar el número de versión que leyó originalmente en el cuerpo o cabecera (`{"versión": 3, ...}`).
3. Si al momento de actualizar, la versión en PostgreSQL es diferente a la enviada por el cliente (porque otro operador guardó antes), la operación se rechaza inmediatamente con `409 Conflict`.
4. La respuesta `409 Conflict` debe informar que el registro fue modificado por otro usuario e invitar a recargar los datos frescos.

### Contrato esperado

Conflicto de Concurrencia Optimista:
- `PATCH /api/v1/catalog/products/{id}/`
  Body: `{"versión": 2, "price_amount": "59.99"}` (cuando en DB ya está en versión 3)
  Response: `409 Conflict`
  ```json
  {
    "error": {
      "code": "CONCURRENCY_CONFLICT",
      "message": "El producto ha sido modificado por otro usuario mientras lo editaba. Recargue la página para ver los cambios actuales.",
      "details": { "current_version": 3, "submitted_version": 2 }
    }
  }
  ```

### Persistencia

Consulta atómica en PostgreSQL: `UPDATE catalog_products SET price_amount = ..., versión = versión + 1 WHERE id = ... AND versión = 2;`.

### Relaciones

`Product`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso basado en roles (RBAC). Requiere que el usuario autenticado cuente con permisos administrativos (`IsAdminUser` o `HasRole(['ADMIN', 'MANAGER'])`).

### Validaciones

Validar presencia de `versión` entero positivo en peticiones de modificación.

### Transacciones

No requiere transacciones largas; la atomicidad está en la propia sentencia `UPDATE`.

### Casos límite

Actualización exitosa (el número de filas afectadas `updated_count` es exactamente 1; si es 0, significa que hubo conflicto de versión o el ID no existe).

### Casos de error

`409 Conflict` ante discrepancia de versiones.

### Consideraciones de seguridad

Garantizar integridad de datos en entornos colaborativos multi-usuario.

### Consideraciones de rendimiento

Cero bloqueos pesimistas en PostgreSQL; ideal para escenarios con baja probabilidad de conflicto pero consecuencias graves si ocurre.

### Fundamentos de Python relacionados

Expresiones `F()` de Django para operaciones atómicas a nivel de base de datos.

### Conceptos Django relacionados

`django.db.models.F`, comprobación de filas afectadas mediante `QuerySet.update()`.

### Conceptos DRF relacionados

Mapeo de `OptimisticLockError` a status code `409 Conflict`.

### PostgreSQL

`UPDATE catalog_products SET name = 'Nuevo', versión = versión + 1 WHERE id = '...' AND versión = 1;`.

### Arquitectura

El control optimista se implementa en la capa de servicios en `apps/catalog/services.py`.

### Dependencias entre módulos

Interno a `apps/catalog`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Cuál es la diferencia fundamental entre Concurrencia Pesimista (`select_for_update`) y Concurrencia Optimista (`version_id`) en términos de contención y bloqueos de base de datos?
2. ¿Por qué el patrón de Concurrencia Optimista es el estándar para paneles de administración web y edición de documentos colaborativos?

### Pruebas mínimas

1. Crear un producto (versión 1). Operador 1 actualiza con `versión=1` -> Actualización exitosa, producto pasa a versión 2.
2. Operador 2 intenta actualizar el mismo producto enviando `versión=1` -> Verificar rechazo `409 Conflict` y comprobar que sus cambios no se apliquen.

### Pruebas negativas

1. Intentar actualizar sin enviar el campo `versión` y verificar que el serializer lo exija con error `400 Bad Request`.

### Documentación

Documentar el protocolo de concurrencia optimista y el manejo de errores 409 en la guía de integración.

### Explicación posterior

Explica cómo las expresiones `F('versión') + 1` de Django previenen condiciones de carrera a nivel de base de datos delegando el incremento atómico al motor de PostgreSQL.

### Aplicación profesional

Sistemas ERP, paneles de administración web, historiales clínicos, wikis colaborativas y edición de inventarios.

### Reto adicional

Implementar soporte para la cabecera estándar HTTP `If-Match: "<version_etag>"` y respuesta `ETag: "<versión>"` según los estándares REST de W3C.
