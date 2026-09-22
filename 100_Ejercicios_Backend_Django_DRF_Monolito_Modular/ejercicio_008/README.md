# Ejercicio 008 — Restricciones de Integridad en PostgreSQL con CheckConstraint

[← Ejercicio 007](../ejercicio_007/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 009 →](../ejercicio_009/README.md)

---

### Contexto de negocio

Para garantizar que ninguna anomalía de concurrencia o script manual pueda corromper los datos financieros del catálogo, el equipo de auditoría exige que las reglas numéricas críticas se apliquen como restricciones físicas a nivel de motor de base de datos en PostgreSQL, además de las validaciones en Python.

### Estado actual del sistema

Modelos `Product`, `Category` y `Tag` creados en `apps/catalog`.

### Nueva necesidad

Agregar restricciones de base de datos (`CheckConstraint`) en el modelo `Product` para garantizar que el precio sea estrictamente mayor a cero y el peso sea mayor o igual a cero.

### Objetivo

Comprender el rol de las restricciones de base de datos (`CHECK`) en PostgreSQL, su definición mediante `models.CheckConstraint(condition=Q(...))` y cómo se integran con el ORM de Django.

### Actor

Ingeniero de Datos / Desarrollador Backend

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Product` (restricciones en `Meta.constraints`).

### Reglas de negocio

1. El campo `price_amount` debe ser estrictamente mayor a 0 (`price_amount > 0`).
2. El campo `weight_grams` debe ser mayor o igual a 0 (`weight_grams >= 0`).
3. La moneda `currency` debe ser exactamente de 3 caracteres en mayúsculas.
4. Estas reglas deben ser invariantes y no poder ser burladas mediante `bulk_create` o queries directas en SQL.

### Contrato esperado

Verificación a nivel de migración DDL de PostgreSQL y rechazo a nivel de base de datos.

### Persistencia

Restricciones `CHECK (price_amount > 0)` y `CHECK (weight_grams >= 0)` en tabla `catalog_products`.

### Relaciones

`Product`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Doble capa: Validación en serializers (Python) y `CheckConstraint` (PostgreSQL).

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Uso de `Product.objects.bulk_create()` con datos corruptos (el ORM no ejecuta `clean()`, pero PostgreSQL abortará la transacción).

### Casos de error

`IntegrityError` (o `CheckViolation` de psycopg) si se intenta violar el constraint en base de datos.

### Consideraciones de seguridad

Defensa en profundidad: la base de datos es la última línea de defensa contra la corrupción de datos.

### Consideraciones de rendimiento

Los `CheckConstraints` en PostgreSQL tienen un impacto de CPU despreciable en inserciones y evitan lecturas de datos inconsistentes.

### Fundamentos de Python relacionados

Operadores lógicos con objetos `Q` de Django (`Q(price_amount__gt=0)`).

### Conceptos Django relacionados

`models.CheckConstraint`, `models.Q`, `Meta.constraints`, generación e inspección de migraciones SQL (`sqlmigrate`).

### Conceptos DRF relacionados

Mapeo de excepciones de integridad en respuestas de error limpias.

### PostgreSQL

`ALTER TABLE catalog_products ADD CONSTRAINT check_positive_price CHECK (price_amount > 0)`.

### Arquitectura

Las restricciones de integridad física residen en la definición del modelo en `apps/catalog/models.py`.

### Dependencias entre módulos

Interno a `apps/catalog`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué validar solo en el serializer o en `clean()` es insuficiente en sistemas con alta concurrencia o procesos batch?
2. ¿Cómo inspeccionar el SQL exacto que generará una migración de Django antes de aplicarla?

### Pruebas mínimas

1. Crear un producto con precio `10.00` y peso `100` -> Inserción exitosa.
2. Inspeccionar el esquema de PostgreSQL mediante `\d catalog_products` y verificar que figuren las cláusulas `Check constraints`.

### Pruebas negativas

1. Ejecutar `Product.objects.create(sku='TEST-01', name='Test', price_amount=Decimal('-5.00'))` -> Verificar que PostgreSQL lance `IntegrityError`.

### Documentación

Documentar en el archivo de diseño del módulo todas las restricciones CHECK activas.

### Explicación posterior

Explica qué diferencia existe entre `sqlmigrate` y `migrate`, y por qué revisar el SQL generado es fundamental en entornos profesionales.

### Aplicación profesional

Sistemas financieros, contables e inventarios donde no puede existir saldo negativo bajo ninguna circunstancia.

### Reto adicional

Agregar un `CheckConstraint` que garantice que si `is_active` es `True`, el campo `description` no puede ser nulo ni una cadena vacía.
