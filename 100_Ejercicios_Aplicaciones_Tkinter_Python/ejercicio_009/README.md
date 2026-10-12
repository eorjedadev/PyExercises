## Ejercicio 009 — Tarjeta de Presentación Digital y Generador de Credenciales (`BadgePreviewApp`)

> [Índice General](../README.md) · [← Ejercicio 008](../ejercicio_008/README.md) · [Ejercicio 010 →](../ejercicio_010/README.md)

### Contexto profesional
En eventos empresariales y ferias comerciales, el personal de acreditación debe generar e imprimir credenciales temporales para ponentes y asistentes con previsualización en vivo.

### Usuario objetivo
Encargado de acreditaciones en eventos y convenciones.

### Problema
Imprimir credenciales con errores ortográficos o campos desalineados desperdicia material plástico y térmico.

### Objetivo
Desarrollar una interfaz de dos paneles (edición a la izquierda y vista previa de credencial a la derecha) que actualice instantáneamente el diseño de la tarjeta conforme se redactan los datos de la persona.

### Flujo principal
El usuario escribe en el panel izquierdo el nombre, cargo, empresa y rol del asistente (Asistente, Ponente, Prensa, VIP). En el panel derecho, una tarjeta estilizada tipo credencial actualiza su aspecto y color de cinta de inmediato.

### Requisitos funcionales
- Panel de edición con entradas para: Nombre, Empresa, Cargo y Rol.
- Selector de Rol que determine el color temático de la credencial (ej. VIP = Dorado, Ponente = Azul, Asistente = Verde).
- Panel derecho con proporciones fijas tipo gafete (aspecto tarjeta vertical u horizontal).
- Botón de restablecimiento y botón de simulación de impresión.

### Requisitos de interfaz
- Distribución de ventana con dos columnas principales expandibles de forma equilibrada.
- Panel de credencial con bordes visibles, sombra o relieve (`relief='groove'` o `'raised'`) y tipografías jerarquizadas.
- Actualización reactiva al escribir o cambiar el rol.

### Datos
- Ficha de credencial: nombre (`str`), empresa (`str`), cargo (`str`), rol (`str`), color de categoría (`str`).

### Estado
- Variables de control de Tkinter para cada campo de la credencial.
- Color activo de la credencial.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Truncar o alertar visualmente si el nombre excede los 30 caracteres para evitar desbordamiento gráfico en la tarjeta.

### Casos límite
- El usuario deja campos vacíos (la vista previa debe mostrar texto de marcador de posición como '[Nombre del Asistente]').
- Nombres extremadamente largos con múltiples apellidos.

### Manejo de errores
- Manejar la longitud máxima de texto para mantener la armonía estética de la tarjeta.

### Fundamentos de Python relacionados
- Diccionarios para mapear roles a códigos de color hexadecimales.
- Métodos de cadenas para recortar o dar formato tipo título (`str.title()`).

### Conceptos Tkinter relacionados
- Composición de layouts con múltiples `Frame`.
- Parámetros `relief` y `borderwidth` en widgets de Tkinter.
- Enlace de variables `StringVar` con argumento `trace_add('write', ...)` o eventos `<KeyRelease>`.

### Herramientas para investigar
- Método `.trace_add('write', callback)` en variables de Tkinter.
- Propiedades de estilo en `Frame` y `Label` (`relief`, `bd`, `bg`).

### Diseño de interfaz
¿Cómo asegurarías que el panel de la credencial mantenga una proporción visual realista similar a un gafete de 85x54 mm?

### Diseño de variables
Usa nombres como `badge_name_var`, `badge_company_var`, `badge_role_var`, `preview_card_frame`, `preview_name_label`.

### Antes de programar
1. ¿Qué ventajas ofrece usar `trace_add` sobre enlazar eventos individuales en cada widget `Entry`?
2. ¿Cómo simulas un valor por defecto ('[TU NOMBRE]') cuando el campo está vacío?

### Arquitectura
```
ejercicio_009/
├── app.py           # Vista dual y vinculación reactiva
└── badge_model.py   # Reglas de formato y paleta cromática de roles
```

### Pruebas mínimas
1. Escribir 'Carlos Ruiz' y seleccionar rol 'VIP' -> La credencial derecha debe mostrar el nombre y aplicar el color dorado de fondo.
2. Borrar el nombre -> Debe mostrar el texto de marcador por defecto sin desestructurar el panel.

### Pruebas de error
1. Ingresar un nombre de 60 caracteres -> Debe ajustar el tamaño o mostrar advertencia de longitud máxima.

### Experiencia de usuario
La vista previa debe sentirse sólida y visualmente agradable, emulando una credencial física real con buena tipografía.

### Explicación posterior
¿Cómo funciona el mecanismo de observador (`trace_add`) en las variables de control de Tkinter para sincronizar vistas?

### Aplicación profesional
Generadores de credenciales en ferias comerciales, tarjetas de identificación temporal en centros educativos y eventos.

### Reto adicional
Añade un selector para alternar la orientación de la credencial entre formato Vertical y formato Horizontal con reestructuración automática del layout.

---
> [Índice General](../README.md) · [← Ejercicio 008](../ejercicio_008/README.md) · [Ejercicio 010 →](../ejercicio_010/README.md)
