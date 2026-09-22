# Ejercicio 009 — Migraciones de Esquema y Migraciones de Datos con RunPython

[← Ejercicio 008](../ejercicio_008/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 010 →](../ejercicio_010/README.md)

---

### Contexto de negocio

El sistema lleva tiempo operando y existen cientos de productos en la base de datos de producción. El negocio decide agregar un campo obligatorio `short_code` al modelo `Product`. No se puede simplemente agregar `null=False` porque fallarían las filas existentes. Se requiere una migración en 3 pasos con migración de datos intermedia (`RunPython`).

### Estado actual del sistema

Modelo `Product` con registros existentes en PostgreSQL.

### Nueva necesidad

Implementar una migración de esquema y datos segura: 1) Agregar `short_code` con `null=True`, 2) Script `RunPython` que genere un código único para cada producto existente, 3) Modificar `short_code` a `null=False` y `unique=True`.

### Objetivo

Dominar el ciclo de vida de migraciones complejas en Django, migraciones de datos con `migrations.RunPython`, funciones reversibles y preservación de datos en producción.

### Actor

Desarrollador Backend / Ingeniero de DevOps

### Módulo responsable

`apps/catalog` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Product`, archivos de migración de Django.

### Reglas de negocio

1. El campo `short_code` debe tener exactamente 8 caracteres alfanuméricos únicos en mayúsculas.
2. Todos los productos existentes deben recibir un `short_code` generado determinista o pseudoaleatoriamente sin colisiones.
3. La migración debe poder ejecutarse en producción sin downtime y debe ser reversible (`reverse_code`).

### Contrato esperado

Comandos `makemigrations`, edición de archivo de migración y ejecución limpia de `migrate`.

### Persistencia

Actualización masiva de registros existentes en la tabla `catalog_products` de PostgreSQL.

### Relaciones

`Product`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

Las migraciones de datos en PostgreSQL se ejecutan dentro de una transacción DDL/DML atómica.

### Casos límite

Colisión accidental de códigos generados durante el bucle de migración (debe resolverse con reintentos).

### Casos de error

Fallo de migración y rollback automático si ocurre un error en el script de datos.

### Consideraciones de seguridad

No importar modelos directamente desde `apps.catalog.models` en migraciones; usar siempre `apps.get_model('catalog', 'Product')` para evitar discrepancias de versiones históricas.

### Consideraciones de rendimiento

Usar `bulk_update` o iteración con lotes (`iterator()`) si existen decenas de miles de productos.

### Fundamentos de Python relacionados

Generación de strings aleatorios con `secrets` o `uuid`, manipulación de funciones como parámetros de primer orden.

### Conceptos Django relacionados

`migrations.RunPython`, `apps.get_model()`, `schema_editor`, dependencias entre migraciones.

### Conceptos DRF relacionados

No aplica directamente en migraciones de base de datos.

### PostgreSQL

`ALTER TABLE catalog_products ADD COLUMN short_code VARCHAR(8);` -> `UPDATE ...` -> `ALTER TABLE catalog_products ALTER COLUMN short_code SET NOT NULL;`

### Arquitectura

Las migraciones forman parte del historial inmutable del módulo `apps/catalog`.

### Dependencias entre módulos

Interno a `apps/catalog`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué nunca se debe hacer `from apps.catalog.models import Product` dentro de un archivo de migración?
2. ¿Qué ocurre si una migración de datos falla a mitad de ejecución en PostgreSQL?

### Pruebas mínimas

1. Crear productos de prueba sin `short_code`, ejecutar la migración y verificar que todos los productos tengan un `short_code` único de 8 caracteres.
2. Revertir la migración con `python manage.py migrate catalog <migration_anterior>` y comprobar que el esquema vuelva a su estado previo.

### Pruebas negativas

1. Intentar insertar manualmente un producto con `short_code` duplicado tras la migración y verificar que PostgreSQL lo rechace.

### Documentación

Documentar en el changelog del módulo el proceso de migración de datos y su impacto en datos históricos.

### Explicación posterior

Explica cómo funciona el historial de migraciones en la tabla `django_migrations` de PostgreSQL y por qué nunca se deben borrar archivos de migración ya desplegados en producción.

### Aplicación profesional

Mantenimiento y evolución de esquemas de bases de datos relacionales en sistemas corporativos de alta disponibilidad.

### Reto adicional

Modificar el script `RunPython` para procesar los registros en lotes de 100 usando `bulk_update(products_to_update, ['short_code'])` para máxima velocidad.
