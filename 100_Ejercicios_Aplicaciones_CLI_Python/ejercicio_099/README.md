## Ejercicio 099 — Motor de Refactorización Automatizada y Codemods AST (`codemod-cli`)

> [← Ejercicio 098](../ejercicio_098/README.md) · [Índice General](../README.md) · [Ejercicio 100 →](../ejercicio_100/README.md)

### Contexto profesional
Al actualizar versiones mayores de frameworks (ej. migrar de Python 3.8 a 3.12, migrar de una versión de librería obsoleta a una nueva API), refactorizar manualmente miles de archivos de código fuente es inviable y propenso a errores humanos. Se utilizan herramientas de refactorización automatizada basadas en el Árbol de Sintaxis Abstracta (AST - Abstract Syntax Tree / Codemods) que transforman el código de forma determinista respetando la semántica del lenguaje.

### Problema
Construir una CLI que analice código fuente de Python, parsee el Árbol de Sintaxis Abstracta (`ast`), aplique transformaciones sintácticas y semánticas configurables (ej. renombrar métodos deprecados, modernizar formateo `%` y `.format()` a f-strings, añadir anotaciones de tipo automáticas, actualizar importaciones obsoletas), genere diffs unificados para revisión previa con `--dry-run` y modifique los archivos de forma segura.

### Usuario objetivo
Ingenieros de plataforma, desarrolladores de librerías y líderes técnicos.

### Objetivo
Desarrollar un motor de transformaciones de código (Codemods) basado en el AST nativo de Python con generación de diffs y refactorización determinista.

### Ejemplo conceptual de uso
```bash
# Simular la refactorización de llamadas a métodos obsoletos generando diffs en terminal
python codemod_cli.py run ./src --transform "replace-deprecated-api" --dry-run

# Aplicar transformación in-place reemplazando .format() por f-strings
python codemod_cli.py run ./src --transform "modernize-fstrings" --write

# Listar todas las recetas de refactorización (codemods) disponibles
python codemod_cli.py list-transforms
```

### Requisitos funcionales
- Parsing del código fuente a nodos AST mediante el módulo estándar `ast`.
- Catálogo de transformaciones (Codemods) integradas:
  - `modernize-fstrings`: convierte llamadas simples `"Hola {}".format(name)` o `"%s" % name` en f-strings modernas `f"Hola {name}"`.
  - `rename-method`: renombra llamadas a métodos deprecados en clases u objetos (ej. `obj.old_fetch()` -> `obj.fetch_all()`).
  - `update-imports`: actualiza declaraciones de importación obsoletas (ej. `from typing import Dict, List` -> tipos nativos `dict`, `list`).
  - `add-type-annotations`: añade sugerencias de anotación de tipo básicas a funciones.
- Subcomando `run`: recorre los archivos del proyecto, ejecuta el `NodeTransformer` correspondiente, regenera el código fuente con `ast.unparse()` (o librerías de AST) y compara contra el archivo original.
- Modo `--dry-run`: genera y muestra un diff unificado estilo `git diff` resaltando las líneas añadidas en verde y eliminadas en rojo sin tocar el disco.
- Flag `--write / -w`: aplica los cambios sobreescribiendo los archivos en disco previa creación de backup de seguridad.

### Requisitos de CLI
- Subcomandos: `run`, `list-transforms`, `test-transform`.
- Argumento posicional: directorio o archivos a refactorizar.
- Opción `-t / --transform <NOMBRE>`.
- Flag `--dry-run`.
- Flag `-w / --write`.
- Exit code 0 si la refactorización se completó (o no hubo archivos que modificar), 1 si se detectaron errores de sintaxis en el código analizado, 2 en errores de argumentos.

### Entradas
- Código fuente en archivos `.py` y recetas de transformación.

### Salidas
- Diffs coloreados en terminal o archivos modificados en disco.

### Persistencia
Modificación directa de archivos de código en disco si se usa `-w / --write`.

### Validaciones
- Verificar que el código resultante tras la transformación sea sintácticamente válido volviendo a parsearlo con `ast.parse()` antes de escribir en disco (garantía de no romper código).
- Comprobar que los archivos existan.

### Casos límite
- Archivos con errores de sintaxis preexistentes (`SyntaxError`; reportar y omitir sin colapsar el proceso global).
- Preservación de comentarios y docstrings durante la regeneración del código.
- Transformaciones complejas con variables anidadas.

### Manejo de errores
- `SyntaxError` al parsear archivos fuente.
- `PermissionError` al intentar escribir.

### Fundamentos de Python relacionados
- Módulo estándar `ast` (`ast.parse`, `ast.NodeTransformer`, `ast.NodeVisitor`, `ast.unparse`).
- Generación de diffs de texto unificados con módulo estándar `difflib` (`difflib.unified_diff`).
- `pathlib.Path` para recorrido recursivo de archivos.

### Conceptos CLI relacionados
- Diseño de herramientas de transformación automatizada de código (Codemods).
- Visualización de diffs unificados en terminal y refactorización segura.

### Herramientas o módulos para investigar
- `ast`.
- `difflib`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `test-transform --transform <NOMBRE> --snippet "código"` para probar una transformación interactivamente sobre un fragmento en memoria?

### Diseño de argumentos
¿Cómo nombrarías la opción para pasar parámetros dinámicos a la transformación (ej. `--param "old_name=foo,new_name=bar"`)?

### Diseño de variables
`source_ast_tree`, `ast_node_transformer_instance`, `transformed_ast_tree`, `unparsed_source_code`, `unified_diff_lines_list`.

### Antes de programar
1. ¿Cómo heredar de `ast.NodeTransformer` y sobreescribir métodos como `visit_Call(self, node)` para interceptar llamadas a funciones y modificar sus argumentos o nombre de método?
2. ¿Cómo usar `difflib.unified_diff(original_lines, new_lines)` para generar la salida estándar de diferencias de Git?

### Arquitectura
Motor de AST (`ast_engine.py`), catálogo de transformaciones (`transforms/`), generador de diffs (`diff_viewer.py`) y CLI.

### Pruebas mínimas
1. Aplicar la transformación `modernize-fstrings` sobre un archivo con `"Hola {}".format(nombre)` con `--dry-run` y verificar que el diff muestre `+ f"Hola {nombre}"`.
2. Aplicar con `--write` y verificar que el archivo físico se actualice y conserve sintaxis válida de Python.

### Pruebas de error
1. Intentar ejecutar una transformación inexistente -> Exit code 2 con lista de transformaciones disponibles.

### Experiencia de usuario
Diffs coloreados en terminal: Rojo `-` para líneas eliminadas y Verde `+` para líneas refactorizadas, con resumen final: `12 archivos modificados, 48 transformaciones aplicadas`.

### Explicación posterior
Explica el concepto del Árbol de Sintaxis Abstracta (AST) y por qué las refactorizaciones basadas en AST son semánticamente seguras comparadas con simples búsquedas y reemplazos por expresiones regulares.

### Aplicación profesional
Migraciones masivas de bases de código corporativas, actualización de versiones de Python y frameworks (Django, FastAPI), y linters con auto-fix.

### Reto adicional
Implementar un transformador que detecte funciones síncronas bloqueantes y las convierta automáticamente a corutinas asíncronas `async def` con `await` en llamadas de I/O.

---
> [← Ejercicio 098](../ejercicio_098/README.md) · [Índice General](../README.md) · [Ejercicio 100 →](../ejercicio_100/README.md)
