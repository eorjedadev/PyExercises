## Ejercicio 044 — Agenda de Citas Médicas con Selector Modal de Horarios (`ClinicAppointmentApp`)

> [Índice General](../README.md) · [← Ejercicio 043](../ejercicio_043/README.md) · [Ejercicio 045 →](../ejercicio_045/README.md)

### Contexto profesional
En consultorios y clínicas odontológicas, las recepcionistas coordinan la agenda diaria de pacientes asignando turnos en intervalos de tiempo predefinidos.

### Usuario objetivo
Recepcionista de clínica médica o asistente dental.

### Problema
La asignación manual en agendas de papel provoca dobles reservas (overbooking) en el mismo horario con el mismo especialista.

### Objetivo
Desarrollar una aplicación de agenda con `ttk.Treeview` diario y una ventana modal `Toplevel` para agendar citas, con selector de especialista, fecha y una cuadrícula interactiva de horarios disponibles (bloqueando automáticamente los slots ya ocupados).

### Flujo principal
La recepcionista ve la lista de citas del día. Hace clic en 'Nueva Cita'. Se abre la ventana modal con la fecha y especialista seleccionados. Una cuadrícula de botones muestra los horarios (ej. de 09:00 a 17:00 en bloques de 30 min). Los horarios ya ocupados aparecen en rojo y deshabilitados. La recepcionista hace clic en un horario libre (verde), escribe los datos del paciente y confirma la cita.

### Requisitos funcionales
- Visualización en `ttk.Treeview`: Hora, Paciente, Especialista, Motivo, Estado ('Confirmada', 'Cancelada').
- Ventana modal `Toplevel` para asignación de turnos.
- Generación de bloques de 30 minutos (09:00 a 17:00).
- Bloqueo dinámico de slots: los horarios ocupados se muestran deshabilitados (`state='disabled'`) con color rojo.
- Selección de horario libre mediante un solo clic.
- Guardado en la lista principal y prevención estricta de doble reserva.

### Requisitos de interfaz
- Ventana modal organizada: datos del paciente arriba, matriz de botones de horarios al centro y botón de confirmación abajo.
- Código cromático evidente: Verde = Libre, Rojo = Ocupado, Azul = Seleccionado actualmente.
- Treeview de la principal ordenado cronológicamente por hora.

### Datos
- Cita: fecha, hora, paciente, especialista, motivo, telefono, estado.

### Estado
- Citas registradas en memoria.
- Horario seleccionado en la ventana modal.

### Persistencia
No requiere persistencia en disco en esta fase (almacena en memoria de sesión).

### Validaciones
- Nombre de paciente y teléfono obligatorios.
- No permitir confirmar la cita sin haber seleccionado un horario de la cuadrícula.

### Casos límite
- Intentar abrir la modal cuando todos los horarios del día están ocupados (debe advertir que no hay disponibilidad).
- Cancelar una cita existente (el slot debe liberarse y volver a verde en futuras aperturas de la modal).

### Manejo de errores
- Notificar con diálogo si el paciente intenta registrarse sin seleccionar turno.

### Fundamentos de Python relacionados
- Generación de secuencias de horarios con `datetime.timedelta`.
- Estructuras de datos para indexar disponibilidad rápidamente (`set` de tuplas `(fecha, especialista, hora)`).

### Conceptos Tkinter relacionados
- Creación dinámica de cuadrículas de botones mediante bucles `for` y `grid`.
- Manejo de variables y selección única entre múltiples botones.

### Herramientas para investigar
- Manejo de rangos de tiempo con `datetime` y `timedelta`.
- Generación procedural de widgets en Tkinter.

### Diseño de interfaz
¿Cómo organizarías una matriz de 16 botones de horarios (4 filas x 4 columnas) para que sea visualmente atractiva y fácil de pulsar?

### Diseño de variables
Usa nombres como `appointments_tree`, `new_appointment_btn`, `slot_btn_grid`, `selected_time_slot_var`, `patient_name_entry`, `confirm_booking_btn`.

### Antes de programar
1. ¿Cómo se genera proceduralmente una lista de botones de horario en un bucle pasando la hora como argumento a una función lambda?
2. ¿Por qué es fundamental usar `command=lambda h=hora: seleccionar_hora(h)` para evitar el problema común de clausura en bucles de Python?

### Arquitectura
```
ejercicio_044/
├── app.py             # Agenda principal y Treeview de citas
├── slot_picker_modal.py # Modal con matriz de botones interactivos
└── appointment_repo.py  # Control de disponibilidad y reservas en memoria
```

### Pruebas mínimas
1. Abrir modal y reservar turno de las 10:00 -> Comprobar que aparezca en la agenda.
2. Abrir la modal de nuevo para el mismo día -> Comprobar que el botón de las 10:00 aparezca en rojo y deshabilitado.

### Pruebas de error
1. Escribir nombre del paciente pero no seleccionar ningún botón de hora y presionar Guardar -> Debe advertir que debe elegir un horario.

### Experiencia de usuario
Al hacer clic en un horario libre, el botón debe destacarse claramente para indicar la selección activa.

### Explicación posterior
¿Cómo se evita el error de captura tardía de variables al vincular callbacks en bucles que generan widgets dinámicos en Tkinter?

### Aplicación profesional
Sistemas de reserva en clínicas dentales, salones de belleza, talleres mecánicos y consultorías profesionales.

### Reto adicional
Añade un botón 'Cancelar Cita' en la ventana principal que cambie el estado de la cita a 'Cancelada' y libere inmediatamente el horario para nuevos pacientes.

---
> [Índice General](../README.md) · [← Ejercicio 043](../ejercicio_043/README.md) · [Ejercicio 045 →](../ejercicio_045/README.md)
