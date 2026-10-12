## Ejercicio 014 — Cotizador de Seguros con Opciones Dinámicas (`InsuranceQuoteApp`)

> [Índice General](../README.md) · [← Ejercicio 013](../ejercicio_013/README.md) · [Ejercicio 015 →](../ejercicio_015/README.md)

### Contexto profesional
En agencias de seguros de vehículos, los promotores necesitan calcular en tiempo real la póliza de un cliente conforme se añaden coberturas adicionales y factores de riesgo.

### Usuario objetivo
Agente de seguros o asesor comercial de pólizas.

### Problema
Calcular manualmente pólizas sumando deducibles, asistencias en carretera y coberturas de daños a terceros en hojas de papel genera demoras y cotizaciones incorrectas.

### Objetivo
Desarrollar una aplicación de cotización reactiva donde la selección de coberturas mediante casillas de verificación (`Checkbutton`) y rango de edad modifique instantáneamente la prima anual y mensual estimada.

### Flujo principal
El agente selecciona la categoría del vehículo, el rango de edad del conductor y activa las coberturas deseadas (Daños a terceros obligatoria, Robo total, Asistencia legal, Auto sustituto). Con cada clic, el precio se actualiza de forma automática en la pantalla.

### Requisitos funcionales
- Tarifa base según tipo de vehículo (Sedán, SUV, Deportivo, Comercial).
- Factor de recargo por edad del conductor (menores de 25 años tienen recargo del 20%).
- Coberturas opcionales independientes mediante casillas de verificación con costos fijos asignados.
- Cálculo de prima anual y desglose de 12 cuotas mensuales.
- Botón para generar resumen en texto listo para enviar al cliente.

### Requisitos de interfaz
- Panel de configuración de vehículo y conductor a la izquierda.
- Panel de coberturas adicionales con `ttk.Checkbutton` al centro.
- Panel destacado a la derecha con la prima total y el botón de resumen.
- Actualización automática al cambiar cualquier opción sin botones de cálculo intermedios.

### Datos
- Precios de coberturas y factores multiplicadores en una estructura de configuración.
- Total anual y mensual: float.

### Estado
- Variables `BooleanVar` para cada cobertura opcional.
- Variable `StringVar` para la categoría del vehículo y edad.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- La cobertura básica de responsabilidad civil debe ser obligatoria e inmodificable (marcada y deshabilitada).

### Casos límite
- Desmarcar todas las opciones adicionales (el total debe ser únicamente la tarifa base ajustada por edad).

### Manejo de errores
- Evitar discrepancias numéricas asegurando que los cálculos se ejecuten sobre números reales antes de formatear a cadena.

### Fundamentos de Python relacionados
- Diccionarios para tarifas y modificadores de riesgo.
- Manejo de porcentajes y redondeo monetario.

### Conceptos Tkinter relacionados
- Enlace del parámetro `command=` en múltiples `ttk.Checkbutton` apuntando a la misma función de recálculo.
- Bloqueo de widgets con `state='disabled'`.
- Diseño multipanel con `Frame`.

### Herramientas para investigar
- Parámetro `command` en `ttk.Checkbutton` y `ttk.Radiobutton`.
- Métodos de inspección de estado de variables booleanas.

### Diseño de interfaz
¿Cómo organizarías los paneles para que el precio total sea visible en todo momento independientemente de qué opciones se marquen?

### Diseño de variables
Usa nombres como `vehicle_type_var`, `young_driver_var`, `theft_coverage_var`, `road_assist_var`, `annual_premium_display`.

### Antes de programar
1. ¿Por qué es más intuitivo recalcular en el evento `command` de cada casilla en lugar de forzar al usuario a presionar un botón 'Calcular'?
2. ¿Cómo mantienes una casilla de verificación marcada permanentemente sin que el usuario pueda desmarcarla?

### Arquitectura
```
ejercicio_014/
├── app.py           # Ventana gráfica y enlace reactivo
└── rating_engine.py # Motor de tarificación y reglas actuariales simples
```

### Pruebas mínimas
1. Seleccionar Sedán base ($500) y marcar Asistencia ($50) -> El total debe actualizarse inmediatamente a $550 anuales.
2. Marcar conductor menor de 25 años (+20%) -> El total de $550 debe subir a $660 anuales.

### Pruebas de error
1. Intentar desmarcar la casilla obligatoria de responsabilidad civil -> El widget debe ignorar el clic o estar deshabilitado.

### Experiencia de usuario
La actualización del precio debe ser fluida, sin parpadeos visuales ni saltos en la ventana.

### Explicación posterior
¿Cómo simplifica el patrón de observador/comando la reactividad de la interfaz frente a múltiples entradas simultáneas?

### Aplicación profesional
Cotizadores en línea de aseguradoras, simuladores de planes de telefonía móvil y configuradores de productos a medida.

### Reto adicional
Añade un botón que genere un desglose en formato texto imprimible que pueda ser copiado directamente a un mensaje de correo electrónico.

---
> [Índice General](../README.md) · [← Ejercicio 013](../ejercicio_013/README.md) · [Ejercicio 015 →](../ejercicio_015/README.md)
