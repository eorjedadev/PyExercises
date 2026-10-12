## Ejercicio 005 — Contador de Palabras y Densidad Léxica en Tiempo Real (`TextMetricsApp`)

> [Índice General](../README.md) · [← Ejercicio 004](../ejercicio_004/README.md) · [Ejercicio 006 →](../ejercicio_006/README.md)

### Contexto profesional
En redacciones editoriales y departamentos de comunicación, los editores deben ajustar notas de prensa a límites estrictos de palabras, caracteres y tiempo de lectura.

### Usuario objetivo
Redactor editorial, copywriter o analista de contenidos.

### Problema
Pegar texto en procesadores de texto pesados solo para revisar el conteo de palabras retrasa la entrega de notas rápidas para redes sociales y gacetillas.

### Objetivo
Crear un editor de texto interactivo con un widget `Text` de Tkinter que analice en tiempo real el contenido ingresado, calculando total de palabras, caracteres con y sin espacios, líneas, párrafos y tiempo estimado de lectura en minutos.

### Flujo principal
El usuario escribe o pega texto en el área principal de redacción. Conforme ingresa texto, un panel inferior de métricas actualiza de inmediato todas las estadísticas sin requerir clics ni recargas.

### Requisitos funcionales
- Área de redacción con barras de desplazamiento vertical.
- Conteo en tiempo real de palabras totales.
- Conteo de caracteres con espacios y caracteres sin espacios.
- Conteo de líneas y párrafos reales (ignorando líneas en blanco consecutivas).
- Estimación de tiempo de lectura (basado en promedio de 200 palabras por minuto).
- Botón para limpiar contenido con confirmación si hay más de 50 palabras.

### Requisitos de interfaz
- Widget `Text` con margen interior (`padx`, `pady`) y scrollbar sincronizado.
- Barra de estado inferior con disposición horizontal y etiquetas descriptivas claras para cada métrica.
- Resalte visual sutil para el contador principal.

### Datos
- Texto crudo: cadena multilínea (`str`).
- Métricas calculadas: diccionario con enteros y flotantes formateados.

### Estado
- Texto actualmente en el buffer del widget `Text`.
- Estado del flag de modificación del widget.

### Persistencia
No requiere almacenamiento permanente en disco.

### Validaciones
- Manejo seguro de texto vacío (todas las métricas deben reflejar cero sin arrojar errores de división).

### Casos límite
- Pegado masivo de miles de líneas (el cálculo debe mantenerse fluido).
- Texto con múltiples espacios consecutivos, tabuladores y saltos de línea continuos.
- Caracteres especiales y emoticonos.

### Manejo de errores
- Evitar bloqueos al procesar cadenas vacías o textos compuestos únicamente de espacios en blanco.

### Fundamentos de Python relacionados
- Métodos de cadenas (`split()`, `strip()`, `count()`).
- Expresiones regulares básicas (`re.findall(r'\w+', texto)`) para tokenización de palabras.
- Formateo de números grandes con separadores de miles.

### Conceptos Tkinter relacionados
- Widget `Text` y recuperación de contenido con `.get('1.0', 'end-1c')`.
- Enlace de eventos `<KeyRelease>` o banderas de modificación `<<Modified>>`.
- Widget `ttk.Scrollbar` acoplado al comando `yscrollcommand` del `Text`.

### Herramientas para investigar
- Mecánica del flag `edit_modified()` en widgets `Text` de Tkinter.
- Índices y marcas de posición en widgets de texto ('1.0', 'end-1c').

### Diseño de interfaz
¿Cómo organizarías la barra de estado en columnas para que las 5 métricas queden perfectamente distribuidas a lo largo del ancho de la ventana?

### Diseño de variables
Usa nombres como `editor_text`, `scroll_bar`, `word_count_label`, `char_count_label`, `reading_time_label`.

### Antes de programar
1. ¿Por qué `.get('1.0', 'end')` agrega un salto de línea adicional y por qué se suele usar `'end-1c'`?
2. ¿Cómo evitar un bucle infinito si se escucha el evento virtual `<<Modified>>` y se modifica el contenido desde el callback?

### Arquitectura
```
ejercicio_005/
├── app.py           # Configuración del widget Text y eventos
└── text_metrics.py  # Funciones puras de análisis estadístico de texto
```

### Pruebas mínimas
1. Escribir 'Hola mundo desde Tkinter' -> Verificar 4 palabras, 25 caracteres totales y 22 sin espacios.
2. Borrar todo el contenido -> Todas las métricas deben volver inmediatamente a 0.

### Pruebas de error
1. Pegar 20 saltos de línea vacíos -> El conteo de palabras debe ser 0 y el de párrafos 0.

### Experiencia de usuario
El área de texto debe tener un tamaño de fuente cómodo (11 o 12 pt) y fuente de ancho proporcional legible para escritura prolongada.

### Explicación posterior
¿Qué diferencia existe en Tkinter entre el índice '1.0' y 'end-1c' al extraer texto de un widget `Text`?

### Aplicación profesional
Módulos de redacción en gestores de contenido (CMS), analizadores de transcripciones y editores de resúmenes ejecutivos.

### Reto adicional
Calcula y muestra la densidad léxica (porcentaje de palabras únicas respecto al total de palabras utilizadas).

---
> [Índice General](../README.md) · [← Ejercicio 004](../ejercicio_004/README.md) · [Ejercicio 006 →](../ejercicio_006/README.md)
