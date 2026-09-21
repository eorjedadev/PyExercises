## Ejercicio 014 — Filtro de Reemplazo y Grep en Pipelines (`stream-replace`)

> [← Ejercicio 013](../ejercicio_013/README.md) · [Índice General](../README.md) · [Ejercicio 015 →](../ejercicio_015/README.md)

### Contexto profesional
En la administración de servidores y automatización de despliegues, es constante la necesidad de procesar flujos continuos de texto, sanitizar salidas en tiempo real o buscar y reemplazar patrones en cadenas dentro de pipelines complejos sin generar archivos intermedios.

### Problema
Construir una CLI que lea líneas desde STDIN o archivo, aplique transformaciones basadas en expresiones regulares o reemplazos literales, filtre líneas que coincidan con un criterio y emita la salida línea a línea de manera inmediata (unbuffered).

### Usuario objetivo
Ingenieros de DevOps y administradores de sistemas.

### Objetivo
Crear un filtro de texto para streaming con soporte de regex, flags de sensibilidad, filtros de inclusión/exclusión y salida directa.

### Ejemplo conceptual de uso
```bash
# Reemplazar una IP por localhost en un flujo de logs
cat app.log | python stream_replace.py --search "192\.168\.1\.[0-9]+" --replace "127.0.0.1" --regex

# Filtrar solo líneas con ERROR y reemplazar timestamp
python stream_replace.py server.log --filter "ERROR" --search "DEBUG" --replace "INFO"
```

### Requisitos funcionales
- Procesar entrada desde `sys.stdin` o archivo especificado.
- Buscar y reemplazar cadenas literales o patrones regex (`--regex`).
- Filtrado previo de líneas (`--filter <PATTERN>` para incluir solo las que coincidan, `--exclude <PATTERN>` para omitir).
- Opción `--ignore-case / -i` para operaciones insensibles a mayúsculas.
- Emisión inmediata a STDOUT usando `flush=True` para trabajar en tiempo real.

### Requisitos de CLI
- Argumento posicional opcional: archivo de entrada (default STDIN).
- Opción `-s / --search`: patrón a buscar.
- Opción `-r / --replace`: texto de reemplazo (default cadena vacía para eliminar).
- Opciones `--filter` y `--exclude`.
- Flag `--regex`.
- Flag `-i / --ignore-case`.
- Exit code 0 si se procesó correctamente, 1 si no hubo ninguna coincidencia en modo búsqueda, 2 en errores.

### Entradas
- Flujo de texto.
- Patrones y opciones de reemplazo.

### Salidas
- Flujo de texto transformado en STDOUT.

### Persistencia
Sin persistencia.

### Validaciones
- Si se especifica `--regex`, validar que el patrón compile correctamente.
- No permitir `--filter` y `--exclude` con patrones idénticos contradictorios.

### Casos límite
- Expresiones regulares que coinciden con cadenas vacías (evitar bucles infinitos).
- Sustituciones de grupos de captura regex (ej. `\1`, `\g<name>`).
- Flujos infinitos (ej. `tail -f app.log | python stream_replace.py ...`).

### Manejo de errores
- `re.error`: Explicar sintaxis inválida en la expresión regular.
- `BrokenPipeError` al cerrarse el pipe consumidor.

### Fundamentos de Python relacionados
- Módulo `re` (`re.compile`, `re.sub`, `re.IGNORECASE`).
- Generadores e iteración sobre `sys.stdin`.
- Función `print(..., flush=True)` o `sys.stdout.write()`.

### Conceptos CLI relacionados
- Procesamiento en streaming sin buffer (unbuffered I/O).
- Composabilidad Unix mediante pipes.

### Herramientas o módulos para investigar
- `re`.
- `sys.stdin` y `sys.stdout`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para limitar el número de reemplazos por línea (`--count N`)?

### Diseño de argumentos
¿Cómo agregarías un flag `--color` para resaltar en terminal las partes reemplazadas?

### Diseño de variables
`compiled_search_regex`, `replacement_text`, `line_filter_regex`, `input_stream`, `processed_line`.

### Antes de programar
1. ¿Por qué es crítico iterar con `for line in sys.stdin:` en lugar de `sys.stdin.readlines()` cuando se procesan logs en tiempo real?
2. ¿Cómo manejar `signal.signal(signal.SIGINT, ...)` para salir limpiamente sin trazas feas?

### Arquitectura
Módulo con pipeline de generadores desacoplados.

### Pruebas mínimas
1. Pasar un texto con 3 IPs y reemplazarlas con `--regex` -> Comprobar que todas cambien.
2. Probar exclusión con `--exclude "IGNORAR"` y comprobar que las líneas desaparezcan.

### Pruebas de error
1. Pasar `--regex "[a-z"` (regex sin cerrar) -> Exit code 2 con mensaje claro.

### Experiencia de usuario
Comportamiento idéntico al estándar Unix: silencioso en éxito, rápido y predecible.

### Explicación posterior
Explica qué es el buffer de E/S del sistema operativo y por qué el vaciado de buffer (`flush`) es necesario en pipelines en vivo.

### Aplicación profesional
Sanitización de credenciales en streaming de logs, filtrado de eventos y formateo de telemetría.

### Reto adicional
Soportar lectura de reemplazos masivos desde un archivo de reglas JSON o YAML con `--rules-file`.

---
> [← Ejercicio 013](../ejercicio_013/README.md) · [Índice General](../README.md) · [Ejercicio 015 →](../ejercicio_015/README.md)
