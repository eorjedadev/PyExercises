## Ejercicio 100 — Suite Empresarial de Control de Proyectos y Presupuestos de Obras (`MasterProjectSuiteApp`)

> [Índice General](../README.md) · [← Ejercicio 099](../ejercicio_099/README.md)

### Contexto profesional
En constructoras y firmas de ingeniería civil, los directores de obra gestionan proyectos de construcción de gran escala supervisando presupuestos asignados, avance físico de partidas de obra, compras de materiales, contratistas y flujo de caja.

### Usuario objetivo
Director de obras, gerente de proyectos de ingeniería o director general de operaciones.

### Problema
La gestión de presupuestos millonarios en hojas de cálculo dispersas provoca desvíos de costos no detectados a tiempo, pagos duplicados a contratistas y retrasos críticos en la entrega de proyectos de infraestructura.

### Objetivo
Desarrollar la aplicación cumbre del programa: una suite empresarial completa de escritorio para control de proyectos y presupuestos de obras. El estudiante debe demostrar maestría absoluta en ingeniería de software de escritorio: arquitectura limpia en capas (`ui/`, `services/`, `models/`, `storage/`), base de datos relacional SQLite con múltiples tablas vinculadas, interfaz multi-pestaña o multi-vista profesional con temas estilizados, tareas en segundo plano con `threading` para generación de reportes pesados, gráficos vectoriales nativos en `Canvas` para avance físico de obra, pruebas automatizadas de servicios con `unittest`, bitácora de auditoría con `logging`, manejo global de excepciones y preparación completa para empaquetado final.

### Flujo principal
El director selecciona un proyecto de obra activo. Visualiza el panel ejecutivo consolidado: presupuesto total vs gasto real acumulado, porcentaje de avance físico con gráfico en `Canvas`, y lista de partidas de obra en un `Treeview`. Puede registrar estimaciones de avance, compras de materiales y pagos a contratistas. En un hilo secundario independiente con barra de progreso, genera reportes consolidados ejecutivos en PDF/Texto sin congelar la ventana. Todas las operaciones están auditadas en base de datos y protegidas contra fallos imprevistos.

### Requisitos funcionales
- Esquema de base de datos SQLite relacional integral con tablas: `proyectos`, `partidas_obra`, `gastos_materiales`, `contratistas`, `estimaciones_avance` y `bitacora_auditoria`.
- Vistas principales modulares: Tablero Ejecutivo (Dashboard con KPIs y gráfico de avance en `Canvas`), Gestión de Partidas de Obra (Árbol jerárquico de partidas y costos en `Treeview`), Control de Gastos y Compras, y Reportes Ejecutivos.
- Renderizado vectorial en `Canvas` de curvas de avance físico y financiero (Curva S de proyecto o barras comparativas Presupuesto vs Real).
- Generación asíncrona de reportes consolidados pesados ejecutada en segundo plano con `threading`, comunicada por `queue.Queue` y reflejada con barra de progreso reactiva.
- Suite exhaustiva de pruebas unitarias automatizadas con `unittest` para los servicios de cálculo presupuestario y desviaciones de costos.
- Bitácora de auditoría técnica con el módulo estándar `logging` que registre todas las transacciones financieras y eventos del sistema.
- Interceptor global de excepciones configurado para garantizar que la suite nunca colapse de forma imprevista ante errores no manejados.
- Preparación formal para empaquetado con PyInstaller mediante resolución de rutas con `sys._MEIPASS` y archivo `.spec` configurado.

### Requisitos de interfaz
- Interfaz gráfica de grado corporativo con estética moderna, tipografías nítidas y paleta de colores profesional.
- Navegación fluida entre módulos mediante menú principal, barra de herramientas y pestañas estructuradas.
- Gráficos y medidores limpios en Canvas con buen contraste.
- Formularios completos y accesibles con validaciones en tiempo real.

### Datos
- Modelo de datos integral con más de 6 entidades relacionales vinculadas mediante claves foráneas y restricciones de integridad.

### Estado
- Proyecto activo seleccionado, sesión de usuario y estado de operaciones asíncronas en memoria.

### Persistencia
Base de datos relacional SQLite (`datos/master_proyectos.db`) con soporte de transacciones atómicas y exportación.

### Validaciones
- Validaciones exhaustivas en todas las capas: validaciones de entrada en la interfaz, validaciones de negocio en los servicios y restricciones `CHECK`/`FOREIGN KEY` en la base de datos.

### Casos límite
- Desviaciones presupuestarias críticas (costo real supera el 120% del presupuesto de la partida, activar alertas).
- Proyectos con cientos de partidas de obra organizadas jerárquicamente.
- Cierre de la aplicación con procesos asíncronos de reporte en ejecución.

### Manejo de errores
- Manejo profesional y multinivel de errores: validaciones de usuario amigables, errores de datos contenidos con rollback y fallos inesperados interceptados por el manejador global.

### Fundamentos de Python relacionados
- Dominio pleno de programación orientada a objetos, patrones de diseño, concurrencia con hilos, bases de datos relacionales, testing automatizado y logging estructurado.

### Conceptos Tkinter relacionados
- Maestría integral en Tkinter y ttk: widgets temáticos, geometrías compuestas, eventos, variables de control, `Canvas` vectorial, diálogos modales y ciclo de eventos con `after()`.

### Herramientas para investigar
- Metodologías de gestión de proyectos de construcción (Curva S, Valor Ganado / Earned Value Management).
- Arquitectura de software empresarial en Python.

### Diseño de interfaz
El estudiante diseña de forma completamente autónoma la arquitectura visual de la suite garantizando una experiencia de usuario de élite.

### Diseño de variables
Nomenclatura semántica, profesional y rigurosa en el 100% de los módulos del proyecto.

### Antes de programar
1. ¿Cómo estructurarás la arquitectura modular del proyecto en paquetes (`ui/`, `services/`, `models/`, `storage/`, `tests/`, `config/`) para garantizar máxima mantenibilidad y testabilidad?
2. ¿Cómo coordinarás la comunicación segura entre el hilo de generación de reportes en segundo plano y el hilo principal de la interfaz gráfica?
3. ¿Cómo defenderás técnica y arquitectónicamente cada una de las decisiones que tomaste a lo largo del desarrollo de esta suite?

### Arquitectura
```
ejercicio_100/
├── main.py                     # Punto de entrada de la suite corporativa
├── app.spec                    # Archivo de empaquetado de PyInstaller
├── config/
│   ├── __init__.py
│   └── settings.py             # Configuración y resolución de rutas _MEIPASS
├── models/
│   ├── __init__.py
│   └── entities.py             # Modelos de dominio y dataclasses
├── services/
│   ├── __init__.py
│   ├── project_service.py      # Lógica de proyectos y partidas
│   ├── budget_service.py       # Fórmulas financieras y valor ganado
│   └── report_worker.py        # Tareas asíncronas con threading y colas
├── storage/
│   ├── __init__.py
│   ├── db_context.py           # Conexión, transacciones e integridad SQLite
│   └── repositories.py         # Repositorios DAO desacoplados
├── ui/
│   ├── __init__.py
│   ├── main_window.py          # Ventana principal y navegación
│   ├── theme.py                # Estilos ttk.Style y paletas
│   ├── views/                  # Vistas modulares por subsistema
│   │   ├── dashboard_view.py
│   │   ├── budget_view.py
│   │   └── reports_view.py
│   └── components/             # Gráficos Canvas, medidores y tablas
│       └── progress_canvas.py
├── tests/
│   ├── __init__.py
│   └── test_services.py        # Suite de pruebas unitarias automatizadas con unittest
├── logs/
│   └── suite_audit.log         # Bitácora de auditoría técnica con logging
└── datos/
    └── master_proyectos.db     # Base de datos relacional de la suite
```

### Pruebas mínimas
1. Ejecutar la suite de pruebas unitarias con `python -m unittest discover tests` -> Todas las pruebas deben pasar con éxito en verde.
2. Iniciar la aplicación -> Navegar entre módulos, registrar partidas y gastos -> Los indicadores financieros y gráficos de Canvas deben actualizarse con precisión.
3. Generar un reporte en segundo plano -> Comprobar que la barra de progreso avance suavemente sin congelar la ventana.

### Pruebas de error
1. Simular una partida con gasto mayor al presupuesto -> El sistema debe alertar sobrecosto en rojo en el dashboard y en la tabla.
2. Provocar un fallo intencional -> El manejador global debe interceptar la excepción, generar folio y registrar el traceback en la bitácora sin cerrar la suite.

### Experiencia de usuario
Experiencia de software de escritorio de élite comercial: rápida, visualmente armónica, intuitiva, responsiva y completamente sólida ante cualquier acción del usuario.

### Explicación posterior
El practicante debe ser capaz de explicar la totalidad de la suite: la arquitectura en capas adoptada, la justificación de cada widget, el diseño relacional de la base de datos, el mecanismo de concurrencia seguro empleado, la estrategia de pruebas automatizadas y la metodología de empaquetado para distribución final.

### Aplicación profesional
Dirección de proyectos de infraestructura en constructoras, gerencia de operaciones en firmas de ingeniería civil y control de presupuestos de obras públicas.

### Reto adicional
Integra una calculadora del Índice de Desempeño del Costo (CPI = EV / AC) y del Cronograma (SPI = EV / PV) según la metodología estándar de Valor Ganado del PMI.

---
> [Índice General](../README.md) · [← Ejercicio 099](../ejercicio_099/README.md)
