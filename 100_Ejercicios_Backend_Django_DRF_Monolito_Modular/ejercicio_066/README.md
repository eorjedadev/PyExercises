# Ejercicio 066 — Uso Avanzado de Campos JSON (JSONField) y Consultas Semiestructuradas

[← Ejercicio 065](../ejercicio_065/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 067 →](../ejercicio_067/README.md)

---

### Contexto de negocio

En el catálogo existen productos con atributos altamente variables según su categoría (ej. una Laptop tiene `{"ram_gb": 16, "processor": "i7", "ports": ["USB-C", "HDMI"]}`; mientras que una Camiseta tiene `{"size": "L", "material": "100% Algodón", "gender": "Unisex"}`). Crear 50 tablas relacionales para cada posible atributo generaría sobreingeniería. Se requiere utilizar `models.JSONField` de PostgreSQL con consultas y filtros semiestructurados.

### Estado actual del sistema

Modelo `Product` en `apps/catalog`. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Agregar el campo `attributes = models.JSONField(default=dict, blank=True)` al modelo `Product`, crear endpoints para filtrar productos por claves JSON internas (ej. `?attributes__ram_gb__gte=16`), y agregar un índice GIN en PostgreSQL para acelerar búsquedas JSON.

### Objetivo

Dominar el uso de `JSONField` (almacenamiento binario JSONB) en PostgreSQL con Django, aprendiendo a consultar rutas internas de objetos JSON, operadores de contención (`contains`, `has_key`) y cuándo elegir JSON vs tablas relacionales normalizadas.

### Actor

Operador de Catálogo / Cliente que filtra por atributos específicos

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Product` (campo `attributes` JSONField), `django.contrib.postgres.indexes.GinIndex`, `ProductFilterSet`.

### Reglas de negocio

1. El campo `attributes` debe almacenar un objeto JSON estructurado válido (diccionario).
2. Se debe permitir filtrar productos por atributos dinámicos: `GET /api/v1/catalog/products/?attributes__ram_gb=16`.
3. Se debe crear un índice `GinIndex(fields=['attributes'])` en PostgreSQL para que las consultas por atributos JSONB sean ultrarrápidas.
4. El serializer debe validar que los atributos no contengan claves maliciosas o tipos no serializables.

### Contrato esperado

Crear Producto con Atributos Variables:
- `POST /api/v1/catalog/products/`
  Body:
  ```json
  {
    "sku": "LAP-PRO-16",
    "name": "Laptop Ultra",
    "price_amount": "1500.00",
    "attributes": {
      "ram_gb": 16,
      "storage_ssd_gb": 512,
      "screen_size_inches": 15.6,
      "features": ["Backlit Keyboard", "Fingerprint"]
    }
  }
  ```

### Persistencia

Columna de tipo `JSONB` en la tabla `catalog_products` de PostgreSQL con índice GIN.

### Relaciones

`Product`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

`IsAuthenticated` para crear; público para consultar.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Filtrar por una clave JSON que no existe en algunos productos (el ORM debe retornar solo los productos que tengan la clave con ese valor sin lanzar error SQL).

### Casos de error

`400 Bad Request` si el campo `attributes` no es un objeto JSON válido.

### Consideraciones de seguridad

Sanitizar claves y valores en el payload JSON.

### Consideraciones de rendimiento

PostgreSQL almacena `JSONB` en formato binario descompuesto, permitiendo indexación GIN de claves y valores sin necesidad de parsear texto.

### Fundamentos de Python relacionados

Manipulación profunda de diccionarios, introspección de esquemas.

### Conceptos Django relacionados

`models.JSONField`, sintaxis de consulta por ruta (`attributes__ram_gb=16`, `attributes__features__contains=['HDMI']`), `GinIndex`.

### Conceptos DRF relacionados

Diseño de contratos REST con `serializers.Serializer` / `ModelSerializer`, vistas delegadoras `APIView` o `GenericAPIView`, normalización de respuestas JSON y documentación declarativa con `@extend_schema`.

### PostgreSQL

`SELECT * FROM catalog_products WHERE attributes->>'ram_gb' = '16'; CREATE INDEX idx_prod_attrs ON catalog_products USING gin (attributes);`.

### Arquitectura

El módulo `apps/catalog` utiliza JSONB para atributos dinámicos sin romper el esquema relacional central.

### Dependencias entre módulos

Interno a `apps/catalog`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Cuál es la diferencia técnica fundamental entre `JSON` (texto plano) y `JSONB` (binario indexable) en PostgreSQL?
2. ¿Cuándo es correcto usar `JSONField` y cuándo es un error grave que debería modelarse como tablas relacionales normalizadas?

### Pruebas mínimas

1. Crear 2 productos con diferentes atributos JSON, filtrar por `attributes__ram_gb=16` y verificar que solo devuelva el producto correspondiente.
2. Filtrar por contención de lista `attributes__features__contains=['Fingerprint']` y verificar resultado.

### Pruebas negativas

1. Enviar un string plano o número en lugar de un diccionario en el campo `attributes` -> Verificar rechazo `400 Bad Request`.

### Documentación

Documentar los esquemas recomendados de atributos por categoría en el README de catálogo.

### Explicación posterior

Explica el balance entre el modelo relacional tradicional y el modelo documental (NoSQL) dentro de una única base de datos gracias al soporte nativo de JSONB en PostgreSQL.

### Aplicación profesional

Catálogos de productos con atributos heterogéneos, almacenamiento de configuraciones de usuario, payloads de eventos y metadatos flexibles.

### Reto adicional

Implementar una validación de esquema JSON usando `jsonschema` en Python dentro del serializer según la categoría del producto.
