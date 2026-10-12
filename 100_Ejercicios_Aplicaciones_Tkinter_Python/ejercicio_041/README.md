## Ejercicio 041 — Asistente Guiado Paso a Paso (`OnboardingWizardApp`)

> [Índice General](../README.md) · [← Ejercicio 040](../ejercicio_040/README.md) · [Ejercicio 042 →](../ejercicio_042/README.md)

### Contexto profesional
En sistemas corporativos y configuraciones iniciales de servidores, los usuarios deben completar un proceso guiado secuencial de configuración (Wizard) antes de acceder a la plataforma principal.

### Usuario objetivo
Nuevo usuario corporativo o administrador de sistema.

### Problema
Presentar 30 campos de configuración en una sola pantalla abruma al usuario y genera altas tasas de abandono o configuraciones incorrectas.

### Objetivo
Desarrollar un asistente guiado de 3 pasos (Paso 1: Datos de Perfil, Paso 2: Configuración de Licencia y Región, Paso 3: Confirmación y Resumen) que intercambie vistas dentro del mismo contenedor (`Frame swapping`), con validación obligatoria antes de permitir avanzar con el botón 'Siguiente'.

### Flujo principal
El usuario inicia en el Paso 1. Llena su nombre, correo y contraseña. Si los campos son válidos, el botón 'Siguiente' se habilita y pasa al Paso 2. Configura su región y tipo de cuenta. Presiona 'Siguiente' y llega al Paso 3, donde revisa un resumen consolidado de todo lo ingresado. Al presionar 'Finalizar Asistente', se confirma la configuración.

### Requisitos funcionales
- Estructura de navegación con contenedor central que reemplaza vistas (`Frame swapping`).
- Barra de navegación inferior fija con botones: 'Anterior', 'Siguiente' y 'Finalizar'.
- Indicador visual de progreso superior que muestre el paso activo (ej. 'Paso 2 de 3: Preferencias').
- Validación estricta de los campos del paso actual antes de permitir el avance al siguiente paso.
- Botón 'Anterior' deshabilitado en el Paso 1; botón 'Siguiente' oculto o reemplazado por 'Finalizar' en el Paso 3.
- Almacenamiento continuo del estado consolidado a través de todos los pasos.

### Requisitos de interfaz
- Marco de contenido central que se limpie y reconstruya de forma fluida.
- Barra de pasos superior con círculos o texto destacado para el paso activo.
- Botones de navegación inferiores con posición fija para evitar saltos visuales.

### Datos
- Diccionario de configuración acumulado: perfil, licencia, región, preferencias.

### Estado
- Índice del paso actualmente activo (1, 2 o 3).
- Datos validados de los pasos previos.

### Persistencia
No requiere persistencia en disco en esta fase (almacena en memoria de sesión).

### Validaciones
- Paso 1: Nombre >= 3 caracteres, correo válido, contraseña >= 6 caracteres.
- Paso 2: Región seleccionada obligatoria, aceptar términos de servicio.

### Casos límite
- El usuario retrocede al Paso 1, modifica su nombre y vuelve a avanzar (los datos deben mantenerse sincronizados).
- Intentar saltar pasos sin validar.

### Manejo de errores
- Mostrar los errores de validación directamente dentro del paso activo sin cambiar de pantalla.

### Fundamentos de Python relacionados
- Máquina de estados o controlador de flujo para gestionar secuencias de pasos.
- Diccionarios acumuladores de configuración global.

### Conceptos Tkinter relacionados
- Técnica de intercambio de vistas mediante `frame.pack_forget()` y `frame.pack()` o `grid_remove()`.
- Reutilización de un marco contenedor principal.

### Herramientas para investigar
- Patrón Wizard en diseño de software de escritorio.
- Métodos de ocultación y reemplazo de geometría en Tkinter (`pack_forget`, `destroy`).

### Diseño de interfaz
¿Cómo asegurarías que la barra de botones inferior no cambie de posición o tamaño al cambiar entre pasos con diferente cantidad de campos?

### Diseño de variables
Usa nombres como `wizard_container_frame`, `step_indicator_label`, `prev_step_btn`, `next_step_btn`, `finish_wizard_btn`, `wizard_state_dict`.

### Antes de programar
1. ¿Por qué es mejor práctica ocultar frames con `pack_forget()` en lugar de destruirlos y recrearlos cada vez que el usuario navega adelante y atrás?
2. ¿Cómo se valida un paso específico antes de permitir la transición al siguiente?

### Arquitectura
```
ejercicio_041/
├── app.py           # Controlador principal del Wizard y botones de navegación
├── steps/
│   ├── step1_profile.py # Frame del paso de perfil
│   ├── step2_license.py # Frame del paso de preferencias
│   └── step3_summary.py # Frame de resumen final
└── wizard_model.py  # Modelo de datos acumulado del asistente
```

### Pruebas mínimas
1. Llenar Paso 1 válido -> Avanzar al Paso 2 -> Retroceder al Paso 1 y verificar que los datos sigan en sus campos.
2. Completar los 3 pasos y presionar 'Finalizar' -> Comprobar que el resumen contenga todos los datos consolidados.

### Pruebas de error
1. En Paso 1, dejar el correo vacío y presionar Siguiente -> No debe permitir avanzar y debe mostrar advertencia en el paso actual.

### Experiencia de usuario
La transición entre pasos debe sentirse limpia y natural, sin parpadeos de la ventana principal.

### Explicación posterior
¿Cómo funciona el patrón de intercambio de vistas (`Frame swapping`) para crear flujos multipaso dentro de una sola ventana de Tkinter?

### Aplicación profesional
Asistentes de instalación de software, wizards de configuración de bases de datos y flujos de onboarding corporativo.

### Reto adicional
Añade una barra de progreso (`ttk.Progressbar`) en la parte superior que refleje el avance porcentual (33%, 66%, 100%) según el paso activo.

---
> [Índice General](../README.md) · [← Ejercicio 040](../ejercicio_040/README.md) · [Ejercicio 042 →](../ejercicio_042/README.md)
