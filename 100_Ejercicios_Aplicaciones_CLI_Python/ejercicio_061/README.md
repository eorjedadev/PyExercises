## Ejercicio 061 — Servidor Mock de APIs REST con Rutas Dinámicas (`mock-api-cli`)

> [← Ejercicio 060](../ejercicio_060/README.md) · [Índice General](../README.md) · [Ejercicio 062 →](../ejercicio_062/README.md)

### Contexto profesional
Durante el desarrollo de aplicaciones frontend o pruebas de integración de microservicios, los equipos necesitan probar contra APIs que aún no han sido construidas o simular respuestas de error de servicios de terceros (ej. errores 500, demoras de red, respuestas con schemas específicos) sin levantar servidores complejos.

### Problema
Construir una CLI que levante un servidor HTTP mock ligero local, configurado mediante un archivo JSON/YAML de rutas o mediante subcomandos interactivos, capaz de responder a diferentes verbos HTTP (`GET`, `POST`, `PUT`, `DELETE`), retornar payloads estáticos o dinámicos con plantillas, simular latencia de red (`--delay`) e inyectar tasas de error aleatorias para pruebas de resiliencia.

### Usuario objetivo
Desarrolladores frontend, QA engineers y desarrolladores de backend.

### Objetivo
Implementar un servidor HTTP mock configurable desde terminal con simulación de latencia, inyección de fallas y registro de peticiones.

### Ejemplo conceptual de uso
```bash
# Iniciar servidor mock cargando catálogo de rutas desde archivo
python mock_api_cli.py serve --routes routes.json --port 8080

# Simular latencia de red de 500ms y 10% de fallos aleatorios HTTP 500
python mock_api_cli.py serve --routes routes.json --delay 500 --error-rate 0.10

# Añadir una ruta mock rápidamente desde la línea de comandos
python mock_api_cli.py add-route GET /api/v1/users --status 200 --response '{"users": [{"id": 1, "name": "Ana"}]}'
```

### Requisitos funcionales
- Servidor HTTP integrado basado en la biblioteca estándar de Python.
- Subcomando `serve`: inicia el servidor en el puerto especificado, cargando rutas con sus respectivos métodos, códigos de estado, cabeceras y cuerpos JSON de respuesta.
- Soporte de rutas con parámetros dinámicos (ej. `/api/users/:id` -> capturar `:id` en la respuesta).
- Simulación de latencia de red configurable mediante `--delay <MS>` (introduce un retardo antes de responder).
- Inyección de fallas con `--error-rate <PROB>` (ej. `0.20` responde con 500 Internal Server Error en el 20% de las peticiones).
- Registro en tiempo real de cada petición recibida en terminal (método, ruta, IP cliente, código devuelto, tiempo).
- Subcomando `add-route`: añade o actualiza una ruta en el archivo de configuración de mocks.

### Requisitos de CLI
- Subcomandos: `serve`, `add-route`, `list-routes`.
- Opción `-p / --port <PUERTO>` (default 8000).
- Opción `--routes <RUTA>` (default `routes.json`).
- Opción `--delay <MS>` (default 0).
- Opción `--error-rate <FLOAT>` (default 0.0).
- Exit code 0 en terminación limpia con `Ctrl+C`, 1 en fallo de puerto ocupado, 2 en errores de configuración.

### Entradas
- Archivo de rutas mock y parámetros de servidor.

### Salidas
- Logs de peticiones en STDOUT en tiempo real.

### Persistencia
Archivo JSON de rutas (`routes.json`).

### Validaciones
- El puerto debe ser un entero entre 1024 y 65535.
- La tasa de error debe ser un flotante entre 0.0 y 1.0.
- El payload de respuesta debe ser JSON válido si la cabecera es `application/json`.

### Casos límite
- Puerto ya en uso por otro proceso del sistema (manejo limpio de `OSError`).
- Peticiones concurrentes simultáneas hacia el servidor mock.
- Interrupción limpia con `Ctrl+C` cerrando los sockets sin dejar el puerto bloqueado (`SO_REUSEADDR`).

### Manejo de errores
- `OSError: [Errno 98/10048] Address already in use`.
- `json.JSONDecodeError` en configuración.

### Fundamentos de Python relacionados
- Módulo estándar `http.server` (`HTTPServer`, `BaseHTTPRequestHandler`, `ThreadingHTTPServer`).
- Módulo `time` (`time.sleep`) para retardo de latencia.
- Módulo `random` para inyección probabilística de fallos.
- Expresiones regulares para matching de rutas con parámetros dinámicos.

### Conceptos CLI relacionados
- Servidores embebidos en herramientas de línea de comandos.
- Registro de accesos web en terminal.

### Herramientas o módulos para investigar
- `http.server` y `socketserver`.
- `json`.
- `time` y `random`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para registrar todas las peticiones recibidas en memoria y consultarlas mediante un endpoint especial `GET /__admin/requests`?

### Diseño de argumentos
¿Cómo nombrarías la opción para habilitar CORS (Cross-Origin Resource Sharing) automáticamente en todas las respuestas (`--cors`)?

### Diseño de variables
`mock_http_server`, `routes_registry_map`, `request_log_entry`, `simulated_latency_seconds`, `error_rate_probability`.

### Antes de programar
1. ¿Por qué es fundamental usar `ThreadingHTTPServer` en lugar de `HTTPServer` para atender múltiples peticiones concurrentes del frontend sin bloquearse cuando se usa `--delay`?
2. ¿Cómo configurar `socketserver.TCPServer.allow_reuse_address = True` para poder reiniciar el servidor inmediatamente sin esperar el timeout TIME_WAIT del SO?

### Arquitectura
Manejador HTTP (`mock_handler.py`), enrutador de rutas (`router.py`), generador de respuestas (`response_factory.py`) y CLI.

### Pruebas mínimas
1. Iniciar servidor mock con una ruta `/api/test`, hacer una petición con `curl` y verificar que devuelva el código 200 y el JSON esperado.
2. Probar `--delay 200` y verificar que la respuesta tarde al menos 200ms.

### Pruebas de error
1. Intentar iniciar en un puerto ocupado -> Exit code 1 con sugerencia de usar otro puerto.

### Experiencia de usuario
Banner visual de bienvenida al iniciar indicando URL base `http://localhost:8080` y rutas activas, seguido de logs coloreados por cada petición entrante.

### Explicación posterior
Explica la diferencia entre mocks, stubs y fakes en pruebas de software y cómo los mocks de API aceleran el desarrollo desacoplado frontend/backend.

### Aplicación profesional
Entornos de desarrollo local para frontend, pruebas de integración de microservicios y simulación de proveedores de pago.

### Reto adicional
Implementar soporte para respuestas con estado (Stateful Mocks), donde un `POST /items` almacene el objeto en memoria y un posterior `GET /items` lo devuelva.

---
> [← Ejercicio 060](../ejercicio_060/README.md) · [Índice General](../README.md) · [Ejercicio 062 →](../ejercicio_062/README.md)
