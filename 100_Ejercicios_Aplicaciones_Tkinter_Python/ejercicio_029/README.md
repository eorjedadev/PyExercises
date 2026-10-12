## Ejercicio 029 — Administrador de Estudiantes y Calificaciones (`GradeTrackerApp`)

> [Índice General](../README.md) · [← Ejercicio 028](../ejercicio_028/README.md) · [Ejercicio 030 →](../ejercicio_030/README.md)

### Contexto profesional
En instituciones educativas y academias técnicas, los docentes coordinan el registro de calificaciones de sus asignaturas, calculando promedios y estados de aprobación.

### Usuario objetivo
Docente, profesor titular o asistente académico.

### Problema
El cálculo manual de promedios ponderados genera errores de transcripción en actas de notas oficiales y reclamos de alumnos.

### Objetivo
Desarrollar una aplicación de gestión escolar con `ttk.Treeview` que liste alumnos con tres parciales y promedio final ponderado, permita registrar nuevos alumnos, ordenar columnas numéricamente al hacer clic en el encabezado y exportar el acta final a CSV.

### Flujo principal
El docente ingresa la matrícula, nombre y tres calificaciones parciales (0 a 100). La aplicación calcula el promedio ponderado (30%, 30%, 40%) y dictamina 'Aprobado' (>= 70) o 'Reprobado'. Los estudiantes se listan en el `Treeview`. Al hacer clic en la cabecera 'Promedio', los alumnos se ordenan de mayor a menor nota.

### Requisitos funcionales
- Captura de: Matrícula, Nombre, Parcial 1, Parcial 2 y Parcial 3.
- Cálculo automático de promedio ponderado: $P = (N_1 \times 0.3) + (N_2 \times 0.3) + (N_3 \times 0.4)$.
- Determinación de estatus: Aprobado (promedio >= 70) o Reprobado (promedio < 70).
- Visualización en `ttk.Treeview` con columnas para cada parcial, promedio y estatus.
- Ordenamiento dinámico ascendente/descendente al hacer clic en cualquier encabezado de columna.
- Botón para exportar el acta completa a un archivo CSV.

### Requisitos de interfaz
- Formulario compacto superior en cuadrícula.
- `ttk.Treeview` amplio con encabezados interactivos.
- Etiquetas de resumen: Total Alumnos, Tasa de Aprobación (%) y Promedio General del Grupo.

### Datos
- Ficha de estudiante: matrícula (`str`), nombre (`str`), p1 (`float`), p2 (`float`), p3 (`float`), promedio (`float`), estatus (`str`).

### Estado
- Lista de estudiantes en memoria.
- Dirección actual de ordenamiento por columna (ascendente / descendente).

### Persistencia
Exportación a CSV (`acta_calificaciones.csv`) mediante diálogo de guardado.

### Validaciones
- Matrícula obligatoria y no duplicada.
- Calificaciones deben ser flotantes válidos entre 0.0 y 100.0.

### Casos límite
- Intentar ingresar una nota de 105 o -2.
- Grupo vacío al momento de calcular estadísticas generales (evitar división por cero).

### Manejo de errores
- Notificar con claridad qué nota específica está fuera del rango permitido de 0 a 100.

### Fundamentos de Python relacionados
- Funciones de ordenamiento con `sort()` o `sorted()` utilizando parámetros `key=lambda x: ...` y `reverse=...`.
- Aritmética de promedios ponderados y porcentajes.

### Conceptos Tkinter relacionados
- Manejo del callback en encabezados de `ttk.Treeview` (`heading(col, command=...)`).
- Diálogo `filedialog.asksaveasfilename` para exportar datos.

### Herramientas para investigar
- Función `sorted()` de Python con función de clave personalizada.
- Callback de columnas en `ttk.Treeview`.

### Diseño de interfaz
¿Cómo indicarías visualmente al usuario si una columna del Treeview está ordenada de forma ascendente o descendente (ej. con flechas ▲/▼ en el encabezado)?

### Diseño de variables
Usa nombres como `student_tree`, `id_entry`, `name_entry`, `grade1_entry`, `grade2_entry`, `grade3_entry`, `export_csv_btn`, `group_average_label`.

### Antes de programar
1. ¿Cómo se implementa una función de ordenamiento de columnas en `Treeview` que funcione correctamente tanto para texto como para números flotantes?
2. ¿Por qué no se debe ordenar numéricamente usando la comparación de cadenas de texto (donde `'10'` es menor que `'2'`)?

### Arquitectura
```
ejercicio_029/
├── app.py           # Vistas, Treeview y eventos de ordenamiento
└── grading_core.py  # Fórmulas de promedios, reglas de aprobación y exportador
```

### Pruebas mínimas
1. Registrar alumno con notas 70, 80, 90 -> Validar promedio 81.0 y estatus 'Aprobado'.
2. Hacer clic en encabezado 'Promedio' -> Verificar que los alumnos se ordenen correctamente por calificación.

### Pruebas de error
1. Ingresar nota 150 en parcial 1 -> Debe advertir que la calificación debe estar entre 0 y 100.

### Experiencia de usuario
Las filas de alumnos aprobados pueden tener un distintivo o texto limpio, mientras que los reprobados pueden resaltarse con tag en color rojo sutil.

### Explicación posterior
¿Cómo se resuelve el problema del ordenamiento lexicográfico frente al ordenamiento numérico al hacer clic en columnas de un `Treeview`?

### Aplicación profesional
Sistemas de gestión escolar (SIS), plataformas de capacitación corporativa y libros de calificaciones universitarios.

### Reto adicional
Añade un gráfico textual o barra de progreso que represente visualmente la proporción de alumnos aprobados frente a reprobados.

---
> [Índice General](../README.md) · [← Ejercicio 028](../ejercicio_028/README.md) · [Ejercicio 030 →](../ejercicio_030/README.md)
