## Ejercicio 012 — Generador Criptográfico de Contraseñas y UUIDs (`sec-gen`)

> [← Ejercicio 011](../ejercicio_011/README.md) · [Índice General](../README.md) · [Ejercicio 013 →](../ejercicio_013/README.md)

### Contexto profesional
Los ingenieros de infraestructura y administradores de bases de datos necesitan generar continuamente contraseñas seguras de alta entropía, llaves de API aleatorias, tokens hexadecimales y UUIDs v4 para aprovisionamiento de credenciales y semillas de bases de datos.

### Problema
Desarrollar una herramienta CLI que genere contraseñas aleatorias seguras con políticas personalizables (longitud, uso de mayúsculas, dígitos, símbolos), tokens hexadecimales, tokens Base64 y UUIDs v4, con opción de generar múltiples valores y verificar su entropía estimada.

### Usuario objetivo
Administradores de sistemas, desarrolladores y especialistas en seguridad.

### Objetivo
Crear un generador de secretos criptográficamente seguro utilizando fuentes de entropía del sistema operativo.

### Ejemplo conceptual de uso
```bash
# Generar una contraseña segura de 24 caracteres
python sec_gen.py password --length 24 --symbols

# Generar 5 UUIDs v4
python sec_gen.py uuid --count 5

# Generar un token hexadecimal de 32 bytes
python sec_gen.py token --type hex --bytes 32
```

### Requisitos funcionales
- Subcomando `password`: longitud configurable (default 16), flags para incluir/excluir mayúsculas, minúsculas, dígitos, símbolos (`!@#$%^&*...`), y flag para excluir caracteres ambiguos (`1`, `l`, `I`, `0`, `O`).
- Subcomando `uuid`: genera UUIDs v4 válidos.
- Subcomando `token`: genera tokens aleatorios en formato `hex`, `base64` o `urlsafe`.
- Opción general `--count N`: número de elementos a generar (default 1).
- Calcular y mostrar opcionalmente los bits de entropía teórica de la contraseña generada (`--entropy`).

### Requisitos de CLI
- Subcomandos: `password`, `uuid`, `token`.
- Opciones específicas según subcomando.
- Opción común `-c / --count <N>`.
- Exit code 0 en éxito, 2 en argumentos inválidos.

### Entradas
- Subcomando y parámetros de longitud/composición.

### Salidas
- Uno o varios secretos generados en STDOUT (uno por línea).
- Métricas de entropía si se solicita.

### Persistencia
Sin persistencia.

### Validaciones
- La longitud de la contraseña debe ser de al menos 4 caracteres.
- No permitir excluir todos los juegos de caracteres simultáneamente.
- El conteo `-c` debe ser un entero positivo mayor a 0.

### Casos límite
- Solicitud de contraseñas muy largas (ej. 1024 caracteres).
- Garantizar que al menos un carácter de cada juego seleccionado esté presente en la contraseña (no confiar únicamente en la probabilidad aleatoria).

### Manejo de errores
- Validación estricta de tipos en argumentos numéricos.
- Captura de combinaciones de flags incompatibles.

### Fundamentos de Python relacionados
- Módulo estándar `secrets` (`secrets.choice`, `secrets.token_hex`, `secrets.token_urlsafe`) — **nunca** usar `random` estándar para seguridad.
- Módulo `uuid` (`uuid.uuid4()`).
- Módulo `string` (`string.ascii_letters`, `string.digits`, `string.punctuation`).
- Cálculo matemático de entropía: $E = L \times \log_2(N)$.

### Conceptos CLI relacionados
- Introducción a subcomandos con `argparse` (`subparsers`).
- Generación de salidas limpias para scripting.

### Herramientas o módulos para investigar
- `secrets`.
- `uuid`.
- `argparse` y `add_subparsers`.

### Diseño de comandos
¿Cómo estructuraste los subparsers para que cada subcomando tenga sus propias opciones sin colisionar?

### Diseño de argumentos
¿Cómo permitirías especificar un conjunto de símbolos personalizado con `--custom-symbols "#@_-"`?

### Diseño de variables
`charset_pool`, `password_length`, `entropy_bits`, `generated_secrets_list`, `token_type`, `item_count`.

### Antes de programar
1. ¿Por qué el módulo `random` de Python es inseguro para generar contraseñas y llaves de cifrado?
2. ¿Cómo garantizar que si se piden mayúsculas, dígitos y símbolos, el resultado contenga efectivamente al menos un carácter de cada categoría?

### Arquitectura
Punto de entrada con configuración de subparsers y funciones generadoras independientes por tipo de secreto.

### Pruebas mínimas
1. `python sec_gen.py password --length 20` -> Verificar longitud exacta de 20 caracteres.
2. `python sec_gen.py uuid -c 3` -> Verificar que emita exactamente 3 UUIDs válidos.

### Pruebas de error
1. `python sec_gen.py password --length 2` -> Exit code 2 por longitud insegura.

### Experiencia de usuario
Cada secreto debe emitirse en una línea separada sin texto decorativo a menos que se use un flag informativo, permitiendo encadenar: `PASSWORD=$(python sec_gen.py password)`.

### Explicación posterior
Explica la fórmula de entropía de Shannon/Hartley y cuántos bits de entropía se consideran seguros hoy en día.

### Aplicación profesional
Aprovisionamiento automatizado de secretos en Terraform, scripts de inicialización de usuarios y generación de fixtures de prueba.

### Reto adicional
Añadir un modo `passphrase` para generar frases de contraseña basadas en palabras de un diccionario (estilo Diceware) separadas por guiones.

---
> [← Ejercicio 011](../ejercicio_011/README.md) · [Índice General](../README.md) · [Ejercicio 013 →](../ejercicio_013/README.md)
