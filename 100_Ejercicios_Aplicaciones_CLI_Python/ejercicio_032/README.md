## Ejercicio 032 — Monitor de Salud de Endpoints API (`api-ping`)

> [← Ejercicio 031](../ejercicio_031/README.md) · [Índice General](../README.md) · [Ejercicio 033 →](../ejercicio_033/README.md)

### Contexto profesional
Los equipos de operaciones y backend necesitan verificar continuamente que sus microservicios y endpoints críticos respondan con códigos 2xx, validando además que el tiempo de respuesta esté por debajo de un umbral y que el cuerpo JSON contenga campos esperados.

### Problema
Construir una CLI con subcomandos para registrar endpoints HTTP objetivo (targets), ejecutar rondas de comprobación de salud (health check), validar aserciones (código HTTP, latencia máxima, presencia de texto/claves JSON en la respuesta) y almacenar el historial de resultados para generar reportes de disponibilidad.

### Usuario objetivo
DevOps, SREs y desarrolladores backend.

### Objetivo
Crear un monitor ligero de disponibilidad de APIs con gestión de targets, motor de aserciones y reporte de métricas.

### Ejemplo conceptual de uso
```bash
# Registrar un endpoint a monitorear con aserciones
python api_ping.py add "users-api" https://api.ejemplo.com/health --expect-status 200 --max-latency 300

# Ejecutar verificación de todos los targets registrados
python api_ping.py check

# Ver reporte de disponibilidad y latencia promedio
python api_ping.py report --days 7
```

### Requisitos funcionales
- Subcomando `add <NOMBRE> <URL>`: registra un target con método HTTP, cabeceras personalizadas, código de estado esperado y latencia máxima tolerada en ms.
- Subcomando `list`: lista los targets configurados y sus reglas.
- Subcomando `remove <NOMBRE>`: elimina un target.
- Subcomando `check [NOMBRE]`: ejecuta peticiones a uno o todos los targets, evalúa las aserciones, registra el resultado (éxito/fallo, latencia real, timestamp) y reporta en terminal.
- Subcomando `report`: genera estadísticas de uptime (% de disponibilidad, latencia media, mín y máx) a partir del historial persistido.
- Subcomando `export`: exporta la telemetría histórica a formato CSV o JSON.

### Requisitos de CLI
- Subcomandos: `add`, `list`, `remove`, `check`, `report`, `export`.
- Opciones de `check`: `--timeout <SEG>`, `--retries <N>`.
- Exit code 0 si todos los checks pasan, 1 si al menos un target falla en sus aserciones, 2 en errores.

### Entradas
- URLs, aserciones y parámetros de red.

### Salidas
- Tabla en terminal con estado visual (`PASS` / `FAIL`), latencia y causas de fallo.

### Persistencia
Archivo JSON o base de datos local con targets y registro histórico de ejecuciones.

### Validaciones
- Validar formato de URL y métodos HTTP válidos (`GET`, `POST`, `HEAD`).
- Validar que los códigos de estado esperados sean enteros entre 100 y 599.

### Casos límite
- Endpoints que caen en timeout de red.
- Respuestas HTTP con códigos 5xx o respuestas no JSON.
- Ejecución concurrente o secuencial de targets.

### Manejo de errores
- `urllib.error.URLError` y `socket.timeout`.
- Errores de parsing de respuesta.

### Fundamentos de Python relacionados
- `urllib.request` y `urllib.error`.
- Módulo `time` (`time.perf_counter()`).
- Módulo `json` y manejo de estructuras de datos históricas.
- Subparsers en `argparse`.

### Conceptos CLI relacionados
- Motor de aserciones configurable desde línea de comandos.
- Uso de exit codes para alertamiento en cron o CI/CD.

### Herramientas o módulos para investigar
- `urllib.request`.
- `time`.
- `json`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para enviar un payload JSON en peticiones POST de verificación (`--payload '{"ping": true}'`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para validar que el body de la respuesta contenga una subcadena específica (`--expect-body "status:ok"`)?

### Diseño de variables
`target_name`, `target_url`, `expected_status_code`, `max_latency_threshold_ms`, `actual_latency_ms`, `check_result_history`.

### Antes de programar
1. ¿Cómo estructurar el motor de aserciones para que reporte exactamente qué falló (ej. 'Falló: código esperado 200, recibido 503' o 'Falló: latencia 450ms > 300ms')?
2. ¿Cómo limitar el tamaño del historial de checks para que no crezca indefinidamente en disco?

### Arquitectura
Modelos de target (`target_model.py`), cliente de verificación (`ping_client.py`), motor de reportes (`reporter.py`) y CLI.

### Pruebas mínimas
1. Registrar un target hacia un endpoint de prueba mock.
2. Ejecutar `check` y verificar que el resultado sea `PASS` y se registre en el historial.
3. Ejecutar `report` y verificar que el uptime sea del 100%.

### Pruebas de error
1. Registrar target con latencia máxima de 1ms hacia internet -> Debe fallar la aserción y retornar exit code 1.

### Experiencia de usuario
Resumen claro en terminal con marcas de color: verde para checks exitosos, rojo para fallidos con el motivo exacto al lado.

### Explicación posterior
Explica la diferencia entre sondas de disponibilidad (Liveness Probes) y sondas de preparación (Readiness Probes) en arquitecturas de microservicios.

### Aplicación profesional
Sondas de monitorización sintética, health checks en pipelines de CD antes de promover tráfico y tableros de status.

### Reto adicional
Implementar ejecución periódica continua en bucle con intervalo configurable (`--watch --interval 10`) mostrando una visualización dinámica en terminal.

---
> [← Ejercicio 031](../ejercicio_031/README.md) · [Índice General](../README.md) · [Ejercicio 033 →](../ejercicio_033/README.md)
