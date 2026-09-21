## Ejercicio 070 — Generador de Software Bill of Materials SBOM (`sbom-gen`)

> [← Ejercicio 069](../ejercicio_069/README.md) · [Índice General](../README.md) · [Ejercicio 071 →](../ejercicio_071/README.md)

### Contexto profesional
Para asegurar la cadena de suministro de software (Software Supply Chain Security) y cumplir con directivas de ciberseguridad internacionales, las organizaciones deben generar un Manifiesto de Componentes de Software (SBOM - Software Bill of Materials) en formatos estándar (CycloneDX o SPDX) que inventaríe todas las dependencias directas y transitivas, licencias, hashes y proveedores de un proyecto.

### Problema
Construir una CLI que analice el entorno de paquetes instalados de Python o archivos de bloqueo de dependencias (`requirements.txt`, `Pipfile.lock`, `poetry.lock`, `pyproject.toml`), resuelva el árbol de dependencias, extraiga licencias y hashes de los paquetes y genere un documento SBOM estándar en formato CycloneDX JSON v1.5 o SPDX v2.3.

### Usuario objetivo
Ingenieros de seguridad, arquitectos de software y release managers.

### Objetivo
Desarrollar un generador de SBOM profesional conforme a los estándares CycloneDX/SPDX con extracción de metadatos de paquetes, licencias y hashes.

### Ejemplo conceptual de uso
```bash
# Generar SBOM en formato CycloneDX JSON del entorno actual de Python
python sbom_gen.py generate --spec cyclonedx -o sbom.cdx.json

# Analizar un archivo requirements.txt y exportar en formato SPDX
python sbom_gen.py generate --from-file requirements.txt --spec spdx -o sbom.spdx.json

# Auditar licencias incompatibles o restrictivas (ej. GPL en proyecto comercial)
python sbom_gen.py audit-licenses sbom.cdx.json --disallow "GPL-3.0,AGPL-3.0"
```

### Requisitos funcionales
- Subcomando `generate`: inspecciona paquetes instalados usando `importlib.metadata` (o parsea archivos lock) y extrae: Nombre del componente, Versión exacta, Autor/Proveedor, Licencia declarada (SPDX License Identifier), Descripción, Hash del paquete (SHA256) y PURL (Package URL estándar, ej. `pkg:pypi/requests@2.31.0`).
- Formatos de salida estándar soportados: `cyclonedx` (CycloneDX JSON 1.5) y `spdx` (SPDX JSON 2.3).
- Subcomando `audit-licenses <SBOM_FILE>`: evalúa todas las licencias del SBOM contra una lista de licencias prohibidas (`--disallow`) o permitidas (`--allow`), alertando sobre riesgos legales.
- Subcomando `validate <SBOM_FILE>`: valida que el archivo SBOM generado cumpla con el esquema JSON oficial de CycloneDX o SPDX.

### Requisitos de CLI
- Subcomandos: `generate`, `audit-licenses`, `validate`.
- Opción `--spec [cyclonedx|spdx]` (default `cyclonedx`).
- Opción `--from-file <RUTA>` (default entorno activo).
- Opción `-o / --output <RUTA>` (default STDOUT).
- Opción `--disallow <LICENCIAS>` en `audit-licenses`.
- Exit code 0 en éxito, 1 si se detectan licencias prohibidas en `audit-licenses`, 2 en errores.

### Entradas
- Entorno de Python, archivos de dependencias y parámetros de especificación.

### Salidas
- Documento SBOM JSON estándar en STDOUT o archivo de destino.

### Persistencia
Escritura del archivo SBOM en disco.

### Validaciones
- Comprobar que los metadatos de los paquetes cumplan con la especificación de Package URL (PURL).
- Validar formato de identificadores de licencia SPDX.

### Casos límite
- Paquetes sin licencia declarada o con licencias propietarias no estándar.
- Dependencias instaladas directamente desde repositorios de Git o URLs de archivo wheel.
- Proyectos con cientos de dependencias anidadas.

### Manejo de errores
- `importlib.metadata.PackageNotFoundError`.
- Errores de validación de esquema JSON.

### Fundamentos de Python relacionados
- Módulo estándar `importlib.metadata` (`distributions()`, `metadata()`, `version()`, `files()`).
- Módulo `json` y formateo de estructuras de datos complejas.
- Especificación de identificadores Package URL (PURL) y licencias SPDX.

### Conceptos CLI relacionados
- Seguridad en la cadena de suministro de software (Supply Chain Security).
- Generación de artefactos estándar de cumplimiento normativo.

### Herramientas o módulos para investigar
- `importlib.metadata`.
- `json`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `diff sbom_v1.json sbom_v2.json` para mostrar qué componentes fueron añadidos, eliminados o actualizados entre dos versiones?

### Diseño de argumentos
¿Cómo nombrarías la opción para incluir información del proyecto raíz como componente principal del SBOM (`--root-name "MiApp" --root-version "1.0.0"`)?

### Diseño de variables
`installed_distributions_list`, `component_metadata_dto`, `cyclonedx_sbom_tree`, `spdx_document_tree`, `disallowed_licenses_set`.

### Antes de programar
1. ¿Cómo estructurar el formato JSON oficial de CycloneDX 1.5 con secciones `bomFormat`, `specVersion`, `metadata` y `components`?
2. ¿Cómo construir un PURL válido según la especificación Package URL (ej. `pkg:pypi/psycopg@3.1.18`)?

### Arquitectura
Extractor de paquetes (`pkg_extractor.py`), formateador CycloneDX (`cyclonedx_builder.py`), formateador SPDX (`spdx_builder.py`), auditor de licencias (`license_auditor.py`) y CLI.

### Pruebas mínimas
1. Generar SBOM CycloneDX del entorno actual y verificar que contenga los paquetes instalados con sus versiones y PURLs correctos.
2. Ejecutar `audit-licenses` con una licencia prohibida presente en el SBOM y verificar que retorne exit code 1.

### Pruebas de error
1. Pasar un archivo SBOM JSON con sintaxis rota a `validate` -> Exit code 2.

### Experiencia de usuario
Documento JSON válido y perfectamente estructurado, con resumen en STDERR indicando total de componentes y licencias catalogadas.

### Explicación posterior
Explica la importancia de los SBOMs para la respuesta rápida ante vulnerabilidades de día cero en dependencias de terceros (como el caso Log4j o XZ Utils).

### Aplicación profesional
Cumplimiento normativo en licitaciones de software empresarial, integración en pipelines de release y auditoría de ciberseguridad.

### Reto adicional
Integrar enriquecimiento automático del SBOM consultando el endpoint de vulnerabilidades de OSV (Open Source Vulnerabilities) para asociar CVEs conocidos a los componentes catalogados.

---
> [← Ejercicio 069](../ejercicio_069/README.md) · [Índice General](../README.md) · [Ejercicio 071 →](../ejercicio_071/README.md)
