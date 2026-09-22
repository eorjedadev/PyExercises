# Ejercicio 058 — Centralización de Parámetros Globales y Configuración Dinámica de Negocio

[← Ejercicio 057](../ejercicio_057/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 059 →](../ejercicio_059/README.md)

---

### Contexto de negocio

Existen parámetros de negocio que cambian frecuentemente y que no deberían requerir un nuevo despliegue de código ni reinicio de servidores cada vez que se modifican: tasa de impuestos por defecto (ej. 18%), monto mínimo para envío gratuito (ej. $100.00), tiempo límite para pagar un pedido antes de cancelarlo (ej. 12 horas), y mensaje global de banner de mantenimiento. Se requiere un módulo de configuración dinámica de negocio.

### Estado actual del sistema

Parámetros de negocio dispersos en constantes de código o `settings.py` estático.

### Nueva necesidad

Crear el módulo `apps/business_settings`, modelar `GlobalSetting` (clave-valor tipado en base de datos con caché en memoria) y exponer endpoints para que administradores consulten y modifiquen parámetros en tiempo real.

### Objetivo

Diseñar un sistema de configuración dinámica de negocio en Django, implementando caché para evitar consultas repetitivas a la base de datos y tipado seguro de valores (enteros, decimales, booleanos, strings, JSON).

### Actor

Administrador del Sistema / Servicios de Negocio

### Módulo responsable

`apps/business_settings` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`GlobalSetting` (`key` VARCHAR unique, `value_type`, `raw_value`, `description`, `updated_at`), servicio `get_setting(key, default)`, `set_setting(key, value)`.

### Reglas de negocio

1. Las claves de configuración deben ser identificadores únicos en mayúsculas (ej. `TAX_RATE_PERCENTAGE`, `FREE_SHIPPING_MIN_AMOUNT`).
2. Los tipos soportados son: `STRING`, `INTEGER`, `DECIMAL`, `BOOLEAN`, `JSON`.
3. La función `get_setting(key)` debe consultar primero la caché en memoria de Django; si no está, consultar PostgreSQL y guardar en caché con TTL de 1 hora.
4. Cuando un Administrador actualiza un parámetro mediante la API, la caché de esa clave debe invalidarse inmediatamente (`cache.delete`).

### Contrato esperado

1. Obtener Parámetro en Servicio Interno:
```python
tax_rate = get_setting('TAX_RATE_PERCENTAGE', default=Decimal('18.00'))
```

2. Actualizar Parámetro (Solo Admin):
- `PUT /api/v1/business-settings/FREE_SHIPPING_MIN_AMOUNT/`
  Body: `{"value": "150.00"}`
  Response: `200 OK`

### Persistencia

Tabla `business_settings_globalsetting` en PostgreSQL y almacenamiento en caché de Django.

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Solo rol `ADMIN` para modificar; cualquier servicio puede leer internamente.

### Validaciones

Validar que el `raw_value` sea convertible al `value_type` declarado (ej. validar que un `DECIMAL` sea un número válido).

### Transacciones

Transacción atómica al actualizar en base de datos e invalidar caché.

### Casos límite

Clave solicitada no existe en base de datos (debe devolver el `default` provisto sin fallar).

### Casos de error

`400 Bad Request` si se intenta guardar un valor incompatible con el tipo; `403 Forbidden` a no administradores.

### Consideraciones de seguridad

No usar este módulo para almacenar secretos criptográficos o contraseñas; solo parámetros de negocio.

### Consideraciones de rendimiento

99.9% de las lecturas se resuelven desde memoria RAM mediante la caché de Django, reduciendo la carga en PostgreSQL a cero.

### Fundamentos de Python relacionados

Conversión dinámica de tipos (`int(val)`, `Decimal(val)`, `json.loads(val)`), tipado genérico con `TypeVar`.

### Conceptos Django relacionados

`django.core.cache.cache`, métodos `cache.get`, `cache.set`, `cache.delete`.

### Conceptos DRF relacionados

Vistas de gestión de configuraciones para el panel administrativo.

### PostgreSQL

`CREATE TABLE business_settings_globalsetting (key VARCHAR(100) PRIMARY KEY, value_type VARCHAR(20) NOT NULL, raw_value TEXT NOT NULL, ...)`.

### Arquitectura

`apps/business_settings` provee una utilidad centralizada de parámetros de dominio para todo el monolito.

### Dependencias entre módulos

Cualquier módulo puede invocar `apps.business_settings.services.get_setting`.

### Antes de programar

1. ¿Por qué tener que desplegar una nueva versión de código y reiniciar servidores solo para cambiar el costo de envío de $10 a $12 es ineficiente?
2. ¿Por qué es crítico invalidar la caché inmediatamente cuando se actualiza un valor en la base de datos?

### Pruebas mínimas

1. Definir un parámetro `FREE_SHIPPING_MIN_AMOUNT` con valor `100.00`, invocar `get_setting` -> Verificar que retorne un objeto `Decimal('100.00')`.
2. Actualizar el valor a `150.00` mediante el endpoint de admin y verificar que la siguiente llamada a `get_setting` devuelva el nuevo valor actualizado.

### Pruebas negativas

1. Intentar asignar el valor `'texto'` a un parámetro de tipo `INTEGER` -> Verificar fallo de validación `400 Bad Request`.

### Documentación

Documentar la lista de claves de configuración globales disponibles en la guía de operaciones.

### Explicación posterior

Explica el patrón Feature Flags / Dynamic Configuration y cómo el balance entre persistencia en base de datos y capas de caché en memoria optimiza tanto la flexibilidad operativa como el rendimiento.

### Aplicación profesional

Sistemas de e-commerce en temporadas de ofertas, plataformas bancarias con límites transaccionales dinámicos y paneles de control SaaS.

### Reto adicional

Agregar soporte para `FeatureFlag` booleano que permita encender o apagar módulos completos del sistema en tiempo real.
