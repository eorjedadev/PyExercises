## Ejercicio 010 — Conversor de Formato y Limpiador de Texto (`TextSanitizerApp`)

> [Índice General](../README.md) · [← Ejercicio 009](../ejercicio_009/README.md) · [Ejercicio 011 →](../ejercicio_011/README.md)

### Contexto profesional
En migración de datos y cargas masivas de catálogos, los analistas reciben listados de productos y nombres con formatos inconsistentes que requieren normalización rápida.

### Usuario objetivo
Analista de bases de datos o gestor de contenido de comercio electrónico.

### Problema
Los textos pegados desde hojas de cálculo traen espacios dobles, mayúsculas arbitrarias, caracteres no ASCII y saltos de línea basura que rompen los importadores automáticos.

### Objetivo
Desarrollar una aplicación de limpieza y transformación de texto con área de entrada, botones de operaciones de transformación y área de salida, mostrando estadísticas de cambios realizados.

### Flujo principal
El usuario pega un bloque de texto en el cuadro superior, elige operaciones de transformación (Mayúsculas, Minúsculas, Formato Título, Eliminar Espacios Dobles, Generar Slug URL, Quitar Acentos), presiona 'Procesar' y obtiene el texto listo en el cuadro inferior junto con un botón de copiado.

### Requisitos funcionales
- Cuadro de texto de entrada y cuadro de texto de salida independientes.
- Botones de transformación directa: 'MAYÚSCULAS', 'minúsculas', 'Tipo Título', 'Eliminar Espacios Extras', 'Formato Slug-URL', 'Limpiar Tildes/Acentos'.
- Conteo de caracteres modificados o eliminados.
- Botón de intercambio para mover la salida a la entrada para transformaciones sucesivas.
- Botón de copiado al portapapeles de la salida procesada.

### Requisitos de interfaz
- Disposición vertical con dos áreas `Text` amplias y una barra de herramientas central con botones agrupados.
- Etiquetas de estado que indiquen la longitud de entrada y longitud de salida resultante.

### Datos
- Texto de entrada: cadena multilínea.
- Texto procesado: cadena multilínea.
- Métrica: diferencia de caracteres.

### Estado
- Texto en el búfer de entrada y salida.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Verificar que el área de entrada no esté vacía antes de ejecutar cualquier transformación.

### Casos límite
- Texto con saltos de línea continuos y tabuladores mezclados.
- Texto con caracteres no latinos o símbolos especiales.
- Entrada que ya está perfectamente normalizada.

### Manejo de errores
- Notificar con aviso amigable si el usuario presiona un botón de transformación con el área de entrada vacía.

### Fundamentos de Python relacionados
- Métodos de cadenas (`upper()`, `lower()`, `title()`, `replace()`).
- Módulo `unicodedata` para normalización y eliminación de tildes (`unicodedata.normalize`).
- Expresiones regulares para colapsar espacios múltiples (`re.sub(r'\s+', ' ', texto)`).

### Conceptos Tkinter relacionados
- Manejo de múltiples widgets `Text` con lectura y escritura controlada.
- Inserción y eliminación de texto con `.delete('1.0', tk.END)` y `.insert('1.0', ...)`. 

### Herramientas para investigar
- Módulo estándar `unicodedata` de Python.
- Expresiones regulares con el módulo `re` para sustitución de patrones.

### Diseño de interfaz
¿Cómo agruparías los botones de transformación en la barra intermedia para que sea fácil distinguir transformaciones de mayúsculas/minúsculas de transformaciones de limpieza estructural?

### Diseño de variables
Usa nombres como `input_text_widget`, `output_text_widget`, `uppercase_btn`, `strip_spaces_btn`, `slug_btn`, `copy_output_btn`.

### Antes de programar
1. ¿Cómo se construye un slug seguro para URLs (minúsculas, sin acentos, espacios reemplazados por guiones)?
2. ¿Por qué es importante limpiar el widget de salida antes de insertar el nuevo resultado?

### Arquitectura
```
ejercicio_010/
├── app.py              # Interfaz gráfica y enlace de botones
└── text_processors.py  # Funciones puras de transformación de cadenas
```

### Pruebas mínimas
1. Ingresar '  hola   MUNDO  ' y aplicar 'Eliminar Espacios Extras' -> Comprobar que resulte 'hola MUNDO'.
2. Ingresar 'Canción del Verano' y aplicar 'Generar Slug' -> Comprobar que resulte 'cancion-del-verano'.

### Pruebas de error
1. Presionar cualquier transformación con la entrada vacía -> Debe mostrar mensaje indicando que no hay texto para procesar.

### Experiencia de usuario
El cuadro de salida debe ser de solo lectura o distinguirse visualmente con un fondo ligeramente atenuado para dejar claro que es el resultado.

### Explicación posterior
¿Por qué es crucial separar las funciones de limpieza de cadenas en un módulo puro antes de conectarlas a los eventos de la interfaz?

### Aplicación profesional
Herramientas de preprocesamiento de datos para analistas de BI, redactores de blogs técnicos y administradores de catálogos e-commerce.

### Reto adicional
Añade una opción para convertir texto a formato JSON escapado de una sola línea (reemplazando comillas dobles y saltos de línea por `\n`).

---
> [Índice General](../README.md) · [← Ejercicio 009](../ejercicio_009/README.md) · [Ejercicio 011 →](../ejercicio_011/README.md)
