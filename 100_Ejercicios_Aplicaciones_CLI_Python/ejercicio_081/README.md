## Ejercicio 081 — Conmutador Blue-Green de Configuraciones con Rollback (`bg-switcher`)

> [← Ejercicio 080](../ejercicio_080/README.md) · [Índice General](../README.md) · [Ejercicio 082 →](../ejercicio_082/README.md)

### Contexto profesional
En despliegues de cero tiempo de inactividad (Zero-Downtime Blue-Green Deployments), los servidores web (Nginx/HAProxy) apuntan su configuración activa a uno de dos entornos idénticos: el entorno Azul (Blue / activo) o el entorno Verde (Green / inactivo). Para conmutar el tráfico de forma atómica y segura, se utilizan enlaces simbólicos (symlinks) o conmutadores de configuración con pruebas de salud previas y capacidad de reversión instantánea (Rollback).

### Problema
Construir una CLI que orqueste la conmutación de entornos Blue/Green mediante manipulación atómica de enlaces simbólicos en el sistema de archivos o actualización de configuraciones en base de datos (PostgreSQL/SQLite), realizando pruebas de salud (preflight health check) al entorno inactivo antes de conmutar, verificando que el nuevo entorno responda correctamente y ejecutando rollback automático si se detectan anomalías tras el cambio.

### Usuario objetivo
Ingenieros de DevOps, release managers y administradores de sistemas.

### Objetivo
Desarrollar un orquestador de conmutación Blue-Green atómico con validación de salud pre/post conmutación y rollback automático.

### Ejemplo conceptual de uso
```bash
# Conmutar tráfico hacia el entorno inactivo tras verificar salud
python bg_switcher.py switch --app "payment-api" --target green --health-url "http://localhost:8081/health"

# Ver estado actual de los entornos Blue y Green
python bg_switcher.py status --app "payment-api"

# Revertir inmediatamente al entorno anterior (Rollback de emergencia)
python bg_switcher.py rollback --app "payment-api"
```

### Requisitos funcionales
- Gestión de dos entornos: `blue` y `green` con sus respectivos directorios o endpoints de servicio.
- Subcomando `status`: muestra qué entorno está actualmente activo (`LIVE`), qué versión tiene desplegada, timestamp de última conmutación y estado de salud de ambos entornos.
- Subcomando `switch`: ejecuta el flujo de conmutación seguro:
  1. Fase Preflight: ejecuta health check contra el entorno inactivo (`--health-url`). Si falla, aborta inmediatamente sin alterar el entorno activo.
  2. Fase Conmutación Atómica: actualiza el enlace simbólico del entorno activo (`current -> /apps/green`) mediante un symlink temporal y `os.replace` atómico, o recarga la configuración del servidor web.
  3. Fase Post-Switch: verifica durante N segundos que el nuevo entorno mantenga respuestas exitosas. Si detecta errores 5xx, ejecuta `rollback` automático inmediatamente.
- Subcomando `rollback`: conmuta de vuelta al entorno previo de forma forzada.
- Registro de auditoría de conmutaciones en PostgreSQL (o SQLite opcional).

### Requisitos de CLI
- Subcomandos: `switch`, `status`, `rollback`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Opción `--app <NOMBRE>`.
- Opción `--target [blue|green|auto]` (default `auto` conmuta al inactivo).
- Opción `--health-url <URL>`.
- Opción `--post-check-seconds <SEG>` (default 5).
- Flag `--force` para omitir preflight checks en emergencias.
- Exit code 0 en conmutación exitosa, 1 si el health check falló y se abortó o ejecutó rollback, 2 en errores de configuración.

### Entradas
- Nombres de aplicación, targets y URLs de verificación de salud.

### Salidas
- Resumen del proceso de conmutación paso a paso en STDOUT.

### Persistencia
Manipulación atómica de symlinks en disco y registro de eventos en base de datos relacional PostgreSQL / SQLite.

### Validaciones
- Comprobar que el directorio o endpoint del entorno objetivo exista y esté operativo.
- Validar que no se intente conmutar hacia el entorno que ya está activo a menos que se use `--force`.

### Casos límite
- Servidor web que no recarga automáticamente el symlink modificado (ofrecer opción de comando de reload `--reload-cmd "nginx -s reload"`).
- Caída del nuevo entorno exactamente durante la fase post-check (activación del rollback automático).
- Entornos en sistemas operativos sin soporte nativo de symlinks atómicos.

### Manejo de errores
- `urllib.error.URLError` en health checks.
- `OSError` en manipulación de enlaces simbólicos.

### Fundamentos de Python relacionados
- Manipulación atómica de symlinks (`os.symlink`, `os.replace`).
- Cliente HTTP para sondas de salud con `urllib.request` y `time.sleep`.
- Persistencia de auditoría con PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Patrón arquitectónico de despliegue Blue-Green (Zero-Downtime Deployment).
- Operaciones atómicas y recuperación automática ante fallos (Automated Rollback).

### Herramientas o módulos para investigar
- `os.symlink` y `os.replace`.
- `urllib.request`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `deploy <ENV> <ARTEFACTO>` para desempaquetar la nueva versión en el entorno inactivo antes de hacer `switch`?

### Diseño de argumentos
¿Cómo nombrarías la opción para enviar un tráfico de prueba progresivo (Canary) antes del switch completo?

### Diseño de variables
`active_environment_name`, `target_environment_name`, `symlink_current_path`, `health_check_endpoint_url`, `rollback_triggered_boolean`.

### Antes de programar
1. ¿Por qué cambiar un symlink directamente con `ln -sf` no es 100% atómico en todos los sistemas operativos y por qué crear un symlink temporal `current_tmp` y renombrarlo con `os.replace()` garantiza atomicidad total a nivel de inodo?
2. ¿Cómo diseñar la fase de post-check para que si 1 de las 5 peticiones posteriores falla, se revierta el symlink al entorno original en menos de 50 milisegundos?

### Arquitectura
Gestor de symlinks (`symlink_switcher.py`), probador de salud (`health_verifier.py`), orquestador de rollback (`rollback_coordinator.py`) y CLI.

### Pruebas mínimas
1. Configurar estructura Blue/Green con 2 carpetas de prueba, ejecutar `switch --target green` con health check exitoso y verificar que el symlink `current` apunte a `green`.
2. Probar con un health check que devuelve error 500 y verificar que aborte sin alterar el symlink original.

### Pruebas de error
1. Simular fallo en post-check y verificar que ejecute el rollback automático restaurando `blue` y retornando exit code 1.

### Experiencia de usuario
Progreso visual detallado: `[1/3] Verificando salud de entorno 'green'... OK (HTTP 200 en 15ms)`, `[2/3] Conmutando symlink atómico... OK`, `[3/3] Monitoreando estabilidad post-switch (5s)... OK. Conmutación exitosa a GREEN`.

### Explicación posterior
Explica la diferencia entre despliegues Blue-Green (conmutación total de tráfico) y despliegues Canary (conmutación gradual por porcentajes de tráfico).

### Aplicación profesional
Orquestación de despliegues de cero inactividad en servidores Nginx, actualización de workers de procesamiento y gestión de releases.

### Reto adicional
Implementar integración con balanceadores de carga para drenar gradualmente las conexiones activas del entorno saliente (Connection Draining) tras el switch.

---
> [← Ejercicio 080](../ejercicio_080/README.md) · [Índice General](../README.md) · [Ejercicio 082 →](../ejercicio_082/README.md)
