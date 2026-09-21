## Ejercicio 033 — Linter de Reglas de Seguridad para Dockerfile (`docker-lint`)

> [← Ejercicio 032](../ejercicio_032/README.md) · [Índice General](../README.md) · [Ejercicio 034 →](../ejercicio_034/README.md)

### Contexto profesional
En la creación de imágenes de contenedores Docker, seguir malas prácticas de seguridad (ej. ejecutar contenedores como usuario `root`, usar imágenes base sin tag fijo como `:latest`, incluir secretos mediante `ENV` o `ARG`, instalar paquetes sin limpiar la caché de `apt`/`apk`) expone vulnerabilidades en producción.

### Problema
Construir una CLI que analice archivos `Dockerfile`, parsee sus instrucciones (`FROM`, `RUN`, `USER`, `COPY`, `ADD`, `ENV`, `EXPOSE`), evalúe un catálogo de reglas de seguridad y buenas prácticas, y genere un reporte con severidades (Error, Warning, Info) y códigos de salida para CI.

### Usuario objetivo
Ingenieros de DevOps, desarrolladores y especialistas en ciberseguridad.

### Objetivo
Desarrollar un analizador estático (linter) para Dockerfiles con motor de reglas extensible y evaluación de severidades.

### Ejemplo conceptual de uso
```bash
# Analizar un Dockerfile del proyecto
python docker_lint.py Dockerfile

# Fallar el pipeline si hay errores o advertencias (warnings)
python docker_lint.py Dockerfile --fail-on warning

# Listar todas las reglas de seguridad disponibles
python docker_lint.py rules list
```

### Requisitos funcionales
- Parsear instrucciones estándar de Dockerfile respetando líneas continuadas con barra invertida (`\`) y comentarios (`#`).
- Reglas integradas esenciales:
  - `DL001`: Prohibir uso de tag `:latest` en instrucción `FROM`.
  - `DL002`: Exigir instrucción `USER` no root antes de finalizar el Dockerfile.
  - `DL003`: Prohibir `ADD` para URLs remotas (recomendar `curl`/`wget` en `RUN` para trazabilidad).
  - `DL004`: Detectar variables `ENV` o `ARG` con nombres sospechosos de contener secretos (`PASSWORD`, `SECRET`, `TOKEN`).
  - `DL005`: Recomendar flag `--no-cache` en comandos `apk add` o `rm -rf /var/lib/apt/lists/*` en `apt-get`.
  - `DL006`: Prohibir exponer puertos inseguros (ej. puerto 22 SSH).
- Subcomando `rules list`: lista reglas, severidad y descripción.
- Opción `--ignore <REGLAS>` para omitir reglas específicas (ej. `--ignore DL001,DL005`).

### Requisitos de CLI
- Argumento posicional: archivo `Dockerfile`.
- Subcomando `rules list`.
- Opción `--fail-on [error|warning|info]` (default `error`).
- Opción `--format [table|json|checkstyle]` (default `table`).
- Exit code 0 si no se superó el umbral de fallos, 1 si se violaron reglas según `--fail-on`, 2 en errores de archivo.

### Entradas
- Archivo `Dockerfile` y configuración de reglas.

### Salidas
- Reporte de hallazgos por línea con severidad, código de regla y recomendación.

### Persistencia
Sin persistencia.

### Validaciones
- Comprobar que el archivo exista y no esté vacío.

### Casos límite
- Dockerfiles multi-etapa (multi-stage builds con múltiples instrucciones `FROM`).
- Instrucciones `RUN` complejas con scripts multilínea.
- Archivos con nombres personalizados (ej. `Dockerfile.prod`, `Dockerfile.dev`).

### Manejo de errores
- `FileNotFoundError`.
- Advertencia si una instrucción de Dockerfile no puede ser parseada.

### Fundamentos de Python relacionados
- Expresiones regulares para parsing de directivas.
- Arquitectura de clases para reglas (`Rule`, `Finding`, `LinterEngine`).
- Módulo `argparse` con subparsers.

### Conceptos CLI relacionados
- Diseño de linters y analizadores estáticos de código.
- Integración de herramientas de análisis estático en flujos de integración continua.

### Herramientas o módulos para investigar
- `re`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo permitirías cargar reglas personalizadas desde un archivo externo JSON/YAML (`--custom-rules rules.json`)?

### Diseño de argumentos
¿Cómo nombrarías la opción para ignorar una regla en una línea específica mediante un comentario en el Dockerfile (ej. `# docker-lint:ignore DL001`)?

### Diseño de variables
`dockerfile_instructions_list`, `active_rules_registry`, `lint_findings`, `severity_threshold`, `multistage_from_targets`.

### Antes de programar
1. ¿Cómo recomponer correctamente las líneas de un Dockerfile que están unidas con el carácter `\` al final de la línea?
2. ¿Cómo comprobar que una imagen multi-etapa tenga `USER` definido en la etapa final?

### Arquitectura
Parser de Dockerfile (`parser.py`), catálogo de reglas (`rules/`), motor de evaluación (`engine.py`) y CLI.

### Pruebas mínimas
1. Analizar un Dockerfile vulnerable de prueba (con `FROM alpine:latest` y sin `USER`) y verificar que reporte `DL001` y `DL002`.
2. Probar `--fail-on error` y verificar que retorne exit code 1.

### Pruebas de error
1. Pasar un archivo que no existe -> Exit code 2 con error claro.

### Experiencia de usuario
Tabla de hallazgos con colores por severidad: Rojo para Error, Amarillo para Warning, Azul para Info, indicando `LÍNEA:CÓDIGO:RECOMENDACIÓN`.

### Explicación posterior
Explica por qué ejecutar contenedores Docker como usuario root representa un riesgo crítico de escape de contenedor (container breakout).

### Aplicación profesional
Security gates en CI/CD (GitHub Actions / GitLab CI) antes de compilar y publicar imágenes en Docker Hub o AWS ECR.

### Reto adicional
Generar automáticamente la salida en formato compatible con SARIF (Static Analysis Results Interchange Format) para visualización nativa en GitHub Code Scanning.

---
> [← Ejercicio 032](../ejercicio_032/README.md) · [Índice General](../README.md) · [Ejercicio 034 →](../ejercicio_034/README.md)
