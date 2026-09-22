# Ejercicio 099 — Desafío de Dominio: Gestión de Incidentes de Seguridad con Registro Forense Inmutable

[← Ejercicio 098](../ejercicio_098/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 100 →](../ejercicio_100/README.md)

---

### Contexto de negocio

El Centro de Operaciones de Seguridad (SOC / CSIRT) de la empresa requiere un sistema interno de Gestión de Incidentes de Ciberseguridad (`apps/security_incidents`). Cuando se detecta un incidente (ej. 'Intento de intrusión por fuerza bruta', 'Fuga potencial de datos', 'Acceso no autorizado'), el sistema debe registrar la evidencia forense inmutable con sellado de tiempo criptográfico, calcular el nivel de severidad (`P1_CRITICAL`, `P2_HIGH`, `P3_MEDIUM`, `P4_LOW`), disparar el reloj de SLA estricto de respuesta y registrar cada acción del equipo de respuesta a incidentes en una cadena de bloques o hash encadenado.

### Estado actual del sistema

Monolito modular completo con módulo de auditoría y usuarios.

### Nueva necesidad

Diseñar de forma autónoma el módulo de incidentes de seguridad (`apps/security_incidents`), modelando incidentes, evidencias forenses, tareas de contención/mitigación y sellado criptográfico encadenado (Hash Chaining) para garantizar que las evidencias sean legalmente admisibles e imposibles de alterar retroactivamente.

### Objetivo

Diseñar un sistema de respuesta a incidentes de seguridad con garantías de inmutabilidad forense (Hash Chaining) y SLAs estrictos en Django/PostgreSQL.

### Actor

Analista de Seguridad SOC / Comandante de Incidentes / Auditor Forense

### Módulo responsable

Determinación autónoma por el practicante (`apps/security_incidents`)

### Entidades involucradas

El practicante debe modelar las entidades necesarias (`SecurityIncident`, `ForensicEvidence`, `IncidentActionLog`, `IncidentContainmentTask`).

### Reglas de negocio

1. Los incidentes P1_CRITICAL tienen un SLA de primera respuesta de 15 minutos y resolución de 4 horas.
2. Cada acción registrada en `IncidentActionLog` debe calcular su hash SHA-256 encadenando el hash de la acción anterior (`current_hash = sha256(prev_hash + timestamp + actor + message)`), creando un registro inmutable a prueba de manipulaciones.
3. La evidencia forense (`ForensicEvidence`) almacena los logs crudos, IPs y hashes MD5/SHA256 de los artefactos capturados.
4. Un incidente no puede cerrarse (`CLOSED`) si existen tareas de contención críticas pendientes de verificación.
5. Acceso estrictamente restringido a usuarios con rol `SECURITY_ANALYST` o `SECURITY_ADMIN`.

### Contrato esperado

El practicante debe diseñar los endpoints REST:
- `POST /api/v1/security/incidents/` (Declarar nuevo incidente de seguridad)
- `POST /api/v1/security/incidents/{id}/actions/` (Registrar acción en cadena forense)
- `POST /api/v1/security/incidents/{id}/close/` (Cierre formal con reporte de lecciones aprendidas)
- `GET /api/v1/security/incidents/{id}/verify-chain/` (Verificar integridad matemática de la cadena forense)

### Persistencia

Tablas en PostgreSQL con permisos de solo inserción (Append-Only) y cálculo de hashes.

### Relaciones

Incidentes, Evidencias, Tareas y Registros Encadenados.

### Autenticación

`IsAuthenticated` con autenticación multifactor requerida conceptualmente.

### Autorización

Solo roles de seguridad certificados (`SECURITY_ANALYST`, `SECURITY_ADMIN`).

### Validaciones

Validación matemática de la integridad de la cadena de hashes.

### Transacciones

Transacción atómica al registrar eventos en la cadena.

### Casos límite

Un atacante que gana acceso a la base de datos e intenta alterar una fila histórica de la bitácora (la función `verify-chain` detectará inmediatamente que el hash encadenado no coincide, delatando la manipulación).

### Casos de error

`403 Forbidden` a cualquier usuario estándar; `400 Bad Request` si la cadena se corrompe.

### Consideraciones de seguridad

Máximo nivel de confidencialidad, integridad y disponibilidad forense.

### Consideraciones de rendimiento

Garantizar presupuesto de consultas O(1) evitando el problema N+1 mediante `select_related` y `prefetch_related`. Uso de índices B-Tree específicos y selección acotada de columnas mediante `only()` o `defer()`.

### Fundamentos de Python relacionados

Criptografía aplicada con `hashlib.sha256`, estructuras de datos encadenadas (Blockchain / Merkle Trees conceptuales).

### Conceptos Django relacionados

Modelos inmutables, permisos de nivel de objeto y rol avanzados.

### Conceptos DRF relacionados

Diseño de contratos REST con `serializers.Serializer` / `ModelSerializer`, vistas delegadoras `APIView` o `GenericAPIView`, normalización de respuestas JSON y documentación declarativa con `@extend_schema`.

### PostgreSQL

`CREATE TABLE security_incidentactionlog (id UUID PRIMARY KEY, incident_id UUID NOT NULL, sequence INT NOT NULL, prev_hash VARCHAR(64) NOT NULL, current_hash VARCHAR(64) NOT NULL, ...);`.

### Arquitectura

`apps/security_incidents` como módulo de gobernanza y seguridad de élite en el monolito.

### Dependencias entre módulos

`apps/security_incidents` se integra con `apps/audit` y `apps/users`.

### Antes de programar

1. ¿Cómo funciona una cadena de hashes criptográficos (Hash Chaining) para probar matemáticamente que ningún registro histórico fue modificado o borrado?
2. ¿Por qué los registros forenses de un incidente de seguridad deben ser inmutables para ser válidos como evidencia legal en un juicio?

### Pruebas mínimas

1. Declarar un incidente crítico, registrar 3 acciones consecutivas -> Verificar que cada acción tenga el `prev_hash` apuntando al `current_hash` de la acción anterior.
2. Invocar `verify-chain` -> Verificar que responda `{"is_valid": true, "total_entries": 3}`.

### Pruebas negativas

1. Simular la alteración manual del texto de la acción número 2 en base de datos e invocar `verify-chain` -> Verificar que responda `{"is_valid": false, "corrupted_at_sequence": 2}`.

### Documentación

Documentar el protocolo de respuesta a incidentes y la verificación criptográfica en `docs/SECURITY_INCIDENT_RESPONSE.md`.

### Explicación posterior

Explica cómo la inmutabilidad criptográfica y los libros de contabilidad encadenados garantizan la no repudiación y la integridad forense en sistemas de seguridad empresarial.

### Aplicación profesional

Sistemas SIEM/SOC, respuesta a incidentes de ciberseguridad, trazabilidad de cadena de custodia y auditorías de cumplimiento militar/financiero.

### Reto adicional

Exportar un informe forense consolidado en formato JSON firmado criptográficamente con clave RSA privada.
