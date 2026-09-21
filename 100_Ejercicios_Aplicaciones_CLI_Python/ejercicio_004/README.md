## Ejercicio 004 — Explorador y Consultor de Códigos HTTP (`http-status`)

> [← Ejercicio 003](../ejercicio_003/README.md) · [Índice General](../README.md) · [Ejercicio 005 →](../ejercicio_005/README.md)

### Contexto profesional
Durante el desarrollo de APIs REST, depuración de microservicios y análisis de logs web (Nginx/Apache), es común necesitar la definición exacta, categoría, especificación RFC y semántica de cacheabilidad de códigos de estado HTTP.

### Problema
Crear una CLI de consulta rápida que brinde información detallada de cualquier código de estado HTTP (1xx, 2xx, 3xx, 4xx, 5xx), permita listar códigos por categoría o buscar por palabra clave en la descripción.

### Usuario objetivo
Desarrolladores de software, QA engineers y administradores de sistemas.

### Objetivo
Construir una herramienta interactiva/no interactiva para consultar la base de conocimiento de códigos HTTP RFC 9110.

### Ejemplo conceptual de uso
```bash
# Consultar un código específico
python http_status.py 418

# Listar todos los códigos de la categoría 5xx (Server Error)
python http_status.py --category 5xx

# Buscar por palabra clave
python http_status.py --search "gateway"
```

### Requisitos funcionales
- Consultar por número de código (ej. 200, 404, 502).
- Mostrar: Código, Nombre canónico, Categoría, Descripción detallada, Si es cacheable según RFC y RFC de referencia.
- Filtrar por categoría (`1xx`, `2xx`, `3xx`, `4xx`, `5xx`).
- Búsqueda difusa o por substring en nombres y descripciones.

### Requisitos de CLI
- Argumento posicional opcional: código numérico (ej. `404`).
- Opciones opcionales: `--category <CAT>`, `--search <TEXTO>`, `--list`.
- Exit code 0 en consulta exitosa, 1 si el código o término no existe, 2 en argumentos inválidos.

### Entradas
- Código numérico entero o flags de búsqueda/categoría.

### Salidas
- Ficha técnica del código o lista de resultados en STDOUT.

### Persistencia
Diccionario estructurado interno o archivo JSON de catálogo integrado.

### Validaciones
- El código numérico debe estar en el rango de 100 a 599.
- La categoría debe ser una de: `1xx`, `2xx`, `3xx`, `4xx`, `5xx` o `informational`, `success`, `redirection`, `client_error`, `server_error`.

### Casos límite
- Código HTTP no estandarizado (ej. 418 I'm a teapot, 499 Client Closed Request de Nginx).
- Búsqueda sin coincidencias.
- Invocación sin argumentos (debe mostrar ayuda o resumen general).

### Manejo de errores
- Validación de tipos al parsear el número de estado.
- Mensaje amable cuando no se encuentran resultados en `--search`.

### Fundamentos de Python relacionados
- Módulo estándar `http.HTTPStatus` o estructura de datos con `dict` anidados.
- Filtrado con list comprehensions y expresiones generadoras.
- Manejo de excepciones y formateo de texto.

### Conceptos CLI relacionados
- Parámetros posicionales opcionales combinados con opciones.
- Búsquedas insensibles a mayúsculas/minúsculas en terminal.

### Herramientas o módulos para investigar
- Módulo `http.HTTPStatus` de la biblioteca estándar.
- `argparse`.

### Diseño de comandos
¿Es mejor `http-status 404` que `http-status get 404`? Evalúa ergonomía de uso.

### Diseño de argumentos
¿Cómo agregarías un flag `--verbose` para mostrar la cita completa del RFC?

### Diseño de variables
`status_code`, `status_name`, `status_category`, `is_cacheable`, `rfc_reference`, `search_term`.

### Antes de programar
1. ¿Qué información mínima necesita un desarrollador cuando consulta un código de error 4xx vs 5xx?
2. ¿Cómo estructurar el catálogo para que sea extensible a códigos no estándar de la industria (Cloudflare 520-527, Nginx 499)?

### Arquitectura
Módulo principal con separación entre catálogo de datos (`status_data.py`) y CLI (`http_status.py`).

### Pruebas mínimas
1. `python http_status.py 201` -> Debe retornar `Created` y detalles del RFC.
2. `python http_status.py --category 4xx` -> Debe listar todos los errores de cliente.

### Pruebas de error
1. `python http_status.py 999` -> Exit code 1 con mensaje de código desconocido.

### Experiencia de usuario
Utilizar código de colores ANSI si la terminal lo soporta (Verde para 2xx, Amarillo para 3xx, Rojo para 4xx/5xx).

### Explicación posterior
Explica la diferencia de cacheabilidad entre respuestas 301 (Moved Permanently) y 302/307 (Found / Temporary Redirect).

### Aplicación profesional
Herramienta de referencia rápida embebida en terminales de desarrollo y bots de diagnóstico.

### Reto adicional
Incluir ejemplos de encabezados HTTP típicamente asociados al código consultado (ej. `Location` para 201/301, `Retry-After` para 429/503).

---
> [← Ejercicio 003](../ejercicio_003/README.md) · [Índice General](../README.md) · [Ejercicio 005 →](../ejercicio_005/README.md)
