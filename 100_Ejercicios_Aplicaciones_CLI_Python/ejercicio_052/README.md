## Ejercicio 052 — Sincronizador Jerárquico de Configuraciones Multi-Entorno (`config-sync`)

> [← Ejercicio 051](../ejercicio_051/README.md) · [Índice General](../README.md) · [Ejercicio 053 →](../ejercicio_053/README.md)

### Contexto profesional
En arquitecturas de microservicios con múltiples entornos de despliegue (Desarrollo, Staging, Producción, Testing), las variables de configuración se estructuran de forma jerárquica: una configuración base compartida, sobreescrita por configuraciones específicas de entorno y finalmente sobreescrita por variables de entorno del sistema o secretos de infraestructura.

### Problema
Construir una CLI que gestione configuraciones jerárquicas en archivos JSON/YAML, resuelva la herencia y sobreescritura de valores (base -> env -> secrets), valide los tipos contra un esquema definido y exporte la configuración final a archivos `.env`, JSON o manifiestos de Kubernetes ConfigMap.

### Usuario objetivo
Ingenieros de DevOps, arquitectos de software y desarrolladores backend.

### Objetivo
Crear un motor de resolución y compilación de configuraciones multi-entorno con validación de esquemas y exportación políglota.

### Ejemplo conceptual de uso
```bash
# Compilar la configuración para el entorno de producción
python config_sync.py compile --env production --output .env.production

# Validar que todas las variables requeridas en el esquema estén definidas en staging
python config_sync.py validate --env staging --schema schema.json

# Exportar configuración como ConfigMap de Kubernetes
python config_sync.py export-k8s --env production --name "backend-config" -o configmap.yaml
```

### Requisitos funcionales
- Estructura de carpetas: `config/base.json`, `config/development.json`, `config/staging.json`, `config/production.json`.
- Algoritmo de mezcla profunda (deep merge): los valores del entorno específico sobreescriben a los de `base.json` recursivamente en objetos anidados.
- Resolución de variables interpoladas (ej. `"db_url": "postgresql://${DB_USER}:${DB_PASS}@${DB_HOST}/mydb"`).
- Subcomando `compile`: genera la configuración consolidada plana o anidada.
- Subcomando `validate`: comprueba tipos de datos y presencia de campos obligatorios contra un esquema JSON.
- Subcomando `diff <ENV1> <ENV2>`: compara las configuraciones finales de dos entornos y resalta las diferencias.
- Subcomando `export-k8s`: genera el manifiesto YAML de `ConfigMap` de Kubernetes.

### Requisitos de CLI
- Subcomandos: `compile`, `validate`, `diff`, `export-k8s`.
- Opción `--env <ENTORNO>` (default `development`).
- Opción `--config-dir <RUTA>` (default `./config`).
- Opción `-o / --output <RUTA>`.
- Exit code 0 en éxito, 1 si la validación de esquema falla o hay variables de interpolación no resueltas, 2 en errores.

### Entradas
- Archivos de configuración JSON y variables de entorno del sistema.

### Salidas
- Configuración compilada en STDOUT o escrita en archivo de destino.

### Persistencia
Escritura de archivos de configuración generados.

### Validaciones
- Validar que los archivos JSON base y de entorno tengan sintaxis correcta.
- Comprobar que no queden variables de interpolación sin resolver (`${VAR_NO_DEFINIDA}`) en modo estricto.

### Casos límite
- Objetos profundamente anidados con arrays de valores.
- Tipos de datos booleanos y enteros que no deben convertirse accidentalmente en cadenas de texto durante la mezcla.

### Manejo de errores
- `json.JSONDecodeError`.
- Error de validación de esquema con indicación de clave y tipo esperado.

### Fundamentos de Python relacionados
- Algoritmo recursivo de mezcla profunda de diccionarios (`deep_merge`).
- Expresiones regulares para interpolación de variables de entorno (`os.environ`).
- Módulo `json`.
- Formateo de manifiestos YAML.

### Conceptos CLI relacionados
- Gestión de configuración según los 12 Factores (The Twelve-Factor App: Config).
- Compilación determinista de artefactos de configuración.

### Herramientas o módulos para investigar
- `json`.
- `os` y `re`.
- `pathlib`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para enmascarar valores sensibles en el subcomando `diff`?

### Diseño de argumentos
¿Cómo nombrarías la opción para permitir valores por defecto en variables de interpolación (ej. `${PORT:-8080}`)?

### Diseño de variables
`base_config_dict`, `env_config_dict`, `merged_config_tree`, `unresolved_placeholders_list`, `k8s_manifest_yaml`.

### Antes de programar
1. ¿Por qué `dict.update()` de Python no realiza una mezcla profunda (deep merge) y sobrescribe diccionarios anidados completos?
2. ¿Cómo diseñar la función recursiva `deep_merge(dict_a, dict_b)` para que combine diccionarios internos respetando arrays?

### Arquitectura
Motor de mezcla (`merger.py`), interpolador (`interpolator.py`), validador de esquemas (`validator.py`) y CLI.

### Pruebas mínimas
1. Mezclar `base.json` (`{"app": {"name": "API", "port": 8080}}`) con `production.json` (`{"app": {"port": 443}}`) y verificar que el resultado conserve `name: API` y actualice `port: 443`.
2. Probar `diff development production` y verificar que detecte el cambio de puerto.

### Pruebas de error
1. Ejecutar `validate` con una variable obligatoria faltante -> Exit code 1.

### Experiencia de usuario
Salida limpia en STDOUT para redirección directa a archivos, y diffs coloreados en terminal.

### Explicación posterior
Explica el principio de *Config in the Environment* del manifiesto Twelve-Factor App y la separación estricta entre código y configuración.

### Aplicación profesional
Preparación de entornos en pipelines de CD antes de desplegar pods en Kubernetes o contenedores Docker.

### Reto adicional
Integrar desencriptación automática de valores cifrados con SOPS o age en archivos de configuración de producción.

---
> [← Ejercicio 051](../ejercicio_051/README.md) · [Índice General](../README.md) · [Ejercicio 053 →](../ejercicio_053/README.md)
