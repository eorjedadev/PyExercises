## Ejercicio 038 — Auditor de Matrices de Traducción e i18n (`i18n-check`)

> [← Ejercicio 037](../ejercicio_037/README.md) · [Índice General](../README.md) · [Ejercicio 039 →](../ejercicio_039/README.md)

### Contexto profesional
En aplicaciones web y móviles internacionalizadas (i18n) con soporte para múltiples idiomas (ej. `es.json`, `en.json`, `fr.json`, `de.json`), es común que los desarrolladores agreguen nuevas claves en el idioma base pero olviden agregarlas en los demás idiomas, o dejen textos vacíos o variables interpoladas incompatibles.

### Problema
Construir una CLI que analice un directorio de archivos de localización (archivos JSON o `.po` de gettext), tome un idioma como referencia base (ej. `en.json`), audite los demás archivos de idioma detectando claves faltantes, claves obsoletas (que ya no existen en base) y variables de interpolación discordantes (ej. `{userName}` en base vs `{nombre}` en destino).

### Usuario objetivo
Desarrolladores frontend, gestores de localización y traductores técnicos.

### Objetivo
Crear un auditor y sincronizador de archivos de internacionalización con validación de variables de reemplazo y reporte de cobertura.

### Ejemplo conceptual de uso
```bash
# Auditar traducciones tomando el inglés como base
python i18n_check.py locales/ --base-lang en.json

# Generar plantilla con las claves faltantes en un archivo nuevo
python i18n_check.py locales/ --base-lang en.json --sync-missing
```

### Requisitos funcionales
- Leer todos los archivos de traducción en el directorio especificado.
- Subcomando `audit`: compara cada archivo contra el archivo base y reporta:
  - Claves faltantes (missing keys).
  - Claves huérfanas/obsoletas (unused keys).
  - Valores vacíos o no traducidos (cadenas idénticas al idioma base).
  - Variables de interpolación rotas (ej. `{count}` en base vs `{total}` en traducción).
  - Porcentaje de cobertura de traducción por idioma.
- Subcomando `sync-missing`: añade automáticamente las claves faltantes al archivo de destino con un prefijo configurable (ej. `"[TODO] "` o el valor base) para que los traductores las completen.
- Subcomando `export-matrix`: genera un CSV donde cada fila es una clave y cada columna un idioma.

### Requisitos de CLI
- Argumento posicional: directorio de traducciones.
- Opción `--base-lang <ARCHIVO>` (default `en.json`).
- Subcomandos: `audit`, `sync-missing`, `export-matrix`.
- Opción `--min-coverage <PORCENTAJE>` (ej. 95 para exigir 95% de traducción en CI).
- Exit code 0 si todas las traducciones cumplen el umbral, 1 si faltan claves o hay variables rotas, 2 en errores.

### Entradas
- Archivos JSON de localización y parámetros de idioma base.

### Salidas
- Tabla de auditoría con porcentajes de cobertura y lista de claves faltantes.

### Persistencia
Modificación de archivos de traducción cuando se usa `sync-missing`.

### Validaciones
- Comprobar que el archivo base exista en el directorio.
- Validar formato JSON válido en todos los archivos de localización.

### Casos límite
- Claves con estructuras JSON profundamente anidadas (ej. `auth.login.errors.invalid_credentials`).
- Formatos de interpolación variados (ej. `{name}`, `{{name}}`, `%s`, `:name`).
- Idiomas con reglas de pluralización complejas.

### Manejo de errores
- `json.JSONDecodeError` con indicación del archivo y línea corrupta.

### Fundamentos de Python relacionados
- Navegación recursiva de árboles JSON y dot-notation.
- Expresiones regulares para extracción de variables de interpolación (`\{([^}]+)\}`).
- Operaciones de conjuntos (`set.difference`, `set.intersection`).

### Conceptos CLI relacionados
- Verificación de paridad de datos y completitud en herramientas de localización.
- Quality gate en pipelines de frontend.

### Herramientas o módulos para investigar
- `json`.
- `re`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para ordenar alfabéticamente las claves de todos los archivos JSON para mantener diffs limpios en Git (`--sort-keys`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para ignorar ciertas claves que intencionalmente no se traducen (ej. nombres de marcas)?

### Diseño de variables
`base_locale_dict`, `target_locales_map`, `missing_keys_set`, `orphaned_keys_set`, `mismatched_variables_list`, `coverage_percentage`.

### Antes de programar
1. ¿Cómo extraer todas las variables de interpolación de una cadena como `"Hola {user}, tienes {count} mensajes nuevos"` y compararlas con la traducción?
2. ¿Cómo sincronizar las claves faltantes en un JSON anidado preservando la jerarquía de objetos original?

### Arquitectura
Parser de i18n (`locale_parser.py`), motor de diferencias (`diff_analyzer.py`), sincronizador (`sync_service.py`) y CLI.

### Pruebas mínimas
1. Auditar un conjunto de prueba con `en.json` (10 claves) y `es.json` (8 claves) -> Debe detectar las 2 claves faltantes y reportar 80% de cobertura.
2. Probar detección de variable rota (`{user}` vs `{usuario}`) y verificar el reporte.

### Pruebas de error
1. Ejecutar con `--min-coverage 100` sobre traducciones incompletas -> Exit code 1.

### Experiencia de usuario
Resumen tabular limpio con barras de porcentaje coloreadas (Verde > 95%, Amarillo > 80%, Rojo < 80%).

### Explicación posterior
Explica el impacto de variables de interpolación ausentes en tiempo de ejecución (errores de frontend / KeyError en renderizado).

### Aplicación profesional
Automatización en pipelines de desarrollo web/móvil (React, Vue, Flutter) y plataformas de localización.

### Reto adicional
Integrar traducción automática preliminar de claves faltantes usando una API de traducción o servicio mock.

---
> [← Ejercicio 037](../ejercicio_037/README.md) · [Índice General](../README.md) · [Ejercicio 039 →](../ejercicio_039/README.md)
