# Ejercicio 086 — Cálculo y Actualización Atómica de Métricas Agregadas de Calificación

[← Ejercicio 085](../ejercicio_085/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 087 →](../ejercicio_087/README.md)

---

### Contexto de negocio

Calcular el promedio de estrellas (`average_rating`) y el total de opiniones (`review_count`) ejecutando un `AVG(rating)` sobre la tabla de reseñas cada vez que un usuario abre la ficha de un producto es ineficiente en catálogos con millones de visitas. El modelo `Product` (o una tabla agregada de métricas) debe almacenar el promedio precalculado y actualizarse atómicamente cada vez que se publica una nueva reseña.

### Estado actual del sistema

Módulo de reseñas operativo. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Crear el servicio `reviews.services.recalculate_product_rating_metrics(product_id)` que calcule atómicamente el promedio exacto y total de reseñas en PostgreSQL y actualice el producto sin condiciones de carrera.

### Objetivo

Dominar el patrón de Vistas Materializadas / Campos Desnormalizados Agregados en Django, actualizando métricas calculadas de forma atómica y manteniendo consistencia con las tablas transaccionales.

### Actor

Sistema de Reseñas ejecutando procesos internos de dominio o tareas programadas de fondo.

### Módulo responsable

`apps/reviews` actualizando métricas de `apps/catalog`

### Entidades involucradas

`ProductReview`, `Product` (campos `average_rating`, `review_count`), servicio `recalculate_product_rating_metrics`.

### Reglas de negocio

1. El `average_rating` debe ser un decimal con 2 dígitos de precisión (ej. `4.85`) entre `0.00` y `5.00`.
2. `review_count` es el número total de reseñas aprobadas.
3. Cada vez que se crea, edita o elimina una reseña aprobada, se debe recalcular y persistir la métrica actualizada.
4. Si un producto no tiene reseñas, `average_rating` debe ser `0.00` y `review_count` debe ser `0`.

### Contrato esperado

Detalle de Producto con Calificación Precalculada:
- `GET /api/v1/catalog/products/{id}/`
  Response incluye:
  ```json
  {
    "id": "uuid-prod",
    "name": "Teclado Mecanico",
    "average_rating": "4.67",
    "review_count": 3
  }
  ```

### Persistencia

Actualización de columnas `average_rating` y `review_count` en la tabla `catalog_products`.

### Relaciones

`ProductReview` -> `Product`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Validar que el promedio esté acotado entre 0.00 y 5.00.

### Transacciones

Transacción atómica durante la inserción de la reseña y la actualización de las métricas agregadas.

### Casos límite

Eliminación de la única reseña existente de un producto (el promedio debe volver a `0.00` y el contador a `0`).

### Casos de error

- `400 Bad Request`: Payload JSON malformado o campos requeridos ausentes.
- `401 Unauthorized`: Token JWT expirado, revocado o ausente.
- `403 Forbidden`: Usuario sin permisos suficientes para la acción.
- `404 Not Found`: Identificador de recurso inexistente.
- `409 Conflict` / `422 Unprocessable`: Violación de invariantes de negocio o concurrencia.
- `500 Internal Server Error`: Errores no controlados capturados por el exception handler global.

### Consideraciones de seguridad

Garantizar que ningún script externo pueda alterar el rating promedio directamente sin pasar por el cálculo de reseñas reales.

### Consideraciones de rendimiento

Lecturas instantáneas de la ficha de producto sin ejecutar ningún `AVG()` ni `COUNT()` en tiempo de petición del cliente.

### Fundamentos de Python relacionados

Redondeo financiero de decimales (`Decimal.quantize`).

### Conceptos Django relacionados

`django.db.models.Avg`, `django.db.models.Count`, actualización con `QuerySet.update()`.

### Conceptos DRF relacionados

Exposición de campos agregados en serializers de producto.

### PostgreSQL

`SELECT AVG(rating), COUNT(*) FROM reviews_productreview WHERE product_id = ... AND is_approved = true; UPDATE catalog_products SET average_rating = ..., review_count = ... WHERE id = ...;`.

### Arquitectura

`apps/reviews` coordina la actualización de métricas hacia `apps/catalog`.

### Dependencias entre módulos

`apps/reviews` invoca la actualización en `apps/catalog`.

### Antes de programar

1. ¿Por qué desnormalizar el promedio de calificación (`average_rating`) en la tabla de productos es una decisión de rendimiento válida para aplicaciones de lectura intensiva?
2. ¿Cómo se garantiza que el campo desnormalizado nunca quede desincronizado de la tabla de reseñas de origen?

### Pruebas mínimas

1. Crear un producto con 0 reseñas (`average_rating = 0.00`, `review_count = 0`).
2. Publicar una reseña de 5 estrellas -> Verificar que `average_rating` sea `5.00` y `review_count` sea 1.
3. Publicar una segunda reseña de 4 estrellas -> Verificar que `average_rating` se actualice exactamente a `4.50` y `review_count` a 2.

### Pruebas negativas

1. Eliminar una reseña y comprobar que el promedio se recalcule automáticamente hacia abajo.

### Documentación

Documentar la estrategia de desnormalización y sincronización de métricas en la guía de base de datos.

### Explicación posterior

Explica el compromiso clásico de la ingeniería de software entre Normalización (cero duplicación, consultas pesadas) y Desnormalización Controlada (lecturas O(1), costo mínimo en escritura).

### Aplicación profesional

Cálculo de calificaciones en Amazon, Uber, MercadoLibre, IMDb y rankings de popularidad en e-commerce.

### Reto adicional

Implementar un comando de gestión `python manage.py recompute_all_product_ratings` para auditar y corregir periódicamente cualquier discrepancia matemática en las métricas desnormalizadas.
