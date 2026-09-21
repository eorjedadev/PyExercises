## Ejercicio 082 — Coordinador y Orquestador de Rotación de Secretos (`secret-rotator`)

> [← Ejercicio 081](../ejercicio_081/README.md) · [Índice General](../README.md) · [Ejercicio 083 →](../ejercicio_083/README.md)

### Contexto profesional
En cumplimiento con estándares de ciberseguridad (PCI-DSS, ISO 27001), las contraseñas de bases de datos, tokens de API y claves de cifrado deben rotarse periódicamente (ej. cada 90 días) siguiendo un protocolo seguro de múltiples pasos (generar nueva credencial, registrar en la base de datos como credencial secundaria, actualizar aplicaciones cliente, promover a credencial primaria y revocar la credencial antigua) para evitar caídas de servicio durante la transición.

### Problema
Construir una CLI que coordine el ciclo de vida completo de rotación de secretos en bases de datos relacionales (PostgreSQL como motor principal, o SQLite opcional), ejecutando la máquina de estados de rotación (`CREATE_NEW` -> `TEST_NEW` -> `PROMOTE` -> `DECOMMISSION`), manteniendo una ventana de gracia con soporte de doble credencial activa y registrando auditoría criptográfica inmutable.

### Usuario objetivo
Ingenieros de seguridad (SecOps), DBAs y arquitectos cloud.

### Objetivo
Crear un orquestador de rotación de secretos con ciclo de vida de múltiples etapas, validación de conectividad y auditoría de revocación.

### Ejemplo conceptual de uso
```bash
# Iniciar proceso de rotación de credenciales para la base de datos de producción
python secret_rotator.py rotate --secret-id "pg-app-user" --db-url "postgresql://admin:pass@localhost:5432/postgres"

# Ver estado de los secretos y días hasta su próxima rotación obligatoria
python secret_rotator.py status

# Forzar revocación de una credencial antigua tras expirar el periodo de gracia
python secret_rotator.py decommission --secret-id "pg-app-user" --version 1
```

### Requisitos funcionales
- Máquina de estados de rotación de credenciales en 4 fases:
  1. `STAGE`: Genera una nueva credencial segura de alta entropía y la crea en el servicio de destino (ej. nuevo usuario/password en PostgreSQL) sin borrar la actual.
  2. `TEST`: Prueba una conexión real usando la nueva credencial generada. Si falla, aborta y elimina la credencial candidata.
  3. `PROMOTE`: Actualiza la bóveda de secretos o archivo de configuración para que las aplicaciones comiencen a usar la nueva credencial, marcando la credencial previa como `GRACE_PERIOD` (periodo de gracia).
  4. `DECOMMISSION`: Tras expirar el periodo de gracia (o mediante confirmación explícita), revoca y elimina definitivamente la credencial antigua del servicio de destino.
- Subcomando `rotate <SECRET_ID>`: orquesta el ciclo de rotación completo de forma interactiva o automatizada.
- Subcomando `status`: tabla con lista de secretos, versión activa, versión en periodo de gracia, fecha de última rotación y días restantes de vigencia.
- Subcomando `decommission <SECRET_ID>`: elimina la credencial en periodo de gracia.

### Requisitos de CLI
- Subcomandos: `rotate`, `status`, `decommission`, `rollback`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Opción `--secret-id <ID>`.
- Opción `--grace-period-hours <N>` (default 24).
- Flag `--auto-decommission`.
- Exit code 0 en rotación exitosa, 1 si el test de la nueva credencial falló (abortando la rotación de forma segura), 2 en errores.

### Entradas
- Identificadores de secreto, credenciales administrativas y políticas de rotación.

### Salidas
- Reporte de fases de rotación completadas y estado de credenciales en STDOUT.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `managed_secrets`, `secret_versions` y `rotation_audit_log`.

### Validaciones
- La nueva credencial generada debe cumplir con políticas de complejidad criptográfica (longitud mínima 32 caracteres, alta entropía).
- Prohibir la rotación simultánea de un secreto que ya tiene un proceso de rotación en curso (estado bloqueado).

### Casos límite
- Fallo de red durante la creación de la nueva credencial (limpieza y descarte automático del estado intermedio).
- Base de datos de destino que no permite múltiples contraseñas activas para el mismo usuario (manejo con usuarios duales `user_a` / `user_b`).
- Rollback de emergencia si las aplicaciones reportan fallos durante la fase de promoción.

### Manejo de errores
- Errores de autenticación y conexión en fase `TEST`.
- Excepciones de base de datos.

### Fundamentos de Python relacionados
- Módulo `secrets` para generación de contraseñas de alta entropía.
- Patrón Máquina de Estados y control transaccional relacional.
- Conexiones administrativas a PostgreSQL (`CREATE USER`, `ALTER USER`, `DROP USER`).

### Conceptos CLI relacionados
- Automatización de protocolos de rotación de credenciales sin interrupción de servicio (Zero-Downtime Credential Rotation).
- Gestión de periodos de gracia y revocación controlada.

### Herramientas o módulos para investigar
- `secrets`.
- `psycopg`.
- `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para notificar a los microservicios consumidores mediante un evento de webhook para que recarguen la nueva credencial en caliente?

### Diseño de argumentos
¿Cómo nombrarías la opción para simular la rotación completa sin alterar usuarios reales (`--dry-run`)?

### Diseño de variables
`secret_identifier_id`, `current_secret_version_dto`, `staged_secret_version_dto`, `rotation_stage_enum`, `rotation_audit_entry`.

### Antes de programar
1. ¿Por qué cambiar una contraseña en un solo paso (`ALTER USER pass`) provoca errores en todas las instancias de aplicación hasta que reinicien y por qué el patrón de credenciales duales en periodo de gracia elimina las caídas?
2. ¿Cómo estructurar el test de conexión para probar la nueva credencial en un pool aislado antes de promoverla a producción?

### Arquitectura
Generador de credenciales (`secret_generator.py`), adaptador de destino PostgreSQL (`postgres_auth_adapter.py`), orquestador de estados (`rotation_orchestrator.py`) y CLI.

### Pruebas mínimas
1. Ejecutar rotación sobre una base de datos PostgreSQL de prueba (o SQLite con `--driver sqlite`), verificar que genere la versión 2, pase la prueba de conexión y marque la versión 1 en periodo de gracia.
2. Ejecutar `decommission` y verificar que la versión 1 sea revocada y eliminada.

### Pruebas de error
1. Simular un fallo forzado en la prueba de conexión de la nueva credencial -> Verificar que aborte la rotación, limpie la credencial candidata y deje la versión 1 intacta con exit code 1.

### Experiencia de usuario
Resumen claro por etapas: `[1/4] Generando nueva credencial v2... OK`, `[2/4] Probando autenticación con v2... OK (Conexión verificada)`, `[3/4] Promoviendo v2 a activa (v1 entra en periodo de gracia de 24h)... OK`.

### Explicación posterior
Explica los riesgos de seguridad de credenciales estáticas de larga duración (Long-Lived Credentials) y las ventajas de la rotación automatizada frecuente.

### Aplicación profesional
Automatización de rotación de contraseñas de bases de datos, claves de cifrado de almacenamiento y tokens de APIs de terceros.

### Reto adicional
Implementar integración con HashiCorp Vault o AWS Secrets Manager mediante adaptadores de backend para sincronizar el valor rotado en la nube.

---
> [← Ejercicio 081](../ejercicio_081/README.md) · [Índice General](../README.md) · [Ejercicio 083 →](../ejercicio_083/README.md)
