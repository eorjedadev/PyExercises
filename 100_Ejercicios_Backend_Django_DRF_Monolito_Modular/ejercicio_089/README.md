# Ejercicio 089 — Migración de Datos Compleja sin Downtime (Patrón Expand and Contract)

[← Ejercicio 088](../ejercicio_088/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 090 →](../ejercicio_090/README.md)

---

### Contexto de negocio

En la base de datos de producción con 1 millón de clientes, el campo `phone_number` fue creado originalmente como un entero `INTEGER` que no soporta códigos internacionales con el signo `+` ni ceros a la izquierda. Cambiar el tipo de columna directamente con `ALTER TABLE` bloquearía la tabla completa durante horas (Downtime) y rompería las versiones antiguas de la API que aún están procesando peticiones. Se requiere aplicar el patrón de migración sin downtime Expand and Contract (Parallel Run).

### Estado actual del sistema

Modelo `CustomerProfile` con campo `phone_number` antiguo en producción.

### Nueva necesidad

Diseñar una migración en 3 fases sin downtime: 1) **Expand**: Agregar la nueva columna `phone_number_e164` (VARCHAR) permitiendo que ambas coexistan y escribiendo en ambas. 2) **Backfill**: Migración de datos en background con `RunPython` en lotes. 3) **Contract**: Desacoplar el campo viejo y finalmente eliminar la columna obsoleta.

### Objetivo

Dominar las migraciones de bases de datos relacionales sin tiempo de inactividad (Zero-Downtime Migrations) en PostgreSQL con Django, aplicando el patrón Expand and Contract utilizado en sistemas de alta disponibilidad.

### Actor

Ingeniero de Base de Datos / Backend Senior

### Módulo responsable

`apps/customers` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`CustomerProfile`, migraciones secuenciales de Django, script de backfill en lotes.

### Reglas de negocio

1. Fase 1 (Expand): Agregar `phone_number_e164` como `VARCHAR(30)` con `null=True`. El servicio debe escribir en ambos campos simultáneamente (Dual Writing).
2. Fase 2 (Migración de datos): Script `RunPython` que convierta los enteros antiguos a formato string internacional en lotes de 1,000 registros para no saturar transacciones de PostgreSQL.
3. Fase 3 (Contract): Modificar el código para que solo lea y escriba del nuevo campo. En una versión posterior, eliminar la columna vieja con una migración DDL limpia.
4. Durante todo el proceso, la API debe permanecer 100% disponible sin interrumpir el servicio a los clientes.

### Contrato esperado

Evolución transparente de esquema en PostgreSQL con 0 segundos de interrupción de servicio.

### Persistencia

PostgreSQL: `ALTER TABLE ... ADD COLUMN ...;` -> `UPDATE ... WHERE ...;` -> `ALTER TABLE ... DROP COLUMN ...;`.

### Relaciones

`CustomerProfile`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Validación del nuevo formato internacional E.164.

### Transacciones

Migración de datos por lotes independientes con commits parciales para evitar bloqueos largos de tabla.

### Casos límite

Registros creados o actualizados por usuarios en producción mientras el script de backfill está corriendo (el patrón Dual Writing garantiza que los datos nuevos queden actualizados de inmediato).

### Casos de error

Rollback seguro si ocurre un fallo en una fase intermedia.

### Consideraciones de seguridad

Preservación de la integridad de los datos de contacto de los clientes.

### Consideraciones de rendimiento

Uso de lotes (`chunk_size=1000`) para no agotar la memoria ni saturar los logs de WAL de PostgreSQL.

### Fundamentos de Python relacionados

Procesamiento por lotes en Python con `itertools.islice` o slicing de QuerySets.

### Conceptos Django relacionados

`migrations.RunPython`, `schema_editor`, separación de migraciones de esquema y datos.

### Conceptos DRF relacionados

Serializadores que transicionan suavemente del campo viejo al nuevo.

### PostgreSQL

`ALTER TABLE customers_customerprofile ADD COLUMN phone_number_e164 VARCHAR(30);`.

### Arquitectura

Evolución controlada del esquema de persistencia en `apps/customers`.

### Dependencias entre módulos

Interno a `apps/customers`. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Por qué ejecutar un `ALTER TABLE customers_customerprofile ALTER COLUMN phone TYPE varchar(30);` directo en una tabla con millones de filas bloquea todas las lecturas y escrituras en PostgreSQL?
2. ¿Cuáles son las 3 fases del patrón Expand and Contract (Expandir, Migrar/Sincronizar, Contraer) y por qué garantiza cero downtime?

### Pruebas mínimas

1. Ejecutar la Fase 1 y verificar que el código pueda guardar clientes escribiendo en ambas columnas.
2. Ejecutar la migración de datos de la Fase 2 sobre registros existentes y comprobar que todos los teléfonos se conviertan al nuevo formato sin errores.
3. Ejecutar la Fase 3 y comprobar que el sistema opere exclusivamente sobre la nueva columna.

### Pruebas negativas

1. Verificar que ninguna consulta SQL durante la migración mantenga un bloqueo exclusivo de tabla por más de 100 milisegundos.

### Documentación

Documentar el plan de migración paso a paso en el runbook de operaciones de base de datos.

### Explicación posterior

Explica cómo empresas de alta disponibilidad (Stripe, GitHub, Netflix) realizan miles de cambios de esquema en bases de datos relacionales en producción cada mes sin interrumpir el servicio a sus usuarios mediante el patrón Expand and Contract.

### Aplicación profesional

Mantenimiento de bases de datos relacionales en sistemas críticos 24/7/365 donde el downtime no es una opción.

### Reto adicional

Escribir la función reversible `reverse_code` en la migración de datos para permitir volver atrás limpiamente si fuera necesario.
