## Ejercicio 024 — Conversor de Archivos INI/Properties a JSON Estructurado (`ini2json`)

> [← Ejercicio 023](../ejercicio_023/README.md) · [Índice General](../README.md) · [Ejercicio 025 →](../ejercicio_025/README.md)

### Contexto profesional
En la modernización de sistemas heredados (legacy) y migración de aplicaciones Java/PHP hacia microservicios modernos en contenedores, se requiere convertir cientos de archivos `.ini`, `.properties` o `.cfg` a formatos estructurados JSON o YAML conservando tipado e inferencia automática.

### Problema
Construir una CLI que lea archivos INI y Java Properties, infiera tipos de datos (enteros, flotantes, booleanos `true`/`false`/`yes`/`no`, listas separadas por comas), soporte secciones anidadas y emita un documento JSON estricto.

### Usuario objetivo
Ingenieros de migración, DevOps y desarrolladores backend.

### Objetivo
Desarrollar un conversor de configuraciones clásicas a JSON estructurado con inferencia inteligente de tipos y validación de sintaxis.

### Ejemplo conceptual de uso
```bash
# Convertir un archivo config.ini a JSON
python ini2json.py config.ini -o config.json

# Convertir sin inferencia de tipos (todo como string) y con indentación de 4
python ini2json.py server.properties --no-type-inference --indent 4
```

### Requisitos funcionales
- Parsear archivos de configuración con secciones `[seccion]` y pares `clave = valor`.
- Soportar comentarios iniciados con `#` o `;`.
- Inferencia automática de tipos: booleanos (`true`, `false`, `yes`, `no`, `on`, `off`), números enteros y decimales, `null`/`none`, y arrays si el valor contiene comas y se usa `--parse-lists`.
- Opciones de estructura: anidar por secciones `{"seccion": {"clave": valor}}` o aplanar claves `{"seccion.clave": valor}` con `--flat`.
- Flag `--strict` para fallar ante claves duplicadas dentro de la misma sección.

### Requisitos de CLI
- Argumento posicional: archivo INI / Properties de entrada.
- Opción `-o / --output <RUTA>`: archivo JSON de salida (default STDOUT).
- Flag `--no-type-inference`: mantiene todos los valores como cadenas de texto puras.
- Flag `--parse-lists`: convierte cadenas separadas por comas en arrays JSON.
- Flag `--flat`: claves aplanadas.
- Opción `--indent <N>` (default 2).
- Exit code 0 en éxito, 1 en error de sintaxis de configuración, 2 en errores de archivo.

### Entradas
- Archivo de configuración INI / Properties.

### Salidas
- JSON generado en STDOUT o archivo de destino.

### Persistencia
Escritura en archivo si se usa `-o`.

### Validaciones
- Validar que el archivo de entrada tenga una sintaxis INI válida.
- Comprobar que no existan secciones duplicadas si se activa `--strict`.

### Casos límite
- Archivos sin secciones (propiedades globales al inicio del archivo; agrupar bajo sección `DEFAULT` o en la raíz).
- Valores multilínea con indentación.
- Claves con espacios o caracteres especiales.

### Manejo de errores
- `configparser.Error` con mensaje claro de línea y causa.
- `FileNotFoundError`.

### Fundamentos de Python relacionados
- Módulo estándar `configparser` (`ConfigParser`, `ExtendedInterpolation`).
- Conversión de tipos con funciones de casteo seguro.
- Módulo `json`.

### Conceptos CLI relacionados
- Transformación de formatos y normalización de esquemas.
- Inferencia de tipos vs tipado estricto.

### Herramientas o módulos para investigar
- `configparser`.
- `json`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la operación inversa (`json2ini`) en una misma herramienta modular?

### Diseño de argumentos
¿Cómo nombrarías la opción para ordenar alfabéticamente las claves en el JSON resultante (`--sort-keys`)?

### Diseño de variables
`ini_parser`, `raw_config_dict`, `typed_config_dict`, `inferred_value`, `json_output_path`.

### Antes de programar
1. ¿Cómo tratar los valores booleanos como `on` y `off` para que se conviertan a `true` y `false` reales en JSON?
2. ¿Cómo manejar variables interpoladas estilo `%(base_dir)s/logs` si el archivo INI las utiliza?

### Arquitectura
Parser (`parser.py`), motor de casteo de tipos (`type_caster.py`) y CLI.

### Pruebas mínimas
1. Convertir un INI de prueba con enteros, booleanos y strings y verificar que el JSON tenga los tipos primitivos nativos correctos.
2. Probar con `--flat` y verificar que las claves sean `seccion.clave`.

### Pruebas de error
1. Pasar un archivo corrupto con líneas sin signo `=` o formato roto con `--strict` -> Exit code 1.

### Experiencia de usuario
Salida limpia en STDOUT lista para redirección a `jq` u otras herramientas.

### Explicación posterior
Explica por qué los formatos INI carecen de especificación estándar formal y las diferencias entre dialectos (Windows INI vs Python configparser vs Java Properties).

### Aplicación profesional
Automatización de migraciones cloud, contenedorización de aplicaciones legacy y generación de ConfigMaps de Kubernetes.

### Reto adicional
Soportar la resolución automática de variables de entorno dentro del archivo INI (ej. `db_host = ${DB_HOST:localhost}`).

---
> [← Ejercicio 023](../ejercicio_023/README.md) · [Índice General](../README.md) · [Ejercicio 025 →](../ejercicio_025/README.md)
