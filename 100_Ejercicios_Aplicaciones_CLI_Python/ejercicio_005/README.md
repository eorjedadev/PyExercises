## Ejercicio 005 — Verificador de Integridad de Archivos por Hash (`hash-check`)

> [← Ejercicio 004](../ejercicio_004/README.md) · [Índice General](../README.md) · [Ejercicio 006 →](../ejercicio_006/README.md)

### Contexto profesional
Al descargar imágenes ISO de servidores, paquetes de software o evidencias forenses, es obligatorio verificar sumas de verificación criptográficas (SHA256, SHA512, MD5) contra manifiestos oficiales de integridad.

### Problema
Se necesita una herramienta CLI que calcule el hash criptográfico de un archivo en bloques para no saturar la memoria RAM y lo compare contra un hash esperado o contra un archivo de sumas (tipo `sha256sums.txt`).

### Usuario objetivo
Administradores de sistemas, analistas de seguridad y operadores de infraestructura.

### Objetivo
Desarrollar una utilidad de cálculo y comparación de checksums con soporte de streaming por bloques y reporte de validación.

### Ejemplo conceptual de uso
```bash
# Calcular SHA256 de un archivo
python hash_check.py firmware.bin --algo sha256

# Verificar contra un hash esperado
python hash_check.py firmware.bin --expected a3f5b8...

# Verificar un archivo de sumas
python hash_check.py --check sha256sums.txt
```

### Requisitos funcionales
- Soportar algoritmos: `md5`, `sha1`, `sha256`, `sha512` (default `sha256`).
- Leer el archivo en bloques (chunks de 64 KB o 1 MB) para procesar archivos de cualquier tamaño (incluso varios gigabytes) sin desbordar memoria.
- Comparar el hash calculado contra un hash provisto en `--expected` (insensible a mayúsculas/minúsculas).
- En modo `--check <FILE>`, parsear líneas con formato `<HASH>  <FILENAME>` y validar cada archivo listado.

### Requisitos de CLI
- Argumento posicional: archivo a analizar (o flag `--check`).
- Opción `--algo`: `md5`, `sha1`, `sha256`, `sha512`.
- Opción `--expected`: cadena hexadecimal del hash esperado.
- Opción `--check`: ruta al archivo de sumas de verificación.
- Exit code 0 si el hash coincide (o todos los hashes en `--check` son correctos).
- Exit code 1 si hay discrepancia de integridad (hash mismatch).
- Exit code 2 si los archivos no existen o los argumentos son inválidos.

### Entradas
- Ruta de archivo objetivo.
- Algoritmo de hash.
- Cadena esperada o archivo de manifiesto.

### Salidas
- Hash calculado en formato hexadecimal.
- En modo verificación: `OK` o `FAILED: Mismatch detectado`.
- Resumen de verificación de múltiples archivos en `--check`.

### Persistencia
Sin persistencia.

### Validaciones
- Comprobar que el archivo exista y no sea un directorio.
- Validar que el algoritmo solicitado esté disponible en `hashlib`.
- Validar que la cadena `--expected` contenga únicamente caracteres hexadecimales y tenga la longitud correspondiente al algoritmo (ej. 64 caracteres para SHA256).

### Casos límite
- Archivo de 0 bytes (debe calcular el hash del buffer vacío).
- Archivos muy grandes (> 4 GB).
- Archivo de sumas con rutas relativas o absolutas.
- Líneas corruptas o con formato incorrecto dentro de `sha256sums.txt`.

### Manejo de errores
- `FileNotFoundError` en archivo objetivo o de sumas.
- `PermissionError` por falta de lectura.
- Notificar archivos faltantes en modo `--check` sin abortar la verificación del resto.

### Fundamentos de Python relacionados
- Módulo estándar `hashlib` (`hashlib.sha256()`, `update()`, `hexdigest()`).
- Lectura en chunks binarios (`file.read(chunk_size)`).
- Manejo de strings y normalización (`str.lower()`, `str.strip()`).

### Conceptos CLI relacionados
- Modos de operación interactivos vs de verificación desatendida en CI/CD.
- Códigos de salida críticos para pipelines (evitar desplegar artefactos corruptos).

### Herramientas o módulos para investigar
- `hashlib`.
- `pathlib.Path`.
- `argparse`.

### Diseño de comandos
Diseña las opciones para soportar el formato estándar de herramientas GNU (`sha256sum -c`).

### Diseño de argumentos
¿Cómo permitirías especificar el tamaño de bloque de lectura mediante `--chunk-size` (ej. 64k, 1M)?

### Diseño de variables
`hasher`, `chunk_size_bytes`, `calculated_hash`, `expected_hash`, `manifest_path`, `match_status`.

### Antes de programar
1. ¿Por qué nunca se debe hacer `hasher.update(file.read())` en archivos de producción?
2. ¿Cómo estructurar el bucle `while chunk := file.read(chunk_size):`?

### Arquitectura
Estructura modular con un módulo `hasher_core.py` y el CLI `hash_check.py`.

### Pruebas mínimas
1. Generar archivo de prueba con texto conocido, calcular SHA256 y comparar con herramienta del sistema.
2. Probar `--expected` con el hash correcto -> Exit code 0.
3. Probar `--expected` con un hash alterado -> Exit code 1.

### Pruebas de error
1. Probar con un hash de longitud incorrecta en `--expected` -> Exit code 2.

### Experiencia de usuario
Mostrar una barra de progreso o porcentaje en archivos muy grandes si la salida es una TTY interactiva, u omitirla si se redirige la salida.

### Explicación posterior
Explica qué es una colisión de hash y por qué MD5 y SHA1 ya no se consideran seguros para verificación criptográfica frente a adversarios activos.

### Aplicación profesional
Verificación de artefactos de software en pipelines de release, validación de backups y auditoría de seguridad.

### Reto adicional
Implementar soporte para generar automáticamente el archivo de manifiesto `sha256sums.txt` para todos los archivos dentro de un directorio con `--generate-manifest <DIR>`.

---
> [← Ejercicio 004](../ejercicio_004/README.md) · [Índice General](../README.md) · [Ejercicio 006 →](../ejercicio_006/README.md)
