## Ejercicio 068 — Exportador Masivo de Base de Datos a Múltiples Formatos (`DbDataExporterApp`)

> [Índice General](../README.md) · [← Ejercicio 067](../ejercicio_067/README.md) · [Ejercicio 069 →](../ejercicio_069/README.md)

### Contexto profesional
En departamentos de tecnología y analítica de datos, los ingenieros de bases de datos generan volcados periódicos de tablas de producción hacia formatos estándar de intercambio como JSON, CSV y XML para consumo de otras aplicaciones.

### Usuario objetivo
Administrador de bases de datos (DBA) o desarrollador backend.

### Problema
Exportar tablas con cientos de miles de registros bloquea la aplicación de escritorio e impide al usuario saber cuánto tiempo falta o cancelar el volcado.

### Objetivo
Desarrollar una herramienta de exportación masiva de datos desde SQLite (`datos/almacen_datos.db`) hacia múltiples formatos (CSV y JSON estructurado) en segundo plano con `threading`, mostrando una barra de progreso que refleje las filas exportadas en tiempo real y gestionando errores de disco sin bloquear la ventana.

### Flujo principal
El usuario selecciona la tabla a exportar (`ventas`, `clientes`, `inventario`), elige el formato de salida (`CSV` o `JSON`) y especifica la ruta del archivo destino. Al presionar 'Iniciar Exportación', un hilo de fondo ejecuta una consulta con cursor por lotes (`fetchmany`), procesa las filas y escribe en el archivo destino. La interfaz muestra las filas exportadas y la barra de progreso hasta completar la tarea con éxito.

### Requisitos funcionales
- Conexión a base de datos SQLite y listado automático de tablas disponibles en un `Combobox`.
- Opciones de formato de salida: CSV delimitado por comas y JSON formateado con indentación.
- Procesamiento en hilo de fondo (`threading.Thread`) usando cursores de base de datos por lotes (`fetchmany(1000)`).
- Actualización continua del conteo de filas transferidas y barra de progreso determinada.
- Comunicación por colas (`queue.Queue`) y refresco con `after()`.
- Notificación modal al finalizar la exportación con el tiempo total transcurrido.

### Requisitos de interfaz
- Formulario superior ordenado con selectores de tabla, formato y destino.
- Barra de progreso determinada con etiqueta de filas procesadas (ej. '15,000 / 50,000 filas exportadas').
- Botones de acción bien diferenciados y barra de estado informativa.

### Datos
- Parámetros de exportación: tabla_origen, formato_destino, ruta_archivo, total_filas.

### Estado
- Hilo de exportación activo.
- Cola de eventos thread-safe.
- Contador de registros transferidos.

### Persistencia
Generación de archivos CSV o JSON en el sistema de archivos local.

### Validaciones
- Verificar que la tabla seleccionada contenga registros.
- Validar que la ruta de destino tenga permisos de escritura.

### Casos límite
- Tablas con más de 100,000 registros (debe procesarse en lotes para no desbordar la memoria RAM).
- Cancelar el diálogo de guardado de archivo.
- Cerrar la ventana mientras la exportación está a la mitad.

### Manejo de errores
- Manejar `sqlite3.Error` y excepciones de entrada/salida de disco capturándolas en el hilo y reportándolas a la interfaz sin abortar de forma abrupta.

### Fundamentos de Python relacionados
- Uso de cursores SQLite con `fetchmany()` para streaming de datos eficiente.
- Módulos estándar `csv` y `json` de Python.
- Medición de tiempos de ejecución con `time.perf_counter()`.

### Conceptos Tkinter relacionados
- Coordinación entre hilos secundarios pesados y la interfaz gráfica mediante colas de eventos.
- Modificación dinámica del estado de los botones durante la ejecución.

### Herramientas para investigar
- Método `cursor.fetchmany()` en el módulo `sqlite3`.
- Serialización JSON incremental en Python.

### Diseño de interfaz
¿Cómo asegurarías que el botón de exportación se bloquee durante el volcado para impedir que el usuario ejecute dos exportaciones concurrentes sobre el mismo archivo?

### Diseño de variables
Usa nombres como `table_selector_combo`, `format_radio_var`, `dest_file_entry`, `export_btn`, `export_progress_bar`, `rows_counter_label`, `export_queue`.

### Antes de programar
1. ¿Por qué es mucho más eficiente usar `cursor.fetchmany(1000)` en lugar de `cursor.fetchall()` cuando se exportan tablas con miles de registros?
2. ¿Cómo se estructura la escritura de un archivo JSON cuando los registros provienen de una consulta por lotes?

### Arquitectura
```
ejercicio_068/
├── app.py             # Formulario de configuración y barra de progreso
├── export_worker.py   # Hilo de extracción por lotes de SQLite y escritura en disco
└── datos/
    └── almacen_datos.db # Base de datos SQLite con tablas de prueba
```

### Pruebas mínimas
1. Exportar la tabla 'ventas' a formato CSV -> Comprobar que la barra avance hasta el 100% y el archivo CSV contenga todas las filas con sus encabezados.
2. Exportar la misma tabla a JSON -> Verificar que el archivo JSON sea sintácticamente válido y contenga la lista de objetos completa.

### Pruebas de error
1. Seleccionar una ruta de destino protegida contra escritura -> El hilo debe capturar `PermissionError` y notificarlo en la interfaz.

### Experiencia de usuario
Al finalizar la exportación, un diálogo informativo debe felicitar al usuario indicando el total exacto de filas exportadas y los segundos requeridos.

### Explicación posterior
¿Cómo optimiza el patrón de lectura por lotes (`fetchmany`) el uso de memoria RAM durante la extracción masiva de datos en aplicaciones de escritorio?

### Aplicación profesional
Herramientas de respaldo de bases de datos para administradores de sistemas, generadores de volcados para data warehouses y módulos de migración de datos.

### Reto adicional
Añade una opción para comprimir automáticamente el archivo generado en formato `.zip` utilizando el módulo estándar `zipfile` tras concluir la exportación.

---
> [Índice General](../README.md) · [← Ejercicio 067](../ejercicio_067/README.md) · [Ejercicio 069 →](../ejercicio_069/README.md)
