# Ejercicio 085 — Sistema de Reseñas y Calificaciones (apps/reviews) con Verified Purchase

[← Ejercicio 084](../ejercicio_084/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 086 →](../ejercicio_086/README.md)

---

### Contexto de negocio

Para generar confianza en los compradores, los clientes deben poder calificar (de 1 a 5 estrellas) y escribir reseñas sobre los productos que han adquirido. Para evitar reseñas falsas o spam competitivo, el sistema debe aplicar la regla estricta de 'Compra Verificada' (Verified Purchase): un usuario SOLO puede reseñar un producto si existe una orden en estado `DELIVERED` en su historial que contenga ese producto.

### Estado actual del sistema

Módulos de catálogo, clientes, órdenes y envíos operativos.

### Nueva necesidad

Crear el módulo `apps/reviews`, modelar `ProductReview`, implementar la validación de compra verificada consultando `apps/orders`, y exponer endpoints para crear y listar reseñas.

### Objetivo

Diseñar un sistema de calificaciones y reseñas desacoplado en el monolito modular, implementando validaciones cruzadas entre dominios (Reseñas -> Órdenes) para garantizar la autenticidad de las opiniones.

### Actor

Cliente Comprador Verificado / Visitante que lee reseñas

### Módulo responsable

`apps/reviews` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`ProductReview` (`id` UUID, `product_id` UUID, `customer_id` UUID, `order_id` UUID, `rating`, `title`, `comment`, `is_verified_purchase`, `is_approved`, `created_at`), servicio `create_product_review`.

### Reglas de negocio

1. El `rating` debe ser un entero entre 1 y 5 estrellas (`CheckConstraint(rating >= 1 AND rating <= 5)`).
2. Un cliente solo puede publicar 1 reseña por producto.
3. La regla de Compra Verificada debe comprobar que el cliente tenga un pedido en estado `DELIVERED` con ese `product_id`.
4. Cualquier visitante puede leer reseñas aprobadas (`is_approved = True`).

### Contrato esperado

Crear Reseña de Producto:
- `POST /api/v1/reviews/`
  Header: `Authorization: Bearer <token>`
  Body:
  ```json
  {
    "product_id": "uuid-producto",
    "rating": 5,
    "title": "Excelente calidad y ergonomía",
    "comment": "Llegó en 24 horas y funciona perfecto para jugar y trabajar."
  }
  ```
  Response: `201 Created` `{ "id": "uuid-review", "is_verified_purchase": true, ... }`

### Persistencia

Tabla `reviews_productreview` en PostgreSQL con restricción única `(product_id, customer_id)` y `CHECK (rating BETWEEN 1 AND 5)`.

### Relaciones

`ProductReview` referencia `product_id`, `customer_id` y `order_id` como UUIDs.

### Autenticación

`IsAuthenticated` para crear; público para leer.

### Autorización

Cliente que haya comprado y recibido el producto.

### Validaciones

Validación de rango de rating (1-5), longitud mínima de comentario (10 caracteres) y verificación de compra entregada previa.

### Transacciones

Operación atómica obligatoria mediante `transaction.atomic()`. Garantiza que todas las mutaciones en la base de datos se confirmen de forma íntegra o se reviertan totalmente (Rollback) ante fallos.

### Casos límite

El cliente compró el producto pero el pedido aún está en estado `SHIPPED` (en camino) -> Debe rechazarse hasta que esté `DELIVERED`.

### Casos de error

`403 Forbidden` o `400 Bad Request` si el cliente nunca ha comprado el producto.

### Consideraciones de seguridad

Sanitización de comentarios para prevenir inyecciones de código HTML/JavaScript (XSS almacenado).

### Consideraciones de rendimiento

Índice compuesto sobre `(product_id, is_approved, -created_at)` en PostgreSQL.

### Fundamentos de Python relacionados

Filtros de validación y consultas booleanas. Tipado estricto con `typing` (`Optional`, `Dict`, `List`), decoradores, dataclasses, manejo estructurado de excepciones y programación modular.

### Conceptos Django relacionados

`models.CheckConstraint(check=Q(rating__gte=1, rating__lte=5))`, `models.UniqueConstraint(fields=['product_id', 'customer_id'])`.

### Conceptos DRF relacionados

Serializadores de reseñas con campos de solo lectura calculados por el servidor.

### PostgreSQL

`CREATE TABLE reviews_productreview (id UUID PRIMARY KEY, product_id UUID NOT NULL, customer_id UUID NOT NULL, rating SMALLINT NOT NULL CHECK (rating >= 1 AND rating <= 5), ...);`.

### Arquitectura

`apps/reviews` aísla el dominio de opiniones y reputación del catálogo.

### Dependencias entre módulos

`apps.reviews.services` consulta `apps.orders.selectors` para verificar compras entregadas.

### Antes de programar

1. ¿Por qué verificar la compra en el backend (`Verified Purchase`) es indispensable para la credibilidad de una tienda frente a ataques de spam o reseñas falsas?
2. ¿Por qué el `UniqueConstraint(fields=['product_id', 'customer_id'])` previene que un usuario califique 100 veces el mismo producto para alterar la puntuación?

### Pruebas mínimas

1. Cliente con orden entregada del producto crea una reseña de 5 estrellas -> Verificar `201 Created` y `is_verified_purchase = True`.
2. Consultar listado de reseñas del producto como anónimo y verificar que aparezca la reseña aprobada.

### Pruebas negativas

1. Cliente que nunca compró el producto intenta publicar una reseña -> Verificar rechazo `403/400` con mensaje explicativo.
2. Intentar enviar `rating = 6` o `rating = 0` -> Verificar rechazo de validación `400`.

### Documentación

Documentar las reglas de compra verificada y moderación en el README de `apps/reviews`.

### Explicación posterior

Explica cómo plataformas como Amazon implementan el sello 'Verified Purchase' y por qué la separación en un módulo `apps/reviews` permite evolucionar hacia moderación con IA sin tocar el módulo de catálogo.

### Aplicación profesional

Sistemas de reputación y reseñas en e-commerce, plataformas de cursos, apps de delivery y servicios turísticos.

### Reto adicional

Implementar un sistema de votos útiles '¿Te resultó útil esta reseña? (Sí / No)' modelando la entidad `ReviewHelpfulVote`.
