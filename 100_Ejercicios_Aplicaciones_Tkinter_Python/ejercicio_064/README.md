## Ejercicio 064 — Generador de Reportes Ejecutivos en Archivos Planos (`AsyncReportBuilderApp`)

> [Índice General](../README.md) · [← Ejercicio 063](../ejercicio_063/README.md) · [Ejercicio 065 →](../ejercicio_065/README.md)

### Contexto profesional
En gerencias de administración corporativa, los directores solicitan la consolidación masiva de múltiples fuentes de datos mensuales para generar un reporte ejecutivo consolidado en formato de texto.

### Usuario objetivo
Asistente de dirección o analista financiero.

### Problema
La consolidación de múltiples fuentes requiere varios segundos de cálculo y procesamiento, y si se ejecuta en el hilo principal de Tkinter, impide al usuario trabajar o consultar otras partes de la aplicación.

### Objetivo
Desarrollar un generador de reportes asíncrono con `threading` que simule la consolidación de tres fuentes de datos pesadas (Ventas, Nómina, Compras), reportando el progreso porcentual paso a paso hacia una barra `ttk.Progressbar` mediante una cola segura, y mostrando el informe final formateado en la interfaz.

### Flujo principal
El usuario selecciona el periodo y las opciones de consolidación. Presiona 'Generar Reporte Consolidado'. Un hilo trabajador ejecuta las tres fases secuencialmente: Fase 1 (Consolidando ventas, 33%), Fase 2 (Procesando nómina, 66%), Fase 3 (Calculando márgenes, 100%). Cada fase emite un mensaje y un porcentaje a la cola. El hilo principal de Tkinter actualiza una barra de progreso y una etiqueta de estado. Al concluir, el reporte final se despliega en un visor de texto.

### Requisitos funcionales
- Opciones de generación en ventana: Año, Mes, Nivel de Consolidación (`Resumido` / `Detallado`).
- Procesamiento pesado simulado en hilo en segundo plano con múltiples etapas cronológicas.
- Despacho de actualizaciones de progreso porcentual y mensajes de estado a través de `queue.Queue`.
- Bucle de sondeo reactivo con `.after()` en el hilo principal.
- Barra de progreso determinada que se actualiza en tiempo real según el avance de cada fase.
- Despliegue del reporte generado en un widget `Text` monoespaciado de la interfaz.

### Requisitos de interfaz
- Formulario superior de selección de parámetros.
- Barra de progreso con etiqueta de fase actual (ej. 'Fase 2 de 3: Procesando nómina...').
- Área `Text` amplia para la visualización del informe final consolidado.
- Botón de guardado a disco activo tras finalizar la generación.

### Datos
- Fases de progreso: porcentaje (int), mensaje_fase (str).
- Reporte final: texto formateado multilínea.

### Estado
- Estado de generación activa en memoria.
- Cola de eventos thread-safe.

### Persistencia
Exportación del informe final a archivo de texto plano mediante `filedialog`.

### Validaciones
- Impedir iniciar una nueva generación si ya existe un reporte generándose en segundo plano.

### Casos límite
- Intentar cerrar la aplicación durante la consolidación (notificar que hay un proceso activo antes de salir).
- Fallo simulado en una de las fuentes de datos.

### Manejo de errores
- Capturar excepciones en el hilo trabajador y notificar el fallo en la cola para restaurar la interfaz a su estado normal.

### Fundamentos de Python relacionados
- Simulación de tareas pesadas con retardos controlados (`time.sleep` en hilos secundarios exclusivamente).
- Construcción de reportes formateados con alineación de cadenas.

### Conceptos Tkinter relacionados
- Prohibición de `time.sleep` en el hilo de Tkinter.
- Patrón productor-consumidor entre hilo trabajador y ciclo de eventos de la GUI.

### Herramientas para investigar
- Patrón productor-consumidor con `queue.Queue`.
- Despacho de estados complejos en tuplas `(tipo_evento, datos)` a través de colas.

### Diseño de interfaz
¿Cómo estructurarías la etiqueta de estado de la barra de progreso para que comunique con precisión qué subproceso se está ejecutando en cada instante?

### Diseño de variables
Usa nombres como `period_combo`, `generate_btn`, `progress_bar`, `stage_status_label`, `report_text`, `report_queue`, `builder_thread`.

### Antes de programar
1. ¿Por qué está estrictamente prohibido llamar a `time.sleep()` dentro de cualquier callback del hilo principal de Tkinter?
2. ¿Cómo se empaquetan mensajes estructurados en la cola como tuplas `('PROGRESO', 45, 'Analizando compras')` para que el hilo principal sepa qué actualizar?

### Arquitectura
```
ejercicio_064/
├── app.py             # Interfaz gráfica, barra y visor de reporte
├── report_worker.py   # Hilo secundario de consolidación de datos
└── report_formatter.py # Motor de formateo textual del informe
```

### Pruebas mínimas
1. Iniciar generación -> La barra de progreso debe avanzar proporcionalmente reportando las tres fases sin bloquear la ventana.
2. Al llegar al 100% -> El informe final debe aparecer en el visor de texto y habilitarse el botón de guardado.

### Pruebas de error
1. Presionar repetidamente el botón 'Generar' durante el proceso -> El botón debe estar deshabilitado para evitar duplicación de tareas.

### Experiencia de usuario
La barra debe reflejar cambios suaves y el visor de texto debe hacer scroll automático hasta el final al recibir el reporte.

### Explicación posterior
¿Cómo permite el protocolo de mensajes por tuplas en `queue.Queue` manejar múltiples tipos de notificaciones (progreso, error, finalización) de forma limpia?

### Aplicación profesional
Generadores de cierres mensuales en sistemas ERP, motores de consolidación de nóminas y compiladores de estadísticas institucionales.

### Reto adicional
Añade un botón de cancelación que permita abortar la consolidación entre fases restableciendo la barra de progreso a cero.

---
> [Índice General](../README.md) · [← Ejercicio 063](../ejercicio_063/README.md) · [Ejercicio 065 →](../ejercicio_065/README.md)
