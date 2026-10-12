## Ejercicio 030 — Registro de Consumo de Medicamentos y Recetas (`MedicationLogApp`)

> [Índice General](../README.md) · [← Ejercicio 029](../ejercicio_029/README.md) · [Ejercicio 031 →](../ejercicio_031/README.md)

### Contexto profesional
En residencias de adultos mayores y centros de atención médica domiciliaria, los enfermeros deben controlar y registrar rigurosamente la administración de dosis de medicamentos según prescripción.

### Usuario objetivo
Enfermero de turno o cuidador de atención domiciliaria.

### Problema
El extravío de libretas de control provoca duplicación de tomas o dosis omitidas de medicamentos críticos como insulina o hipertensivos.

### Objetivo
Construir una aplicación de registro de tomas médicas con `ttk.Treeview`, persistencia en JSON, filtros por paciente y advertencia visual de dosis omitidas o próximas a vencer.

### Flujo principal
El enfermero selecciona el paciente de una lista, visualiza su esquema de medicamentos (fármaco, dosis, horario programado y estado). Al administrar una dosis, presiona 'Registrar Toma', lo cual estampa la fecha/hora exacta y cambia el estado a 'Administrado'. Los datos se guardan en `registro_medicamentos.json`.

### Requisitos funcionales
- Carga y guardado en archivo `registro_medicamentos.json`.
- Visualización en `ttk.Treeview` con columnas: Paciente, Medicamento, Dosis, Horario, Estado ('Pendiente', 'Administrado', 'Omitido'), Hora Real de Toma.
- Formulario para prescribir un nuevo medicamento para un paciente.
- Botón para registrar administración de dosis del ítem seleccionado.
- Filtro por paciente (`Combobox`).
- Resalte visual de medicamentos pendientes cuya hora programada ya pasó (en rojo).

### Requisitos de interfaz
- Treeview con scrollbar y tags de color según estatus de toma.
- Formulario organizado para captura rápida de prescripciones.
- Reloj o marca de tiempo visible que muestre la hora del sistema en tiempo real.

### Datos
- Registro de dosis: id, paciente, fármaco, dosis, hora_programada, estado, hora_administracion.

### Estado
- Lista de tomas en memoria.
- Paciente seleccionado en el filtro.

### Persistencia
Archivo JSON (`datos/registro_medicamentos.json`).

### Validaciones
- Fármaco y dosis obligatorios.
- Formato de hora en HH:MM (24 horas).
- No permitir registrar como administrada una dosis que ya fue registrada previamente.

### Casos límite
- Pasar de la medianoche (cambio de día en horarios programados).
- Registro de pacientes con múltiples tomas al mismo horario.

### Manejo de errores
- Manejar horas mal formateadas y advertir al usuario sin colapsar.

### Fundamentos de Python relacionados
- Comparación de horas con `datetime.time` o cadenas comparables.
- Manejo de JSON estructurado con múltiples entidades.

### Conceptos Tkinter relacionados
- Uso de `.after()` para actualizar un reloj digital en vivo en la barra de estado.
- Tags de filas para alertar medicamentos retrasados.

### Herramientas para investigar
- Módulo `datetime` para manejo de horas de reloj.
- Métodos de `Treeview` para actualizar celdas específicas con `.item(item_id, values=...)`.

### Diseño de interfaz
¿Cómo organizarías la vista para que el enfermero identifique de un solo vistazo cuáles medicamentos de qué pacientes están atrasados?

### Diseño de variables
Usa nombres como `med_tree`, `patient_filter_combo`, `drug_name_entry`, `dose_entry`, `time_entry`, `record_dose_btn`, `live_clock_label`.

### Antes de programar
1. ¿Cómo se actualiza un reloj digital en Tkinter cada segundo usando `after(1000, ...)` sin bloquear la interfaz?
2. ¿Cómo se modifica el valor de una fila específica en un `Treeview` sin tener que recargar toda la tabla?

### Arquitectura
```
ejercicio_030/
├── app.py             # Interfaz gráfica, reloj y Treeview
├── med_service.py     # Lógica de administración y comprobación de horarios
└── datos/
    └── registro_medicamentos.json # Datos persistidos en JSON
```

### Pruebas mínimas
1. Seleccionar una dosis 'Pendiente' y registrar toma -> Comprobar que pase a 'Administrado' con la hora actual.
2. Reiniciar la app -> Verificar que el estado administrado persista desde el archivo JSON.

### Pruebas de error
1. Intentar registrar toma sobre una dosis ya administrada -> Debe advertir 'Esta dosis ya fue administrada previamente'.

### Experiencia de usuario
El botón de registrar toma debe ser grande y claro para evitar pulsaciones erróneas en pantallas táctiles o tabletas.

### Explicación posterior
¿Cómo se combinan las variables de tiempo de Python con las etiquetas de estilo de `ttk.Treeview` para generar alarmas visuales?

### Aplicación profesional
Software hospitalario de enfermería, sistemas de control de residencias geriátricas y dispensadores médicos.

### Reto adicional
Añade un botón 'Registrar Dosis Omitida' que solicite mediante un diálogo el motivo médico de la omisión (ej. 'Paciente en ayunas').

---
> [Índice General](../README.md) · [← Ejercicio 029](../ejercicio_029/README.md) · [Ejercicio 031 →](../ejercicio_031/README.md)
