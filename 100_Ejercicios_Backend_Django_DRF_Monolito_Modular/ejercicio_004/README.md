# Ejercicio 004 — Validaciones de Formato vs Validaciones de Dominio en Serializers

[← Ejercicio 003](../ejercicio_003/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 005 →](../ejercicio_005/README.md)

---

### Contexto de negocio

El equipo de operaciones ha detectado productos con nombres basura (ej. caracteres repetidos), SKUs con caracteres especiales inválidos y precios incongruentes. Se requiere un sistema de validaciones estricto que rechace datos inválidos antes de que toquen la base de datos.

### Estado actual del sistema

Serializers básicos de `Product` creados en `apps/catalog`.

### Nueva necesidad

Implementar validadores a nivel de campo (`validate_<field>`), validadores a nivel de objeto (`validate()`) y validadores reutilizables para garantizar integridad.

### Objetivo

Aprender a estructurar validaciones en DRF distinguiendo validaciones sintácticas de formato y reglas de negocio del módulo de catálogo.

### Actor

Cliente de API de Catálogo autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Product`, `ProductCreateInputSerializer`.

### Reglas de negocio

1. El SKU debe tener entre 6 y 20 caracteres, compuesto solo por letras mayúsculas, números y guiones medios (ej. `ABC-123-XYZ`).
2. El nombre debe tener al menos 3 caracteres significativos y no puede contener solo espacios o símbolos.
3. Si el precio es mayor a $10,000.00 USD, se requiere obligatoriamente una descripción de más de 50 caracteres (regla de productos de alto valor).

### Contrato esperado

Petición inválida:
- `POST /api/v1/catalog/products/`
  Request Body: `{"sku": "invalid sku!", "name": "A", "price_amount": "15000.00", "description": "Short"}`
  Response: `400 Bad Request`
  ```json
  {
    "sku": ["El SKU solo puede contener letras mayúsculas, números y guiones (ej. ABC-123)."],
    "name": ["El nombre debe tener al menos 3 caracteres."],
    "non_field_errors": ["Productos de más de $10,000 requieren una descripción detallada de al menos 50 caracteres."]
  }
  ```

### Persistencia

No se realiza persistencia si las validaciones fallan.

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

Acceso público desatendido (`permissions.AllowAny`). No requiere cabeceras Bearer; la seguridad perimetral se basa en validación de payloads, firmas criptográficas o rate limiting.

### Autorización

Acceso irrestricto a nivel de endpoint (`permissions.AllowAny`). Cualquier consumidor puede consultar la información pública sin privilegios especiales.

### Validaciones

Validadores de campo `validate_sku`, `validate_name` y validador cruzado `validate(attrs)`.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

SKU en minúsculas (debe normalizarse automáticamente a mayúsculas o rechazarse explícitamente según la regla elegida).

### Casos de error

`400 Bad Request` con detalle estructurado por campo.

### Consideraciones de seguridad

Sanitización de cadenas de texto para prevenir inyecciones de control o caracteres no imprimibles.

### Consideraciones de rendimiento

Validaciones de CPU rápidas en Python antes de realizar cualquier llamada a base de datos.

### Fundamentos de Python relacionados

Expresiones regulares (`re.match`), manipulación de cadenas (`strip()`, `upper()`), lanzamiento de excepciones `serializers.ValidationError`.

### Conceptos Django relacionados

`core.validators.RegexValidator`, mensajes de error personalizados.

### Conceptos DRF relacionados

`validate_<fieldname>()`, `validate()`, `serializers.ValidationError`, estructura de errores en `serializer.errors`.

### PostgreSQL

La base de datos queda protegida de recibir datos incongruentes.

### Arquitectura

Las validaciones de formato residen en el serializer; las validaciones complejas entre múltiples entidades pertenecerán a servicios en etapas posteriores.

### Dependencias entre módulos

Interno a `apps/catalog`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Cuándo debe utilizarse `validate_<field>` y cuándo es obligatorio usar `validate(self, attrs)`?
2. ¿Por qué es una mala práctica capturar y transformar errores de validación en la vista en lugar de dejar que el serializer los estructure?

### Pruebas mínimas

1. Probar un payload con SKU `PROD-001-A`, nombre válido y precio normal -> `is_valid()` es `True`.
2. Probar precio `15000.00` con descripción de 60 caracteres -> `is_valid()` es `True`.

### Pruebas negativas

1. Probar SKU `invalid_sku` (minúsculas y guión bajo) -> `is_valid()` es `False` con error en `sku`.
2. Probar precio `15000.00` con descripción corta -> `is_valid()` es `False` con error en `non_field_errors`.

### Documentación

Documentar los formatos de validación y expresiones regulares admitidas para cada campo en el módulo.

### Explicación posterior

Explica el orden en que DRF ejecuta las validaciones: campos individuales, validadores de campo, validadores a nivel de serializer y método `validate()` general.

### Aplicación profesional

Construcción de APIs con retroalimentación instantánea y precisa a clientes de integración y aplicaciones móviles.

### Reto adicional

Crear un validador reutilizable basado en clase `AlphanumericCodeValidator` que reciba longitud mínima y máxima como parámetros.
