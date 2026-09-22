# Ejercicio 003 — Contrato REST y Serialización con Serializer vs ModelSerializer

[← Ejercicio 002](../ejercicio_002/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 004 →](../ejercicio_004/README.md)

---

### Contexto de negocio

El equipo de frontend necesita consumir los datos del catálogo mediante una API REST. El backend debe exponer un endpoint para listar y crear productos, asegurando una separación clara entre la estructura de persistencia en base de datos y la representación JSON expuesta al cliente.

### Estado actual del sistema

Modelo `Product` implementado y migrado en PostgreSQL dentro de `apps/catalog`.

### Nueva necesidad

Implementar serializers en `apps/catalog/serializers.py` para transformar datos entre JSON y modelos, controlando campos de solo lectura y formatos de salida.

### Objetivo

Construir serializers claros para lectura (`ProductDetailOutputSerializer`) y escritura (`ProductCreateInputSerializer`), comprendiendo el balance entre `serializers.Serializer` explícito y `serializers.ModelSerializer`.

### Actor

Cliente HTTP / Frontend Web autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Product`, Serializers de DRF (`ProductCreateInputSerializer`, `ProductOutputSerializer`).

### Reglas de negocio

1. El cliente no puede enviar el `id`, `slug`, `created_at` ni `updated_at`; son campos calculados o generados por el servidor.
2. El precio debe devolverse como cadena numérica formateada con 2 decimales ('199.99') para evitar truncamientos en clientes JavaScript.
3. La salida debe incluir un campo calculado `is_in_stock` (booleano) basado en las reglas del producto.

### Contrato esperado

Crear Producto:
- `POST /api/v1/catalog/products/`
  Request Body:
  ```json
  {
    "sku": "TECH-MOU-001",
    "name": "Wireless Gaming Mouse",
    "description": "Optical sensor with 16000 DPI",
    "price_amount": "49.90",
    "currency": "USD",
    "weight_grams": 120
  }
  ```
  Response: `201 Created`
  ```json
  {
    "id": "b3c1d2e4-5678-4a9b-8c1d-123456789abc",
    "sku": "TECH-MOU-001",
    "name": "Wireless Gaming Mouse",
    "slug": "wireless-gaming-mouse",
    "description": "Optical sensor with 16000 DPI",
    "price_amount": "49.90",
    "currency": "USD",
    "weight_grams": 120,
    "is_active": true,
    "created_at": "2026-09-22T10:00:00Z"
  }
  ```

### Persistencia

Persistencia en `catalog_products` mediante `Product.objects.create()` tras la validación.

### Relaciones

Entidad `Product` individual. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

Validación de tipos de datos, obligatoriedad de `sku`, `name`, `price_amount`.

### Transacciones

No requerida para inserción simple de una sola fila.

### Casos límite

Cuerpo JSON vacío `{}` o envío de campos inesperados/maliciosos no declarados en el serializer.

### Casos de error

`400 Bad Request` con estructura JSON detallando los campos inválidos.

### Consideraciones de seguridad

Evitar Mass Assignment: no permitir que el cliente fuerce valores en campos de auditoría (`created_at`) o IDs mediante el payload.

### Consideraciones de rendimiento

Uso de serializers ligeros evitando campos anidados innecesarios en listados masivos.

### Fundamentos de Python relacionados

Diccionarios, desempaquetado de kwargs (`**validated_data`), métodos `to_representation`.

### Conceptos Django relacionados

`utils.text.slugify`, ciclo de vida de guardado en el ORM.

### Conceptos DRF relacionados

`serializers.Serializer`, `serializers.ModelSerializer`, `read_only_fields`, `validated_data`, `is_valid()`.

### PostgreSQL

Inserción `INSERT INTO catalog_products ...` y retorno de fila generada.

### Arquitectura

Los serializers residen en `apps/catalog/serializers.py` y solo definen contratos de entrada/salida de este módulo.

### Dependencias entre módulos

Interno a `apps/catalog`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué usar serializers separados para lectura y escritura ayuda a mantener contratos limpios y seguros?
2. ¿Qué ocurre si un cliente envía un campo adicional que no existe en el serializer?

### Pruebas mínimas

1. Serializar una instancia de `Product` y comprobar que todos los campos del contrato estén presentes en el diccionario resultante.
2. Deserializar un payload válido y verificar que `serializer.is_valid()` sea `True`.

### Pruebas negativas

1. Deserializar un payload sin el campo obligatorio `name` y comprobar que `serializer.errors` contenga `'name'` con mensaje de requerido.

### Documentación

Documentar el esquema de entrada y salida esperado en el archivo de contratos de `apps/catalog`.

### Explicación posterior

Explica qué diferencia existe entre `serializer.validated_data` y `serializer.data`, y en qué momento se ejecuta la transformación de cada uno.

### Aplicación profesional

Diseño de APIs robustas donde el contrato público está desacoplado del esquema interno de la base de datos.

### Reto adicional

Agregar un serializador de resumen (`ProductListSummarySerializer`) que solo incluya `id`, `sku`, `name` y `price_amount` para optimizar ancho de banda.
