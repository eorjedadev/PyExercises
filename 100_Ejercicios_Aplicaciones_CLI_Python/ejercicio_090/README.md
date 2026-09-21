## Ejercicio 090 — Controlador de Despliegues Canary con Rollback Automatizado (`canary-ctl`)

> [← Ejercicio 089](../ejercicio_089/README.md) · [Índice General](../README.md) · [Ejercicio 091 →](../ejercicio_091/README.md)

### Contexto profesional
En despliegues continuos avanzados, las nuevas versiones de software no se liberan al 100% de los usuarios de inmediato, sino de forma gradual (Canary Releases: 5% -> 25% -> 50% -> 100%). Un controlador automatizado monitorea continuamente las métricas de salud (tasa de errores 5xx, latencia p99) durante cada fase de incremento; si las métricas se degradan, aborta y ejecuta un rollback inmediato al 0%.

### Problema
Construir una CLI que controle y orqueste el ciclo de vida de un despliegue Canary, actualizando los porcentajes de peso de tráfico (simulados en configuración o mediante balanceador de carga), consultando métricas de salud en tiempo real desde PostgreSQL o SQLite opcional, evaluando umbrales de seguridad en cada intervalo y decidiendo de forma autónoma si promover a la siguiente fase o ejecutar un rollback total.

### Usuario objetivo
Release managers, ingenieros de DevOps y SREs.

### Objetivo
Crear un controlador de despliegues Canary automatizado con análisis de métricas en bucle cerrado, fases de progresión gradual y reversión de emergencia.

### Ejemplo conceptual de uso
```bash
# Iniciar despliegue Canary de la versión v2.4.0 con progresión automática
python canary_ctl.py start --app "orders-service" --version "v2.4.0" --steps "5,25,50,100" --interval 60 --max-error-rate 0.01

# Consultar estado en vivo del Canary activo
python canary_ctl.py status --app "orders-service"

# Forzar rollback manual inmediato al 0%
python canary_ctl.py abort --app "orders-service"
```

### Requisitos funcionales
- Subcomando `start`: inicia el despliegue Canary ejecutando la secuencia de pasos de porcentaje de tráfico (ej. 5% -> 25% -> 50% -> 100%).
- En cada fase de porcentaje:
  1. Ajustar el peso del tráfico hacia la versión Canary.
  2. Monitorear durante N segundos (`--interval`) las métricas del Canary: tasa de error % y latencia p99.
  3. Evaluar umbrales de seguridad (`--max-error-rate` y `--max-latency-p99`).
  4. Si las métricas son saludables, avanzar al siguiente paso de porcentaje.
  5. Si cualquier umbral se viola, disparar la fase de `Rollback Automático` inmediatamente (ajustar tráfico de Canary a 0%, restaurar versión estable y registrar causa del aborto).
- Subcomando `status`: muestra el porcentaje actual de tráfico, versión estable vs canary, métricas comparativas en vivo y tiempo restante en la fase.
- Subcomando `promote`: fuerza la promoción inmediata al 100% omitiendo los pasos restantes.
- Subcomando `abort`: ejecuta rollback inmediato al 0%.
- Persistencia del historial de despliegues en PostgreSQL (o SQLite opcional).

### Requisitos de CLI
- Subcomandos: `start`, `status`, `promote`, `abort`, `history`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite`.
- Opción `--steps <LISTA>` (default `10,25,50,100`).
- Opción `--interval <SEG>` (tiempo de observación por fase, default 60).
- Opción `--max-error-rate <FLOAT>` (default 0.01 = 1%).
- Opción `--max-latency-p99 <MS>` (default 500).
- Exit code 0 si el Canary se completó y promovió al 100%, 1 si se abortó por violación de métricas (Rollback), 2 en errores de configuración.

### Entradas
- Parámetros de despliegue, umbrales de métricas y credenciales de base de datos.

### Salidas
- Progreso del despliegue en tiempo real en STDOUT y registros de auditoría.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `canary_deployments`, `canary_metric_samples` y `canary_events`.

### Validaciones
- La lista de pasos debe ser estrictamente creciente y terminar en 100.
- Los umbrales de error deben ser valores entre 0.0 y 1.0.

### Casos límite
- Caída total del servicio Canary en el primer segundo del 5% de tráfico (detección inmediata sin esperar al final del intervalo).
- Tráfico insuficiente durante la fase de prueba (advertir sobre falta de muestras estadísticas).
- Interrupción de la CLI por `Ctrl+C` (preguntar si se desea abortar con rollback o dejar el Canary en el estado actual).

### Manejo de errores
- Errores de consulta de métricas de base de datos.
- Fallos de red.

### Fundamentos de Python relacionados
- Bucle de control autónomo (Closed-Loop Control Loop) con `time.sleep` y `time.time`.
- Patrón Máquina de Estados para despliegues (`STARTING`, `ANALYZING`, `PROMOTING`, `ROLLING_BACK`, `COMPLETED`, `FAILED`).
- Conexión y persistencia relacional con PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Automatización de estrategias de despliegue progresivo (Canary Deployments).
- Control de bucle cerrado y toma de decisiones autónoma en terminal.

### Herramientas o módulos para investigar
- `time`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `dry-run` para simular la progresión del Canary con métricas sintéticas antes del deploy real?

### Diseño de argumentos
¿Cómo nombrarías la opción para enviar alertas a Slack ante cada cambio de fase o ante un rollback (`--slack-webhook <URL>`)?

### Diseño de variables
`canary_deployment_id`, `current_traffic_weight_percent`, `canary_step_progression_list`, `canary_health_metrics_sample`, `canary_lifecycle_state`.

### Antes de programar
1. ¿Cómo estructurar el bucle de observación para que verifique las métricas cada 5 segundos dentro del intervalo de 60 segundos y no espere al final para abortar si hay un pico masivo de errores?
2. ¿Cómo comparar las métricas de la versión Canary contra la versión de control (versión estable actual) en lugar de usar solo umbrales absolutos?

### Arquitectura
Controlador de despliegue (`canary_controller.py`), analizador de métricas (`metric_evaluator.py`), adaptador de tráfico (`traffic_router.py`), repositorio (`canary_repo.py`) y CLI.

### Pruebas mínimas
1. Iniciar un Canary con pasos 10 -> 100 con métricas simuladas saludables y verificar que complete al 100% y retorne exit code 0.
2. Iniciar Canary e inyectar un error rate del 5% en la fase del 25%; verificar que aborte inmediatamente, ajuste el tráfico a 0% y retorne exit code 1.

### Pruebas de error
1. Configurar pasos inválidos `50,20,100` -> Exit code 2 con error de validación.

### Experiencia de usuario
Barra visual de progresión Canary: `Fase [2/4] - 25% Tráfico | Error Rate: 0.12% (Límite 1.0%) | Latencia p99: 140ms | Observando: 35s/60s...`.

### Explicación posterior
Explica la diferencia entre despliegues Canary y pruebas A/B (Canary evalúa estabilidad técnica, A/B evalúa comportamiento de negocio del usuario).

### Aplicación profesional
Automatización de releases en arquitecturas de microservicios, integración con service meshes (Istio/Linkerd) y pipelines de CD.

### Reto adicional
Implementar análisis de degradación relativo (comparación estadística Mann-Whitney U o Kolmogorov-Smirnov) entre las métricas de la versión estable y la versión Canary.

---
> [← Ejercicio 089](../ejercicio_089/README.md) · [Índice General](../README.md) · [Ejercicio 091 →](../ejercicio_091/README.md)
