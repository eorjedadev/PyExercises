# Ejercicio 069 — Seguridad Avanzada de APIs: Prevención de Mass Assignment y OWASP Top 10 API

[← Ejercicio 068](../ejercicio_068/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 070 →](../ejercicio_070/README.md)

---

### Contexto de negocio

Las vulnerabilidades en APIs REST pueden comprometer la integridad y los datos del negocio si no se diseñan con seguridad por defecto. Entre los riesgos principales descritos en OWASP API Security Top 10 se encuentran: Mass Assignment (asignación masiva de campos privilegiados), Parameter Tampering (manipulación de parámetros ocultos), exposición excesiva de datos en respuestas y omisión de controles de autorización a nivel de función (BFLA).

### Estado actual del sistema

Múltiples endpoints implementados en el monolito.

### Nueva necesidad

Realizar una auditoría de seguridad y endurecimiento (Hardening) de todos los serializers y vistas del sistema, asegurando listas blancas estrictas de campos (`fields = [...]`), declarando campos de solo lectura (`read_only_fields`), bloqueando asignación masiva de roles/estados y validando permisos a nivel de método.

### Objetivo

Dominar las mejores prácticas de seguridad en Django REST Framework alineadas con el OWASP API Security Top 10, previniendo vulnerabilidades críticas de asignación masiva y elevación de privilegios.

### Actor

Atacante Potencial / Cliente Malicioso autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

Transversal en todas las `apps/` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

Serializers, Vistas, Permisos de todos los módulos.

### Reglas de negocio

1. NUNCA usar `fields = '__all__'` en serializers de entrada (`Create` / `Update`); declarar explícitamente la lista blanca de campos permitidos.
2. Campos críticos (`is_staff`, `is_superuser`, `role`, `status`, `total_amount`, `discount_amount`, `id`, `created_at`) deben ser `read_only_fields` o no figurar en el serializer de entrada.
3. Si un cliente malicioso envía `{"role": "ADMIN"}` en el endpoint de registro, el campo DEBE ser ignorado o la petición rechazada.
4. Prevenir Parameter Tampering: no confiar en IDs o precios enviados en el body que deban calcularse en el servidor.

### Contrato esperado

Rechazo o descarte seguro de cualquier intento de sobreescritura de campos privilegiados.

### Persistencia

Persistencia protegida contra datos manipulados.

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación estricta de listas blancas de campos.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Envío de campos no declarados en el serializer con payloads JSON complejos anidados.

### Casos de error

`400 Bad Request` ante datos incongruentes o manipulación de parámetros.

### Consideraciones de seguridad

Mitigación directa de: API1: BOLA, API3: Broken Object Property Level Authorization (Mass Assignment), API5: Broken Function Level Authorization (BFLA).

### Consideraciones de rendimiento

Serializadores ligeros con solo los campos necesarios.

### Fundamentos de Python relacionados

Manipulación segura de diccionarios, exclusión de claves.

### Conceptos Django relacionados

Políticas de seguridad en modelos y formularios.

### Conceptos DRF relacionados

`serializers.ModelSerializer`, `fields = [...]`, `read_only_fields = [...]`, `extra_kwargs`.

### PostgreSQL

Restricciones `CHECK` y valores por defecto como última línea de defensa.

### Arquitectura

Diseño defensivo (Secure by Default) en todas las capas del monolito modular.

### Dependencias entre módulos

Aplica a todas las apps del proyecto. Comunicación entre módulos restringida exclusivamente a través de interfaces públicas documentadas en `services.py` y `selectors.py`. Prohibido importar modelos directos de otras apps.

### Antes de programar

1. ¿Qué es la vulnerabilidad de Mass Assignment y cómo un atacante podría convertirse en Administrador enviando un JSON con `{"is_staff": true}` en una API mal configurada?
2. ¿Por qué `fields = '__all__'` es considerado una mala práctica de seguridad en serializers de DRF?

### Pruebas mínimas

1. Enviar una petición a `POST /api/v1/users/register/` incluyendo `"role": "ADMIN"` y `"is_staff": true` -> Verificar que el usuario se cree con rol `CUSTOMER` y `is_staff = False` (intento neutralizado).
2. Enviar una petición `POST /api/v1/orders/` incluyendo `"total_amount": "1.00"` para un producto de $100 -> Verificar que la orden se cree con el total real de $100.00.

### Pruebas negativas

1. Intentar actualizar el `sku` de un producto existente mediante `PATCH` y verificar que el SKU no se modifique.

### Documentación

Documentar la guía de seguridad de serializers y checklist OWASP en `docs/SECURITY.md`.

### Explicación posterior

Explica el decálogo OWASP API Security Top 10 y cómo la combinación de serializers con listas blancas, permisos por objeto y servicios de dominio previene el 95% de las vulnerabilidades comunes en APIs.

### Aplicación profesional

Auditorías de seguridad (Penetration Testing), cumplimiento normativo y protección contra fraudes e intrusiones.

### Reto adicional

Configurar una clase base `StrictModelSerializer` que lance un error `400 Bad Request` si el cliente envía campos desconocidos que no están definidos en `fields`.
