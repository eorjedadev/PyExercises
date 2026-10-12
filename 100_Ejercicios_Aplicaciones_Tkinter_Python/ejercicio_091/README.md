## Ejercicio 091 — Validador de Datos Empresariales con Pipeline de Reglas (`EnterpriseDataValidatorApp`)

> [Índice General](../README.md) · [← Ejercicio 090](../ejercicio_090/README.md) · [Ejercicio 092 →](../ejercicio_092/README.md)

### Contexto profesional
En departamentos de integración de datos y migración a sistemas ERP, los analistas validan lotes de registros antes de cargarlos a producción, contrastándolos contra múltiples reglas de negocio desacopladas.

### Usuario objetivo
Analista de integración de datos o ingeniero de aseguramiento de calidad de datos.

### Problema
Tener reglas de validación dispersas en condicionales `if` anidados dentro de formularios de la interfaz gráfica impide reutilizar las mismas reglas en procesos de lote o scripts de integración.

### Objetivo
Desarrollar una aplicación de validación de registros con un pipeline de validación desacoplado (`ValidationPipeline`), donde cada regla de negocio sea una clase independiente (`Rule`) que evalúe campos de clientes/proveedores, reporte discrepancias con severidades (`ERROR`, `WARNING`), y muestre retroalimentación visual granular por campo en la interfaz gráfica.

### Flujo principal
El analista ingresa los datos de un registro comercial o carga un lote. Al validar, el registro atraviesa un pipeline compuesto por reglas independientes: `TaxIdFormatRule`, `EmailDomainRule`, `CreditLimitRule`, `AddressPostalCodeRule`. La interfaz resalta en rojo los campos con errores bloqueantes y en amarillo las advertencias sugeridas, mostrando un reporte detallado de discrepancias en un panel lateral.

### Requisitos funcionales
- Arquitectura de validación basada en pipeline: Clase base `ValidationRule` con método `validate(entity) -> RuleResult`.
- Reglas independientes desacopladas: Formato fiscal, Dominio corporativo de correo, Límite de crédito coherente con ventas anuales, Teléfono de contacto.
- Pipeline coordinador `ValidationPipeline` que ejecute las reglas en orden y acumule los resultados sin abortar en el primer fallo.
- Clasificación de severidades: `ERROR` (impide procesar el registro) y `WARNING` (alerta que permite confirmación manual).
- Retroalimentación granular en la interfaz: cambio dinámico del borde o color de fondo del widget `Entry` correspondiente al campo con fallo.
- Panel lateral de resumen con la lista de violaciones de reglas detectadas.

### Requisitos de interfaz
- Formulario amplio con múltiples campos estructurados.
- Indicadores cromáticos inmediatos al lado de cada campo evaluado.
- Panel lateral con lista de mensajes de error y advertencias claras.
- Botón de 'Validar Registro' y botón de 'Guardar' (habilitado solo si 0 errores bloqueantes).

### Datos
- Entidad validada: registro comercial con 8 atributos.
- Resultado de regla: campo, severidad, mensaje, codigo_regla.

### Estado
- Estado de validación del formulario activo.
- Lista de fallos detectados.

### Persistencia
No requiere persistencia en disco en esta fase (enfoque en validación arquitectónica).

### Validaciones
- Reglas fiscales estrictas.
- Correos no personales (exigir dominios corporativos).
- Límites crediticios numéricos mayores a cero.

### Casos límite
- Registro con múltiples errores en el mismo campo (el pipeline debe reportar todas las discrepancias).
- Registro completamente perfecto (todos los campos deben marcarse con tilde verde de aprobación).

### Manejo de errores
- Garantizar que la ejecución de una regla no falle con excepciones no controladas si un campo es nulo o de tipo inesperado.

### Fundamentos de Python relacionados
- Patrón Pipeline y Patrón Strategy en Python.
- Clases abstractas (`abc.ABC`, `@abstractmethod`).
- Colección y agregación de objetos de resultado.

### Conceptos Tkinter relacionados
- Cambio dinámico de propiedades visuales de widgets individuales (`entry.config(highlightbackground='red', highlightthickness=1)`).
- Resalte contextual de errores por campo.

### Herramientas para investigar
- Módulo `abc` (Abstract Base Classes) de la biblioteca estándar de Python.
- Patrón Pipeline de validación de datos.

### Diseño de interfaz
¿Cómo asegurarías que el usuario comprenda claramente la diferencia visual entre un error bloqueante (rojo) y una advertencia no bloqueante (amarillo)?

### Diseño de variables
Usa nombres como `val_pipeline`, `tax_id_entry`, `email_entry`, `credit_limit_entry`, `errors_tree`, `validate_form_btn`, `save_record_btn`.

### Antes de programar
1. ¿Cómo se define una clase base abstracta `ValidationRule` usando el módulo `abc` de Python para obligar a que cada regla implemente su propio método `validate`?
2. ¿Cómo se asocia el resultado de una regla fallida con el widget de entrada específico de la interfaz para colorear su borde?

### Arquitectura
```
ejercicio_091/
├── app.py             # Formulario interactivo con retroalimentación visual granular
├── pipeline/
│   ├── __init__.py
│   ├── base_rule.py   # Clase abstracta Rule y clase RuleResult
│   ├── pipeline.py    # Coordinador ValidationPipeline
│   └── rules.py       # Reglas concretas: TaxRule, EmailRule, CreditRule
└── entity_model.py    # Modelo de datos a validar
```

### Pruebas mínimas
1. Llenar registro con datos válidos -> El pipeline debe retornar 0 errores y todos los campos deben mostrarse en verde.
2. Ingresar correo '@gmail.com' cuando la regla exige correo corporativo -> El campo de correo debe tornarse amarillo y mostrar la advertencia correspondiente.

### Pruebas de error
1. Dejar la identificación fiscal en blanco -> El campo debe tornarse rojo, deshabilitarse el botón de guardar y listarse el error bloqueante.

### Experiencia de usuario
Al corregir un campo inválido y volver a presionar validar, el borde rojo debe desaparecer de inmediato restaurando el aspecto normal del widget.

### Explicación posterior
¿Cómo permite el Patrón Pipeline añadir nuevas reglas de validación en el futuro sin modificar la interfaz gráfica ni alterar las reglas existentes?

### Aplicación profesional
Motores de ingesta de datos para almacenes de datos (ETL), sistemas de onboarding de proveedores en ERPs y validadores de cumplimiento normativo.

### Reto adicional
Añade la opción de validar un archivo CSV con 50 registros en lote utilizando el mismo pipeline y exportando un reporte de discrepancias.

---
> [Índice General](../README.md) · [← Ejercicio 090](../ejercicio_090/README.md) · [Ejercicio 092 →](../ejercicio_092/README.md)
