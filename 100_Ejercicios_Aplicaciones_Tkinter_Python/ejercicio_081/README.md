## Ejercicio 081 — Diseñador y Previsualizador de Credenciales con Código de Barras Falso (`IdCardVisualizerApp`)

> [Índice General](../README.md) · [← Ejercicio 080](../ejercicio_080/README.md) · [Ejercicio 082 →](../ejercicio_082/README.md)

### Contexto profesional
En oficinas de seguridad corporativa y control de accesos, los guardias generan tarjetas de identidad plásticas para contratistas y empleados con fotografía simulada, textos tipográficos y código de barras vectorial.

### Usuario objetivo
Encargado de credencialización o técnico de seguridad patrimonial.

### Problema
Las plantillas impresas con fuentes desalineadas generan carnets ilegibles que son rechazados por lectores ópticos de torniquetes.

### Objetivo
Desarrollar una aplicación de composición y previsualización de credenciales plásticas en `Canvas` que dibuje una tarjeta con proporción ISO/IEC 7810 (tarjeta de crédito), integrando recuadro para fotografía con silueta vectorial, campos de texto tipográficos escalados, banda de color corporativa y un generador procedimental de código de barras falso (Code 128 o Code 39 simplificado) dibujado con líneas vectoriales en el lienzo.

### Flujo principal
El usuario llena el formulario con el nombre del empleado, ID de empleado, departamento y tipo de acceso. Conforme escribe, la credencial en el `Canvas` actualiza sus textos en tiempo real. Un algoritmo procedimental traduce el ID numérico a un código de barras de líneas verticales de grosor variable en la parte inferior de la credencial. Puede exportar el diseño o limpiar.

### Requisitos funcionales
- Renderizado vectorial de credencial plástica en `Canvas` con esquinas redondeadas y proporción estándar.
- Silueta vectorial o marco para fotografía de empleado.
- Tipografías corporativas jerárquicas: Nombre (grande negrita), Cargo, ID y Empresa.
- Generador vectorial procedimental de código de barras falso: dibuja líneas verticales negras de grosor variable (1, 2 o 3 px) separadas por espacios proporcionales según los dígitos del ID.
- Selector de color de banda corporativa (para distinguir departamentos por color).
- Actualización reactiva inmediata conforme se redactan los datos del colaborador.

### Requisitos de interfaz
- Panel izquierdo: Formulario de datos personales y selectores de color.
- Panel derecho: `Canvas` amplio que muestre la credencial centrada con apariencia realista.
- Botón de 'Exportar Ficha' y botón de 'Limpiar'.

### Datos
- Ficha de credencial: id_empleado, nombre, departamento, cargo, color_banda.

### Estado
- Variables de control de Tkinter enlazadas a los elementos del Canvas.

### Persistencia
No requiere persistencia en disco en esta fase.

### Validaciones
- ID de empleado debe contener al menos 6 caracteres alfanuméricos para generar el código de barras.
- Nombre obligatorio.

### Casos límite
- Nombres muy largos (ajustar tamaño de fuente o truncar con elipsis).
- IDs con caracteres especiales.

### Manejo de errores
- Proteger el generador de código de barras contra cadenas vacías dibujando un patrón estándar neutro.

### Fundamentos de Python relacionados
- Algoritmos procedimentales para generación de patrones de código de barras.
- Manejo de diccionarios de patrones binarios para codificación de caracteres.

### Conceptos Tkinter relacionados
- Dibujo vectorial compuesto en `Canvas` combinando rectángulos, textos y líneas.
- Creación de rectángulos con esquinas visualmente redondeadas mediante polígonos o arcos.

### Herramientas para investigar
- Especificación física de tarjetas plásticas ISO/IEC 7810 ID-1.
- Principio de funcionamiento de códigos de barras Code 39 / Code 128.

### Diseño de interfaz
¿Cómo asegurarías que la credencial se vea estéticamente similar a un carnet corporativo real de PVC?

### Diseño de variables
Usa nombres como `badge_canvas`, `emp_id_entry`, `emp_name_entry`, `dept_combo`, `color_palette_combo`, `barcode_group_tag`.

### Antes de programar
1. ¿Cómo se traduce una cadena de texto `'EMP102'` a una serie de líneas verticales de grosores variables en un `Canvas`?
2. ¿Cómo se actualizan los textos de un `Canvas` usando `canvas.itemconfig(tag_o_id, text=nuevo_texto)`?

### Arquitectura
```
ejercicio_081/
├── app.py             # Formulario y ventana contenedora
├── badge_renderer.py  # Renderizado de la tarjeta en Canvas
└── barcode_logic.py   # Algoritmo procedimental de barras para el ID
```

### Pruebas mínimas
1. Ingresar 'EMP-4455' y nombre 'Laura Torres' -> La tarjeta en el Canvas debe mostrar el nombre en negrita y las barras verticales correspondientes.
2. Cambiar color de departamento a Rojo -> La franja superior de la tarjeta debe actualizarse a rojo de inmediato.

### Pruebas de error
1. Dejar el campo de ID vacío -> Debe mostrar un código de barras neutro sin provocar excepciones matemáticas.

### Experiencia de usuario
La actualización en el Canvas debe ser instantánea al teclear sin retardos ni saltos en la ventana.

### Explicación posterior
¿Cómo se combinan primitivas vectoriales de `Canvas` para construir composiciones gráficas complejas tipo credencial o documento comercial?

### Aplicación profesional
Módulos de emisión de credenciales en software de control de accesos, tarjetas de membresía de gimnasios y gafetes de congresos.

### Reto adicional
Añade la opción de cargar una imagen `.png` real con `filedialog` y colocarla dentro del recuadro de fotografía de la credencial.

---
> [Índice General](../README.md) · [← Ejercicio 080](../ejercicio_080/README.md) · [Ejercicio 082 →](../ejercicio_082/README.md)
