## Ejercicio 032 — Visor y Analizador de Archivos de Log Web (`AccessLogViewerApp`)

> [Índice General](../README.md) · [← Ejercicio 031](../ejercicio_031/README.md) · [Ejercicio 033 →](../ejercicio_033/README.md)

### Contexto profesional
En operaciones de infraestructura web y ciberseguridad, los ingenieros de sistemas necesitan inspeccionar archivos de logs de servidores web (estilo Nginx/Apache) para detectar picos de errores HTTP.

### Usuario objetivo
Administrador de sistemas (SysAdmin) o ingeniero de DevOps.

### Problema
Abrir archivos de log de cientos de megabytes en editores de texto ordinarios los bloquea y no permite filtrar por códigos de error HTTP de forma rápida.

### Objetivo
Desarrollar una aplicación para abrir archivos de logs en texto plano, parsear cada línea con expresiones regulares a un `ttk.Treeview` (IP, Fecha/Hora, Método, Ruta, Código HTTP, Tamaño), filtrar por estado (4xx, 5xx) y mostrar un resumen estadístico.

### Flujo principal
El usuario hace clic en 'Abrir Archivo de Log' y selecciona un archivo `.log` con `filedialog`. La aplicación procesa las líneas y las lista en la tabla. El analista puede marcar la casilla 'Ver solo errores (4xx y 5xx)' o buscar por una IP específica, actualizando los registros y visualizando la tasa de error porcentual.

### Requisitos funcionales
- Apertura y parseo de logs con formato común (`Common Log Format` o similar).
- Columnas en Treeview: IP Cliente, Timestamp, Método HTTP, URL Solicitada, Status Code, Bytes Transferidos.
- Filtro rápido para códigos 4xx (Errores de cliente) y 5xx (Errores de servidor).
- Búsqueda por coincidencia de dirección IP.
- Resumen inferior: Total solicitudes, Solicitudes exitosas (2xx/3xx), Solicitudes con error (4xx/5xx) y Tasa de error (%).

### Requisitos de interfaz
- Barra superior con botón de apertura de archivo y filtros rápidos.
- Treeview central con barras de desplazamiento vertical y horizontal.
- Tags de colores: 200 en verde, 404 en amarillo, 500 en rojo.

### Datos
- Entrada de log: IP (`str`), fecha (`str`), método (`str`), ruta (`str`), status (`int`), tamaño (`int`).

### Estado
- Lista maestra de eventos de log parseados.
- Filtros activos en memoria.

### Persistencia
Lectura desde archivo de log local (`datos/access.log`).

### Validaciones
- Verificar que el archivo seleccionado exista y tenga formato de log compatible.

### Casos límite
- Líneas de log corruptas o que no coinciden con la expresión regular (deben ignorarse o contarse como no parseables sin detener el programa).
- Archivos de log vacíos.

### Manejo de errores
- Manejar `re.error` o fallos de parseo con un contador de 'Líneas ignoradas'.

### Fundamentos de Python relacionados
- Expresiones regulares con grupos de captura nombrados (`(?P<ip>\S+) ...`).
- Manejo de archivos grandes línea por línea con generadores.

### Conceptos Tkinter relacionados
- Diálogo `filedialog.askopenfilename`.
- Carga progresiva y tags de colores según rangos numéricos de códigos HTTP.

### Herramientas para investigar
- Formato estándar `Combined Log Format` de Apache/Nginx.
- Expresiones regulares con grupos nombrados en Python.

### Diseño de interfaz
¿Cómo asegurarías que las columnas de IP y Código HTTP tengan anchos fijos y la URL se expanda para aprovechar el espacio?

### Diseño de variables
Usa nombres como `log_tree`, `open_log_btn`, `error_only_check`, `ip_search_entry`, `error_rate_label`, `total_reqs_label`.

### Antes de programar
1. ¿Cómo se diseña un regex con grupos nombrados para extraer IP, fecha, método, ruta y código de una línea de log?
2. ¿Por qué es fundamental procesar línea por línea con `for linea in archivo:` en vez de leer todo con `.read()`?

### Arquitectura
```
ejercicio_032/
├── app.py           # Visor gráfico y controles de filtro
├── log_parser.py    # Motor de análisis sintáctico con regex de logs
└── datos/
    └── access.log   # Muestra de archivo de log para pruebas
```

### Pruebas mínimas
1. Abrir `access.log` de muestra -> Comprobar que cargue las filas en la tabla con sus columnas correctas.
2. Activar 'Solo Errores' -> Comprobar que solo queden visibles códigos >= 400 y el porcentaje se actualice.

### Pruebas de error
1. Intentar abrir un archivo de texto no estructurado -> Debe informar cuántas líneas no pudieron parsearse.

### Experiencia de usuario
Los códigos 4xx y 5xx deben distinguirse de inmediato visualmente para facilitar el diagnóstico operativo.

### Explicación posterior
¿Cómo facilita el uso de expresiones regulares con grupos nombrados la extracción limpia de datos semiestructurados?

### Aplicación profesional
Herramientas de auditoría forense para DevOps, analizadores de tráfico web local y visores de incidencias de servidores.

### Reto adicional
Añade un contador del 'Top 3 de URLs más solicitadas' mostrado en un panel lateral de estadísticas rápidas.

---
> [Índice General](../README.md) · [← Ejercicio 031](../ejercicio_031/README.md) · [Ejercicio 033 →](../ejercicio_033/README.md)
