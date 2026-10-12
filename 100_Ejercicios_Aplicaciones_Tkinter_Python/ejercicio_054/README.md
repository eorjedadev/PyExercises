## Ejercicio 054 — Catálogo de Proveedores y Evaluación de Desempeño (`VendorEvaluationApp`)

> [Índice General](../README.md) · [← Ejercicio 053](../ejercicio_053/README.md) · [Ejercicio 055 →](../ejercicio_055/README.md)

### Contexto profesional
En departamentos de compras y abastecimiento corporativo, los compradores gestionan el padrón de proveedores y registran evaluaciones de calidad y cumplimiento de entregas.

### Usuario objetivo
Comprador corporativo o analista de abastecimiento.

### Problema
La falta de un historial de desempeño de proveedores conduce a recontratar empresas con retrasos crónicos o altos índices de devolución.

### Objetivo
Desarrollar una aplicación de gestión y evaluación de proveedores en SQLite (`proveedores.db`), con catálogo de empresas, registro de evaluaciones (Calidad de Producto, Cumplimiento de Plazos, Precios) en escala de 1 a 10, y cálculo del índice de confiabilidad general con consultas SQL parametrizadas.

### Flujo principal
El comprador busca un proveedor en el directorio. La tabla muestra la información de la empresa y su calificación promedio de desempeño. Al seleccionar un proveedor, presiona 'Evaluar Desempeño'. En una ventana o panel registra las tres notas (1 a 10) de la última entrega. El sistema calcula el nuevo promedio ponderado, actualiza el estatus (Confiable, Condicional, Bloqueado) y lo guarda en SQLite.

### Requisitos funcionales
- Esquema SQLite con tablas `proveedores` y `evaluaciones_proveedor`.
- Campos en proveedor: ID, Razón Social, RFC/NIT, Contacto, Teléfono, Correo, Calificación Promedio, Estatus (`Confiable`, `Condicional`, `Bloqueado`).
- Registro de nueva evaluación: Puntuación de Calidad (1-10), Cumplimiento de Plazo (1-10), Nivel de Precios (1-10) y Comentarios.
- Cálculo del score global: $(Q \times 0.4) + (P \times 0.4) + (C \times 0.2)$.
- Clasificación automática del proveedor: Score >= 8.0: Confiable (verde); 6.0 a 7.9: Condicional (amarillo); < 6.0: Bloqueado (rojo).
- Búsqueda por nombre de proveedor o identificación fiscal mediante consultas seguras.

### Requisitos de interfaz
- Panel con tabla de proveedores a la izquierda.
- Panel con ficha de desempeño y formulario de evaluación a la derecha.
- Tags de colores según el estatus de confiabilidad del proveedor.

### Datos
- Proveedor: id, nombre, rfc, contacto, telefono, correo, score_promedio, estatus.
- Evaluación: id, proveedor_id, fecha, calidad, plazo, precio, score, comentarios.

### Estado
- Proveedor actualmente seleccionado.
- Lista de proveedores consultados.

### Persistencia
Base de datos relacional SQLite (`datos/proveedores.db`).

### Validaciones
- Las calificaciones deben ser flotantes o enteros entre 1.0 y 10.0.
- Nombre de proveedor obligatorio y único.

### Casos límite
- Proveedor nuevo sin ninguna evaluación previa registrada (score inicial 'S/E' o 0.0).
- Evaluaciones con decimales (ej. 8.5).

### Manejo de errores
- Emplear exclusivamente consultas parametrizadas con `?` para prevenir inyección SQL al buscar por texto libre.

### Fundamentos de Python relacionados
- Promedios ponderados y normalización de puntuaciones.
- Consultas SQL parametrizadas con `LIKE ?` para búsquedas seguras.

### Conceptos Tkinter relacionados
- Coordinación entre tabla principal y panel de detalle de evaluaciones.
- Estilos de texto y etiquetas cromáticas dinámicas.

### Herramientas para investigar
- Consultas SQL con `LIKE` parametrizado (`SELECT ... WHERE nombre LIKE ?`).
- Modelos de evaluación de proveedores en cadenas de suministro (Vendor Rating).

### Diseño de interfaz
¿Cómo diseñarías el panel derecho para que el comprador visualice con claridad el desglose de calidad, plazo y precio antes de emitir una orden de compra?

### Diseño de variables
Usa nombres como `vendor_tree`, `search_vendor_entry`, `quality_score_scale`, `delivery_score_scale`, `price_score_scale`, `vendor_score_label`, `db_vendor`.

### Antes de programar
1. ¿Cómo se pasa un parámetro con comodines `%` a una consulta SQLite parametrizada de forma segura?
2. ¿Cómo se actualiza el campo de calificación promedio en la tabla del proveedor tras insertar una nueva evaluación?

### Arquitectura
```
ejercicio_054/
├── app.py             # Directorio de proveedores y formulario de evaluación
├── vendor_repo.py     # Consultas parametrizadas a SQLite
└── datos/
    └── proveedores.db # Base de datos relacional de proveedores
```

### Pruebas mínimas
1. Registrar evaluación de 10 en Calidad, 10 en Plazo y 10 en Precio -> Score debe ser 10.0 y estatus 'Confiable' en verde.
2. Buscar por texto 'aceros' -> Comprobar que liste proveedores cuyos nombres coincidan de forma segura.

### Pruebas de error
1. Ingresar calificación de 12 en Calidad -> Debe advertir que las notas deben estar entre 1 y 10.

### Experiencia de usuario
Al seleccionar un proveedor de la tabla, su historial reciente de notas y comentarios debe cargarse al instante en el panel lateral.

### Explicación posterior
¿Por qué es obligatorio utilizar marcadores de posición `?` incluso al realizar búsquedas con comodines `LIKE %...%` en SQL?

### Aplicación profesional
Sistemas de compras corporativas (e-procurement), gestión de cadena de suministro (SCM) y auditorías de calidad ISO 9001.

### Reto adicional
Añade un botón 'Exportar Ficha de Proveedor' que genere un informe en archivo de texto con el histórico completo de evaluaciones del proveedor seleccionado.

---
> [Índice General](../README.md) · [← Ejercicio 053](../ejercicio_053/README.md) · [Ejercicio 055 →](../ejercicio_055/README.md)
