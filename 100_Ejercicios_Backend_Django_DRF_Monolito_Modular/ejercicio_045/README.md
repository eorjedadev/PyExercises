# Ejercicio 045 — Pruebas de Integración y Validación de Rollback en Cascada

[← Ejercicio 044](../ejercicio_044/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 046 →](../ejercicio_046/README.md)

---

### Contexto de negocio

La confiabilidad de un sistema transaccional se demuestra cuando ocurren fallos inesperados. El equipo de calidad requiere una batería exhaustiva de pruebas de integración que simule caídas durante flujos multi-módulo (Creación de Pedido -> Reserva de Stock -> Aplicación de Cupón) y verifique que la base de datos ejecute Rollback perfecto sin dejar dinero, cupones ni stock en estados inconsistentes.

### Estado actual del sistema

Módulos `catalog`, `customers`, `orders`, `inventory` y `promotions` integrados.

### Nueva necesidad

Crear la suite de pruebas de integración multi-módulo en `tests/integration/test_order_flow.py`, validando el flujo completo de compra y verificando la integridad de rollback ante fallos forzados con mocks.

### Objetivo

Dominar las pruebas de integración transaccional en Django, validando que las excepciones en módulos dependientes reviertan todos los cambios previos en la base de datos.

### Actor

Ingeniero de Calidad / Desarrollador Backend

### Módulo responsable

``tests/integration/`` como módulo de negocio responsable de la capacidad.

### Entidades involucradas

`test_order_flow.py`, `pytest-django`, `unittest.mock.patch`, todas las entidades de los módulos de compra.

### Reglas de negocio

1. Prueba de Flujo Completo: Usuario crea orden con 2 productos y cupón válido -> Se crea la orden, se descuenta stock reservado, se incrementa uso del cupón y se responde 201.
2. Prueba de Rollback por Inventario: Si falla la reserva en inventario -> Comprobar que no exista la orden en DB y que el cupón no haya sumado usos.
3. Prueba de Rollback por Cupón: Si el cupón falla -> Comprobar que no exista la orden y que el stock permanezca intacto.
4. Las aserciones deben validar el estado exacto de las tablas en PostgreSQL post-ejecución.

### Contrato esperado

Suite de pruebas de integración ejecutada con `pytest tests/integration/` finalizando al 100% en verde.

### Persistencia

Base de datos de pruebas en PostgreSQL. Persistencia física garantizada mediante tablas relacionales en PostgreSQL, con tipos de datos nativos e integridad referencial protegida.

### Relaciones

Integración de todos los modelos del ciclo de compra.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Aserciones sobre base de datos y respuestas HTTP.

### Transacciones

Verificación de comportamiento ACID en el runner de pruebas.

### Casos límite

Simulación de fallo en la base de datos justo antes del commit.

### Casos de error

Verificación de respuestas `400` y `409` estructuradas ante fallos de integración.

### Consideraciones de seguridad

Garantizar que no existan fugas de memoria o transacciones colgadas en pruebas.

### Consideraciones de rendimiento

Optimizar la creación de datos de prueba usando factories limpias (`UserFactory`, `ProductFactory`, `StockFactory`).

### Fundamentos de Python relacionados

Uso de `unittest.mock` para simular fallos controlados (`side_effect=Exception('DB Error')`).

### Conceptos Django relacionados

`TestCase` transaccional (`TransactionTestCase` o `pytest.mark.django_db(transaction=True)`).

### Conceptos DRF relacionados

Pruebas de endpoints compuestos de extremo a extremo.

### PostgreSQL

Comprobación de atomicidad real en PostgreSQL.

### Arquitectura

Las pruebas de integración validan los contratos y la coordinación entre módulos del monolito.

### Dependencias entre módulos

Los tests importan los módulos de `apps/` para configurar escenarios complejos.

### Antes de programar

1. ¿Por qué se debe usar `pytest.mark.django_db(transaction=True)` cuando se prueban bloques `transaction.atomic()` que involucran rollbacks explícitos?
2. ¿Cuál es la diferencia de alcance entre una prueba unitaria de servicio y una prueba de integración de flujo de compra?

### Pruebas mínimas

1. Ejecutar el test de camino feliz completo de creación de pedido y verificar todos los efectos en las 4 tablas involucradas.
2. Ejecutar el test con mock en `inventory.services.reserve_stock` forzando una excepción y comprobar con `Order.objects.count() == 0` que la orden fue deshecha.

### Pruebas negativas

1. Probar intento de compra concurrente de stock agotado simulando 2 peticiones y comprobar consistencia total.

### Documentación

Documentar la estrategia de pruebas de integración y los escenarios críticos en la guía de testing.

### Explicación posterior

Explica por qué una suite de integración con validación de rollback es la mayor garantía de estabilidad para un backend antes de un pase a producción.

### Aplicación profesional

Aseguramiento de calidad en pasarelas de pago, motores de comercio y sistemas de misión crítica.

### Reto adicional

Configurar un pipeline de CI con GitHub Actions que levante un contenedor de PostgreSQL y ejecute la suite de integración automáticamente en cada pull request.
