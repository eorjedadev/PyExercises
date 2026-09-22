# Ejercicio 057 — Refactorización: Detección y Resolución de Imports Circulares entre Módulos

[← Ejercicio 056](../ejercicio_056/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 058 →](../ejercicio_058/README.md)

---

### Contexto de negocio

Durante el crecimiento rápido del monolito, dos desarrolladores introdujeron imports cruzados directos: `apps/orders/services.py` importa un modelo de `apps/payments/models.py`, y `apps/payments/models.py` importa un servicio de `apps/orders/services.py`. Al arrancar el servidor en un nuevo entorno o ejecutar tests, Python falla catastróficamente con `ImportError: cannot import name ... from partially initialized module (most likely due to a circular import)`.

### Estado actual del sistema

Error de import circular bloqueando el arranque del proyecto.

### Nueva necesidad

Analizar el grafo de dependencias entre `apps/orders` y `apps/payments`, romper el acoplamiento circular reorganizando las interfaces, moviendo contratos compartidos o usando eventos/servicios desacoplados.

### Objetivo

Comprender la causa raíz de los imports circulares en Python/Django, aprender a diagnosticarlos y aplicar soluciones arquitectónicas definitivas sin recurrir al antipatrón de 'hacer imports adentro de las funciones'.

### Actor

Arquitecto de Software / Desarrollador Backend

### Módulo responsable

`apps/orders` y `apps/payments` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

Grafo de imports entre módulos, `AppConfig`, estructura de paquetes.

### Reglas de negocio

1. El grafo de dependencias entre módulos debe ser estrictamente un Grafo Acíclico Dirigido (DAG - Directed Acyclic Graph).
2. Ningún módulo puede depender directa o indirectamente de otro módulo que ya depende de él.
3. Prohibido solucionar imports circulares colocando `import ...` adentro del cuerpo de métodos o funciones (deuda técnica inaceptable).
4. La comunicación bidireccional debe resolverse mediante: inversión de dependencias, identificadores abstractos (UUIDs) o servicios de orquestación.

### Contrato esperado

Arranque 100% limpio con `python manage.py check` y ejecución fluida de toda la suite de tests sin advertencias de inicialización parcial.

### Persistencia

Sin cambios en esquemas relacionales. Persistencia física garantizada mediante tablas relacionales en PostgreSQL, con tipos de datos nativos e integridad referencial protegida.

### Relaciones

Referencias foráneas basadas en strings (`'app_label.ModelName'`) en lugar de imports directos de clases de modelos.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Validación de carga estática de módulos de Python.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Imports en `__init__.py` que exponen submódulos antes de tiempo.

### Casos de error

`ImportError` o `AttributeError` durante la carga de Django.

### Consideraciones de seguridad

La estabilidad del arranque del sistema es un requisito básico de disponibilidad.

### Consideraciones de rendimiento

Carga rápida de módulos al iniciar el proceso.

### Fundamentos de Python relacionados

Mecanismo de importación de Python (`sys.modules`), cómo el intérprete evalúa los archivos de arriba a abajo y el concepto de módulos parcialmente inicializados.

### Conceptos Django relacionados

Claves foráneas con strings perezosos (`ForeignKey('orders.Order', ...)`), `apps.get_model()`, ciclo de vida de `AppConfig.ready()`.

### Conceptos DRF relacionados

Serializadores que referencian modelos de otras apps.

### PostgreSQL

Alineación con el motor relacional PostgreSQL 16: tipos de datos nativos (`UUID`, `NUMERIC`, `TIMESTAMPTZ`, `JSONB`), índices B-Tree compuestos y garantías transaccionales ACID en nivel de aislamiento `READ COMMITTED`.

### Arquitectura

Regla de Oro del Monolito Modular: El flujo de dependencias entre módulos debe ser unidireccional y acíclico.

### Dependencias entre módulos

Reestructuración del grafo: `apps/payments` depende de `apps/orders` (o viceversa), pero NUNCA ambas mutuamente.

### Antes de programar

1. ¿Por qué poner un `from apps.x.services import y` adentro de una función es considerado un parche sucio (hack) que oculta un defecto de diseño arquitectónico?
2. ¿Cómo resuelve Django las claves foráneas definidas como strings (`'catalog.Product'`) de forma perezosa para evitar imports circulares entre modelos?

### Pruebas mínimas

1. Ejecutar `python manage.py check` y verificar que el proceso complete con 0 errores de importación.
2. Ejecutar `pytest` completo y comprobar que todos los módulos se importen limpiamente.

### Pruebas negativas

1. Comprobar que no existan imports locales dentro de métodos en el código refactorizado.

### Documentación

Documentar el mapa del grafo acíclico de dependencias en `MAPA_ARQUITECTURA.md`.

### Explicación posterior

Explica el Principio de Dependencias Acíclicas (ADP - Acyclic Dependencies Principle) de la arquitectura de software y las 3 estrategias para romper ciclos (Mover clases compartidas, Invertir dependencia mediante interfaces, o usar identificadores escalares).

### Aplicación profesional

Mantenimiento y refactorización de grandes monolitos Django en empresas con decenas de desarrolladores y módulos.

### Reto adicional

Crear un test automatizado con `pytest` que inspeccione el AST (Abstract Syntax Tree) del proyecto para detectar e impedir la introducción de nuevos imports circulares en CI.
