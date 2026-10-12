## Ejercicio 023 — Generador de Encuestas de Clima Laboral (`SurveyFeedbackApp`)

> [Índice General](../README.md) · [← Ejercicio 022](../ejercicio_022/README.md) · [Ejercicio 024 →](../ejercicio_024/README.md)

### Contexto profesional
En consultoras de desarrollo organizacional, los analistas aplican encuestas de satisfacción y clima laboral a colaboradores de empresas clientes.

### Usuario objetivo
Colaborador de la empresa que responde la encuesta de clima.

### Problema
Las encuestas digitales que no validan que todas las preguntas obligatorias hayan sido respondidas generan matrices de datos incompletas que arruinan los análisis estadísticos.

### Objetivo
Construir una interfaz de encuesta con 5 preguntas evaluadas en escala Likert (1: Totalmente en desacuerdo a 5: Totalmente de acuerdo) mediante grupos de `Radiobutton`, un campo de comentarios opcionales y validación estricta de que ninguna pregunta quede sin respuesta.

### Flujo principal
El colaborador lee cada pregunta y selecciona una opción del 1 al 5 en cada una de las 5 preguntas. Al presionar 'Enviar Encuesta', el sistema verifica que todas las preguntas tengan una opción seleccionada. Si falta alguna, señala visualmente la pregunta omitida; si todas están completas, calcula el puntaje promedio de satisfacción y agradece la participación.

### Requisitos funcionales
- 5 preguntas obligatorias sobre el entorno de trabajo.
- Cada pregunta dispone de una escala Likert horizontal del 1 al 5 (`ttk.Radiobutton`).
- Campo `Text` para sugerencias o comentarios finales (opcional).
- Validación de que las 5 preguntas hayan sido respondidas antes de enviar.
- Cálculo del puntaje total (sobre 25 puntos) y promedio de satisfacción (1 a 5).
- Mensaje de confirmación y reseteo del cuestionario.

### Requisitos de interfaz
- Disposición clara con las preguntas rotuladas y los botones de radio alineados horizontalmente.
- Espaciado vertical que facilite la lectura sin amontonamiento.
- Resalte en color de la pregunta que el usuario haya omitido contestar.

### Datos
- Respuestas: lista o diccionario de 5 enteros (1 a 5).
- Comentario opcional: cadena.
- Puntuación promedio: float.

### Estado
- 5 variables `IntVar` independientes, una para cada grupo de preguntas.
- Estado de validación general.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Cada una de las 5 variables `IntVar` debe tener un valor distinto de cero (o del valor por defecto no seleccionado).

### Casos límite
- El usuario responde las preguntas 1, 2, 4 y 5 y deja la 3 vacía.
- Comentarios extremadamente extensos.

### Manejo de errores
- Identificar exactamente el número de la primera pregunta omitida y advertir al usuario sin borrar las respuestas previas.

### Fundamentos de Python relacionados
- Listas de variables de control de Tkinter.
- Funciones de agregación (`sum()`, `len()`).
- Bucles `for` con `enumerate` para validar colecciones de controles.

### Conceptos Tkinter relacionados
- Agrupación de `ttk.Radiobutton` mediante la misma variable para opciones mutuamente excluyentes.
- Múltiples grupos independientes de botones de radio.

### Herramientas para investigar
- Escalas Likert en diseño de formularios.
- Métodos de inspección de listas de variables en Tkinter.

### Diseño de interfaz
¿Cómo alinearías los 5 radiobuttons horizontalmente debajo de cada pregunta para que la interfaz se sienta espaciosa y fácil de responder?

### Diseño de variables
Usa nombres como `q1_var`, `q2_var`, `q3_var`, `q4_var`, `q5_var`, `comments_text`, `submit_survey_btn`.

### Antes de programar
1. ¿Por qué cada pregunta debe tener su propia instancia independiente de `IntVar`?
2. ¿Qué valor inicial debes asignarle a las variables para saber si el usuario aún no ha seleccionado ninguna opción?

### Arquitectura
```
ejercicio_023/
├── app.py           # Presentación del cuestionario y grupos de radiobuttons
└── survey_eval.py   # Lógica de validación de completitud y promedios
```

### Pruebas mínimas
1. Responder todas las preguntas con valor 4 -> Comprobar que permita enviar y calcule promedio exacto de 4.0 / 5.0.
2. Limpiar cuestionario -> Todas las opciones deben quedar desmarcadas.

### Pruebas de error
1. Responder solo 4 preguntas y hacer clic en Enviar -> Debe mostrar advertencia indicando 'Debe responder la pregunta 3 para continuar'.

### Experiencia de usuario
Las preguntas deben tener un contraste nítido y las opciones deben responder al clic de manera inmediata.

### Explicación posterior
¿Cómo garantiza el uso de una variable `IntVar` por cada grupo de `Radiobutton` la independencia entre las distintas preguntas de la encuesta?

### Aplicación profesional
Sistemas de evaluación de desempeño 360, cuestionarios de satisfacción del cliente y auditorías internas.

### Reto adicional
Añade una barra de progreso visual (`ttk.Progressbar`) en la parte superior que se actualice de 0% a 100% conforme el usuario va contestando cada pregunta.

---
> [Índice General](../README.md) · [← Ejercicio 022](../ejercicio_022/README.md) · [Ejercicio 024 →](../ejercicio_024/README.md)
