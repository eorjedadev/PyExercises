## Ejercicio 013 — Formulario de Alta de Empleados y Ficha de Personal (`EmployeeOnboardingApp`)

> [Índice General](../README.md) · [← Ejercicio 012](../ejercicio_012/README.md) · [Ejercicio 014 →](../ejercicio_014/README.md)

### Contexto profesional
En departamentos de recursos humanos, los asistentes de nómina deben registrar nuevos colaboradores validando rigurosamente correos electrónicos, identificaciones y departamentos.

### Usuario objetivo
Analista de recursos humanos o asistente de contratación.

### Problema
El ingreso manual sin validación provoca altas con correos mal escritos, fechas invertidas y campos obligatorios omitidos, afectando el alta de nómina.

### Objetivo
Construir un formulario completo con `ttk.Combobox`, `ttk.Radiobutton` y validaciones de formato de correo, fecha de ingreso ISO (YYYY-MM-DD) y código de empleado.

### Flujo principal
El usuario llena los datos del empleado, selecciona el departamento y tipo de jornada (Completa/Parcial). Al presionar 'Guardar Ficha', el sistema valida la coherencia de todos los campos. Si pasa la validación, muestra un diálogo de éxito y añade la ficha a una lista temporal en memoria.

### Requisitos funcionales
- Entradas: Código de Empleado (EMP-XXXX), Nombre Completo, Correo Institucional, Fecha de Ingreso (YYYY-MM-DD).
- Selector de Departamento (`ttk.Combobox`: TI, Ventas, Finanzas, RRHH, Operaciones).
- Selector de Jornada (`ttk.Radiobutton`: Tiempo Completo, Medio Tiempo, Remoto).
- Validación de formato de correo mediante expresión regular.
- Validación de fecha válida con formato año-mes-día.

### Requisitos de interfaz
- Uso de widgets temáticos `ttk` para una apariencia visual consistente.
- Separación clara entre datos personales y datos contractuales mediante marcos.
- Etiquetas de error contextuales al lado de cada campo inválido.

### Datos
- Ficha de empleado: diccionario con código, nombre, correo, fecha, departamento y modalidad de trabajo.

### Estado
- Lista en memoria de empleados registrados durante la sesión.
- Variables `StringVar` asociadas a cada widget.

### Persistencia
No requiere persistencia en disco en esta fase (almacena en memoria de sesión).

### Validaciones
- Código de empleado debe coincidir con el patrón `EMP-\d{4}`.
- Correo debe contener `@` y un dominio válido.
- Fecha debe ser una fecha de calendario real y no futura.

### Casos límite
- Ingresar 30 de febrero en la fecha de ingreso.
- Ingresar nombres con números o caracteres extraños.
- Intentar registrar un código de empleado que ya fue dado de alta en la misma sesión.

### Manejo de errores
- Capturar errores de parsing de fecha con `datetime.strptime`.
- Mostrar mensajes específicos señalando exactamente qué campo falló.

### Fundamentos de Python relacionados
- Expresiones regulares con `re.match()` para validación de formatos.
- Parsing y validación estricta de fechas con `datetime.strptime(fecha, '%Y-%m-%d')`.
- Colecciones en memoria (listas de diccionarios).

### Conceptos Tkinter relacionados
- Widgets `ttk.Combobox`, `ttk.Radiobutton`, `ttk.Entry`.
- Configuración de valores en Combobox (`values=(...)`, `state='readonly'`).
- Diálogos informativos `messagebox.showinfo` y `messagebox.showerror`.

### Herramientas para investigar
- Módulo `re` para expresiones regulares en Python.
- Método `datetime.strptime` en la biblioteca `datetime`.

### Diseño de interfaz
¿Cómo asegurarías que los radiobuttons de jornada laboral queden agrupados en una sola fila para ahorrar espacio vertical?

### Diseño de variables
Usa nombres como `emp_code_entry`, `emp_name_entry`, `emp_email_entry`, `hire_date_entry`, `dept_combobox`, `shift_type_var`.

### Antes de programar
1. ¿Por qué es recomendable establecer `state='readonly'` en un `Combobox` cuando se desea restringir la selección a opciones válidas?
2. ¿Cómo se valida que una fecha exista realmente en el calendario sin escribir complejas reglas de años bisiestos a mano?

### Arquitectura
```
ejercicio_013/
├── app.py           # Formulario interactivo con ttk
└── validators.py    # Funciones de validación pura (correo, fecha, código)
```

### Pruebas mínimas
1. Llenar datos válidos (EMP-1001, Juan Perez, juan@empresa.com, 2026-03-01, TI) -> Debe mostrar confirmación de éxito y limpiar campos.
2. Verificar que el selector de departamento no permita escribir texto arbitrario.

### Pruebas de error
1. Ingresar fecha '2026-02-30' -> Debe señalar que la fecha no existe en el calendario.
2. Ingresar correo 'juan@empresa' sin TLD -> Debe señalar correo inválido.

### Experiencia de usuario
Al fallar la validación, el foco debe trasladarse automáticamente al primer campo que contenga el error.

### Explicación posterior
¿Cómo ayuda la separación de la lógica de validación con regex y datetime a mantener limpios los callbacks de la interfaz?

### Aplicación profesional
Módulos de registro en portales de autoservicio de personal, ERPs corporativos y sistemas de nómina.

### Reto adicional
Añade un contador en la parte superior que muestre en tiempo real cuántos empleados han sido registrados en la sesión actual.

---
> [Índice General](../README.md) · [← Ejercicio 012](../ejercicio_012/README.md) · [Ejercicio 014 →](../ejercicio_014/README.md)
