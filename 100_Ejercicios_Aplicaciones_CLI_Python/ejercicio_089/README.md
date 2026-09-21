## Ejercicio 089 — Ejecutor de Transacciones Sintéticas End-to-End (`synthetic-probe`)

> [← Ejercicio 088](../ejercicio_088/README.md) · [Índice General](../README.md) · [Ejercicio 090 →](../ejercicio_090/README.md)

### Contexto profesional
Para verificar la experiencia real del usuario en plataformas de comercio electrónico y banca digital, no basta con hacer un simple ping HTTP a la página de inicio; es necesario ejecutar flujos transaccionales completos de múltiples pasos (ej. 1. Iniciar sesión -> 2. Buscar producto -> 3. Añadir al carrito -> 4. Simular checkout) validando cookies de sesión, tokens CSRF y aserciones de negocio en cada paso.

### Problema
Construir una CLI que ejecute flujos de transacciones sintéticas de extremo a extremo definidos en un archivo declarativo JSON/YAML, gestione sesiones HTTP con estado (cookies, cabeceras de autorización, variables dinámicas capturadas de pasos anteriores), evalúe aserciones en cada etapa, mida latencias acumuladas y persista el resultado y capturas de error en PostgreSQL o SQLite opcional.

### Usuario objetivo
Ingenieros de SRE, QA Automation y DevOps.

### Objetivo
Desarrollar un motor de pruebas sintéticas E2E con gestión de estado de sesión, extracción dinámica de variables (JSONPath/Regex) y persistencia relacional.

### Ejemplo conceptual de uso
```bash
# Ejecutar un flujo de transacción sintética de compra
python synthetic_probe.py run --scenario checkout_flow.json --env production

# Ver historial de ejecuciones sintéticas y tasas de éxito por paso en PostgreSQL
python synthetic_probe.py report --scenario "checkout_flow" --days 30
```

### Requisitos funcionales
- Archivo de escenario declarativo `scenario.json` que define una secuencia ordenada de pasos:
  - `step_name`: nombre del paso.
  - `request`: método HTTP, URL (con variables interpoladas), cabeceras, payload.
  - `extract`: variables a capturar de la respuesta para pasos posteriores (ej. extraer `token` de la respuesta JSON o cookie de sesión `session_id`).
  - `assert`: condiciones de éxito (código de estado esperado, latencia máxima del paso, validación de campos JSON o presencia de texto).
- Subcomando `run`: ejecuta el flujo paso a paso preservando el estado de sesión (cookies automáticas).
- Si un paso falla en sus aserciones, abortar el resto del flujo, registrar el fallo con la respuesta completa recibida para depuración y retornar exit code 1.
- Subcomando `report`: consulta estadísticas en base de datos PostgreSQL / SQLite: tasa de éxito del flujo completo, paso donde ocurren más fallos y desglose de latencia por etapa.
- Subcomando `validate-scenario`: comprueba la coherencia del archivo de escenario antes de ejecutar.

### Requisitos de CLI
- Subcomandos: `run`, `report`, `validate-scenario`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Opción `--scenario <RUTA>`.
- Opción `--timeout-total <SEG>` (default 30).
- Opción `--format [table|json]`.
- Exit code 0 si todos los pasos del escenario fueron exitosos, 1 si falló alguna aserción, 2 en errores de configuración.

### Entradas
- Archivo de escenario sintético y variables de entorno.

### Salidas
- Desglose de pasos ejecutados, latencias y causas de fallo en STDOUT.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) con tablas `synthetic_runs`, `step_results` y `captured_failures`.

### Validaciones
- Validar la estructura del escenario y que las variables extraídas en un paso no se usen antes de haber sido definidas.
- Validar métodos HTTP y URLs de cada paso.

### Casos límite
- Pasos que devuelven redirecciones HTTP (302) preservando cookies de autenticación.
- Extracción de valores de cabeceras de respuesta (ej. `Set-Cookie`, `Location`).
- Flujos con pasos condicionales o bucles de espera.

### Manejo de errores
- `urllib.error.URLError` y `TimeoutError` en peticiones.
- Fallos de aserción con guardado del payload de error.

### Fundamentos de Python relacionados
- Manejo de sesiones HTTP y cookies con `http.cookiejar.CookieJar` y `urllib.request.HTTPCookieProcessor`.
- Interpolación de variables en plantillas de cadenas.
- Medición de tiempos de alta precisión con `time.perf_counter`.
- Persistencia de ejecuciones en PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Monitoreo sintético transaccional (Synthetic Transaction Monitoring).
- Gestión de estado y encadenamiento de peticiones complejas en terminal.

### Herramientas o módulos para investigar
- `urllib.request` y `http.cookiejar`.
- `json` y `re`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para inyectar credenciales secretas en el escenario mediante variables de entorno (`--env-var "PASSWORD=secreto"`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para exportar la sesión HTTP completa en formato HAR (HTTP Archive) para reproducir en navegadores ante fallos (`--export-har failure.har`)?

### Diseño de variables
`synthetic_scenario_config`, `http_session_context`, `extracted_flow_variables_map`, `step_execution_metrics`, `scenario_run_history_dto`.

### Antes de programar
1. ¿Cómo configurar `urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))` para que todas las peticiones compartan y actualicen automáticamente las cookies de sesión entre pasos?
2. ¿Cómo capturar una variable de un JSON anidado usando dot-notation (ej. `extract: {"auth_token": "data.session.token"}`) e inyectarla en el siguiente paso en la cabecera `Authorization: Bearer ${auth_token}`?

### Arquitectura
Motor de ejecución de pasos (`step_runner.py`), gestor de sesión y cookies (`session_manager.py`), evaluador de aserciones (`assertion_engine.py`), repositorio relacional (`synthetic_repo.py`) y CLI.

### Pruebas mínimas
1. Ejecutar un escenario de prueba de 3 pasos (Login -> Get Profile -> Logout) contra una API mock local y verificar que las cookies y el token pasen correctamente de un paso al siguiente.
2. Provocar un fallo intencional en el paso 2 y verificar que el paso 3 no se ejecute y se retorne exit code 1.

### Pruebas de error
1. Pasar un archivo de escenario con sintaxis JSON rota -> Exit code 2 con mensaje claro.

### Experiencia de usuario
Resumen visual por pasos: `[Paso 1/3] Login: PASS (200 OK en 120ms)`, `[Paso 2/3] Add to Cart: PASS (201 Created en 85ms)`, `[Paso 3/3] Checkout: PASS (200 OK en 310ms) -> Transacción Sintética EXITOSA (Total: 515ms)`.

### Explicación posterior
Explica por qué el monitoreo sintético transaccional detecta caídas antes de que los usuarios reales las reporten a soporte.

### Aplicación profesional
Monitoreo proactivo de flujos de checkout en e-commerce, login bancario, verificación post-despliegue en producción y observabilidad de SLAs.

### Reto adicional
Implementar soporte para aserciones basadas en esquemas JSON Schema completos para validar la estructura del cuerpo de respuesta.

---
> [← Ejercicio 088](../ejercicio_088/README.md) · [Índice General](../README.md) · [Ejercicio 090 →](../ejercicio_090/README.md)
