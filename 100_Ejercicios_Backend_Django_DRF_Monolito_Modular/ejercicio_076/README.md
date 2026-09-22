# Ejercicio 076 — Auditoría de Cohesión y Acoplamiento en el Monolito Modular

[← Ejercicio 075](../ejercicio_075/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 077 →](../ejercicio_077/README.md)

---

### Contexto de negocio

A medida que el sistema alcanza 8 módulos de negocio (`users`, `customers`, `catalog`, `orders`, `inventory`, `payments`, `notifications`, `billing`), el equipo técnico debe realizar una auditoría formal de dependencias. Se debe garantizar que cada módulo tenga alta cohesión interna (sus clases y funciones cambian juntas por la misma razón) y bajo acoplamiento externo (conocen lo mínimo indispensable de otros módulos).

### Estado actual del sistema

Múltiples módulos interactuando en el monolito.

### Nueva necesidad

Crear un informe de auditoría arquitectónica en `MAPA_ARQUITECTURA.md`, mapear la matriz de dependencias permitidas entre módulos, identificar violaciones de límites (fugas de abstracción) y corregir dependencias inadecuadas.

### Objetivo

Desarrollar criterio arquitectónico senior para evaluar la salud de un monolito modular, aplicando los principios de Alta Cohesión y Bajo Acoplamiento para mantener el sistema mantenible a largo plazo.

### Actor

Arquitecto de Software / Tech Lead responsable del diseño y mantenimiento del monolito modular.

### Módulo responsable

Transversal en todas las `apps/` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

Matriz de dependencias inter-módulo, interfaces públicas en `services.py` y `selectors.py`.

### Reglas de negocio

1. Cada módulo debe tener una única responsabilidad de negocio claramente definida.
2. Un módulo solo puede interactuar con otro módulo a través de sus servicios públicos (`services.py`) o selectores públicos (`selectors.py`), NUNCA accediendo directamente a modelos internos o tablas de persistencia de otro módulo.
3. La carpeta `apps/core` o `common` NO debe ser un cajón de sastre; solo debe albergar código agnóstico al negocio (middlewares, pagination, exception handling).
4. Si un módulo A necesita datos del módulo B, debe recibir DTOs, diccionarios o IDs escalares tipados, no instancias acopladas de ORM.

### Contrato esperado

Matriz de dependencias actualizada en `MAPA_ARQUITECTURA.md` y suite de tests validando aislamiento.

### Persistencia

No aplica cambios de esquema relacional. Persistencia física garantizada mediante tablas relacionales en PostgreSQL, con tipos de datos nativos e integridad referencial protegida.

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Validación en múltiples capas: validación sintáctica de tipos y presencia en Serializers de DRF, validación semántica de reglas de negocio en la Capa de Servicios y restricciones `CheckConstraint` en PostgreSQL.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Módulos que necesitan compartir un concepto común (debe extraerse una entidad abstracta o comunicarse mediante identificadores universales UUID).

### Casos de error

- `400 Bad Request`: Payload JSON malformado o campos requeridos ausentes.
- `401 Unauthorized`: Token JWT expirado, revocado o ausente.
- `403 Forbidden`: Usuario sin permisos suficientes para la acción.
- `404 Not Found`: Identificador de recurso inexistente.
- `409 Conflict` / `422 Unprocessable`: Violación de invariantes de negocio o concurrencia.
- `500 Internal Server Error`: Errores no controlados capturados por el exception handler global.

### Consideraciones de seguridad

El aislamiento modular reduce la superficie de ataque y previene efectos secundarios imprevistos en seguridad.

### Consideraciones de rendimiento

Módulos desacoplados permiten optimizar consultas individualmente sin impacto en el resto del sistema.

### Fundamentos de Python relacionados

Diseño orientado a objetos (SOLID), análisis estático de dependencias.

### Conceptos Django relacionados

Organización modular de aplicaciones Django, arquitectura por capas.

### Conceptos DRF relacionados

Diseño de contratos REST con `serializers.Serializer` / `ModelSerializer`, vistas delegadoras `APIView` o `GenericAPIView`, normalización de respuestas JSON y documentación declarativa con `@extend_schema`.

### PostgreSQL

Alineación con el motor relacional PostgreSQL 16: tipos de datos nativos (`UUID`, `NUMERIC`, `TIMESTAMPTZ`, `JSONB`), índices B-Tree compuestos y garantías transaccionales ACID en nivel de aislamiento `READ COMMITTED`.

### Arquitectura

Consolidación de la Arquitectura Monolítica Modular.

### Dependencias entre módulos

Revisión exhaustiva de todos los imports entre `apps/`.

### Antes de programar

1. ¿Por qué poder hacer `import any_model from any_app` en Django es una trampa peligrosa que convierte monolitos en sistemas espagueti inmanejables?
2. ¿Cuál es la diferencia entre acoplamiento por datos (compartir un UUID) y acoplamiento por estructura (importar clases de modelo con sus métodos)?

### Pruebas mínimas

1. Verificar que ningún módulo de `apps/` importe modelos de persistencia de otro módulo directamente en sus vistas o serializadores.
2. Comprobar que todas las interacciones inter-módulo se realicen a través de `services` o `selectors` públicos.

### Pruebas negativas

1. Detectar e impedir cualquier import circular o dependencia bidireccional entre módulos.

### Documentación

Actualizar el documento `MAPA_ARQUITECTURA.md` con la tabla de dependencias permitidas y prohibidas.

### Explicación posterior

Explica cómo el Monolito Modular ofrece las ventajas de modularidad y límites claros de los microservicios, pero sin la complejidad operativa, costos de infraestructura ni latencia de red de los sistemas distribuidos.

### Aplicación profesional

Liderazgo técnico en equipos de ingeniería, gobernanza de arquitectura de software y prevención de deuda técnica.

### Reto adicional

Escribir un script de análisis estático con `importlinter` o `pytest` que falle automáticamente si un módulo realiza un import no autorizado de otro módulo.
