## Ejercicio 049 — Validador de Conventional Commits y Hook de Git (`commit-lint`)

> [← Ejercicio 048](../ejercicio_048/README.md) · [Índice General](../README.md) · [Ejercicio 050 →](../ejercicio_050/README.md)

### Contexto profesional
En proyectos de desarrollo colaborativo con metodologías CI/CD y generación automatizada de changelogs, todos los mensajes de commit de Git deben cumplir con la especificación estándar *Conventional Commits* (ej. `feat(auth): add OAuth2 login support` o `fix(db): handle connection timeout`).

### Problema
Construir una CLI que valide mensajes de commit contra la especificación Conventional Commits (validando tipo, scope opcional, descripción en minúsculas, longitud máxima de cabecera y cuerpo), permitiendo instalarse automáticamente como un Git Hook (`commit-msg`) en el repositorio local y registrando estadísticas de commits en base de datos relacional.

### Usuario objetivo
Desarrolladores, líderes de equipo y mantenedores de repositorios.

### Objetivo
Crear un linter de mensajes de commit con integración de Git Hooks, validación estricta de expresiones regulares y soporte para reglas de equipo personalizadas.

### Ejemplo conceptual de uso
```bash
# Validar un mensaje de commit pasado como texto o archivo
python commit_lint.py verify -m "feat(auth): implement JWT token refresh"

# Instalar el hook de Git automáticamente en el repositorio actual
python commit_lint.py hook-install

# Validar el mensaje de commit generado por Git durante commit-msg
python commit_lint.py verify --msg-file .git/COMMIT_EDITMSG
```

### Requisitos funcionales
- Validar estructura estándar: `<type>(<scope>): <subject>` seguido opcionalmente de cuerpo y pie (`BREAKING CHANGE:` o referencias a issues `Closes #123`).
- Tipos permitidos por defecto: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.
- Reglas de validación estrictas:
  - Longitud máxima de la primera línea (cabecera): 72 caracteres.
  - El asunto (`subject`) no debe iniciar con mayúscula ni terminar con punto final.
  - El tipo debe estar en minúsculas.
- Subcomando `hook-install`: copia o escribe el script ejecutable en `.git/hooks/commit-msg` para interceptar `git commit`.
- Subcomando `hook-uninstall`: desinstala el hook de forma segura.
- Subcomando `history-audit`: analiza los últimos N commits del historial de Git (`git log`) y reporta porcentaje de cumplimiento de la convención.

### Requisitos de CLI
- Subcomandos: `verify`, `hook-install`, `hook-uninstall`, `history-audit`.
- Opciones de `verify`: `-m / --message <TEXTO>` o `--msg-file <RUTA>`.
- Opción `--config <RUTA>` para tipos o scopes personalizados.
- Exit code 0 si el mensaje es válido, 1 si viola las reglas (bloqueando el commit en Git), 2 en errores.

### Entradas
- Mensajes de commit (texto o archivo `COMMIT_EDITMSG`).

### Salidas
- Confirmación de éxito o reporte detallado de errores de sintaxis en STDERR.

### Persistencia
Creación del hook ejecutable en `.git/hooks/` y persistencia opcional de métricas de calidad en PostgreSQL/SQLite.

### Validaciones
- Rechazar mensajes vacíos o con solo espacios en blanco.
- Validar que el archivo `.git/hooks` exista al instalar el hook.

### Casos límite
- Commits de merge automáticos generados por Git (ej. `Merge branch 'main' of ...` -> permitir omitir validación con `--allow-merge-commits`).
- Commits de revert o fixup (`fixup! ...`).
- Mensajes multilínea con descripción detallada.

### Manejo de errores
- `FileNotFoundError` si no se encuentra en la raíz de un repo Git.

### Fundamentos de Python relacionados
- Expresiones regulares avanzadas con grupos de captura nombrados.
- Manejo de archivos y permisos ejecutables (`os.chmod` en Unix para `0o755`).
- Módulo `subprocess` para invocar `git log`.

### Conceptos CLI relacionados
- Integración nativa con el ciclo de vida de Git (Git Hooks).
- Bloqueo de operaciones mediante códigos de salida no nulos.

### Herramientas o módulos para investigar
- `re`.
- `pathlib` y `os.chmod`.
- `subprocess`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para que el hook pregunte interactivamente si se desea editar el mensaje en caso de error?

### Diseño de argumentos
¿Cómo nombrarías la opción para exigir scopes obligatorios pertenecientes a una lista cerrada (`--scopes "api,ui,core,db"`)?

### Diseño de variables
`commit_header_regex`, `parsed_commit_type`, `commit_scope`, `commit_subject`, `lint_error_messages_list`.

### Antes de programar
1. ¿Cómo diseñar la expresión regular para capturar `type`, `scope` opcional, `!` para breaking changes y `subject` en una sola pasada?
2. ¿Cómo funciona el hook `commit-msg` de Git y qué argumento recibe (la ruta al archivo temporal que contiene el mensaje escrito por el usuario)?

### Arquitectura
Linter de mensajes (`commit_validator.py`), instalador de hooks (`hook_installer.py`), auditor de historial (`history_scanner.py`) y CLI.

### Pruebas mínimas
1. Validar `feat(auth): add google login` -> Debe pasar exitosamente con exit code 0.
2. Validar `Arreglo de bug en login.` (sin tipo, mayúscula, punto final) -> Debe fallar con exit code 1 y listar los 3 errores detectados.

### Pruebas de error
1. Ejecutar `hook-install` fuera de un repositorio Git -> Exit code 2 con error claro.

### Experiencia de usuario
Mensajes de error altamente pedagógicos que indiquen qué regla falló y muestren un ejemplo correcto de cómo corregirlo.

### Explicación posterior
Explica cómo Conventional Commits habilita la automatización total de releases semánticos (Semantic Release) y generación de Changelogs sin intervención humana.

### Aplicación profesional
Estandarización de repositorios de código en empresas de tecnología y quality gates en pipelines de CI/CD.

### Reto adicional
Implementar un modo asistente interactivo (`wizard`) que guíe al desarrollador paso a paso haciendo preguntas para armar el mensaje de commit perfecto y ejecutar `git commit`.

---
> [← Ejercicio 048](../ejercicio_048/README.md) · [Índice General](../README.md) · [Ejercicio 050 →](../ejercicio_050/README.md)
