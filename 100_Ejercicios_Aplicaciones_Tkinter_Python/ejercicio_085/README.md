## Ejercicio 085 — Refactorización de Monolito: Sistema de Facturación a Tres Capas (`RefactorBillingApp`)

> [Índice General](../README.md) · [← Ejercicio 084](../ejercicio_084/README.md) · [Ejercicio 086 →](../ejercicio_086/README.md)

### Contexto profesional
En proyectos de mantenimiento de software legado, los ingenieros reciben aplicaciones antiguas escritas en un solo archivo gigantesco donde la interfaz gráfica, las consultas SQL y las reglas matemáticas están mezcladas en un caos difícil de mantener.

### Usuario objetivo
Arquitecto de software o desarrollador senior de refactorización.

### Problema
Un archivo de código monolítico de 1,200 líneas con variables globales y sentencias SQL incrustadas directamente dentro de los callbacks de los botones es imposible de probar con pruebas unitarias y cualquier cambio en la interfaz rompe la lógica contable.

### Objetivo
Tomar una aplicación monolítica legacy de facturación y refactorizarla integralmente en una arquitectura limpia y profesional desacoplada en tres capas (`ui/`, `services/`, `models/`), eliminando todas las variables globales, separando las reglas fiscales y garantizando que la lógica de cálculo pueda ejecutarse y probarse sin levantar ventanas de Tkinter.

### Flujo principal
El estudiante recibe el diagnóstico del código monolítico original. Identifica los vicios de diseño (Code Smells). Rediseña la estructura en paquetes: extrae las entidades de negocio a `models/`, encapsula los cálculos fiscales (subtotales, retenciones, IVA, descuentos) en `services/`, y reescribe la interfaz gráfica en `ui/` como una capa consumidora delgada que solo delega eventos y muestra resultados.

### Requisitos funcionales
- Análisis e identificación formal de al menos 4 'code smells' en la versión previa.
- Desacoplamiento total: separación en paquetes `models/`, `services/` y `ui/`.
- Capa de Modelos: Clases de datos (`dataclass`) para `Cliente`, `ConceptoFactura` y `Factura`.
- Capa de Servicios: `BillingService` con funciones puras para cálculo de subtotales, tasa de IVA (16%), retención de ISR/IVA y descuentos comerciales.
- Capa de Interfaz (Tkinter): Ventanas y formularios que interactúan con el servicio a través de métodos limpios sin conocer detalles matemáticos ni base de datos.
- Ausencia absoluta de variables globales (`global`) en toda la base de código.

### Requisitos de interfaz
- Interfaz moderna, limpia y modular construida a partir de componentes encapsulados.
- Formulario de captura de líneas de factura y tabla `ttk.Treeview` con el desglose.
- Panel lateral con los totales calculados por la capa de servicios.

### Datos
- Modelos de datos desacoplados: dataclasses independientes de Tkinter.

### Estado
- Estado de la factura gestionado enteramente dentro del objeto `Factura` en el servicio.

### Persistencia
No requiere persistencia en disco en esta fase (enfoque en arquitectura en memoria).

### Validaciones
- Validaciones de negocio encapsuladas dentro de la capa de servicios (no en los widgets).
- Precios, cantidades y tasas positivas.

### Casos límite
- Intentar calcular factura con 0 conceptos (el servicio debe retornar totales en cero de forma limpia).
- Descuentos comerciales superiores al subtotal.

### Manejo de errores
- La capa de servicios debe lanzar excepciones de negocio personalizadas (`BillingValidationError`) que la interfaz capture y muestre amigablemente.

### Fundamentos de Python relacionados
- Arquitectura en capas y patrones de diseño en Python.
- Clases de datos con `@dataclass` del módulo estándar `dataclasses`.
- Creación de excepciones personalizadas heredando de `Exception`.

### Conceptos Tkinter relacionados
- La interfaz gráfica como cliente consumidor pasivo del servicio de negocio.
- Eliminación de acoplamiento entre eventos de GUI y modelos de datos.

### Herramientas para investigar
- Módulo `dataclasses` de Python.
- Principios SOLID (especialmente Responsabilidad Única e Inversión de Dependencias).

### Diseño de interfaz
¿Cómo diseñarías la interfaz para que ningún widget tenga conocimiento de cómo se calcula el IVA o las retenciones fiscales?

### Diseño de variables
Usa nombres como `billing_service`, `current_invoice_model`, `invoice_view_frame`, `tax_calculation_result`, `items_tree`.

### Antes de programar
1. ¿Qué es un 'Code Smell' y por qué tener sentencias SQL y fórmulas fiscales dentro de una función de botón `def on_click():` destruye la mantenibilidad del software?
2. ¿Cómo se diseñan las clases de modelo para que puedan utilizarse en un script de consola sin importar Tkinter?

### Arquitectura
```
ejercicio_085/
├── main.py                  # Punto de entrada de la aplicación
├── models/
│   ├── __init__.py
│   └── invoice_models.py    # Dataclasses de Factura, Cliente e Ítems
├── services/
│   ├── __init__.py
│   └── billing_service.py   # Reglas fiscales puras y cálculos matemáticos
└── ui/
    ├── __init__.py
    ├── main_window.py       # Ventana principal de facturación
    └── components/          # Widgets reutilizables de formulario y tabla
```

### Pruebas mínimas
1. Ejecutar el servicio de cálculo desde un script de prueba independiente sin abrir ventanas -> Debe calcular subtotales e impuestos con precisión.
2. Abrir la interfaz gráfica -> Añadir conceptos y verificar que muestre exactamente los mismos resultados.

### Pruebas de error
1. Ingresar cantidad negativa en un ítem -> El servicio debe lanzar `BillingValidationError` y la GUI debe capturarla mostrando un diálogo amigable.

### Experiencia de usuario
La refactorización debe preservar la funcionalidad para el usuario final pero dejar una base de código limpia, modular y fácil de ampliar.

### Explicación posterior
¿Por qué la separación estricta en tres capas permite probar la lógica de cálculo sin necesidad de interactuar manualmente con la interfaz gráfica?

### Aplicación profesional
Modernización de sistemas empresariales legacy, preparación de bases de código para auditorías de arquitectura y escalamiento de software.

### Reto adicional
Añade un método en el servicio de facturación que soporte la adición de una tasa de retención especial sin requerir modificar ni una sola línea de la interfaz gráfica.

---
> [Índice General](../README.md) · [← Ejercicio 084](../ejercicio_084/README.md) · [Ejercicio 086 →](../ejercicio_086/README.md)
