# Ejercicio 056 — Refactorización: Extracción de Lógica de Vistas Sobrecargadas a Servicios Puros

[← Ejercicio 055](../ejercicio_055/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 057 →](../ejercicio_057/README.md)

---

### Contexto de negocio

El sistema ha acumulado deuda técnica en un módulo legado: una vista contiene más de 200 líneas de código con consultas ORM manuales, cálculos matemáticos, transacciones mezcladas, llamadas HTTP y formateo de respuestas. Esta 'Vista Gorda' (Fat View) es imposible de probar unitariamente sin simular peticiones HTTP y contiene código duplicado. Se requiere realizar una refactorización arquitectónica profesional hacia Servicios Puros.

### Estado actual del sistema

Módulo legado con vista sobrecargada identificada para refactorización.

### Nueva necesidad

Identificar las responsabilidades de la vista, extraer la lógica de negocio a funciones puras en `services.py`, extraer las consultas a `selectors.py` y dejar la vista como un controlador delgado de menos de 15 líneas.

### Objetivo

Dominar la técnica de refactorización de código legado en Django/DRF, reduciendo la complejidad ciclomática de las vistas y mejorando drásticamente la mantenibilidad y testabilidad del sistema.

### Actor

Desarrollador Backend / Refactorizador responsable del diseño y mantenimiento del monolito modular.

### Módulo responsable

`Módulo bajo refactorización` como módulo de negocio responsable de la capacidad.

### Entidades involucradas

Vista sobrecargada original vs nueva arquitectura: `View` (delgada) -> `Serializer` (contrato) -> `Service` (lógica) -> `Selector` (consultas).

### Reglas de negocio

1. El contrato público de la API (URLs, requests, responses, status codes, errores) NO DEBE CAMBIAR (preservación total de compatibilidad hacia atrás).
2. Toda la lógica de negocio y cálculos debe residir en funciones de servicio independientes de `request`.
3. Todas las pruebas existentes deben seguir pasando en verde sin modificar sus expectativas.

### Contrato esperado

Exactamente el mismo contrato HTTP original, pero con una base de código limpia y modular.

### Persistencia

Misma persistencia subyacente. Persistencia física garantizada mediante tablas relacionales en PostgreSQL, con tipos de datos nativos e integridad referencial protegida.

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validaciones movidas al serializer y servicio.

### Transacciones

Operación atómica obligatoria mediante `transaction.atomic()`. Garantiza que todas las mutaciones en la base de datos se confirmen de forma íntegra o se reviertan totalmente (Rollback) ante fallos.

### Casos límite

Garantizar que ningún caso límite o validación implícita de la vista original se pierda durante la extracción.

### Casos de error

- `400 Bad Request`: Payload JSON malformado o campos requeridos ausentes.
- `401 Unauthorized`: Token JWT expirado, revocado o ausente.
- `403 Forbidden`: Usuario sin permisos suficientes para la acción.
- `404 Not Found`: Identificador de recurso inexistente.
- `409 Conflict` / `422 Unprocessable`: Violación de invariantes de negocio o concurrencia.
- `500 Internal Server Error`: Errores no controlados capturados por el exception handler global.

### Consideraciones de seguridad

Garantizar que las verificaciones de permisos y ownership no se omitan al delegar.

### Consideraciones de rendimiento

La refactorización permite optimizar consultas que estaban duplicadas en la vista original.

### Fundamentos de Python relacionados

Técnicas de refactorización de Martin Fowler (Extract Function, Replace Temp with Query, Move Method).

### Conceptos Django relacionados

Separación limpia de capas de arquitectura. Arquitectura de apps de Django (`AppConfig`), ORM avanzado con `QuerySet`, `F()` expressions, señales vs llamadas explícitas a servicios y transacciones atómicas.

### Conceptos DRF relacionados

Controladores delgados en DRF: `serializer.is_valid() -> service_call() -> Response()`.

### PostgreSQL

Alineación con el motor relacional PostgreSQL 16: tipos de datos nativos (`UUID`, `NUMERIC`, `TIMESTAMPTZ`, `JSONB`), índices B-Tree compuestos y garantías transaccionales ACID en nivel de aislamiento `READ COMMITTED`.

### Arquitectura

Transformación de código espagueti a Arquitectura Limpia por capas.

### Dependencias entre módulos

Eliminación de dependencias innecesarias que la vista sobrecargada importaba.

### Antes de programar

1. ¿Cuáles son las señales (Code Smells) que indican que una vista de Django tiene demasiada responsabilidad?
2. ¿Por qué es fundamental ejecutar la suite de pruebas antes y después de cada paso de refactorización?

### Pruebas mínimas

1. Ejecutar la suite de pruebas completa del módulo antes de tocar el código y verificar que esté en verde.
2. Ejecutar las pruebas tras la refactorización y comprobar que sigan pasando sin haber cambiado una sola línea de los tests.

### Pruebas negativas

1. Escribir nuevos tests unitarios directos sobre las funciones de servicio extraídas sin necesidad de levantar `APIClient`.

### Documentación

Documentar la justificación técnica de la refactorización en el log de decisiones arquitectónicas.

### Explicación posterior

Explica el principio 'Skinny Views, Fat Services' (Vistas Delgadas, Servicios Cohesivos) y por qué las vistas solo deben actuar como adaptadores de protocolo HTTP.

### Aplicación profesional

Mantenimiento de bases de código legadas, reducción de deuda técnica y preparación de sistemas para escalabilidad.

### Reto adicional

Medir la complejidad ciclomática de la vista antes y después de la refactorización usando herramientas como `radon` o `flake8`.
