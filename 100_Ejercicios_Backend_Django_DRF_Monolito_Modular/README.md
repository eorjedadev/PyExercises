# 100 Ejercicios Profesionales de Backend con Django REST Framework y Arquitectura Monolítica Modular

Programa intensivo de formación para desarrolladores backend enfocado en el diseño, construcción, optimización, seguridad y evolución de aplicaciones de gran escala mediante una **Arquitectura Monolítica Modular** utilizando **Python, Django, Django REST Framework y PostgreSQL**.

---

## 1. Filosofía del Programa

> **"Un monolito modular bien diseñado es 10 veces más fácil de construir, probar, desplegar y mantener que una red prematura de microservicios."**

Este programa no contiene 100 CRUDs aislados ni ejercicios desconectados de juguete. Enseña a construir un sistema backend desplegable como una sola unidad pero dividido internamente en módulos de negocio altamente cohesivos y de bajo acoplamiento:

```text
                   ┌───────────────────────────────────────┐
                   │       API Gateway / HTTP Router       │
                   │        (/api/v1/  y  /api/v2/)        │
                   └──────────────────┬────────────────────┘
                                      │
        ┌─────────────┬───────────────┼───────────────┬─────────────┐
        ▼             ▼               ▼               ▼             ▼
   ┌─────────┐   ┌─────────┐    ┌───────────┐   ┌───────────┐ ┌───────────┐
   │  Users  │   │ Catalog │    │  Orders   │   │ Inventory │ │ Payments  │
   │  & IAM  │   │ & Taxon │    │ & Snapsh. │   │ & Stocks  │ │ & Gatew.  │
   └─────────┘   └─────────┘    └───────────┘   └───────────┘ └───────────┘
        ▲             ▲               ▲               ▲             ▲
        └─────────────┴───────┬───────┴───────────────┴─────────────┘
                              │
               ┌──────────────┴──────────────┐
               │    Base de Datos Unificada  │
               │   PostgreSQL (ACID Local)   │
               └─────────────────────────────┘
```

---

## 2. Stack Tecnológico

* **Lenguaje:** Python 3.12+ (Tipado estricto, decoradores, dataclasses, generadores, excepciones).
* **Framework Web:** Django 5.x + Django REST Framework 3.15+.
* **Base de Datos:** PostgreSQL 16 (Tipos nativos, constraints físicas, índices parciales, GIN, FTS, JSONB, Range types).
* **Autenticación y Seguridad:** JWT con SimpleJWT, rotación de tokens, lista negra, hashing Argon2/PBKDF2, RBAC, ownership, rate limiting.
* **Documentación:** OpenAPI 3.0 interactivo con `drf-spectacular` (Swagger UI y Redoc).
* **Testing:** `pytest`, `pytest-django`, `CaptureQueriesContext` para auditoría de queries SQL.
* **Infraestructura:** Docker, Docker Compose multi-stage con volúmenes persistentes y compatibilidad total con Windows (PowerShell) y Linux.

---

## 3. Estructura de Cada Ejercicio

Cada uno de los 100 ejercicios está documentado en su propia carpeta `ejercicio_XXX/README.md` y cuenta con las **31 secciones obligatorias** de ingeniería:
1. `Contexto de negocio`
2. `Estado actual del sistema`
3. `Nueva necesidad`
4. `Objetivo`
5. `Actor`
6. `Módulo responsable`
7. `Entidades involucradas`
8. `Reglas de negocio`
9. `Contrato esperado` (Endpoints, Verbos, Payloads, Status Codes)
10. `Persistencia`
11. `Relaciones`
12. `Autenticación`
13. `Autorización`
14. `Validaciones`
15. `Transacciones`
16. `Casos límite`
17. `Casos de error`
18. `Consideraciones de seguridad`
19. `Consideraciones de rendimiento`
20. `Fundamentos de Python relacionados`
21. `Conceptos Django relacionados`
22. `Conceptos DRF relacionados`
23. `PostgreSQL`
24. `Arquitectura`
25. `Dependencias entre módulos`
26. `Antes de programar` (Preguntas de razonamiento)
27. `Pruebas mínimas`
28. `Pruebas negativas`
29. `Documentación`
30. `Explicación posterior`
31. `Aplicación profesional`
32. `Reto adicional`

---

## 4. Guía de Inicio Rápido (Windows y PowerShell)

### Requisitos Previos
* Python 3.12+ instalado en Windows.
* PostgreSQL 16 instalado localmente o Docker Desktop para Windows.
* Visual Studio Code o PyCharm.

### Configuración del Entorno Local en PowerShell
```powershell
# 1. Clonar el repositorio y acceder a la carpeta
cd 100_Ejercicios_Backend_Django_DRF_Monolito_Modular

# 2. Crear y activar el entorno virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Copiar variables de entorno de ejemplo
Copy-Item .env.example .env

# 5. Ejecutar migraciones iniciales y verificar el servidor
python manage.py migrate
python manage.py runserver
```

### Ejecución con Docker Compose
```powershell
# Levantar el stack completo (Django + PostgreSQL)
docker compose up -d --build

# Ver logs en tiempo real
docker compose logs -f web

# Ejecutar suite de pruebas dentro del contenedor
docker compose exec web pytest -v
```

---

## 5. Índice General de Ejercicios

| # | Ejercicio | Módulo | Foco Principal |
| :-: | :--- | :--- | :--- |
| `001` | [Ejercicio 001](ejercicio_001/README.md) — Fundación del Monolito Modular y Configuración de Módulos | ``config`` | Establecer la estructura de directorios del monolito modular, configurar la inte... |
| `002` | [Ejercicio 002](ejercicio_002/README.md) — Modelado de Dominio de Catálogo y Tipos de Datos en PostgreSQL | ``apps/catalog`` | Diseñar el modelo `Product`, definir tipos de datos precisos para dinero y canti... |
| `003` | [Ejercicio 003](ejercicio_003/README.md) — Contrato REST y Serialización con Serializer vs ModelSerializer | ``apps/catalog`` | Construir serializers claros para lectura (`ProductDetailOutputSerializer`) y es... |
| `004` | [Ejercicio 004](ejercicio_004/README.md) — Validaciones de Formato vs Validaciones de Dominio en Serializers | ``apps/catalog`` | Aprender a estructurar validaciones en DRF distinguiendo validaciones sintáctica... |
| `005` | [Ejercicio 005](ejercicio_005/README.md) — Vistas Explícitas con APIView y Semántica de Verbos HTTP | ``apps/catalog`` | Dominar el ciclo de vida de `APIView`, `request.data`, `request.query_params`, i... |
| `006` | [Ejercicio 006](ejercicio_006/README.md) — Categorías y Relaciones Jerárquicas con ForeignKey Auto-referencial | ``apps/catalog`` | Modelar relaciones 1 a N y árboles de categorías en PostgreSQL, configurar `Fore... |
| `007` | [Ejercicio 007](ejercicio_007/README.md) — Relaciones Many-to-Many con Metadata mediante Tabla Intermedia Explícita | ``apps/catalog`` | Dominar relaciones N a M en Django y PostgreSQL usando modelos intermedios explí... |
| `008` | [Ejercicio 008](ejercicio_008/README.md) — Restricciones de Integridad en PostgreSQL con CheckConstraint | ``apps/catalog`` | Comprender el rol de las restricciones de base de datos (`CHECK`) en PostgreSQL,... |
| `009` | [Ejercicio 009](ejercicio_009/README.md) — Migraciones de Esquema y Migraciones de Datos con RunPython | ``apps/catalog`` | Dominar el ciclo de vida de migraciones complejas en Django, migraciones de dato... |
| `010` | [Ejercicio 010](ejercicio_010/README.md) — Vistas Genéricas de DRF y Selección Consciente de Abstracciones | ``apps/catalog`` | Aprender a elegir la abstracción correcta de DRF (`generics.*` vs `APIView` vs `... |
| `011` | [Ejercicio 011](ejercicio_011/README.md) — Paginación de Recursos y Control de Carga en Memoria | ``apps/catalog`` | Comprender el funcionamiento de la paginación en DRF y PostgreSQL (`LIMIT` y `OF... |
| `012` | [Ejercicio 012](ejercicio_012/README.md) — Filtrado Declarativo, Búsqueda Textual y Ordenamiento Seguro | ``apps/catalog`` | Diseñar una capa de filtrado profesional evitando `if 'param' in request.GET` ma... |
| `013` | [Ejercicio 013](ejercicio_013/README.md) — Introducción a la Capa de Servicios y Desacoplamiento de Lógica | ``apps/catalog`` | Implementar el patrón Service Layer en Django/DRF, entendiendo por qué la lógica... |
| `014` | [Ejercicio 014](ejercicio_014/README.md) — Introducción a la Capa de Selectores y Consultas Reutilizables | ``apps/catalog`` | Aprender el patrón Selectors en Django/DRF, entendiendo la separación entre oper... |
| `015` | [Ejercicio 015](ejercicio_015/README.md) — Formato de Respuestas de Error Estandarizado y Custom Exception Handler | ``apps/core`` | Implementar el manejo centralizado de excepciones en DRF, mapear excepciones de ... |
| `016` | [Ejercicio 016](ejercicio_016/README.md) — Modelo de Usuario Personalizado y Migración Inicial en apps/users | ``apps/users`` | Implementar un Custom User Model profesional en Django, crear su `UserManager` p... |
| `017` | [Ejercicio 017](ejercicio_017/README.md) — Registro de Usuarios y Validación Criptográfica de Contraseñas | ``apps/users`` | Construir un flujo de registro seguro en DRF, aplicando validadores de contraseñ... |
| `018` | [Ejercicio 018](ejercicio_018/README.md) — Autenticación con JWT (JSON Web Tokens) y Emisión de Tokens | ``apps/users`` | Comprender la anatomía de un JWT (Header, Payload, Signature), configurar Simple... |
| `019` | [Ejercicio 019](ejercicio_019/README.md) — Rotación de Refresh Tokens, Expiración y Revocación | ``apps/users`` | Dominar el ciclo de vida de tokens de refresco, rotación automática y revocación... |
| `020` | [Ejercicio 020](ejercicio_020/README.md) — Protección de Endpoints y Clases de Permisos en DRF | ``apps/catalog`` | Dominar el sistema de permisos de DRF (`permission_classes`), la diferencia entr... |
| `021` | [Ejercicio 021](ejercicio_021/README.md) — Módulo de Clientes (apps/customers) y Perfil Desacoplado 1 a 1 | ``apps/customers`` | Diseñar límites limpios entre módulos: separar la identidad técnica (`User` en `... |
| `022` | [Ejercicio 022](ejercicio_022/README.md) — Verificación de Ownership y Permiso Personalizado IsOwner | ``apps/customers`` | Dominar la prevención de vulnerabilidades IDOR/BOLA en DRF mediante `has_object_... |
| `023` | [Ejercicio 023](ejercicio_023/README.md) — Control de Acceso Basado en Roles (RBAC) sin Dispersar if user.role | ``apps/users`` | Implementar Role-Based Access Control (RBAC) limpio y extensible en Django/DRF, ... |
| `024` | [Ejercicio 024](ejercicio_024/README.md) — Permisos Dinámicos basados en Rol y Estado del Recurso | ``apps/catalog`` | Dominar permisos contextuales y dinámicos a nivel de objeto en DRF, integrando e... |
| `025` | [Ejercicio 025](ejercicio_025/README.md) — Gestión Segura de Configuración y Variables de Entorno | ``config`` | Profesionalizar la gestión de configuración en Django siguiendo los principios d... |
| `026` | [Ejercicio 026](ejercicio_026/README.md) — Throttling y Rate Limiting para Protección contra Abusos | ``apps/core`` | Proteger la API contra abusos, scraping y ataques de fuerza bruta mediante Throt... |
| `027` | [Ejercicio 027](ejercicio_027/README.md) — Flujo de Recuperación de Contraseña con Tokens Criptográficos | ``apps/users`` | Diseñar un flujo completo de recuperación de contraseña en backend, utilizando `... |
| `028` | [Ejercicio 028](ejercicio_028/README.md) — Módulo de Auditoría y Trazabilidad de Eventos de Negocio | ``apps/audit`` | Diseñar un subsistema de auditoría inmutable en el monolito modular, comprendien... |
| `029` | [Ejercicio 029](ejercicio_029/README.md) — Desactivación de Cuentas y Soft Delete vs Eliminación Física | ``apps/users`` | Comprender cuándo aplicar Soft Delete vs eliminación física, las consecuencias d... |
| `030` | [Ejercicio 030](ejercicio_030/README.md) — Suite de Pruebas Automatizadas para Autenticación y Autorización con pytest | ``tests/`` | Dominar el testing profesional de APIs en Django con `pytest-django`, creando fi... |
| `031` | [Ejercicio 031](ejercicio_031/README.md) — Módulo de Pedidos (apps/orders) y Definición de Límites de Dominio | ``apps/orders`` | Diseñar los límites de dominio (Bounded Context) para el módulo de pedidos, iden... |
| `032` | [Ejercicio 032](ejercicio_032/README.md) — Modelado de Líneas de Pedido e Inmutabilidad de Precios Históricos | ``apps/orders`` | Garantizar la inmutabilidad histórica de transacciones comerciales, modelando en... |
| `033` | [Ejercicio 033](ejercicio_033/README.md) — Interfaces Públicas entre Módulos y Creación de Pedidos | ``apps/orders`` | Aprender a diseñar e invocar interfaces públicas entre módulos en una arquitectu... |
| `034` | [Ejercicio 034](ejercicio_034/README.md) — Transacciones Atómicas con transaction.atomic y Consistencia | ``apps/orders`` | Dominar el control de transacciones en PostgreSQL y Django (`django.db.transacti... |
| `035` | [Ejercicio 035](ejercicio_035/README.md) — Módulo de Inventario (apps/inventory) y Movimientos de Almacén | ``apps/inventory`` | Diseñar el dominio de inventario en una arquitectura modular, manteniendo la sep... |
| `036` | [Ejercicio 036](ejercicio_036/README.md) — Coordinación Transaccional entre Orders e Inventory | ``apps/orders`` | Aprender la coordinación transaccional entre módulos dentro de un monolito modul... |
| `037` | [Ejercicio 037](ejercicio_037/README.md) — Máquina de Estados del Pedido y Transiciones Válidas | ``apps/orders`` | Modelar el ciclo de vida de entidades con máquinas de estados en Django/Python, ... |
| `038` | [Ejercicio 038](ejercicio_038/README.md) — Endpoints de Acción de Negocio Específicos (POST /orders/{id}/cancel/) | ``apps/orders`` | Diseñar e implementar endpoints de acción en DRF (`@action` en ViewSets o vistas... |
| `039` | [Ejercicio 039](ejercicio_039/README.md) — Jerarquía de Excepciones de Dominio y Mapeo Limpio a HTTP | ``apps/core`` | Desacoplar completamente la capa de dominio de la capa HTTP de DRF, estructurand... |
| `040` | [Ejercicio 040](ejercicio_040/README.md) — Control de Concurrencia con Bloqueo Pesimista (select_for_update) | ``apps/inventory`` | Dominar el control de concurrencia pesimista en bases de datos relacionales con ... |
| `041` | [Ejercicio 041](ejercicio_041/README.md) — Módulo de Promociones (apps/promotions) y Validación de Cupones | ``apps/promotions`` | Diseñar un módulo de promociones desacoplado, modelando reglas complejas de nego... |
| `042` | [Ejercicio 042](ejercicio_042/README.md) — Idempotencia en APIs y Prevención de Doble Cobro con Idempotency-Key | ``apps/core`` | Dominar el concepto de Idempotencia en APIs REST para métodos no seguros (`POST`... |
| `043` | [Ejercicio 043](ejercicio_043/README.md) — Django Admin Operativo para Gestión de Pedidos e Inventario | ``apps/orders`` | Dominar la personalización avanzada del Django Admin para uso operativo profesio... |
| `044` | [Ejercicio 044](ejercicio_044/README.md) — Comando Personalizado de Gestión para Cancelar Pedidos Expirados | ``apps/orders`` | Aprender a construir Custom Management Commands en Django para tareas de manteni... |
| `045` | [Ejercicio 045](ejercicio_045/README.md) — Pruebas de Integración y Validación de Rollback en Cascada | ```tests/integration/``` | Dominar las pruebas de integración transaccional en Django, validando que las ex... |
| `046` | [Ejercicio 046](ejercicio_046/README.md) — Módulo de Pagos (apps/payments) y Registro de Intentos de Cobro | ``apps/payments`` | Diseñar el dominio de pagos en una arquitectura modular, separando la orden come... |
| `047` | [Ejercicio 047](ejercicio_047/README.md) — Aislamiento de Pasarela Externa mediante Patrón Gateway / Adapter | ``apps/payments`` | Aplicar el patrón Adapter / Gateway en Python y Django para desacoplar la lógica... |
| `048` | [Ejercicio 048](ejercicio_048/README.md) — Webhooks de Pagos y Verificación de Firma Criptográfica | ``apps/payments`` | Dominar el diseño y aseguramiento de Webhooks en APIs REST, implementando verifi... |
| `049` | [Ejercicio 049](ejercicio_049/README.md) — Módulo de Notificaciones (apps/notifications) y Desacoplamiento de Eventos | ``apps/notifications`` | Diseñar un sistema de notificaciones desacoplado en el monolito modular, modelan... |
| `050` | [Ejercicio 050](ejercicio_050/README.md) — Procesamiento Asíncrono y Tareas en Segundo Plano (Background Tasks) | ``apps/core`` | Comprender por qué las operaciones lentas de I/O (emails, generación de reportes... |
| `051` | [Ejercicio 051](ejercicio_051/README.md) — Módulo de Facturación (apps/billing) y Validación Estricta de Archivos | ``apps/billing`` | Dominar la carga segura de archivos en Django REST Framework, implementando vali... |
| `052` | [Ejercicio 052](ejercicio_052/README.md) — Generación de Reportes PDF y CSV sin Bloquear el Servidor | ``apps/billing`` | Dominar la generación y transmisión de archivos dinámicos (CSV/PDF) en Django/DR... |
| `053` | [Ejercicio 053](ejercicio_053/README.md) — Descarga Segura de Archivos Privados mediante URLs Firmadas / Endpoints Autorizados | ``apps/billing`` | Proteger el acceso a archivos privados en aplicaciones backend, implementando co... |
| `054` | [Ejercicio 054](ejercicio_054/README.md) — Gestión de Datos Iniciales y Fixtures Profesionales con Seeds | ``apps/core`` | Dominar la inicialización y siembra de datos (Data Seeding) en Django, entendien... |
| `055` | [Ejercicio 055](ejercicio_055/README.md) — Módulo de Envíos y Logística (apps/shipping) y Asignación de Transportista | ``apps/shipping`` | Diseñar el dominio logístico en el monolito modular, modelando el ciclo de vida ... |
| `056` | [Ejercicio 056](ejercicio_056/README.md) — Refactorización: Extracción de Lógica de Vistas Sobrecargadas a Servicios Puros | ``Módulo` | Dominar la técnica de refactorización de código legado en Django/DRF, reduciendo... |
| `057` | [Ejercicio 057](ejercicio_057/README.md) — Refactorización: Detección y Resolución de Imports Circulares entre Módulos | ``apps/orders`` | Comprender la causa raíz de los imports circulares en Python/Django, aprender a ... |
| `058` | [Ejercicio 058](ejercicio_058/README.md) — Centralización de Parámetros Globales y Configuración Dinámica de Negocio | ``apps/business_settings`` | Diseñar un sistema de configuración dinámica de negocio en Django, implementando... |
| `059` | [Ejercicio 059](ejercicio_059/README.md) — Endpoints de Comprobación de Salud del Sistema (Health Checks) | ``apps/core`` | Construir Health Check Endpoints profesionales en Django/DRF, distinguiendo comp... |
| `060` | [Ejercicio 060](ejercicio_060/README.md) — Documentación Automática OpenAPI / Swagger con drf-spectacular | ``config/`` | Dominar la generación profesional de documentación OpenAPI 3.0 en Django REST Fr... |
| `061` | [Ejercicio 061](ejercicio_061/README.md) — Detección y Diagnóstico del Problema N+1 en Listados de Pedidos | ``apps/orders`` | Comprender qué es el problema N+1 en los ORMs relacionales, cómo medirlo de form... |
| `062` | [Ejercicio 062](ejercicio_062/README.md) — Optimización con select_related y Prefetch Personalizado | ``apps/orders`` | Dominar el uso quirúrgico de `select_related` (SQL `INNER/LEFT JOIN`) y `prefetc... |
| `063` | [Ejercicio 063](ejercicio_063/README.md) — Consultas Agregadas, Anotaciones y Subqueries con el ORM | ``apps/customers`` | Dominar las capacidades analíticas avanzadas del ORM de Django (`annotate`, `agg... |
| `064` | [Ejercicio 064](ejercicio_064/README.md) — Diseño Profesional de Índices en PostgreSQL (Compuestos y Parciales) | ``apps/catalog`` | Comprender cuándo y cómo crear índices en PostgreSQL con Django, evaluando el co... |
| `065` | [Ejercicio 065](ejercicio_065/README.md) — Búsqueda Avanzada de Texto Completo en PostgreSQL (Full-Text Search) | ``apps/catalog`` | Dominar Full-Text Search (FTS) nativo de PostgreSQL con Django, ponderando campo... |
| `066` | [Ejercicio 066](ejercicio_066/README.md) — Uso Avanzado de Campos JSON (JSONField) y Consultas Semiestructuradas | ``apps/catalog`` | Dominar el uso de `JSONField` (almacenamiento binario JSONB) en PostgreSQL con D... |
| `067` | [Ejercicio 067](ejercicio_067/README.md) — Optimización de Memoria en Consultas Masivas con only(), defer() y values_list() | ``apps/catalog`` | Dominar la optimización de memoria y transporte en Django mediante `only()`, `de... |
| `068` | [Ejercicio 068](ejercicio_068/README.md) — Logging Estructurado Profesional en Formato JSON para Producción | ``config/`` | Dominar el logging estructurado profesional en Django, entendiendo la configurac... |
| `069` | [Ejercicio 069](ejercicio_069/README.md) — Seguridad Avanzada de APIs: Prevención de Mass Assignment y OWASP Top 10 API | `Transversal` | Dominar las mejores prácticas de seguridad en Django REST Framework alineadas co... |
| `070` | [Ejercicio 070](ejercicio_070/README.md) — Versionado de APIs y Evolución de Contratos (/api/v1/ vs /api/v2/) | ``config/urls.py`` | Dominar las estrategias de versionado de APIs en Django REST Framework, aprendie... |
| `071` | [Ejercicio 071](ejercicio_071/README.md) — Transiciones Suaves de Contratos y Deprecación de Campos con Sunset Headers | ``apps/core`` | Dominar la gestión profesional de deprecación y obsolescencia de APIs REST, comu... |
| `072` | [Ejercicio 072](ejercicio_072/README.md) — Estrategias de Caché en Lecturas Frecuentes e Invalidación Granular | ``apps/catalog`` | Dominar el patrón Cache-Aside (Lazy Loading) en Django, comprendiendo la seriali... |
| `073` | [Ejercicio 073](ejercicio_073/README.md) — Control de Concurrencia Optimista mediante version_id / Timestamps | ``apps/catalog`` | Dominar el Control de Concurrencia Optimista (OCC) en Django y PostgreSQL, compr... |
| `074` | [Ejercicio 074](ejercicio_074/README.md) — Monitoreo de Rendimiento y Medición de Consultas SQL en Tests | ``tests/`` | Implementar pruebas automatizadas de regresión de rendimiento en Django, garanti... |
| `075` | [Ejercicio 075](ejercicio_075/README.md) — Configuración Multientorno (Development, Testing, Production) y Settings Modulares | ``config`` | Dominar la organización modular de settings en proyectos Django profesionales de... |
| `076` | [Ejercicio 076](ejercicio_076/README.md) — Auditoría de Cohesión y Acoplamiento en el Monolito Modular | `Transversal` | Desarrollar criterio arquitectónico senior para evaluar la salud de un monolito ... |
| `077` | [Ejercicio 077](ejercicio_077/README.md) — Módulo de Devoluciones y Reembolsos (apps/returns) | ``apps/returns`` | Diseñar un nuevo módulo de negocio sobre un monolito modular existente, respetan... |
| `078` | [Ejercicio 078](ejercicio_078/README.md) — Coordinación Multi-Módulo: Devoluciones -> Inventario + Pagos + Notificaciones | ``apps/returns`` | Dominar la coordinación de flujos de negocio complejos que abarcan múltiples mód... |
| `079` | [Ejercicio 079](ejercicio_079/README.md) — Sistema de Suscripciones Periódicas (apps/subscriptions) y Ciclos de Facturación | ``apps/subscriptions`` | Diseñar el dominio de suscripciones recurrentes en Django/DRF, modelando ciclos ... |
| `080` | [Ejercicio 080](ejercicio_080/README.md) — Facturación Recurrente Automática y Gestión de Períodos de Gracia | ``apps/subscriptions`` | Dominar la automatización de cobros recurrentes y la gestión de morosidad (Dunni... |
| `081` | [Ejercicio 081](ejercicio_081/README.md) — Sistema Multisede / Sucursales (apps/branches) y Stock Distribuido | ``apps/branches`` | Evolucionar la arquitectura de inventario de un modelo monosede a un modelo mult... |
| `082` | [Ejercicio 082](ejercicio_082/README.md) — Transferencias de Inventario entre Sucursales con Trazabilidad y Confirmación | ``apps/inventory`` | Dominar el modelado de transferencias físicas de inventario en tránsito, aplican... |
| `083` | [Ejercicio 083](ejercicio_083/README.md) — Sistema de Soporte y Tickets de Atención al Cliente (apps/support) | ``apps/support`` | Diseñar el dominio de Helpdesk y atención al cliente en el monolito modular, mod... |
| `084` | [Ejercicio 084](ejercicio_084/README.md) — Permisos Granulares de Soporte, Asignación de Agentes y Escalado | ``apps/support`` | Dominar el control de acceso basado en roles jerárquicos (Hierarchical RBAC), fl... |
| `085` | [Ejercicio 085](ejercicio_085/README.md) — Sistema de Reseñas y Calificaciones (apps/reviews) con Verified Purchase | ``apps/reviews`` | Diseñar un sistema de calificaciones y reseñas desacoplado en el monolito modula... |
| `086` | [Ejercicio 086](ejercicio_086/README.md) — Cálculo y Actualización Atómica de Métricas Agregadas de Calificación | ``apps/reviews`` | Dominar el patrón de Vistas Materializadas / Campos Desnormalizados Agregados en... |
| `087` | [Ejercicio 087](ejercicio_087/README.md) — Dockerización Profesional del Monolito Modular con PostgreSQL y Windows | `Raíz` | Dominar la contenerización profesional de aplicaciones Django + PostgreSQL con D... |
| `088` | [Ejercicio 088](ejercicio_088/README.md) — Gestión Segura de Secretos en Docker para Entornos Windows y CI/CD | ``config/`` | Dominar las mejores prácticas de seguridad en la gestión de secretos con Docker ... |
| `089` | [Ejercicio 089](ejercicio_089/README.md) — Migración de Datos Compleja sin Downtime (Patrón Expand and Contract) | ``apps/customers`` | Dominar las migraciones de bases de datos relacionales sin tiempo de inactividad... |
| `090` | [Ejercicio 090](ejercicio_090/README.md) — Refactorización Arquitectónica Mayor: Desacoplamiento con Eventos de Dominio Internos | ``apps/core`` | Implementar Arquitectura Dirigida por Eventos (EDA - Event-Driven Architecture) ... |
| `091` | [Ejercicio 091](ejercicio_091/README.md) — Desafío de Dominio: Sistema de Subastas en Tiempo Real y Cierre Atómico | `Determinación` | Demostrar autonomía técnica para modelar un dominio de alta contención y concurr... |
| `092` | [Ejercicio 092](ejercicio_092/README.md) — Desafío de Dominio: Plataforma B2B de Compras con Aprobación Jerárquica | `Determinación` | Diseñar un sistema empresarial B2B complejo con jerarquías organizacionales, pre... |
| `093` | [Ejercicio 093](ejercicio_093/README.md) — Desafío de Dominio: Sistema de Citas Médicas y Quirófanos con Control de Solapamientos | `Determinación` | Dominar el control estricto de intervalos de tiempo y reservas sin solapamiento ... |
| `094` | [Ejercicio 094](ejercicio_094/README.md) — Desafío de Dominio: Gestión de Flotas y Logística de Envíos en Rutas Multiparada | `Determinación` | Diseñar un sistema de logística avanzada y gestión de flotas en Django/DRF, cont... |
| `095` | [Ejercicio 095](ejercicio_095/README.md) — Desafío de Dominio: Plataforma de Cursos con Prerrequisitos y Certificación Automática | `Determinación` | Diseñar un sistema de E-Learning completo en Django/DRF, modelando grafos de pre... |
| `096` | [Ejercicio 096](ejercicio_096/README.md) — Desafío de Dominio: Billetera Digital (Wallets) con Contabilidad de Doble Entrada | `Determinación` | Diseñar un sistema financiero de misión crítica aplicando el principio contable ... |
| `097` | [Ejercicio 097](ejercicio_097/README.md) — Desafío de Dominio: Alquiler de Propiedades/Vehículos con Depósito en Custodia (Escrow) | `Determinación` | Diseñar un sistema de reservas de alquiler y retención de depósitos en garantía ... |
| `098` | [Ejercicio 098](ejercicio_098/README.md) — Desafío de Dominio: Comisiones de Afiliados Multinivel y Liquidación Fiscal Mensual | `Determinación` | Diseñar un sistema de comisiones multinivel y liquidación contable/fiscal en Dja... |
| `099` | [Ejercicio 099](ejercicio_099/README.md) — Desafío de Dominio: Gestión de Incidentes de Seguridad con Registro Forense Inmutable | `Determinación` | Diseñar un sistema de respuesta a incidentes de seguridad con garantías de inmut... |
| `100` | [Ejercicio 100](ejercicio_100/README.md) — El Gran Desafío Arquitectónico: Plataforma Omnicanal Integrada | `Todo` | Consolidar la autonomía técnica absoluta como Backend Engineer Senior: diseñar, ... |

---

## 6. Documentos de Referencia Arquitectónica

* 🗺️ [**MAPA_APRENDIZAJE.md**](MAPA_APRENDIZAJE.md): Progresión técnica, capacidades y matriz de conceptos.
* 🏛️ [**MAPA_ARQUITECTURA.md**](MAPA_ARQUITECTURA.md): Bounded Contexts, límites modulares y grafo de dependencias.

---

## 7. Reglas de Mentoría y Autonomía

1. **Sin soluciones prehechas:** No existen archivos de soluciones; el practicante debe diseñar, codificar y probar cada solución por sí mismo.
2. **Pregunta antes de codificar:** Responder siempre las preguntas de la sección *Antes de programar* en papel o notas antes de abrir el editor.
3. **Defensa posterior:** Al terminar cada ejercicio, responder las preguntas de la sección *Explicación posterior* para consolidar el criterio de ingeniería.
