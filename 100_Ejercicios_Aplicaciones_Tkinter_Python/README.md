# 100 Ejercicios Profesionales de Aplicaciones Tkinter con Python

> Programa integral de formación en ingeniería de software de escritorio orientado exclusivamente al diseño de interfaces, arquitectura en capas, programación dirigida por eventos, estado reactivo, concurrencia no bloqueante, persistencia estructurada, bases de datos SQLite y distribución con Python y Tkinter.

---

## 1. Filosofía del Programa de Formación

Una aplicación gráfica de escritorio no es simplemente un script con tres botones y un color de fondo. Una aplicación de escritorio profesional es un **producto de software completo de grado de ingeniería**, diseñado para:

1. **Resolver problemas reales de escritorio**: Enfocado en flujos operativos donde las aplicaciones locales superan a la web (baja latencia, manipulación directa de archivos locales, operación sin conexión, seguridad perimetral de datos).
2. **Separación estricta de responsabilidades (SoC)**: Ninguna lógica de negocio ni sentencia SQL dentro de los callbacks de los widgets. La interfaz gráfica (`ui/`) es únicamente una capa delgada que delega en servicios (`services/`) y repositorios (`storage/`).
3. **Programación dirigida por eventos y reactividad**: Comprensión profunda del bucle de eventos (`mainloop`), propagación de eventos, bindings del teclado y ratón, y actualización fluida de variables reactivas.
4. **Interfaces no bloqueantes y concurrencia**: Prohibición terminante de congelar la GUI durante tareas pesadas. Integración segura de hilos trabajadores con `threading` comunicados mediante colas thread-safe `queue.Queue` y sondeo con `root.after()`.
5. **Persistencia robusta y profesional**: Progresión natural desde almacenamiento en memoria volátil, archivos estructurados delimitados (TXT, CSV), estructuras jerárquicas (JSON) hasta bases de datos relacionales locales con **SQLite** con claves foráneas y transacciones atómicas.
6. **Diseño, ergonomía y accesibilidad**: Interfaces pensadas para el usuario (jerarquía visual, gestores `grid` y `pack`, componentes temáticos `ttk`, accesibilidad por teclado y manejo de estados vacíos, de carga y de error).
7. **Empaquetado y distribución**: Comprensión formal del ciclo de congelamiento con **PyInstaller**, resolución de recursos con `sys._MEIPASS` y creación de ejecutables autónomos.

---

## 2. Progresión Natural del Aprendizaje

El programa descarta las clasificaciones tradicionales artificiales ('básico', 'intermedio', 'avanzado'). La complejidad surge orgánicamente a través de 9 etapas de evolución técnica:

```
┌────────────────────────────────────────────────────────────────────────┐
│ Etapa 1: Ventanas, Geometría, Eventos Esenciales y Estado Reactivo    │ (001 - 012)
├────────────────────────────────────────────────────────────────────────┤
│ Etapa 2: Formularios Estructurados, ttk, Validaciones y Diálogos       │ (013 - 024)
├────────────────────────────────────────────────────────────────────────┤
│ Etapa 3: Listas, Tablas (Treeview), Scrollbars, Filtros y Archivos     │ (025 - 036)
├────────────────────────────────────────────────────────────────────────┤
│ Etapa 4: Múltiples Ventanas (Toplevel), Navegación Multi-Vista y Menús  │ (037 - 048)
├────────────────────────────────────────────────────────────────────────┤
│ Etapa 5: Aplicaciones CRUD con Persistencia Relacional en SQLite       │ (049 - 060)
├────────────────────────────────────────────────────────────────────────┤
│ Etapa 6: Tareas Largas, Concurrencia con Threading y Barras de Progreso│ (061 - 072)
├────────────────────────────────────────────────────────────────────────┤
│ Etapa 7: Visualización con Canvas, Gráficos Vectoriales y Temas        │ (073 - 084)
├────────────────────────────────────────────────────────────────────────┤
│ Etapa 8: Arquitectura Empresarial, Pruebas Automatizadas y Logging     │ (085 - 092)
├────────────────────────────────────────────────────────────────────────┤
│ Etapa 9: Distribución con PyInstaller y Autonomía Profesional Completa │ (093 - 100)
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Metodología de Resolución Paso a Paso

Antes de escribir una sola línea de código, el practicante debe seguir rigurosamente este ciclo de ingeniería:

```
Comprender Requerimientos ➔ Diseñar Boceto de UI ➔ Modelar Estado y Datos ➔ Construir Capa Lógica
          ▲                                                                         │
          │                                                                         ▼
Refactorizar & Explicar ◄── Realizar Pruebas Mínimas y de Error ◄── Ensamblar Vista Tkinter
```

### Preguntas obligatorias antes de programar:
1. ¿Qué problema operativo resolverá la aplicación y quién la utilizará?
2. ¿Qué información necesita visualizar y qué datos debe ingresar el usuario?
3. ¿Qué widgets de `tkinter` o `ttk` representan mejor esas acciones?
4. ¿Cómo debe distribuirse visualmente la información (`grid` vs `pack`)?
5. ¿Qué estado necesita mantener la aplicación y cómo evitar variables globales?
6. ¿Qué entradas deben validarse y qué puede salir mal?
7. ¿Qué pertenece a la interfaz gráfica y qué pertenece a la lógica de negocio pura?
8. ¿Cómo probar la lógica sin depender exclusivamente de hacer clic manualmente?

---

## 4. Registro de Aprendizaje Obligatorio

Al finalizar cada ejercicio, se recomienda completar la siguiente bitácora técnica de reflexión en su cuaderno o archivo personal:

| Sección | Descripción |
| :--- | :--- |
| **Qué construí** | Resumen funcional de la aplicación terminada. |
| **Qué problema resolví** | Valor práctico aportado al usuario final. |
| **Conceptos de Python aplicados** | Estructuras de datos, POO, módulos estándar utilizados. |
| **Conceptos de Tkinter aplicados** | Widgets, gestores de geometría, bindings, variables reactivas. |
| **Qué me costó más** | Desafíos técnicos encontrados durante el desarrollo. |
| **Qué errores cometí** | Bugs o fallos de diseño y cómo los corregí. |
| **Decisión de diseño tomada** | Justificación de la arquitectura o layout elegido. |
| **Qué componente podría reutilizar** | Clases o funciones exportables a futuros proyectos. |

---

## 5. Catálogo Completo de los 100 Ejercicios

| N° | Aplicación | Usuario Objetivo | Estrategia de Persistencia | Enlace |
| :--- | :--- | :--- | :--- | :--- |
| 001 | **Calculadora de Presupuesto Rápido de Viaje (`TravelBudgetApp`)** | Coordinador de operaciones o gestor de viajes corporativos. | No requiere persistencia en disco; op... | [001](ejercicio_001/README.md) |
| 002 | **Convertidor de Divisas y Unidades Métricas (`UnitConverterApp`)** | Técnico de laboratorio o asistente de compras internacionales. | No requiere almacenamiento persistent... | [002](ejercicio_002/README.md) |
| 003 | **Temporizador y Cronómetro de Presentaciones (`StageTimerApp`)** | Moderador de eventos técnicos o presentador en conferencias. | No requiere persistencia en disco. | [003](ejercicio_003/README.md) |
| 004 | **Generador Seguro de Contraseñas Corporativas (`PassGenApp`)** | Administrador de sistemas (SysAdmin) o técnico de soporte de identidades. | No persiste contraseñas en disco por ... | [004](ejercicio_004/README.md) |
| 005 | **Contador de Palabras y Densidad Léxica en Tiempo Real (`TextMetricsApp`)** | Redactor editorial, copywriter o analista de contenidos. | No requiere almacenamiento permanente... | [005](ejercicio_005/README.md) |
| 006 | **Bloc de Notas Rápido con Selector de Formato (`ScratchPadApp`)** | Operador de soporte técnico o analista de operaciones. | No requiere persistencia en disco | [006](ejercicio_006/README.md) |
| 007 | **Selector Interactivo de Paletas de Color RGB/HEX (`ColorPickerApp`)** | Diseñador de interfaces, maquetador web o desarrollador frontend. | No requiere persistencia en disco. | [007](ejercicio_007/README.md) |
| 008 | **Formulario de Registro Rápido de Visitantes (`VisitorCheckInApp`)** | Recepcionista o guardia de seguridad de control de accesos. | No requiere persistencia en archivo | [008](ejercicio_008/README.md) |
| 009 | **Tarjeta de Presentación Digital y Generador de Credenciales (`BadgePreviewApp`)** | Encargado de acreditaciones en eventos y convenciones. | No requiere persistencia en disco. | [009](ejercicio_009/README.md) |
| 010 | **Conversor de Formato y Limpiador de Texto (`TextSanitizerApp`)** | Analista de bases de datos o gestor de contenido de comercio electrónico. | No requiere persistencia en disco. | [010](ejercicio_010/README.md) |
| 011 | **Calculadora de Cuotas y Préstamos Amortizados (`LoanEstimatorApp`)** | Asesor financiero o ejecutivo de créditos. | No requiere persistencia en disco. | [011](ejercicio_011/README.md) |
| 012 | **Panel de Verificación de Requisitos de Hardware (`SysCheckUI`)** | Técnico de soporte de TI o instalador de software corporativo. | No requiere persistencia en disco. | [012](ejercicio_012/README.md) |
| 013 | **Formulario de Alta de Empleados y Ficha de Personal (`EmployeeOnboardingApp`)** | Analista de recursos humanos o asistente de contratación. | No requiere persistencia en disco en ... | [013](ejercicio_013/README.md) |
| 014 | **Cotizador de Seguros con Opciones Dinámicas (`InsuranceQuoteApp`)** | Agente de seguros o asesor comercial de pólizas. | No requiere persistencia en disco. | [014](ejercicio_014/README.md) |
| 015 | **Gestor de Solicitudes de Vacaciones Laborales (`VacationRequestApp`)** | Empleado solicitante o supervisor de área. | No requiere persistencia en disco. | [015](ejercicio_015/README.md) |
| 016 | **Registro de Incidentes de Soporte Nivel 1 (`HelpdeskIncidentApp`)** | Analista de mesa de ayuda (Service Desk Nivel 1). | No requiere persistencia en disco. | [016](ejercicio_016/README.md) |
| 017 | **Validador y Probador Local de Expresiones Regulares (`RegexTesterApp`)** | Desarrollador de software, analista de datos o auditor de seguridad. | No requiere persistencia en disco. | [017](ejercicio_017/README.md) |
| 018 | **Calculadora de Huella de Carbono y Consumo Energético (`CarbonFootprintApp`)** | Auditor ambiental, gestor de sostenibilidad o encargado de instalaciones. | No requiere persistencia en disco. | [018](ejercicio_018/README.md) |
| 019 | **Registro de Mantenimiento Preventivo de Maquinaria (`EquipmentMaintenanceApp`)** | Supervisor de mantenimiento o técnico mecánico de planta. | No requiere persistencia en disco en ... | [019](ejercicio_019/README.md) |
| 020 | **Solicitud de Reembolso de Gastos de Viaje (`ExpenseClaimApp`)** | Consultor o empleado que rinde gastos de viaje. | No requiere persistencia en disco. | [020](ejercicio_020/README.md) |
| 021 | **Formulario de Registro para Pruebas Clínicas (`ClinicalTrialFormApp`)** | Coordinador de investigación clínica o enfermero de protocolo. | No requiere persistencia en disco. | [021](ejercicio_021/README.md) |
| 022 | **Inspección y Control de Calidad de Lotes (`QualityInspectionApp`)** | Inspector de calidad o analista de aseguramiento de calidad (QA). | No requiere persistencia en disco. | [022](ejercicio_022/README.md) |
| 023 | **Generador de Encuestas de Clima Laboral (`SurveyFeedbackApp`)** | Colaborador de la empresa que responde la encuesta de clima. | No requiere persistencia en disco. | [023](ejercicio_023/README.md) |
| 024 | **Simulador de Tarifas de Envíos y Paquetería (`ShippingCalculatorApp`)** | Operador de mostrador de paquetería o asistente de logística. | No requiere persistencia en disco. | [024](ejercicio_024/README.md) |
| 025 | **Agenda Telefónica y Directorio Profesional (`ContactBookApp`)** | Secretario ejecutivo o recepcionista corporativo. | Persistencia en archivo de texto plan... | [025](ejercicio_025/README.md) |
| 026 | **Catálogo de Inventario en Bodega (`WarehouseInventoryApp`)** | Jefe de almacén o supervisor de inventarios. | Archivo CSV local | [026](ejercicio_026/README.md) |
| 027 | **Gestor de Tareas Pendientes con Prioridades (`TaskMasterApp`)** | Líder de proyecto o coordinador operativo. | Archivo JSON | [027](ejercicio_027/README.md) |
| 028 | **Visor y Buscador de Transacciones Financieras (`TransactionViewerApp`)** | Auditor contable o analista financiero. | Lectura desde archivo CSV | [028](ejercicio_028/README.md) |
| 029 | **Administrador de Estudiantes y Calificaciones (`GradeTrackerApp`)** | Docente, profesor titular o asistente académico. | Exportación a CSV | [029](ejercicio_029/README.md) |
| 030 | **Registro de Consumo de Medicamentos y Recetas (`MedicationLogApp`)** | Enfermero de turno o cuidador de atención domiciliaria. | Archivo JSON | [030](ejercicio_030/README.md) |
| 031 | **Catálogo de Biblioteca y Préstamo de Libros (`BookCatalogApp`)** | Bibliotecario o asistente de biblioteca. | Archivo JSON | [031](ejercicio_031/README.md) |
| 032 | **Visor y Analizador de Archivos de Log Web (`AccessLogViewerApp`)** | Administrador de sistemas (SysAdmin) o ingeniero de DevOps. | Lectura desde archivo de log local | [032](ejercicio_032/README.md) |
| 033 | **Registro de Activos de TI y Asignación de Equipos (`AssetTrackerApp`)** | Administrador de activos de TI o analista de compras. | Archivo CSV | [033](ejercicio_033/README.md) |
| 034 | **Gestor de Menús y Precios de Restaurante (`RestaurantMenuManagerApp`)** | Gerente de restaurante o chef ejecutivo. | Archivo JSON | [034](ejercicio_034/README.md) |
| 035 | **Monitor de Precios de Competidores (`PriceBenchmarkApp`)** | Analista de pricing o especialista comercial. | Lectura desde CSV | [035](ejercicio_035/README.md) |
| 036 | **Visor de Metadatos de Archivos en Directorio (`DirectoryMetadataViewerApp`)** | Administrador de sistemas o auditor de almacenamiento. | No requiere persistencia en disco; op... | [036](ejercicio_036/README.md) |
| 037 | **Editor de Texto Plano con Menús y Diálogos de Archivo (`MiniNotepadApp`)** | Desarrollador, administrador de sistemas o redactor técnico. | Lectura y escritura directa en archiv... | [037](ejercicio_037/README.md) |
| 038 | **Panel de Control Multi-Pestaña de Sucursal (`BranchDashboardApp`)** | Gerente de sucursal comercial o supervisor de tienda. | No requiere persistencia en disco en ... | [038](ejercicio_038/README.md) |
| 039 | **Gestor de Clientes con Ventana Modal de Edición (`CustomerDirectoryModalApp`)** | Ejecutivo de cuentas o asesor de servicio al cliente. | No requiere persistencia en disco en ... | [039](ejercicio_039/README.md) |
| 040 | **Sistema de Punto de Venta Simple con Selector de Productos (`SimplePosApp`)** | Cajero de tienda o dependiente de mostrador. | No requiere persistencia en disco en ... | [040](ejercicio_040/README.md) |
| 041 | **Asistente Guiado Paso a Paso (`OnboardingWizardApp`)** | Nuevo usuario corporativo o administrador de sistema. | No requiere persistencia en disco en ... | [041](ejercicio_041/README.md) |
| 042 | **Gestor de Preferencias y Configuración de Aplicación (`SettingsManagerApp`)** | Usuario final o administrador de la aplicación. | Archivo JSON | [042](ejercicio_042/README.md) |
| 043 | **Visor de Reportes con Ventana Secundaria de Previsualización (`ReportPreviewerApp`)** | Analista contable o asistente administrativo. | Exportación a archivo TXT en disco | [043](ejercicio_043/README.md) |
| 044 | **Agenda de Citas Médicas con Selector Modal de Horarios (`ClinicAppointmentApp`)** | Recepcionista de clínica médica o asistente dental. | No requiere persistencia en disco en ... | [044](ejercicio_044/README.md) |
| 045 | **Administrador de Evaluaciones y Preguntas (`QuizAuthoringApp`)** | Diseñador instruccional, profesor o capacitador corporativo. | Archivo JSON | [045](ejercicio_045/README.md) |
| 046 | **Gestor de Proyectos con Ventana de Detalles de Tarea (`ProjectWorkspaceApp`)** | Director de proyectos (Project Manager) o consultor líder. | No requiere persistencia en disco en ... | [046](ejercicio_046/README.md) |
| 047 | **Explorador de Esquema de Datos y Diccionario de Campos (`DataDictionaryApp`)** | Arquitecto de datos, administrador de bases de datos (DBA) o analista de BI. | Lectura desde JSON | [047](ejercicio_047/README.md) |
| 048 | **Consola de Diagnóstico de Red Local con Historial (`NetworkPingToolApp`)** | Técnico de soporte de redes o administrador de sistemas. | Exportación opcional a archivo de tex... | [048](ejercicio_048/README.md) |
| 049 | **Gestor CRUD de Alumnos y Matrícula Universitaria (`StudentEnrollmentSqliteApp`)** | Secretario académico o coordinador de registro escolar. | Base de datos relacional SQLite local | [049](ejercicio_049/README.md) |
| 050 | **Control de Cuentas por Cobrar y Facturas Pendientes (`InvoicingSqliteApp`)** | Analista de cobranza o contador de cuentas por cobrar. | Base de datos relacional SQLite | [050](ejercicio_050/README.md) |
| 051 | **Sistema de Registro de Horas de Trabajo (`TimesheetTrackerApp`)** | Consultor de proyectos o analista de control de gestión. | Base de datos relacional SQLite | [051](ejercicio_051/README.md) |
| 052 | **Administración de Socios y Cuotas de Club Deportivo (`ClubMembershipSqliteApp`)** | Administrador de recepción o coordinador de membresías. | Base de datos relacional SQLite | [052](ejercicio_052/README.md) |
| 053 | **Control de Mermas y Desperdicios en Línea de Producción (`WasteTrackingApp`)** | Supervisor de producción o analista de calidad de planta. | Base de datos SQLite local | [053](ejercicio_053/README.md) |
| 054 | **Catálogo de Proveedores y Evaluación de Desempeño (`VendorEvaluationApp`)** | Comprador corporativo o analista de abastecimiento. | Base de datos relacional SQLite | [054](ejercicio_054/README.md) |
| 055 | **Sistema de Préstamo de Herramientas de Taller Mecánico (`ToolCribSqliteApp`)** | Encargado de pañol de herramientas o supervisor de taller. | Base de datos relacional SQLite | [055](ejercicio_055/README.md) |
| 056 | **Gestor de Órdenes de Trabajo para Servicios Técnicos (`ServiceWorkOrdersApp`)** | Técnico de reparación o recepcionista de taller. | Base de datos relacional SQLite | [056](ejercicio_056/README.md) |
| 057 | **Control de Gastos Personales y Presupuestos Mensuales (`BudgetExpenseSqliteApp`)** | Usuario particular o profesional independiente. | Base de datos relacional SQLite | [057](ejercicio_057/README.md) |
| 058 | **Registro de Donaciones y Padrinos en ONG (`DonationsTrackerApp`)** | Coordinador de procuración de fondos o asistente administrativo de la ONG. | Base de datos relacional SQLite | [058](ejercicio_058/README.md) |
| 059 | **Directorio de Propiedades Inmobiliarias (`RealEstateListingApp`)** | Agente inmobiliario o asesor de bienes raíces. | Base de datos relacional SQLite | [059](ejercicio_059/README.md) |
| 060 | **Gestor de Suscripciones y Pagos Periódicos (`SubscriptionVaultApp`)** | Administrador financiero o encargado de operaciones. | Base de datos relacional SQLite | [060](ejercicio_060/README.md) |
| 061 | **Monitor de Disponibilidad de Servidores e URLs (`UrlUptimeMonitorApp`)** | Analista de NOC o ingeniero de confiabilidad del sitio (SRE). | No requiere persistencia en disco en ... | [061](ejercicio_061/README.md) |
| 062 | **Procesador Masivo de Renombrado de Archivos por Lotes (`BatchFileRenamerApp`)** | Archivista digital o fotógrafo profesional. | Modificación directa en el sistema de... | [062](ejercicio_062/README.md) |
| 063 | **Analizador de Archivos CSV Masivos con Cálculos Estadísticos (`CsvCruncherApp`)** | Analista de datos o especialista en inteligencia de negocios. | No requiere persistencia en disco | [063](ejercicio_063/README.md) |
| 064 | **Generador de Reportes Ejecutivos en Archivos Planos (`AsyncReportBuilderApp`)** | Asistente de dirección o analista financiero. | Exportación del informe final a archi... | [064](ejercicio_064/README.md) |
| 065 | **Buscador Rápido de Texto dentro de Archivos (`DesktopFileGrepApp`)** | Desarrollador de software, auditor forense o analista de seguridad. | No requiere persistencia en disco | [065](ejercicio_065/README.md) |
| 066 | **Simulador de Descarga y Sincronización de Recursos (`SyncDownloaderApp`)** | Usuario final de software corporativo o jugador de plataforma de entretenimiento. | No requiere persistencia en disco. | [066](ejercicio_066/README.md) |
| 067 | **Verificador Masivo de Hashes Criptográficos en Disco (`BulkHashVerifierApp`)** | Perito en informática forense o auditor de ciberseguridad. | Exportación del informe de integridad... | [067](ejercicio_067/README.md) |
| 068 | **Exportador Masivo de Base de Datos a Múltiples Formatos (`DbDataExporterApp`)** | Administrador de bases de datos (DBA) o desarrollador backend. | Generación de archivos CSV o JSON en ... | [068](ejercicio_068/README.md) |
| 069 | **Limpiador de Duplicados en Carpetas con Cancelación (`DuplicateCleanerApp`)** | Administrador de sistemas o gestor de almacenamiento. | Eliminación directa de archivos redun... | [069](ejercicio_069/README.md) |
| 070 | **Simulador de Sensor IoT y Adquisición Continua de Datos (`IotTelemetrySimulatorApp`)** | Operador de planta o ingeniero de automatización y control. | No requiere persistencia en disco en ... | [070](ejercicio_070/README.md) |
| 071 | **Convertidor Masivo de Codificación de Archivos (ANSI a UTF-8) (`EncodingConverterApp`)** | Desarrollador de software o ingeniero de migración de datos. | Modificación y sobreescritura de arch... | [071](ejercicio_071/README.md) |
| 072 | **Revisor de Calidad de Código y Conteo de Líneas (`CodebaseMetricsApp`)** | Líder técnico, arquitecto de software o evaluador de calidad de código. | Exportación del informe consolidado a... | [072](ejercicio_072/README.md) |
| 073 | **Generador Interactivo de Diagramas de Flujo y Nodos (`NodeGraphEditorApp`)** | Ingeniero de procesos, diseñador de flujos o analista de automatización. | No requiere persistencia en disco en ... | [073](ejercicio_073/README.md) |
| 074 | **Monitor de Temperatura y Termómetro Visual Interactivo (`VisualThermometerApp`)** | Operador de cámara frigorífica o supervisor de cadena de frío. | No requiere persistencia en disco. | [074](ejercicio_074/README.md) |
| 075 | **Diseñador de Croquis y Distribución de Mesas para Eventos (`FloorPlanDesignerApp`)** | Coordinador de eventos o maître de sala de banquetes. | Archivo JSON | [075](ejercicio_075/README.md) |
| 076 | **Visor de Métricas con Gráfico de Barras Nativo en Canvas (`CanvasBarChartApp`)** | Analista de negocios o desarrollador de tableros ejecutivos. | No requiere persistencia en disco en ... | [076](ejercicio_076/README.md) |
| 077 | **Tablero de Dibujo y Firma Digital de Conformidad (`SignaturePadApp`)** | Receptor de mercancía, cliente de entrega o auditor de almacén. | Archivo JSON | [077](ejercicio_077/README.md) |
| 078 | **Visualizador de Ondas de Señal o Pulso Cardíaco (`SignalWaveViewerApp`)** | Técnico de biomédica o laboratorista de instrumentación electrónica. | No requiere persistencia en disco. | [078](ejercicio_078/README.md) |
| 079 | **Visor de Tarjetas Kanban con Columnas Arrastrables o Interactivas (`MiniKanbanBoardApp`)** | Scrum Master, líder técnico o coordinador de operaciones. | Archivo JSON | [079](ejercicio_079/README.md) |
| 080 | **Editor y Marcador Visual de Zonas en Planos (`ImageRegionMarkerApp`)** | Inspector de calidad o auditor de seguridad industrial. | Archivo JSON | [080](ejercicio_080/README.md) |
| 081 | **Diseñador y Previsualizador de Credenciales con Código de Barras Falso (`IdCardVisualizerApp`)** | Encargado de credencialización o técnico de seguridad patrimonial. | No requiere persistencia en disco en ... | [081](ejercicio_081/README.md) |
| 082 | **Selector de Asientos de Cine o Teatro con Estados de Color (`SeatBookingCanvasApp`)** | Cajero de taquilla o espectador en kiosco de autoservicio. | No requiere persistencia en disco en ... | [082](ejercicio_082/README.md) |
| 083 | **Indicador de Nivel de Tanques de Combustible y Alarma (`TankLevelGaugeApp`)** | Operador de planta de combustibles o supervisor de seguridad de tanques. | No requiere persistencia en disco. | [083](ejercicio_083/README.md) |
| 084 | **Generador de Gráficos Circulares (Pastel/Torta) en Canvas (`PieChartRendererApp`)** | Analista financiero o gestor de presupuestos. | No requiere persistencia en disco. | [084](ejercicio_084/README.md) |
| 085 | **Refactorización de Monolito: Sistema de Facturación a Tres Capas (`RefactorBillingApp`)** | Arquitecto de software o desarrollador senior de refactorización. | No requiere persistencia en disco en ... | [085](ejercicio_085/README.md) |
| 086 | **Gestor de Inventario con Pruebas Unitarias de Lógica de Negocio (`TestableInventoryApp`)** | Desarrollador de software o ingeniero de aseguramiento de calidad (QA Automation). | No requiere persistencia en disco en ... | [086](ejercicio_086/README.md) |
| 087 | **Sistema de Autenticación Local con Bitácora Técnica (`SecureAuthAuditApp`)** | Operador de sistema o auditor de seguridad informática. | Archivo de bitácora técnica rotativo | [087](ejercicio_087/README.md) |
| 088 | **Consola de Gestión con Manejador Global de Excepciones (`CrashSafeManagerApp`)** | Operador de sistema corporativo y equipo de soporte técnico de nivel 3. | Archivo de bitácora de fallos | [088](ejercicio_088/README.md) |
| 089 | **Aplicación con Motor de Temas Dinámicos y Soporte Claro/Oscuro (`ThemeEngineApp`)** | Operador de turno diurno/nocturno o usuario corporativo. | Archivo JSON | [089](ejercicio_089/README.md) |
| 090 | **Gestor de Tareas con Historial de Acciones y Deshacer (`UndoRedoTaskApp`)** | Planificador de tareas o usuario corporativo de gestión. | No requiere persistencia en disco en ... | [090](ejercicio_090/README.md) |
| 091 | **Validador de Datos Empresariales con Pipeline de Reglas (`EnterpriseDataValidatorApp`)** | Analista de integración de datos o ingeniero de aseguramiento de calidad de datos. | No requiere persistencia en disco en ... | [091](ejercicio_091/README.md) |
| 092 | **Formulario Accesible por Teclado con Atajos y Navegación Universal (`AccessibleFormApp`)** | Operador de datos con discapacidad visual/motriz o digitador intensivo de alta velocidad. | No requiere persistencia en disco en ... | [092](ejercicio_092/README.md) |
| 093 | **Aplicación Empaquetable con PyInstaller y Gestión de Recursos (`DistributableToolApp`)** | Ingeniero de release de software o desarrollador de aplicaciones de escritorio. | Base de datos SQLite local persistida... | [093](ejercicio_093/README.md) |
| 094 | **Monitor de Procesos y Uso de Recursos del Sistema (`ProcessMonitorSysApp`)** | Administrador de sistemas (SysAdmin) o ingeniero de soporte de infraestructura. | No requiere persistencia en disco. | [094](ejercicio_094/README.md) |
| 095 | **Centro de Despachos y Enrutamiento Logístico (`DispatchHubApp`)** | Coordinador de despachos o despachador de flota logística. | Estrategia de persistencia elegida y ... | [095](ejercicio_095/README.md) |
| 096 | **Sistema Integral de Gestión de Clínica Veterinaria (`VetCareClinicApp`)** | Médico veterinario o recepcionista de clínica de animales. | Base de datos relacional SQLite diseñ... | [096](ejercicio_096/README.md) |
| 097 | **Terminal de Punto de Venta para Cafetería con Control de Caja (`CoffeeShopPosApp`)** | Barista, cajero de cafetería o encargado de turno. | Base de datos relacional SQLite con t... | [097](ejercicio_097/README.md) |
| 098 | **Mesa de Ayuda y Ticketing Corporativo con Niveles de SLA (`CorporateHelpdeskSlaApp`)** | Analista de soporte de TI, despachador de tickets o gerente de servicio. | Base de datos relacional SQLite | [098](ejercicio_098/README.md) |
| 099 | **Gestor Integral de Alquiler de Vehículos y Flota (`FleetRentalManagerApp`)** | Agente de mostrador de alquiler de autos o gerente de flota. | Base de datos relacional SQLite | [099](ejercicio_099/README.md) |
| 100 | **Suite Empresarial de Control de Proyectos y Presupuestos de Obras (`MasterProjectSuiteApp`)** | Director de obras, gerente de proyectos de ingeniería o director general de operaciones. | Base de datos relacional SQLite | [100](ejercicio_100/README.md) |

---

## 6. Configuración del Entorno de Desarrollo

Se requiere **Python 3.10 o superior** (Python 3.11+ recomendado). Tkinter forma parte de la biblioteca estándar en Windows y macOS. En sistemas Linux basados en Debian/Ubuntu o Arch Linux, asegúrese de contar con el paquete del sistema:

```bash
# En Ubuntu / Debian / Kali Linux:
sudo apt update && sudo apt install python3-tk

# En Arch Linux / CachyOS / Manjaro:
sudo pacman -S tk

# Comprobación de instalación de Tkinter:
python -m tkinter
```

---

## 7. Filosofía Final de Evaluación

Nunca evalúes tu progreso preguntando únicamente: *'¿La ventana abre?'*

Evalúa con rigor técnico:
- **¿La aplicación resuelve el problema del usuario de forma intuitiva?**
- **¿La interfaz permanece reactiva sin congelarse ante operaciones pesadas?**
- **¿Todas las entradas se validan rigurosamente antes de procesarse?**
- **¿Los errores se comunican al usuario con claridad y profesionalismo?**
- **¿La lógica de negocio está totalmente desacoplada de la interfaz gráfica?**
- **¿La base de datos maneja transacciones seguras contra inyecciones y corrupción?**
- **¿Eres capaz de explicar y defender cada una de tus decisiones de arquitectura?**

*El objetivo de este programa no es construir 100 ventanas de juguete. El objetivo es completar 100 experiencias de ingeniería de software de escritorio con Python y Tkinter.*
