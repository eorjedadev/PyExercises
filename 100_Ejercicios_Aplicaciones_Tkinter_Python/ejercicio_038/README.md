## Ejercicio 038 — Panel de Control Multi-Pestaña de Sucursal (`BranchDashboardApp`)

> [Índice General](../README.md) · [← Ejercicio 037](../ejercicio_037/README.md) · [Ejercicio 039 →](../ejercicio_039/README.md)

### Contexto profesional
En oficinas regionales de cadenas comerciales, los gerentes de sucursal necesitan supervisar en una sola pantalla ventas diarias, plantilla de empleados en turno e indicadores de cumplimiento de metas.

### Usuario objetivo
Gerente de sucursal comercial o supervisor de tienda.

### Problema
Tener que abrir aplicaciones distintas o ventanas dispersas para ver ventas, personal y metas genera demoras en la toma de decisiones durante el turno.

### Objetivo
Construir un panel de control consolidado utilizando `ttk.Notebook` con tres pestañas temáticas independientes ('Resumen de Ventas', 'Personal en Turno' y 'Metas Mensuales'), con datos reactivos y navegación limpia entre vistas.

### Flujo principal
El gerente abre el panel y navega entre las pestañas del Notebook. En la primera pestaña registra ventas por caja; en la segunda consulta y marca la asistencia del personal; en la tercera visualiza las metas alcanzadas con barras de progreso. Cada pestaña mantiene su propio estado de forma ordenada.

### Requisitos funcionales
- Estructura principal basada en `ttk.Notebook` con 3 pestañas claramente rotuladas.
- Pestaña 1 ('Ventas'): Registro rápido de ticket con monto y forma de pago, tabla con ventas del día y total acumulado.
- Pestaña 2 ('Personal'): Lista de colaboradores con casillas de verificación para marcar quién está presente en turno.
- Pestaña 3 ('Metas'): Indicadores visuales de cumplimiento porcentual con barras de progreso (`ttk.Progressbar`).
- Barra de estado global persistente en la parte inferior compartida por todas las pestañas.

### Requisitos de interfaz
- Uso de `ttk.Notebook` con pestañas estilizadas y legibles.
- Cada pestaña debe ser un `Frame` independiente encapsulado.
- Barra de estado global visible independientemente de la pestaña activa.

### Datos
- Datos de ventas: lista de tickets.
- Datos de personal: lista de empleados con estado de asistencia.
- Metas: enteros de meta y valores reales.

### Estado
- Pestaña activa actualmente seleccionada.
- Estados independientes de cada subsistema en memoria.

### Persistencia
No requiere persistencia en disco en esta fase (opera en memoria de sesión).

### Validaciones
- Ventas deben ser números positivos mayores a cero.
- No permitir registrar ventas sin seleccionar forma de pago.

### Casos límite
- Cambiar rápidamente de pestaña mientras se digita en un formulario.
- Cumplimiento de metas mayor al 100% (la barra de progreso debe topar al 100% sin desbordarse visualmente).

### Manejo de errores
- Validar entradas numéricas en la pestaña de ventas sin afectar la visualización de las otras pestañas.

### Fundamentos de Python relacionados
- Modularización del código dividiendo componentes en clases o funciones de construcción de pestañas.
- Diccionarios para modelar indicadores clave de rendimiento (KPIs).

### Conceptos Tkinter relacionados
- Widget `ttk.Notebook` y métodos `.add(child, text=...)`, `.select()`.
- Evento virtual `<<NotebookTabChanged>>`.
- Widget `ttk.Progressbar` en modo determinado.

### Herramientas para investigar
- Documentación de `ttk.Notebook`.
- Eventos virtuales de pestañas en `ttk.Notebook`.

### Diseño de interfaz
¿Cómo asegurarías que el diseño visual de cada pestaña mantenga una coherencia de márgenes, tipografías y paletas de color con las demás?

### Diseño de variables
Usa nombres como `notebook_control`, `sales_tab_frame`, `staff_tab_frame`, `goals_tab_frame`, `goal_progressbar`, `global_status_bar`.

### Antes de programar
1. ¿Por qué es una buena práctica arquitectónica implementar cada pestaña como un `Frame` derivado o en una clase independiente en lugar de poner todo el código en una sola función gigante?
2. ¿Cómo se detecta cuándo el usuario cambia de pestaña usando el evento virtual `<<NotebookTabChanged>>`?

### Arquitectura
```
ejercicio_038/
├── app.py           # Notebook principal y ventana contenedora
├── tabs/
│   ├── sales_tab.py # Vista y lógica de la pestaña de ventas
│   ├── staff_tab.py # Vista y lógica de personal en turno
│   └── goals_tab.py # Vista y barras de progreso de metas
└── store_model.py   # Estado compartido de la sucursal
```

### Pruebas mínimas
1. Registrar una venta de $150 en la pestaña 1 -> Cambiar a la pestaña 3 y verificar que el porcentaje de la meta de ventas se actualice.
2. Navegar entre las tres pestañas -> Verificar que los datos ingresados en cada una se conserven intactos.

### Pruebas de error
1. Ingresar venta con monto de texto en pestaña 1 -> Debe advertir error sin desconfigurar las demás pestañas.

### Experiencia de usuario
El cambio entre pestañas debe ser instantáneo y los encabezados de las pestañas deben ser amplios para fácil clic.

### Explicación posterior
¿Cómo ayuda la composición modular de pestañas con `ttk.Notebook` a evitar clases monolíticas gigantescas en interfaces complejas?

### Aplicación profesional
Paneles de administración de sucursales, consolas de configuración de software corporativo y sistemas de gestión de turnos.

### Reto adicional
Añade un atajo de teclado (`Ctrl+1`, `Ctrl+2`, `Ctrl+3`) para alternar rápidamente entre las pestañas sin usar el ratón.

---
> [Índice General](../README.md) · [← Ejercicio 037](../ejercicio_037/README.md) · [Ejercicio 039 →](../ejercicio_039/README.md)
