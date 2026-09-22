# Ejercicio 030 — Suite de Pruebas Automatizadas para Autenticación y Autorización con pytest

[← Ejercicio 029](../ejercicio_029/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 031 →](../ejercicio_031/README.md)

---

### Contexto de negocio

Para evitar regresiones en los mecanismos de seguridad al añadir nuevas funcionalidades, el equipo exige una suite exhaustiva de pruebas automatizadas con `pytest-django`. Deben probarse caminos felices, rechazos por contraseñas débiles, expiración de tokens, permisos por rol y protección de ownership.

### Estado actual del sistema

Módulos `apps/users`, `apps/catalog`, `apps/customers` y `apps/audit` con lógica de seguridad implementada.

### Nueva necesidad

Crear la suite de pruebas en `tests/` y dentro de cada módulo (`apps/users/tests/`), configurando fixtures de `pytest`, clientes autenticados (`APIClient`) y factories reutilizables.

### Objetivo

Dominar el testing profesional de APIs en Django con `pytest-django`, creando fixtures limpias para usuarios con diferentes roles y validando aserciones sobre status codes, payloads y efectos secundarios en base de datos.

### Actor

Ingeniero de Calidad / Desarrollador Backend

### Módulo responsable

`tests/` y `apps/*/tests/` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`pytest.ini`, `conftest.py`, fixtures (`api_client`, `user_factory`, `auth_client_factory`, `admin_user`, `customer_user`).

### Reglas de negocio

1. Las pruebas deben ejecutarse sobre una base de datos de pruebas aislada en PostgreSQL o SQLite en memoria para tests rápidos.
2. Cada test debe ser independiente y no depender del orden de ejecución.
3. Debe probarse obligatoriamente la matriz completa de autorización: anónimo, cliente, gestor y admin sobre un endpoint protegido.
4. No deben hardcodearse tokens en los tests; generarlos dinámicamente mediante las fixtures.

### Contrato esperado

Ejecución limpia de `pytest` con todos los tests en verde (`PASSED`).

### Persistencia

Base de datos de pruebas recreada y limpiada por cada test (`@pytest.mark.django_db`).

### Relaciones

Todas las entidades involucradas en los módulos creados.

### Autenticación

Simulación de autenticación JWT mediante `client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')`.

### Autorización

Verificación de respuestas `200`, `201`, `401`, `403`, `404` según el rol.

### Validaciones

Aserciones sobre `response.status_code` y `response.json()`.

### Transacciones

Rollback automático por test gracias al runner transaccional de pytest-django.

### Casos límite

Tokens expirados o manipulados en las aserciones de prueba.

### Casos de error

Verificación explícita de que las respuestas de error contengan la estructura estándar `{"error": {"code": ...}}`.

### Consideraciones de seguridad

Asegurar que los datos de prueba usen contraseñas falsas de test sin exponer secretos de producción.

### Consideraciones de rendimiento

Uso de fixtures con scope adecuado (`session` vs `function`) para optimizar el tiempo total de la suite de pruebas.

### Fundamentos de Python relacionados

Framework `pytest`, decoradores `@pytest.fixture`, `@pytest.mark.parametrize`.

### Conceptos Django relacionados

`pytest-django`, `django_db`, `APIClient` de DRF.

### Conceptos DRF relacionados

`rest_framework.test.APIClient`, `force_authenticate` vs autenticación real con JWT.

### PostgreSQL

Creación y destrucción de base de datos de test (`test_ecommerce_db`).

### Arquitectura

Organización de pruebas unitarias (servicios aislados) y pruebas de integración (endpoints HTTP) en el monolito modular.

### Dependencias entre módulos

Los tests importan servicios, modelos y serializers de los módulos bajo prueba.

### Antes de programar

1. ¿Por qué `pytest.mark.parametrize` es ideal para probar múltiples combinaciones de roles y status codes esperados con poco código?
2. ¿Cuál es la diferencia entre usar `client.force_authenticate(user)` y enviar el header real `Authorization: Bearer <token>` en una prueba de integración?

### Pruebas mínimas

1. Escribir test parametrizado que verifique que Anónimo recibe 401, Customer recibe 403 y CatalogManager recibe 201 en `POST /api/v1/catalog/products/`.
2. Escribir test que verifique que el registro de usuario cree el hash y no exponga la contraseña en el JSON.

### Pruebas negativas

1. Escribir test que intente modificar un recurso con un usuario que no es el propietario y compruebe que retorne 404/403.

### Documentación

Documentar en el README cómo ejecutar la suite de tests (`pytest -v --durations=10`) y cómo interpretar fallos.

### Explicación posterior

Explica cómo configurar `pytest.ini` con `DJANGO_SETTINGS_MODULE` y por qué las fixtures de `conftest.py` facilitan la reutilización de clientes y usuarios en toda la suite.

### Aplicación profesional

Cultura de testing y aseguramiento de calidad en pipelines de integración continua (CI) con GitHub Actions / GitLab CI.

### Reto adicional

Configurar medición de cobertura con `pytest-cov` y verificar que la cobertura de código en `apps/users` y `apps/catalog` supere el 90%.
