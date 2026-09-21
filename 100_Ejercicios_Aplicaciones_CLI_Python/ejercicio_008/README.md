## Ejercicio 008 — Inspector y Validador de Claves JSON (`json-probe`)

> [← Ejercicio 007](../ejercicio_007/README.md) · [Índice General](../README.md) · [Ejercicio 009 →](../ejercicio_009/README.md)

### Contexto profesional
En arquitecturas orientadas a eventos y consumo de APIs de terceros (webhooks de Stripe, GitHub, etc.), los payloads JSON complejos con múltiples niveles de anidación deben inspeccionarse para verificar la presencia y tipo de campos requeridos.

### Problema
Desarrollar una herramienta CLI que reciba un archivo JSON o flujo por STDIN, extraiga valores usando notación de puntos (dot-notation, ej. `user.profile.address.city`), liste el esquema de claves y valide la presencia de un conjunto de campos obligatorios.

### Usuario objetivo
Desarrolladores backend, integradores de APIs y equipos de QA.

### Objetivo
Crear un inspector de estructuras JSON con soporte de dot-notation, extracción de tipos y validación de contratos.

### Ejemplo conceptual de uso
```bash
# Extraer un campo anidado
python json_probe.py config.json --get "database.credentials.host"

# Listar todas las rutas de claves disponibles en el documento
python json_probe.py payload.json --schema

# Validar presencia de campos requeridos
python json_probe.py webhook.json --require "event_id,timestamp,data.user_id"
```

### Requisitos funcionales
- Parsear documentos JSON desde archivo o STDIN.
- Navegación profunda con dot-notation y acceso a arrays por índice (ej. `items.0.id`).
- Generar el mapa plano de claves completas del documento en modo `--schema`.
- Validar lista de campos requeridos con `--require`.
- Devolver el valor extraído en texto plano o JSON formateado si es un objeto/lista.

### Requisitos de CLI
- Argumento posicional opcional: ruta al archivo JSON (lee de STDIN si se omite).
- Opción `--get <KEYPATH>`: ruta de clave a consultar.
- Opción `--schema`: imprime árbol plano de claves y tipos.
- Opción `--require <KEYPATHS>`: lista separada por comas de claves obligatorias.
- Exit code 0 si la clave/validación es exitosa.
- Exit code 1 si la clave no existe o falta algún campo requerido.
- Exit code 2 si el JSON está mal formado o hay error de sintaxis en los argumentos.

### Entradas
- Archivo JSON o flujo STDIN.
- Rutas de claves en dot-notation.

### Salidas
- Valor extraído o esquema de claves en STDOUT.
- Lista de campos faltantes o errores en STDERR.

### Persistencia
Sin persistencia.

### Validaciones
- Sintaxis JSON válida.
- Sintaxis de dot-notation correcta (no permitir rutas vacías o con puntos consecutivos).

### Casos límite
- JSON con arrays anidados dentro de objetos y objetos dentro de arrays.
- Claves JSON que contienen puntos literales en su nombre (manejo de escape o comillas).
- Valores `null`, `false`, `0` o cadenas vacías (deben extraerse correctamente sin confundirse con valores faltantes).

### Manejo de errores
- `json.JSONDecodeError`: Indicar línea y columna del error sintáctico en el JSON.
- Claves faltantes en navegación.

### Fundamentos de Python relacionados
- Módulo estándar `json` (`json.loads`, `json.dumps`, `json.load`).
- Recursividad o iteración para recorrer diccionarios y listas anidadas.
- Manejo seguro de diccionarios y listas (`isinstance(obj, dict)`).

### Conceptos CLI relacionados
- Lectura polimórfica de fuentes (archivo vs `sys.stdin`).
- Notación jerárquica de claves.

### Herramientas o módulos para investigar
- `json`.
- `sys.stdin`.
- `argparse`.

### Diseño de comandos
Compara esta herramienta con utilidades como `jq`. ¿Qué ventajas ofrece una herramienta con validaciones semánticas integradas?

### Diseño de argumentos
¿Cómo agregarías un flag `--type` para verificar que el valor extraído sea del tipo esperado (ej. `--type int`)?

### Diseño de variables
`json_data`, `key_path`, `path_tokens`, `current_node`, `missing_keys`, `schema_paths`.

### Antes de programar
1. ¿Cómo diferenciar si un valor es `None` (JSON `null`) vs si la clave no existe en el diccionario?
2. ¿Cómo recorrer recursivamente un árbol JSON para generar la lista plana de todas las rutas posibles?

### Arquitectura
Separar la función de navegación `traverse_path(data, path)` y la función `generate_schema(data)`.

### Pruebas mínimas
1. Extraer clave anidada `a.b.c` de un archivo de prueba -> Comprobar valor exacto.
2. Validar `--require` con todas las claves presentes -> Exit code 0.
3. Validar `--require` con una clave faltante -> Exit code 1 y listar la clave en STDERR.

### Pruebas de error
1. Pasar archivo JSON inválido (ej. falta una llave) -> Exit code 2 con mensaje de error.

### Experiencia de usuario
Si el valor extraído es un string, emitir sin comillas para facilitar su uso en variables de bash (`VAR=$(python json_probe.py ...)`). Si es un objeto, emitir JSON formateado.

### Explicación posterior
Explica la diferencia entre complejidad temporal de búsqueda en árbol vs indexación directa.

### Aplicación profesional
Scripts de verificación de contratos en pruebas de integración y validación de configs en pipelines de despliegue.

### Reto adicional
Añadir soporte para comodines en arrays (ej. `users.*.email` para extraer todos los correos de una lista de usuarios).

---
> [← Ejercicio 007](../ejercicio_007/README.md) · [Índice General](../README.md) · [Ejercicio 009 →](../ejercicio_009/README.md)
