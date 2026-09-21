## Ejercicio 055 — Gestor de Feature Flags con Backend Relacional (`feature-flag-cli`)

> [← Ejercicio 054](../ejercicio_054/README.md) · [Índice General](../README.md) · [Ejercicio 056 →](../ejercicio_056/README.md)

### Contexto profesional
En el desarrollo de software moderno con integración continua y despliegues sin interrupción (Trunk-Based Development), las funcionalidades en desarrollo se ocultan o activan condicionalmente mediante banderas de características (Feature Flags / Feature Toggles). Los equipos necesitan administrar estas banderas desde la terminal, habilitándolas por porcentaje de usuarios, por rol o por entorno.

### Problema
Construir una CLI que administre banderas de características (Feature Flags) persistidas en una base de datos relacional (PostgreSQL como backend principal, o SQLite local opcional), permitiendo crear flags, alternar su estado (`enable`/`disable`), configurar reglas de segmentación (ej. porcentaje de rollout 0-100%, lista blanca de usuarios, entornos permitidos) y evaluar en tiempo real si un flag está activo para un contexto dado.

### Usuario objetivo
Desarrolladores de software, DevOps y product managers.

### Objetivo
Crear un gestor de banderas de características con reglas de segmentación porcentual determinista, persistencia relacional y exportación de SDK.

### Ejemplo conceptual de uso
```bash
# Crear una nueva feature flag con rollout del 25%
python feature_flag_cli.py create "new_checkout_v2" --description "Nuevo flujo de pago" --rollout 25 --env production

# Alternar estado global de una flag
python feature_flag_cli.py toggle "new_checkout_v2" --enable

# Evaluar si la flag está activa para un usuario específico
python feature_flag_cli.py evaluate "new_checkout_v2" --user-id "usr_8832" --env production
```

### Requisitos funcionales
- Subcomando `create <NOMBRE>`: registra un nuevo flag con descripción, estado global (`ENABLED`/`DISABLED`), porcentaje de rollout (0 a 100%), lista blanca de usuarios permitidos y entorno (`development`, `staging`, `production`).
- Subcomando `toggle <NOMBRE> [--enable|--disable]`: cambia el estado global del flag.
- Subcomando `set-rollout <NOMBRE> <PORCENTAJE>`: ajusta el porcentaje de rollout gradual.
- Subcomando `add-user <NOMBRE> <USER_ID>`: añade un usuario específico a la lista blanca de acceso anticipado.
- Subcomando `list`: tabla de flags con estado, rollout %, total de usuarios permitidos y entorno.
- Subcomando `evaluate <NOMBRE> --user-id <ID> --env <ENTORNO>`: evalúa las reglas y determina si la flag está activa para ese usuario mediante hash determinista (hashing del `user_id + flag_name % 100 < rollout_percent`).
- Subcomando `export-sdk`: exporta el estado actual de todas las flags a un archivo JSON optimizado para ser consumido por aplicaciones cliente.

### Requisitos de CLI
- Subcomandos: `create`, `toggle`, `set-rollout`, `add-user`, `list`, `evaluate`, `export-sdk`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Exit code 0 en éxito (o si el flag evalúa como TRUE en `evaluate`), 1 si el flag no existe o evalúa como FALSE, 2 en errores.

### Entradas
- Nombres de flags, porcentajes, IDs de usuario y credenciales de BD.

### Salidas
- Tablas de flags, estado de evaluación (`TRUE` / `FALSE`) y archivos JSON exportados.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `feature_flags`, `flag_user_whitelist` y `flag_audit_log`.

### Validaciones
- El nombre del flag debe ser un slug válido (letras minúsculas, números y guiones bajos).
- El porcentaje de rollout debe ser un entero entre 0 y 100.

### Casos límite
- Banderas deshabilitadas globalmente (deben evaluar siempre a FALSE salvo que el usuario esté en la lista blanca con override forzado).
- Rollout determinista: el mismo usuario debe recibir consistentemente el mismo resultado de evaluación para un porcentaje dado.
- Banderas con nombres duplicados en el mismo entorno.

### Manejo de errores
- Excepciones de base de datos.
- Flag no encontrada.

### Fundamentos de Python relacionados
- Hashing determinista para distribución uniforme con `hashlib.md5` o `hashlib.sha256`.
- Persistencia relacional con PostgreSQL / SQLite.
- Dataclasses y serialización JSON.

### Conceptos CLI relacionados
- Implementación de lógica de segmentación y evaluación condicional.
- Uso de códigos de salida semánticos para evaluación booleana en scripts (0=True, 1=False).

### Herramientas o módulos para investigar
- `hashlib`.
- `psycopg` / `sqlite3`.
- `json` y `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `delete <NOMBRE>` para retirar una feature flag obsoleta tras completar su rollout al 100%?

### Diseño de argumentos
¿Cómo nombrarías la opción para evaluar múltiples flags simultáneamente para un usuario (`--flags "flag1,flag2,flag3"`)?

### Diseño de variables
`flag_name_slug`, `global_enabled_status`, `rollout_percentage_int`, `whitelist_users_set`, `evaluation_hash_value`, `evaluation_boolean_result`.

### Antes de programar
1. ¿Cómo funciona el algoritmo de rollout porcentual determinista: `int(hashlib.md5(f'{user_id}:{flag_name}'.encode()).hexdigest(), 16) % 100 < rollout_percent`?
2. ¿Por qué este algoritmo garantiza que si aumentas el rollout del 20% al 30%, todos los usuarios que ya tenían la flag activa sigan teniéndola activa?

### Arquitectura
Motor de evaluación (`evaluator.py`), repositorio relacional (`flag_repository.py`), servicio de exportación (`sdk_exporter.py`) y CLI.

### Pruebas mínimas
1. Crear flag con rollout del 50%, evaluar 100 usuarios de prueba y verificar que aproximadamente el 50% de las evaluaciones retornen TRUE de forma consistente.
2. Añadir un usuario a la whitelist de una flag con 0% de rollout y verificar que evalúe como TRUE.

### Pruebas de error
1. Intentar crear un flag con rollout de 150% -> Exit code 2 con error de validación.

### Experiencia de usuario
Tabla clara con colores: Verde para flags habilitadas, Gris para deshabilitadas, y resumen visual del porcentaje de rollout.

### Explicación posterior
Explica la diferencia entre Feature Flags de lanzamiento (Release Toggles), de experimentación (A/B Testing Toggles) y de operaciones (Kill Switches).

### Aplicación profesional
Despliegues progresivos (Canary Releases), pruebas A/B en producción y desactivación inmediata de funcionalidades defectuosas sin requerir nuevo deploy.

### Reto adicional
Implementar soporte para reglas de activación basadas en fechas de inicio y fin programadas (ej. activar automáticamente una promoción el día X a las 00:00 UTC).

---
> [← Ejercicio 054](../ejercicio_054/README.md) · [Índice General](../README.md) · [Ejercicio 056 →](../ejercicio_056/README.md)
