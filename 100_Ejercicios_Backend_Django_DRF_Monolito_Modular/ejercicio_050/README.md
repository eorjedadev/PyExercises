# Ejercicio 050 — Procesamiento Asíncrono y Tareas en Segundo Plano (Background Tasks)

[← Ejercicio 049](../ejercicio_049/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 051 →](../ejercicio_051/README.md)

---

### Contexto de negocio

Enviar un correo electrónico de confirmación mediante un servidor SMTP externo puede tardar entre 2 y 5 segundos. Si ese envío se realiza de forma síncrona dentro del ciclo de la petición HTTP del usuario, el cliente experimentará lentitud extrema y la conexión podría cancelarse por timeout. El envío de emails y tareas pesadas debe delegarse a ejecución en segundo plano (Background Tasks).

### Estado actual del sistema

Módulo de notificaciones operativo. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Diseñar la infraestructura conceptual de tareas en segundo plano en `apps/core/tasks.py` y el servicio de envío asíncrono de emails transaccionales, integrando `django.core.mail` con soporte para ejecución no bloqueante (simulación con Threading/Worker o Celery conceptual).

### Objetivo

Comprender por qué las operaciones lentas de I/O (emails, generación de reportes, llamadas a APIs externas) no deben bloquear el hilo HTTP de la petición, dominando el desacoplamiento mediante tareas asíncronas.

### Actor

Sistema Backend ejecutando procesos internos de dominio o tareas programadas de fondo.

### Módulo responsable

`apps/core` y `apps/notifications` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`apps/core/tasks.py`, servicio `send_email_async`, `django.core.mail.backends.locmem.EmailBackend` para tests.

### Reglas de negocio

1. Toda petición HTTP debe responder al cliente en menos de 200 ms; las tareas que tomen más tiempo deben encolarse como tareas en background.
2. El envío del correo de confirmación de pedido debe dispararse SOLO tras la confirmación exitosa de la transacción en base de datos (`transaction.on_commit`).
3. Si el servidor SMTP falla, la tarea debe registrar el error sin afectar la transacción del pedido ya guardada en PostgreSQL.
4. En entorno de pruebas y desarrollo local, los emails no deben enviarse a internet real; deben registrarse en consola o en la memoria de Django (`locmem`).

### Contrato esperado

Respuesta HTTP instantánea (`201 Created`) mientras el email se procesa en segundo plano de forma no bloqueante.

### Persistencia

No bloquea la persistencia de la orden. Persistencia física garantizada mediante tablas relacionales en PostgreSQL, con tipos de datos nativos e integridad referencial protegida.

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Validar formato de destinatarios y existencia de plantilla.

### Transacciones

Uso obligatorio de `transaction.on_commit(lambda: task.delay(...))` para evitar enviar correos si la transacción hace rollback.

### Casos límite

La base de datos hace rollback por un error posterior (el email nunca debe enviarse gracias a `on_commit`).

### Casos de error

Captura y registro de fallos de SMTP en logs sin lanzar error 500 al cliente HTTP.

### Consideraciones de seguridad

No incluir datos altamente sensibles (contraseñas en texto plano) en el cuerpo de los correos electrónicos.

### Consideraciones de rendimiento

Liberación inmediata del hilo de peticiones WSGI/ASGI de Django.

### Fundamentos de Python relacionados

Programación concurrente con `threading.Thread`, closures, funciones lambda.

### Conceptos Django relacionados

`django.core.mail.send_mail`, `transaction.on_commit`, configuración de `EMAIL_BACKEND`.

### Conceptos DRF relacionados

No bloquear la vista de DRF con llamadas I/O de red.

### PostgreSQL

Alineación con el motor relacional PostgreSQL 16: tipos de datos nativos (`UUID`, `NUMERIC`, `TIMESTAMPTZ`, `JSONB`), índices B-Tree compuestos y garantías transaccionales ACID en nivel de aislamiento `READ COMMITTED`.

### Arquitectura

Las tareas asíncronas residen en `apps/notifications/tasks.py` o utilidades en `apps/core`.

### Dependencias entre módulos

`apps.orders` encola la tarea expuesta por `apps.notifications`.

### Antes de programar

1. ¿Por qué llamar a `send_mail()` directamente dentro de `create_order` dentro de un bloque `transaction.atomic()` es una pésima práctica?
2. ¿Qué ocurre si `send_mail()` se ejecuta, el correo llega al cliente, pero 1 milisegundo después la base de datos aborta la transacción por un fallo de persistencia?

### Pruebas mínimas

1. Crear una orden y verificar mediante el backend `locmem` de Django (`mail.outbox`) que el correo haya sido encolado y enviado con el asunto y destinatario correctos.
2. Probar un escenario de rollback y verificar que `len(mail.outbox) == 0` (el correo no se envió).

### Pruebas negativas

1. Simular un fallo de conexión SMTP y verificar que la orden se guarde exitosamente y el endpoint devuelva 201 sin caerse.

### Documentación

Documentar la arquitectura de tareas en background y la configuración de `EMAIL_BACKEND` en la guía del sistema.

### Explicación posterior

Explica el rol de herramientas como Celery, Redis y RabbitMQ en ecosistemas Django para tareas asíncronas a gran escala y por qué `transaction.on_commit` es el pegamento fundamental entre transacciones ACID y sistemas de colas.

### Aplicación profesional

Envío masivo de correos, transcodificación de videos, procesamiento de imágenes, sincronización con CRMs externos.

### Reto adicional

Construir una plantilla HTML profesional renderizada con `django.template.loader.render_to_string` para el correo de confirmación de pedido.
