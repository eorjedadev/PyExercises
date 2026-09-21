## Ejercicio 010 — Inspector y Auditor de Variables de Entorno (`env-inspect`)

> [← Ejercicio 009](../ejercicio_009/README.md) · [Índice General](../README.md) · [Ejercicio 011 →](../ejercicio_011/README.md)

### Contexto profesional
En entornos cloud-native (contenedores Docker, pods de Kubernetes), la configuración se inyecta mediante variables de entorno. Los operadores necesitan auditar qué variables están presentes, verificar que las variables críticas existan y comprobar que no contengan valores peligrosos o no definidos, protegiendo siempre los secretos.

### Problema
Construir una CLI que inspeccione el entorno de ejecución actual o un archivo `.env`, filtre variables por prefijo, valide una lista de variables requeridas y enmascare valores sensibles (como passwords, tokens, API keys).

### Usuario objetivo
DevOps, SREs y desarrolladores backend.

### Objetivo
Crear una herramienta de auditoría de configuración de entorno con detección automática de secretos y validación de variables requeridas.

### Ejemplo conceptual de uso
```bash
# Listar variables con prefijo APP_ enmascarando secretos
python env_inspect.py --prefix APP_

# Auditar un archivo .env específico y validar variables requeridas
python env_inspect.py --file .env.production --require "DATABASE_URL,PORT,SECRET_KEY"
```

### Requisitos funcionales
- Leer variables desde el entorno del sistema (`os.environ`) o desde un archivo `.env` proporcionado.
- Filtrar variables por prefijo (ej. `--prefix AWS_`).
- Enmascarar automáticamente (ej. `********` o `sk-...4a2b`) cualquier variable cuyo nombre contenga términos como `SECRET`, `PASSWORD`, `KEY`, `TOKEN`, `AUTH`, `PRIVATE`.
- Opción `--unmask` para mostrar valores reales únicamente bajo confirmación explícita.
- Validar lista de variables obligatorias con `--require`.

### Requisitos de CLI
- Opción `--file <RUTA>`: archivo `.env` a inspeccionar.
- Opción `--prefix <PREFIJO>`: filtra por inicio de nombre.
- Opción `--require <VARS>`: lista separada por comas de variables obligatorias.
- Flag `--unmask`: desactiva el enmascaramiento de seguridad.
- Opción `--format [table|json|dotenv]` (default `table`).
- Exit code 0 si todas las validaciones pasan, 1 si faltan variables obligatorias, 2 en errores de archivo.

### Entradas
- Variables de entorno o archivo `.env`.
- Prefijos y listas de requisitos.

### Salidas
- Tabla formateada en terminal, JSON o formato .env en STDOUT.
- Lista de variables faltantes en STDERR.

### Persistencia
Sin persistencia.

### Validaciones
- Parsear correctamente archivos `.env` considerando comentarios (`#`), líneas vacías y valores entrecomillados.
- Validar que ninguna variable requerida esté vacía si está declarada.

### Casos límite
- Variables con valores multilínea o que contienen caracteres `=` en su valor (ej. connection strings Base64).
- Valores con espacios en blanco iniciales o finales.
- Variables presentes en el sistema pero con valor de cadena vacía `""`.

### Manejo de errores
- Archivo `.env` inexistente o sin permisos.
- Errores de sintaxis en el archivo de entorno.

### Fundamentos de Python relacionados
- Módulo estándar `os` (`os.environ`).
- Parsing manual de archivos `.env` o uso de lógica de strings (`str.partition('=')`).
- Módulo `re` para detección de nombres sensibles.

### Conceptos CLI relacionados
- Seguridad en terminal: evitar fugas involuntarias de secretos en logs o grabaciones de pantalla.
- Validación de configuración pre-flight.

### Herramientas o módulos para investigar
- `os`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías una opción para exportar las variables auditadas a un template limpio (`.env.example`) sin valores?

### Diseño de argumentos
¿Cómo nombrarías la opción para fallar si una variable requerida existe pero está vacía (`--disallow-empty`)?

### Diseño de variables
`env_variables`, `sensitive_keywords`, `prefix_filter`, `required_keys`, `masked_value`, `missing_variables`.

### Antes de programar
1. ¿Por qué es una mala práctica imprimir contraseñas o tokens en texto claro por defecto en una CLI?
2. ¿Cómo parsear una línea como `DATABASE_URL="postgres://user:pass@host:5432/db?sslmode=true"` sin romper en el primer `=`?

### Arquitectura
Módulo de carga (`env_loader.py`), módulo de auditoría y enmascaramiento (`masker.py`) y CLI.

### Pruebas mínimas
1. Auditar variables con prefijo y verificar que `API_KEY` se muestre como `********`.
2. Auditar con `--require "VAR1,VAR2"` donde ambas existen -> Exit code 0.

### Pruebas de error
1. Auditar con `--require "VAR_INEXISTENTE"` -> Exit code 1 y listar el nombre faltante.

### Experiencia de usuario
La salida tabular debe presentar columnas: `VARIABLE`, `ESTADO` (Set/Empty), `LONGITUD` y `VALOR (ENMASCARADO)`.

### Explicación posterior
Explica la precedencia de configuración en aplicaciones modernas (argumentos CLI > variables de entorno > archivos de config > valores por defecto).

### Aplicación profesional
Diagnóstico de pre-arranque en contenedores Docker y verificación de despliegues en CI/CD.

### Reto adicional
Generar automáticamente un archivo `.env.example` donde todos los valores sean reemplazados por descripciones de tipo (ej. `PORT=<int>`, `DB_HOST=<string>`).

---
> [← Ejercicio 009](../ejercicio_009/README.md) · [Índice General](../README.md) · [Ejercicio 011 →](../ejercicio_011/README.md)
