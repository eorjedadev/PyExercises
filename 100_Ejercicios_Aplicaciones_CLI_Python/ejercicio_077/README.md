## Ejercicio 077 — Validador de Especificaciones OpenAPI y Cambios Rupturistas (`openapi-check`)

> [← Ejercicio 076](../ejercicio_076/README.md) · [Índice General](../README.md) · [Ejercicio 078 →](../ejercicio_078/README.md)

### Contexto profesional
En arquitecturas orientadas a APIs REST, los contratos de servicios se documentan formalmente mediante especificaciones OpenAPI v3.0 / v3.1 (Swagger). Al modificar una API, introducir cambios que rompen la compatibilidad hacia atrás (Breaking Changes, como eliminar un endpoint, renombrar un campo requerido o cambiar el tipo de dato de una respuesta) interrumpe el funcionamiento de aplicaciones móviles y clientes externos.

### Problema
Construir una CLI que valide la sintaxis de documentos OpenAPI (JSON/YAML) contra el esquema oficial y compare dos versiones de una especificación OpenAPI (v1 vs v2), detectando automáticamente cambios que rompen la compatibilidad hacia atrás y emitiendo un reporte de compatibilidad semántica para CI/CD.

### Usuario objetivo
Arquitectos de API, desarrolladores backend y QA engineers.

### Objetivo
Crear un validador de contratos OpenAPI y detector de Breaking Changes semánticos entre versiones de APIs.

### Ejemplo conceptual de uso
```bash
# Validar sintaxis y estructura de una especificación OpenAPI
python openapi_check.py validate openapi.json

# Comparar dos versiones de OpenAPI y detectar breaking changes
python openapi_check.py diff openapi_v1.json openapi_v2.json --fail-on-breaking
```

### Requisitos funcionales
- Subcomando `validate <SPEC_FILE>`: valida que el documento OpenAPI contenga campos obligatorios (`openapi`, `info.title`, `info.version`, `paths`) y que los métodos HTTP, parámetros y esquemas de respuesta estén bien formados.
- Subcomando `diff <SPEC_V1> <SPEC_V2>`: analiza diferencias semánticas identificando:
  - Breaking Changes (Cambios Rupturistas):
    - Rutas o métodos HTTP eliminados (ej. `DELETE /users/{id}` eliminado).
    - Nuevos parámetros obligatorios (`required: true`) en endpoints existentes.
    - Eliminación de campos en respuestas exitosas (200 OK).
    - Cambio de tipos de datos en propiedades de respuesta (ej. `integer` a `string`).
    - Nuevos códigos de error obligatorios.
  - Non-Breaking Changes (Cambios Compatibles):
    - Nuevos endpoints o métodos HTTP añadidos.
    - Nuevos parámetros opcionales añadidos.
    - Nuevos campos opcionales en respuestas.
- Subcomando `stats <SPEC_FILE>`: resume total de endpoints, operaciones agrupadas por método y modelos definidos.

### Requisitos de CLI
- Subcomandos: `validate`, `diff`, `stats`.
- Flag `--fail-on-breaking`: retorna exit code 1 si se detectan breaking changes en `diff`.
- Opción `--format [table|json|markdown]`.
- Exit code 0 si la validación o diff no tiene breaking changes, 1 si hay breaking changes con `--fail-on-breaking`, 2 en errores.

### Entradas
- Archivos de especificación OpenAPI en formato JSON o YAML.

### Salidas
- Reporte de validación, ficha de diferencias semánticas y alertas en STDOUT.

### Persistencia
Sin persistencia.

### Validaciones
- Comprobar que los archivos de especificación existan y sean JSON/YAML válidos.
- Validar que la versión declarada sea OpenAPI 3.0.x o 3.1.x.

### Casos límite
- Referencias internas `$ref` anidadas (ej. `"$ref": "#/components/schemas/UserDto"`; resolver referencias para comparar esquemas reales).
- Respuestas polimórficas (`oneOf`, `anyOf`, `allOf`).
- Parámetros en query string vs path vs header vs body.

### Manejo de errores
- `json.JSONDecodeError`.
- Referencias `$ref` rotas o no resolubles.

### Fundamentos de Python relacionados
- Navegación y resolución recursiva de diccionarios JSON anidados.
- Resolución de referencias JSON Pointer (`$ref`).
- Comparación de grafos y esquemas de tipos de datos.

### Conceptos CLI relacionados
- Diseño de herramientas de gobernanza y compatibilidad de APIs (API Governance).
- Control de compatibilidad hacia atrás (Backward Compatibility) en CI/CD.

### Herramientas o módulos para investigar
- `json`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `export-postman` para convertir la especificación OpenAPI a una colección de Postman?

### Diseño de argumentos
¿Cómo nombrarías la opción para ignorar cambios en endpoints marcados con `deprecated: true` (`--ignore-deprecated`)?

### Diseño de variables
`openapi_spec_v1_dict`, `openapi_spec_v2_dict`, `resolved_schemas_map`, `breaking_changes_list`, `non_breaking_changes_list`.

### Antes de programar
1. ¿Cómo resolver referencias `$ref: '#/components/schemas/Item'` siguiendo las claves del propio diccionario JSON en memoria?
2. ¿Por qué añadir una nueva propiedad obligatoria a la petición de un cliente existente rompe a los clientes antiguos, mientras que añadir una propiedad opcional no lo hace?

### Arquitectura
Parser y resolutor `$ref` (`spec_resolver.py`), validador de sintaxis (`spec_validator.py`), comparador semántico (`breaking_diff_engine.py`) y CLI.

### Pruebas mínimas
1. Validar un `openapi.json` de prueba bien formado y verificar que retorne exit code 0.
2. Comparar v1 vs v2 donde se eliminó un campo de respuesta en v2 y verificar que `diff` lo clasifique como `BREAKING CHANGE` y retorne exit code 1 con `--fail-on-breaking`.

### Pruebas de error
1. Pasar un archivo OpenAPI sin la sección obligatoria `paths` -> Exit code 2 con error de validación.

### Experiencia de usuario
Reporte visual claro con categorías diferenciadas: Rojo con icono `[BREAKING]` para cambios rupturistas y Verde con `[COMPATIBLE]` para adiciones seguras.

### Explicación posterior
Explica la Ley de Postel (Principio de Robustez: *'Sé conservador en lo que envías y liberal en lo que aceptas'*) y su aplicación al diseño de contratos de API.

### Aplicación profesional
Quality gates en pipelines de CI/CD para repositorios de microservicios, previniendo despliegues que rompan clientes frontend o móviles.

### Reto adicional
Generar automáticamente la recomendación de incremento de versión SemVer requerida (ej. si hay breaking changes sugerir incremento `MAJOR`, si solo hay adiciones compatibles sugerir `MINOR`).

---
> [← Ejercicio 076](../ejercicio_076/README.md) · [Índice General](../README.md) · [Ejercicio 078 →](../ejercicio_078/README.md)
