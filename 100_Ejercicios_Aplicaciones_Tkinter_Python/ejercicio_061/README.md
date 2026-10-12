## Ejercicio 061 — Monitor de Disponibilidad de Servidores e URLs (`UrlUptimeMonitorApp`)

> [Índice General](../README.md) · [← Ejercicio 060](../ejercicio_060/README.md) · [Ejercicio 062 →](../ejercicio_062/README.md)

### Contexto profesional
En centros de operaciones de red (NOC) y monitoreo de infraestructura de TI, los analistas supervisan continuamente la disponibilidad de servicios web críticos de la organización.

### Usuario objetivo
Analista de NOC o ingeniero de confiabilidad del sitio (SRE).

### Problema
Ejecutar comprobaciones periódicas de red en el hilo principal de Tkinter congela la interfaz gráfica durante varios segundos si un servidor tarda en responder (timeout).

### Objetivo
Desarrollar una aplicación de monitoreo de disponibilidad de URLs en segundo plano utilizando `threading` y `queue.Queue`, actualizando una tabla `ttk.Treeview` con el estado HTTP, tiempo de respuesta en ms y última hora de sondeo sin congelar en ningún momento la ventana.

### Flujo principal
El usuario ingresa URLs en una lista de monitoreo. Al presionar 'Iniciar Monitoreo', un hilo trabajador secundario ejecuta las peticiones periódicamente en intervalos configurables. Las respuestas se envían a través de una cola thread-safe (`queue.Queue`) al hilo principal de Tkinter, que actualiza la tabla mediante sondeos con `.after()`.

### Requisitos funcionales
- Lista de URLs a monitorear (agrega/elimina URLs mediante formulario).
- Hilo en segundo plano (`threading.Thread(daemon=True)`) que ejecuta comprobaciones sin bloquear la interfaz.
- Comunicación segura hilo -> interfaz mediante `queue.Queue`.
- Método `.after()` en el hilo principal que consulta la cola periódicamente y actualiza la tabla.
- Columnas en Treeview: URL, Estado ('En Línea' / 'Caído'), Código HTTP, Latencia (ms), Última Comprobación.
- Controles para Iniciar y Detener el monitoreo periódico.

### Requisitos de interfaz
- Treeview con doble scrollbar y tags: Verde para 200 OK, Rojo para Caído o Timeout.
- Barra de estado con indicador animado o texto 'Monitoreo activo' en verde.
- Botones 'Iniciar Monitoreo' y 'Detener Monitoreo' que alternen su disponibilidad.

### Datos
- Ficha de sondeo: url, status_code, latencia_ms, exito (bool), timestamp.

### Estado
- Bandera de ejecución del hilo de monitoreo (`threading.Event`).
- Cola de mensajes (`queue.Queue`).
- Lista de URLs activas.

### Persistencia
No requiere persistencia en disco en esta fase (opera en memoria de sesión).

### Validaciones
- Validar formato de URL (debe iniciar con `http://` o `https://`).
- Configurar timeout estricto de conexión (ej. 3 segundos) para evitar bloqueos prolongados.

### Casos límite
- Intentar cerrar la ventana mientras el hilo secundario está activo (debe detenerse limpiamente).
- URLs que no responden o lanzan error de DNS.
- Iniciar el monitoreo con 0 URLs en la lista.

### Manejo de errores
- Capturar `urllib.error.URLError` o excepciones de red en el hilo secundario sin interrumpir el bucle de sondeo.

### Fundamentos de Python relacionados
- Módulo estándar `threading` (`Thread`, `Event`).
- Módulo estándar `queue` (`Queue`, `get_nowait`, `Empty`).
- Módulo `urllib.request` para peticiones HTTP simples de la biblioteca estándar.

### Conceptos Tkinter relacionados
- Prohibición estricta de actualizar widgets de Tkinter directamente desde un hilo secundario.
- Patrón seguro de actualización con `root.after()` consultando una cola `queue.Queue`.

### Herramientas para investigar
- Módulo `queue` y clase `queue.Queue` de Python.
- Manejo de hilos demonio (`daemon=True`) y banderas `threading.Event`.

### Diseño de interfaz
¿Cómo asegurarías que el usuario sepa que la ventana sigue viva y no congelada durante la comprobación de una URL lenta?

### Diseño de variables
Usa nombres como `monitor_tree`, `url_entry`, `start_btn`, `stop_btn`, `event_queue`, `stop_event`, `worker_thread`.

### Antes de programar
1. ¿Por qué NUNCA se debe invocar `widget.config(...)` o `tree.insert(...)` directamente desde dentro de un hilo secundario en Tkinter?
2. ¿Cómo garantiza `queue.Queue` la transferencia segura de datos entre el hilo secundario y el hilo principal de Tkinter?

### Arquitectura
```
ejercicio_061/
├── app.py           # Ventana Tkinter, ciclo de sondeo after() y Treeview
├── url_worker.py    # Hilo trabajador en segundo plano y peticiones HTTP
└── url_validator.py # Validación sintáctica de URLs
```

### Pruebas mínimas
1. Iniciar monitoreo con 'https://www.google.com' -> Comprobar que la ventana se mantenga interactiva y se actualice el estado a 'En Línea' en verde.
2. Mover la ventana o hacer clics mientras se realiza el sondeo -> Comprobar que no haya ningún congelamiento visual.

### Pruebas de error
1. Probar con una URL inexistente ('http://servidor-ficticio-xyz.com') -> El hilo debe capturar el error y reportar 'Caído' en rojo sin detener la app.

### Experiencia de usuario
La ventana debe responder instantáneamente a cualquier interacción del ratón o teclado incluso durante la ejecución de las pruebas de red.

### Explicación posterior
¿Por qué es obligatorio utilizar el patrón de colas (`queue.Queue`) y sondeo con `after()` para comunicar hilos secundarios con la GUI de Tkinter?

### Aplicación profesional
Herramientas de monitoreo de servidores web, dashboards de estado de microservicios y utilidades de guardia de DevOps.

### Reto adicional
Añade un contador en la tabla que registre el 'Número de fallos consecutivos' y emita un sonido de alarma si un servidor falla 3 veces seguidas.

---
> [Índice General](../README.md) · [← Ejercicio 060](../ejercicio_060/README.md) · [Ejercicio 062 →](../ejercicio_062/README.md)
