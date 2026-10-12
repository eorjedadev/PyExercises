## Ejercicio 008 — Formulario de Registro Rápido de Visitantes (`VisitorCheckInApp`)

> [Índice General](../README.md) · [← Ejercicio 007](../ejercicio_007/README.md) · [Ejercicio 009 →](../ejercicio_009/README.md)

### Contexto profesional
En recepciones de edificios corporativos e industrias, el personal de seguridad debe registrar a cada visitante que ingresa a las instalaciones con rapidez y validación de campos obligatorios.

### Usuario objetivo
Recepcionista o guardia de seguridad de control de accesos.

### Problema
El uso de libros de firmas en papel genera registros ilegibles, pérdida de trazabilidad de horas de ingreso y datos incompletos de a quién visitan.

### Objetivo
Desarrollar un formulario estructurado en cuadrícula para registrar nombre completo, documento de identidad, empresa de procedencia y persona a quien visita, validando los campos y mostrando una ficha de confirmación inmediata.

### Flujo principal
El guardia digita los datos del visitante, presiona 'Registrar Ingreso'. El sistema valida que los campos requeridos no estén en blanco. Si todo es correcto, muestra un resumen del registro en un panel inferior con la hora exacta y limpia el formulario para el siguiente visitante.

### Requisitos funcionales
- Campos para: Nombre Completo (obligatorio), Documento de Identidad (obligatorio), Empresa (opcional), Funcionario al que visita (obligatorio) y Motivo de visita (selector).
- Botón de 'Registrar Ingreso'.
- Botón de 'Limpiar Formulario'.
- Panel de resumen inferior que muestra la confirmación del último visitante registrado junto con la fecha y hora exacta.
- Contador visible de 'Total de visitantes registrados hoy'.

### Requisitos de interfaz
- Distribución estricta con `grid`, manteniendo todas las etiquetas alineadas a la derecha y los campos a la izquierda.
- Indicador visual (asterisco rojo `*`) en los campos obligatorios.
- Marco rotulado (`LabelFrame`) para el formulario y otro para la ficha del último ingreso.

### Datos
- Ficha de visitante: diccionario con nombre, identificación, empresa, anfitrión, motivo y timestamp de ingreso.

### Estado
- Contador numérico de visitantes en memoria.
- Registro temporal del último visitante procesado.

### Persistencia
No requiere persistencia en archivo (opera en memoria de turno).

### Validaciones
- Nombre completo debe tener al menos 3 caracteres y contener caracteres alfabéticos.
- Documento de identidad no debe estar vacío ni contener caracteres especiales no autorizados.
- Anfitrión a visitar es estrictamente obligatorio.

### Casos límite
- Presionar registrar con todos los campos vacíos.
- Ingresar nombres con espacios accidentales al inicio o al final (deben limpiarse con `.strip()`).
- Ingresar textos muy largos que puedan desbordar el panel de confirmación.

### Manejo de errores
- Mostrar los mensajes de error en una etiqueta de aviso de color rojo dentro del mismo formulario, evitando ventanas emergentes intrusivas.

### Fundamentos de Python relacionados
- Manipulación de cadenas y limpieza con `.strip()` y `.title()`.
- Manejo de diccionarios para agrupar registros de entidad.
- Módulo `datetime` para registro de hora de entrada.

### Conceptos Tkinter relacionados
- Gestor de geometría `grid` con pesos y alineación (`sticky='w'`, `sticky='e'`).
- Widget `ttk.LabelFrame` para agrupar visualmente secciones de formulario.
- Limpieza coordinada de múltiples widgets `Entry`.

### Herramientas para investigar
- Parámetros de `grid`: `row`, `column`, `padx`, `pady`, `sticky`.
- Método `.strip()` de cadenas en Python.

### Diseño de interfaz
¿Cómo asegurarías que el botón principal 'Registrar Ingreso' tenga un peso visual mayor que el botón secundario 'Limpiar'?

### Diseño de variables
Usa nombres como `visitor_name_entry`, `doc_id_entry`, `company_entry`, `host_entry`, `last_visitor_display`, `daily_count_var`.

### Antes de programar
1. ¿Por qué es mejor práctica validar con `.strip()` antes de comprobar si una cadena está vacía?
2. ¿Cómo estructurarías una función reutilizable que limpie todos los campos de un formulario?

### Arquitectura
```
ejercicio_008/
├── app.py           # Formulario gráfico y presentación
└── checkin_core.py  # Modelado de datos del visitante y validaciones de negocio
```

### Pruebas mínimas
1. Llenar los campos requeridos y presionar registrar -> El contador debe incrementarse en 1 y la ficha inferior debe mostrar el nombre y la hora.
2. Presionar 'Limpiar' -> Todos los campos de entrada deben quedar vacíos.

### Pruebas de error
1. Dejar el campo 'Nombre' vacío y presionar registrar -> Debe aparecer la alerta indicando que el nombre es obligatorio.

### Experiencia de usuario
Tras un registro exitoso, el foco del cursor debe volver automáticamente al primer campo de entrada (`visitor_name_entry.focus()`).

### Explicación posterior
¿Cómo contribuye el uso de `LabelFrame` y `grid` a una jerarquía visual clara y ordenada en un formulario corporativo?

### Aplicación profesional
Sistemas de control de acceso físico en plantas industriales, oficinas de gobierno y recepciones corporativas.

### Reto adicional
Agrega una casilla de verificación 'Requiere tarjeta de acceso temporal' que active o desactive un campo de entrada adicional para el número de gafete asignado.

---
> [Índice General](../README.md) · [← Ejercicio 007](../ejercicio_007/README.md) · [Ejercicio 009 →](../ejercicio_009/README.md)
