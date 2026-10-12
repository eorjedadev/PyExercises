## Ejercicio 088 — Consola de Gestión con Manejador Global de Excepciones (`CrashSafeManagerApp`)

> [Índice General](../README.md) · [← Ejercicio 087](../ejercicio_087/README.md) · [Ejercicio 089 →](../ejercicio_089/README.md)

### Contexto profesional
En aplicaciones de escritorio corporativas distribuidas a cientos de operadores, un error de programación imprevisto (bug no capturado) no debe cerrar la aplicación silenciosamente ni asustar al usuario con tracebacks crudos en consola.

### Usuario objetivo
Operador de sistema corporativo y equipo de soporte técnico de nivel 3.

### Problema
Cuando ocurre una excepción imprevista en un callback de Tkinter, la ventana puede comportarse de forma errática o cerrarse sin dejar rastro en disco para que los desarrolladores identifiquen el error.

### Objetivo
Desarrollar una aplicación de gestión empresarial equipada con un Manejador Global de Excepciones no capturadas utilizando `Tk.report_callback_exception`, que intercepte cualquier fallo inesperado, muestre un diálogo amigable al usuario ('Ha ocurrido un problema inesperado') con opción de enviar reporte, y escriba automáticamente el traceback completo y contexto del sistema en un archivo `crash_reports.log`.

### Flujo principal
El usuario opera normalmente la consola de gestión (registra datos, consulta tablas). La aplicación incluye un botón especial de prueba 'Simular Error Inesperado' (que provoca una división por cero o `KeyError` no manejado). Al dispararse el error, en lugar de colapsar la consola, el interceptor global lo captura, genera un folio de incidencia (ej. `CRASH-7721`), graba el traceback detallado en `crash_reports.log` y muestra un diálogo profesional informando al usuario el folio generado para su reporte a soporte.

### Requisitos funcionales
- Configuración del interceptor global de excepciones de Tkinter sobrescribiendo `root.report_callback_exception = mi_manejador_global`.
- Captura de excepciones fuera de Tkinter mediante `sys.excepthook` para blindaje total.
- Registro automático en archivo `logs/crash_reports.log` con: Timestamp, Versión de la app, Sistema Operativo, Tipo de Excepción y Traceback completo formateado con `traceback.format_exception`.
- Generación de un folio único de error para trazabilidad del usuario.
- Diálogo modal amigable (`messagebox.showerror` o ventana personalizada) que informe al usuario con lenguaje comprensible sin exponer código crudo.
- Mantenimiento de la estabilidad de la ventana principal tras la captura del error.

### Requisitos de interfaz
- Interfaz corporativa con operaciones normales y un botón visible de 'Prueba de Robustez: Provocar Excepción'.
- Diálogo de error personalizado que incluya el folio de la incidencia y un botón 'Copiar Reporte a Portapapeles'.
- Barra de estado que refleje la estabilidad del sistema.

### Datos
- Reporte de fallo: folio_incidencia, timestamp, tipo_error, mensaje, traceback_str, info_sistema.

### Estado
- Estado de la aplicación activo.
- Último folio de error registrado.

### Persistencia
Archivo de bitácora de fallos (`logs/crash_reports.log`).

### Validaciones
- El manejador de excepciones en sí mismo nunca debe lanzar una excepción no controlada.

### Casos límite
- Excepciones concurrentes sucesivas.
- Fallos de permisos al intentar escribir el archivo de log (debe intentar escribir en carpeta temporal o mostrarlo en pantalla).

### Manejo de errores
- Manejar la captura exhaustiva de `Exception` sin silenciar señales de terminación del sistema operativo (`KeyboardInterrupt`, `SystemExit`).

### Fundamentos de Python relacionados
- Módulo estándar `traceback` (`format_exception`, `print_exc`).
- Manejo de `sys.excepthook` para excepciones a nivel de intérprete de Python.
- Generación de identificadores de incidencias.

### Conceptos Tkinter relacionados
- Método nativo `Tk.report_callback_exception` para captura de excepciones dentro del bucle de eventos de Tkinter.
- Diálogos de recuperación ante fallos.

### Herramientas para investigar
- Mecanismo `report_callback_exception` en la clase `tk.Tk`.
- Módulo `traceback` de la biblioteca estándar de Python.

### Diseño de interfaz
¿Cómo diseñarías el diálogo de incidencia para que transmita tranquilidad al usuario y le facilite reportar el problema a soporte técnico?

### Diseño de variables
Usa nombres como `global_crash_handler`, `crash_dialog`, `error_id_label`, `copy_trace_btn`, `simulate_bug_btn`, `crash_logger`.

### Antes de programar
1. ¿Qué es `Tk.report_callback_exception` y por qué los bloques `try/except` tradicionales en el punto de entrada no capturan los errores dentro de los callbacks de los widgets?
2. ¿Cómo se utiliza `traceback.format_exception(*exc_info)` para obtener la pila completa de llamadas en una cadena de texto?

### Arquitectura
```
ejercicio_088/
├── app.py             # Ventana principal y configuración de interceptores
├── crash_handler.py   # Manejador global de excepciones y generador de reportes
├── error_dialog.py    # Diálogo modal amigable con opción de copia de folio
└── logs/
    └── crash_reports.log # Registro detallado de trazas de errores
```

### Pruebas mínimas
1. Presionar el botón 'Simular Error Inesperado' -> Comprobar que la ventana no se cierre, se muestre el diálogo con el folio y se escriba el traceback en `crash_reports.log`.
2. Presionar 'Copiar Reporte' -> Verificar que el portapapeles contenga el folio y los datos técnicos limpios.

### Pruebas de error
1. Provocar un error dentro de una función de menú -> Comprobar que el interceptor capture el fallo con la misma eficacia que en un botón.

### Experiencia de usuario
El usuario nunca debe ver una ventana desaparecer repentinamente sin explicación ni quedar frente a un sistema congelado.

### Explicación posterior
¿Cómo garantiza `Tk.report_callback_exception` la resiliencia de una aplicación de escritorio corporativa frente a bugs no previstos en producción?

### Aplicación profesional
Software bancario de sucursal, terminales de punto de venta, herramientas de campo para técnicos y suites de gestión de misión crítica.

### Reto adicional
Añade en el reporte de log la captura de la cantidad de memoria RAM libre del sistema en el momento del fallo utilizando `shutil.disk_usage` y variables del entorno.

---
> [Índice General](../README.md) · [← Ejercicio 087](../ejercicio_087/README.md) · [Ejercicio 089 →](../ejercicio_089/README.md)
