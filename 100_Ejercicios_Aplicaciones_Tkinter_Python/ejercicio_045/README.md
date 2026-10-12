## Ejercicio 045 — Administrador de Evaluaciones y Preguntas (`QuizAuthoringApp`)

> [Índice General](../README.md) · [← Ejercicio 044](../ejercicio_044/README.md) · [Ejercicio 046 →](../ejercicio_046/README.md)

### Contexto profesional
En plataformas de educación a distancia y departamentos de capacitación empresarial, los instructores diseñan bancos de reactivos y cuestionarios de opción múltiple.

### Usuario objetivo
Diseñador instruccional, profesor o capacitador corporativo.

### Problema
Crear evaluaciones directamente en plataformas web complejas resulta tedioso y no permite probar la experiencia del estudiante de forma rápida.

### Objetivo
Construir una herramienta de autoría de evaluaciones con dos pestañas (`ttk.Notebook`): 'Editor de Preguntas' (para redactar el enunciado, cuatro opciones y marcar la clave correcta) y 'Vista Previa Interactiva' (donde el evaluador puede responder el examen simulado y obtener su calificación inmediata).

### Flujo principal
En la pestaña 1, el docente redacta una pregunta, cuatro opciones (A, B, C, D) y marca cuál es la correcta mediante un radiobutton. Presiona 'Añadir Pregunta' y se agrega a una lista. En la pestaña 2 ('Vista Previa'), el docente puede responder el examen como si fuera un estudiante; al terminar, la aplicación evalúa las respuestas y muestra la puntuación final.

### Requisitos funcionales
- Pestaña 1 ('Editor'): Formulario para Enunciado de la pregunta, 4 opciones de respuesta y selector de la opción correcta (`A`, `B`, `C` o `D`).
- Tabla en el editor que muestre las preguntas creadas con opciones para editar o eliminar.
- Pestaña 2 ('Simulador'): Visualización secuencial o completa de las preguntas con grupos de radiobuttons para responder.
- Botón 'Calificar Evaluación' en la pestaña 2 que compare las respuestas con las claves correctas y muestre el porcentaje y aciertos.
- Persistencia del banco de preguntas en `preguntas.json`.

### Requisitos de interfaz
- `ttk.Notebook` con pestañas 'Editor de Reactivos' y 'Simulador de Examen'.
- Cuadrícula clara para las cuatro opciones de respuesta con indicación de la clave.
- Panel de calificación en la pestaña de simulador con retroalimentación cromática.

### Datos
- Pregunta: id, enunciado, opciones (dict con A, B, C, D), respuesta_correcta ('A'|'B'|'C'|'D').

### Estado
- Lista de preguntas en memoria.
- Respuestas marcadas en el simulador.

### Persistencia
Archivo JSON (`datos/preguntas.json`).

### Validaciones
- Enunciado y las 4 opciones son estrictamente obligatorios.
- Debe seleccionarse cuál de las 4 opciones es la correcta.

### Casos límite
- Intentar pasar al simulador con 0 preguntas creadas (mostrar mensaje de 'No hay preguntas en la evaluación').
- Calificar el examen sin haber respondido todas las preguntas (advertir al usuario).

### Manejo de errores
- Manejar la persistencia en JSON asegurando que el esquema sea consistente.

### Fundamentos de Python relacionados
- Modelado de cuestionarios con listas de diccionarios.
- Comparación de claves de respuesta y cálculo de puntuaciones ponderadas.

### Conceptos Tkinter relacionados
- Sincronización entre pestañas de un `ttk.Notebook` mediante el evento `<<NotebookTabChanged>>`.
- Generación dinámica de componentes de examen en la vista previa.

### Herramientas para investigar
- Evento virtual `<<NotebookTabChanged>>` en `ttk.Notebook`.
- Serialización JSON de cuestionarios.

### Diseño de interfaz
¿Cómo asegurarías que al cambiar a la pestaña del simulador, el examen se reconstruya automáticamente con las preguntas recién agregadas en el editor?

### Diseño de variables
Usa nombres como `quiz_notebook`, `question_text_entry`, `opt_a_entry`, `opt_b_entry`, `correct_opt_var`, `add_question_btn`, `grade_quiz_btn`.

### Antes de programar
1. ¿Cómo se reconstruye proceduralmente la interfaz del simulador al detectar el evento de cambio de pestaña?
2. ¿Cómo almacenas las respuestas seleccionadas por el estudiante para contrastarlas contra las claves correctas?

### Arquitectura
```
ejercicio_045/
├── app.py           # Notebook principal y control de pestañas
├── editor_tab.py    # Formulario y tabla de autoría de preguntas
├── simulator_tab.py # Motor interactivo de simulación y calificación
└── datos/
    └── preguntas.json # Archivo de persistencia de reactivos
```

### Pruebas mínimas
1. Agregar 2 preguntas en el editor -> Cambiar al simulador -> Responder 1 correcta y 1 incorrecta -> Comprobar calificación del 50%.
2. Reiniciar la app -> Verificar que las preguntas sigan cargadas desde el archivo JSON.

### Pruebas de error
1. Intentar agregar una pregunta dejando una opción vacía -> Debe exigir completar las 4 opciones.

### Experiencia de usuario
En el simulador, al calificar, debe mostrarse claramente cuáles preguntas se respondieron bien (en verde) y cuáles mal (en rojo).

### Explicación posterior
¿Cómo se coordina el ciclo de vida entre la pestaña de edición y la de vista previa para reflejar cambios en tiempo real?

### Aplicación profesional
Sistemas de evaluación técnica para selección de personal, plataformas e-learning y creadores de cuestionarios.

### Reto adicional
Añade un temporizador regresivo de 5 minutos en el simulador que envíe y califique automáticamente el examen al llegar a cero.

---
> [Índice General](../README.md) · [← Ejercicio 044](../ejercicio_044/README.md) · [Ejercicio 046 →](../ejercicio_046/README.md)
