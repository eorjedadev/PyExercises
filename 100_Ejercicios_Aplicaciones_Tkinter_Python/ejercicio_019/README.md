## Ejercicio 019 — Registro de Mantenimiento Preventivo de Maquinaria (`EquipmentMaintenanceApp`)

> [Índice General](../README.md) · [← Ejercicio 018](../ejercicio_018/README.md) · [Ejercicio 020 →](../ejercicio_020/README.md)

### Contexto profesional
En plantas de manufactura y talleres de maquinaria pesada, los jefes de mantenimiento deben registrar inspecciones preventivas y calcular la fecha del próximo servicio según el horómetro.

### Usuario objetivo
Supervisor de mantenimiento o técnico mecánico de planta.

### Problema
El retraso en los servicios de mantenimiento preventivo por falta de seguimiento de horas de uso causa averías graves y pérdida de garantía de equipos industriales.

### Objetivo
Desarrollar una aplicación para registrar inspecciones de equipos con selección de máquina (`Combobox`), horómetro actual, tipo de mantenimiento y cálculo automático de advertencia si el equipo ha superado el límite de horas para servicio.

### Flujo principal
El técnico selecciona la máquina de una lista predefinida. La aplicación muestra el límite de horas del próximo servicio. El técnico ingresa la lectura actual del horómetro y observaciones. Si la lectura supera el límite de mantenimiento, la pantalla emite una alerta visual destacada indicando que el equipo requiere parada técnica inmediata.

### Requisitos funcionales
- Selección de equipo industrial desde catálogo (`Combobox`).
- Visualización de la última lectura registrada y el límite recomendado para el próximo servicio.
- Entrada para la lectura actual del horómetro (entero positivo).
- Selector de estado del equipo: Operativo, Requiere Servicio, En Reparación.
- Alerta visual en color ámbar/rojo si el horómetro actual excede el límite del próximo mantenimiento.
- Botón para registrar inspección y actualizar el estatus.

### Requisitos de interfaz
- Panel de información del equipo seleccionado.
- Formulario de captura de la inspección actual.
- Indicador de estado de alerta con semáforo cromático.

### Datos
- Ficha de equipo: código, modelo, último servicio (horas), próximo servicio (horas), estado actual.

### Estado
- Datos del equipo actualmente seleccionado en memoria.
- Variable para la lectura actual del horómetro.

### Persistencia
No requiere persistencia en disco en esta fase (opera sobre catálogo en memoria).

### Validaciones
- Horómetro actual debe ser un número entero estrictamente mayor o igual a la última lectura registrada (no se permite retroceso de horas).

### Casos límite
- Ingresar una lectura menor a la lectura histórica anterior.
- Intentar registrar sin haber seleccionado un equipo.

### Manejo de errores
- Advertir con diálogo de error si el horómetro ingresado es menor al registrado previamente.

### Fundamentos de Python relacionados
- Diccionarios estructurados para modelar entidades de maquinaria.
- Validaciones numéricas de consistencia histórica.

### Conceptos Tkinter relacionados
- Enlace de eventos de selección `<<ComboboxSelected>>` para actualizar campos dependientes.
- Configuración dinámica de estilos visuales según el estado de alerta.

### Herramientas para investigar
- Eventos de `ttk.Combobox` (`<<ComboboxSelected>>`).
- Manejo de estados de advertencia en interfaces industriales.

### Diseño de interfaz
¿Cómo asegurarías que la alerta de parada técnica por horómetro excedido sea imposible de pasar por alto para el operario?

### Diseño de variables
Usa nombres como `machine_selector`, `last_hours_display`, `current_hours_entry`, `status_combobox`, `alert_banner`.

### Antes de programar
1. ¿Cómo sincronizas los datos mostrados en pantalla cuando el usuario cambia de máquina en la lista desplegable?
2. ¿Qué regla de negocio impide que el horómetro registre un valor menor al histórico?

### Arquitectura
```
ejercicio_019/
├── app.py              # Interfaz de inspección de maquinaria
└── maintenance_core.py # Reglas de horas de servicio y catálogo de equipos
```

### Pruebas mínimas
1. Seleccionar 'Torno CNC 01' (próximo servicio en 500 hrs), ingresar 520 hrs -> Debe mostrar alerta roja de 'Servicio Vencido por 20 hrs'.
2. Ingresar 480 hrs -> Debe mostrar estado 'Dentro de parámetros normales' en verde.

### Pruebas de error
1. Ingresar 300 hrs cuando la última lectura fue 450 hrs -> Debe rechazar el registro indicando que el horómetro no puede disminuir.

### Experiencia de usuario
La selección del equipo debe refrescar de inmediato toda la información de contexto sin requerir clics adicionales.

### Explicación posterior
¿Cómo se vincula el evento `<<ComboboxSelected>>` para actualizar dinámicamente otros componentes de la ventana?

### Aplicación profesional
Sistemas CMMS (Gestión de Mantenimiento Asistido por Computadora) en plantas industriales y flotas de transporte.

### Reto adicional
Añade un campo que estime los días restantes antes del próximo servicio asumiendo una jornada laboral de 8 horas de uso diario.

---
> [Índice General](../README.md) · [← Ejercicio 018](../ejercicio_018/README.md) · [Ejercicio 020 →](../ejercicio_020/README.md)
