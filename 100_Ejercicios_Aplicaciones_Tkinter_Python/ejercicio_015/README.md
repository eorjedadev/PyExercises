## Ejercicio 015 — Gestor de Solicitudes de Vacaciones Laborales (`VacationRequestApp`)

> [Índice General](../README.md) · [← Ejercicio 014](../ejercicio_014/README.md) · [Ejercicio 016 →](../ejercicio_016/README.md)

### Contexto profesional
En portales internos de recursos humanos, los empleados solicitan periodos de descanso anual que deben descontarse de su saldo de días acumulados.

### Usuario objetivo
Empleado solicitante o supervisor de área.

### Problema
Las solicitudes enviadas con fechas invertidas, fines de semana mal calculados o que exceden el saldo disponible generan reprocesos y quejas en nómina.

### Objetivo
Construir una aplicación que reciba fecha de inicio y fecha de fin de vacaciones, calcule los días hábiles solicitados, valide que no excedan el saldo disponible del empleado y registre la solicitud tras confirmación formal.

### Flujo principal
El empleado visualiza su saldo actual (ej. 15 días disponibles). Ingresa la fecha de inicio y fecha de fin de sus vacaciones. El sistema calcula los días solicitados en tiempo real. Si los días son válidos y no superan el saldo, se habilita el botón 'Confirmar Solicitud', el cual pide confirmación con diálogo antes de descontar los días.

### Requisitos funcionales
- Mostrar saldo de días disponibles del colaborador.
- Entradas para Fecha de Inicio y Fecha de Fin (YYYY-MM-DD).
- Cálculo de días naturales o laborables entre ambas fechas.
- Validación de que la fecha de fin sea igual o posterior a la fecha de inicio.
- Validación de que los días solicitados no superen el saldo disponible.
- Diálogo de confirmación modal (`messagebox.askyesno`).
- Descuento del saldo en caso de confirmación exitosa.

### Requisitos de interfaz
- Tarjeta superior con el saldo de días en tipografía destacada.
- Formulario central con validaciones de fechas.
- Panel inferior con el cálculo del saldo restante proyectado.

### Datos
- Saldo disponible: entero.
- Fecha inicio y fin: objetos `date`.
- Días solicitados: entero.

### Estado
- Saldo actual en memoria.
- Días solicitados calculados.
- Estado del botón de confirmación (`normal` o `disabled`).

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Fechas en formato ISO válido.
- Fecha de fin >= Fecha de inicio.
- Fecha de inicio >= Fecha actual (no permitir vacaciones retroactivas).
- Días solicitados <= Saldo disponible.

### Casos límite
- Solicitar un solo día (fecha inicio igual a fecha fin, cálculo = 1 día).
- Intentar pedir 0 días o fechas invertidas.

### Manejo de errores
- Mostrar avisos claros mediante `messagebox.showwarning` si se intenta solicitar más días de los disponibles.

### Fundamentos de Python relacionados
- Aritmética de fechas con `datetime.date` y `timedelta` (`(fecha_fin - fecha_inicio).days + 1`).
- Comparaciones lógicas entre objetos de fecha.

### Conceptos Tkinter relacionados
- Diálogos estándar con `tkinter.messagebox`.
- Habilitación e inhabilitación dinámica de botones (`btn.config(state=...)`).

### Herramientas para investigar
- Clase `datetime.date` y restas entre fechas.
- Módulo `tkinter.messagebox`.

### Diseño de interfaz
¿Cómo asegurarías que el usuario comprenda claramente la diferencia entre su 'Saldo Actual' y su 'Saldo Restante Proyectado'?

### Diseño de variables
Usa nombres como `available_days_var`, `start_date_entry`, `end_date_entry`, `requested_days_label`, `submit_request_btn`.

### Antes de programar
1. ¿Cómo se calculan los días inclusivos entre dos fechas (ej. del lunes al viernes son 5 días)?
2. ¿Qué diálogo es el adecuado para solicitar confirmación irreversible al usuario?

### Arquitectura
```
ejercicio_015/
├── app.py           # Formulario y diálogos
└── vacation_core.py # Aritmética de fechas y validación de saldo
```

### Pruebas mínimas
1. Con saldo de 10 días, solicitar del 2026-06-01 al 2026-06-05 -> Debe calcular 5 días, proyectar 5 restantes y permitir confirmar.
2. Al confirmar 'Sí', el saldo disponible debe actualizarse a 5.

### Pruebas de error
1. Solicitar del 2026-06-10 al 2026-06-05 (fecha fin anterior a inicio) -> Debe advertir fecha inválida y deshabilitar confirmación.

### Experiencia de usuario
El saldo restante proyectado debe actualizarse en cuanto ambas fechas sean válidas sin forzar un clic previo.

### Explicación posterior
¿Cómo garantiza el uso de objetos `date` de Python frente a cadenas de texto la correcta validación cronológica?

### Aplicación profesional
Módulos de autoservicio de personal en intranets corporativas y sistemas de control de asistencia.

### Reto adicional
Añade una función que excluya sábados y domingos del cálculo de días solicitados utilizando el método `.weekday()`.

---
> [Índice General](../README.md) · [← Ejercicio 014](../ejercicio_014/README.md) · [Ejercicio 016 →](../ejercicio_016/README.md)
