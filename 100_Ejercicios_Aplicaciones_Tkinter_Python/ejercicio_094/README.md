## Ejercicio 094 — Monitor de Procesos y Uso de Recursos del Sistema (`ProcessMonitorSysApp`)

> [Índice General](../README.md) · [← Ejercicio 093](../ejercicio_093/README.md) · [Ejercicio 095 →](../ejercicio_095/README.md)

### Contexto profesional
En estaciones de trabajo técnicas y servidores locales, los administradores de sistemas supervisan procesos en ejecución y consumo de memoria RAM y CPU para detectar procesos colgados o fugas de recursos.

### Usuario objetivo
Administrador de sistemas (SysAdmin) o ingeniero de soporte de infraestructura.

### Problema
El monitor de tareas nativo consume recursos adicionales si se mantiene abierto en segundo plano y no permite filtrar procesos específicos según patrones definidos por el usuario.

### Objetivo
Construir un monitor de procesos del sistema operativo en tiempo real con `ttk.Treeview`, que consulte periódicamente la lista de procesos activos (PID, Nombre, Uso de Memoria, Estado), permita filtrar por nombre de proceso, ordene columnas por consumo de memoria y proporcione una acción de terminación segura de procesos con confirmación formal.

### Flujo principal
El usuario abre la aplicación y visualiza la lista de procesos activos del sistema operativo en el `Treeview`. Puede escribir en la barra de búsqueda para filtrar (ej. 'python' o 'chrome'). Al hacer clic en el encabezado 'Memoria', la lista se ordena de mayor a menor consumo. Al seleccionar un proceso problemático, puede pulsar 'Finalizar Proceso', lo que solicita confirmación modal antes de enviar la señal de terminación al sistema.

### Requisitos funcionales
- Inspección periódica de procesos del sistema operativo utilizando comandos nativos (`tasklist` en Windows o `ps` en Linux) o utilidades de la biblioteca estándar.
- Visualización en `ttk.Treeview`: PID, Nombre del Proceso, Memoria en MB, Estado del Proceso.
- Búsqueda y filtrado incremental por nombre de ejecutable.
- Ordenamiento numérico de procesos por consumo de memoria o PID.
- Acción 'Finalizar Proceso' que solicite confirmación obligatoria con `messagebox.askyesno` antes de terminar el proceso.
- Barra inferior de estado con: Total de procesos en ejecución y porcentaje de memoria global disponible.

### Requisitos de interfaz
- Barra superior con buscador en tiempo real y selector de intervalo de actualización (ej. cada 2s, 5s o Manual).
- `Treeview` amplio con scrollbars.
- Panel inferior con total de procesos y botón de finalización de proceso destacado en color de advertencia.

### Datos
- Proceso: pid (int), nombre (str), memoria_mb (float), usuario (str).

### Estado
- Lista de procesos activos consultados.
- Proceso seleccionado en la tabla.
- Intervalo de sondeo con `after()`.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Validar permisos antes de intentar finalizar un proceso de sistema protegido.
- Impedir terminar procesos críticos vitales para el funcionamiento del propio sistema operativo.

### Casos límite
- Proceso que desaparece de forma natural entre el momento de la selección y el clic de terminación.
- Procesos con nombres duplicados (diferenciados por su PID único).

### Manejo de errores
- Capturar `PermissionError` o fallos de acceso denegado al intentar terminar procesos restringidos mostrando advertencia clara.

### Fundamentos de Python relacionados
- Interacción con el sistema operativo mediante el módulo estándar `subprocess` o inspección de `/proc` en Linux.
- Parseo de salidas de texto de comandos de sistema.

### Conceptos Tkinter relacionados
- Actualización periódica en bucle no bloqueante con `root.after()`.
- Preservación de la fila seleccionada durante el refresco de datos de la tabla.

### Herramientas para investigar
- Comando `tasklist` de Windows y comando `ps` de Unix.
- Módulo estándar `subprocess` (`subprocess.run`).

### Diseño de interfaz
¿Cómo asegurarías que al refrescar la tabla cada 2 segundos, la fila que el usuario tenía seleccionada no pierda su selección ni salte la barra de scroll?

### Diseño de variables
Usa nombres como `process_tree`, `search_proc_entry`, `refresh_interval_combo`, `kill_proc_btn`, `total_procs_label`, `sys_monitor_service`.

### Antes de programar
1. ¿Cómo se preserva la posición de scroll y la fila seleccionada de un `Treeview` cuando se actualizan los datos periódicamente con `after()`?
2. ¿Cómo se parsea la salida de `tasklist /FO CSV` en Windows o `ps aux` en Linux usando el módulo `subprocess` y `csv` de Python?

### Arquitectura
```
ejercicio_094/
├── app.py             # Monitor gráfico, tabla y barra de herramientas
├── proc_service.py    # Consulta multiplataforma de procesos del SO
└── process_model.py   # Dataclass de información de proceso
```

### Pruebas mínimas
1. Iniciar monitor -> Comprobar que liste los procesos reales del sistema con PID y memoria en MB.
2. Filtrar por 'python' -> La tabla debe mostrar únicamente las instancias de Python activas.
3. Ordenar por Memoria -> El proceso con mayor consumo debe situarse en la primera fila.

### Pruebas de error
1. Intentar finalizar un proceso de sistema protegido -> Debe capturar el error de permisos y avisar 'Acceso denegado por el sistema operativo'.

### Experiencia de usuario
La actualización debe sentirse suave y no generar parpadeos molestos en la tabla mientras el usuario inspecciona un proceso.

### Explicación posterior
¿Cómo se gestiona el refresco continuo de datos en un `Treeview` preservando el estado de navegación y scroll del usuario?

### Aplicación profesional
Herramientas de diagnóstico de soporte técnico, paneles de monitoreo para operadores de servidores y utilidades de optimización de estaciones de trabajo.

### Reto adicional
Añade una gráfica visual en Canvas en la parte superior que muestre el historial de uso de memoria global de los últimos 60 segundos.

---
> [Índice General](../README.md) · [← Ejercicio 093](../ejercicio_093/README.md) · [Ejercicio 095 →](../ejercicio_095/README.md)
