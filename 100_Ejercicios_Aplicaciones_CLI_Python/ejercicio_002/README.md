## Ejercicio 002 — Codificador y Decodificador Base64 para Terminal (`b64codec`)

> [← Ejercicio 001](../ejercicio_001/README.md) · [Índice General](../README.md) · [Ejercicio 003 →](../ejercicio_003/README.md)

### Contexto profesional
En operaciones de despliegue, configuración de secretos en Kubernetes, inspección de tokens JWT y depuración de APIs, los ingenieros deben codificar y decodificar datos en Base64 rápidamente sin depender de navegadores o herramientas web inseguras.

### Problema
Construir una utilidad CLI que permita codificar o decodificar cadenas de texto o archivos completos en Base64, admitiendo salida a terminal o escritura directa en un archivo de destino.

### Usuario objetivo
Ingenieros de DevOps, administradores de sistemas y desarrolladores backend.

### Objetivo
Diseñar una herramienta robusta con flags de modo (`--encode`/`--decode`), soporte de fuentes (texto directo vs archivo) y redirección de salida.

### Ejemplo conceptual de uso
```bash
# Codificar un texto plano
python b64codec.py -e "usuario:secreto123"

# Decodificar un archivo y guardarlo en destino
python b64codec.py -d -f payload.b64 -o resultado.bin
```

### Requisitos funcionales
- Codificar cadenas de texto plano a formato Base64 estándar (RFC 4648).
- Decodificar cadenas Base64 válidas a su representación en texto plano o binario.
- Soportar entrada mediante argumento directo (`-s / --string`) o mediante archivo (`-f / --file`).
- Permitir especificar un archivo de salida (`-o / --output`) o emitir por STDOUT.

### Requisitos de CLI
- Opciones mutuamente excluyentes de acción: `-e / --encode` y `-d / --decode`.
- Opciones de entrada: `-s / --string <TEXTO>` o `-f / --file <RUTA>`.
- Opción de salida: `-o / --output <RUTA>`.
- Exit code 0 en éxito, 1 en error de decodificación/archivo, 2 en argumentos incompatibles.

### Entradas
- Modos de operación (flags).
- Fuente de datos (texto literal o ruta de archivo).
- Ruta opcional de destino.

### Salidas
- Datos codificados o decodificados en STDOUT o escritos en el archivo indicado en `-o`.
- Mensajes de error en STDERR.

### Persistencia
Escritura directa en el sistema de archivos cuando se usa `-o`.

### Validaciones
- No permitir usar `-e` y `-d` simultáneamente.
- Exigir al menos una fuente de entrada (`-s` o `-f`).
- Validar que la cadena de entrada en modo decodificación cumpla con el alfabeto y padding Base64.

### Casos límite
- Cadena vacía de entrada (debe devolver cadena vacía y exit code 0).
- Cadena Base64 con padding incompleto o caracteres fuera del alfabeto Base64.
- Archivo de entrada con contenido binario arbitrario (imágenes, PDFs).

### Manejo de errores
- `binascii.Error`: Informar que el payload no es un Base64 válido.
- `FileNotFoundError` / `PermissionError`: Errores de acceso a archivos.
- Argumentos contradictorios.

### Fundamentos de Python relacionados
- Módulo estándar `base64` (`b64encode`, `b64decode`).
- Manejo de tipos de datos `bytes` vs `str` y codificaciones (`utf-8`, `latin-1`).
- Modos de apertura de archivos binarios (`'rb'`, `'wb'`).

### Conceptos CLI relacionados
- Argumentos mutuamente excluyentes (`mutually exclusive groups`).
- Flags cortos (`-e`, `-d`, `-o`) vs largos (`--encode`, `--output`).
- Manejo de flujos binarios hacia la salida estándar.

### Herramientas o módulos para investigar
- `argparse.ArgumentParser.add_mutually_exclusive_group`.
- Módulo `base64` y `binascii`.
- `pathlib.Path`.

### Diseño de comandos
Determina si las acciones deben ser flags (`-e`/`-d`) o subcomandos (`b64codec encode` / `b64codec decode`). Compara ambas alternativas.

### Diseño de argumentos
¿Qué flag elegirías para Base64 seguro para URL (`--url-safe`)?

### Diseño de variables
Nombres recomendados: `raw_bytes`, `encoded_string`, `decoded_bytes`, `input_source`, `output_target`.

### Antes de programar
1. ¿Por qué Base64 requiere trabajar con secuencias de bytes y no con cadenas de texto nativas?
2. ¿Cómo manejarás los saltos de línea al final del archivo si el usuario codifica un archivo de texto?

### Arquitectura
Estructura modular:
```
ejercicio_002/
├── b64codec.py
└── fixtures/
    ├── plain.txt
    └── sample.b64
```

### Pruebas mínimas
1. Codificar `"hello world"` y comprobar que resulte `aGVsbG8gd29ybGQ=`.
2. Decodificar `aGVsbG8gd29ybGQ=` y comprobar que retorne `hello world`.

### Pruebas de error
1. Ejecutar `python b64codec.py -d -s "%%%NoEsBase64%%%"` -> Verificar error y exit code 1.

### Experiencia de usuario
Si la salida decodificada es texto UTF-8, debe mostrarse directamente; si contiene bytes no imprimibles y no se indicó `-o`, advertir al usuario.

### Explicación posterior
Explica la diferencia entre representación de caracteres Unicode y bytes brutos en la codificación Base64.

### Aplicación profesional
Imprescindible en pipelines CI/CD para ofuscar o empaquetar certificados, llaves SSH y tokens de acceso.

### Reto adicional
Implementar el modo `--urlsafe` que utiliza los caracteres `-` y `_` en lugar de `+` y `/` según RFC 4648 sección 5.

---
> [← Ejercicio 001](../ejercicio_001/README.md) · [Índice General](../README.md) · [Ejercicio 003 →](../ejercicio_003/README.md)
