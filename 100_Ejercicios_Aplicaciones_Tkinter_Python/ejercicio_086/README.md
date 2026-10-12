## Ejercicio 086 — Gestor de Inventario con Pruebas Unitarias de Lógica de Negocio (`TestableInventoryApp`)

> [Índice General](../README.md) · [← Ejercicio 085](../ejercicio_085/README.md) · [Ejercicio 087 →](../ejercicio_087/README.md)

### Contexto profesional
En empresas que aplican metodologías de desarrollo guiado por pruebas (TDD) e integración continua (CI), los desarrolladores deben garantizar que toda la lógica crítica de inventario y descuentos esté cubierta por pruebas automatizadas sin depender de la GUI.

### Usuario objetivo
Desarrollador de software o ingeniero de aseguramiento de calidad (QA Automation).

### Problema
Si las reglas de negocio de stock, precios y descuentos están atrapadas dentro de los widgets de Tkinter, resulta imposible escribir pruebas automatizadas con `unittest` o `pytest` en pipelines de integración continua sin un servidor gráfico.

### Objetivo
Desarrollar un sistema de gestión de inventario donde el 100% de la lógica de negocio (validación de SKU, cálculo de descuentos por volumen, actualización de existencias y reglas de reabastecimiento) resida en una clase de servicio pura `InventoryService`, acompañada de una suite completa de pruebas unitarias automatizadas con `unittest` que se ejecuten en consola.

### Flujo principal
El desarrollador diseña primero las pruebas unitarias para las reglas de inventario: regla de descuento por volumen (10% si cantidad >= 10, 20% si >= 50), validación de SKU (`PROD-XXXX`), y prevención de stock negativo. Implementa la clase `InventoryService`. Ejecuta las pruebas en consola con `python -m unittest` pasando todas las pruebas en verde. Finalmente, monta la interfaz de Tkinter conectada al servicio probado.

### Requisitos funcionales
- Clase pura `InventoryService` totalmente independiente de Tkinter.
- Métodos de negocio: `agregar_producto(sku, nombre, precio, stock)`, `registrar_venta(sku, cantidad)`, `calcular_descuento(sku, cantidad)`, `obtener_productos_bajo_stock(umbral)`.
- Regla de descuentos: 0% si cantidad < 10; 10% si cantidad entre 10 y 49; 20% si cantidad >= 50.
- Suite de pruebas automatizadas con el módulo estándar `unittest` (`test_inventory_service.py`) con al menos 8 casos de prueba exhaustivos.
- Interfaz gráfica con `ttk.Treeview` que consuma los métodos del servicio probado sin duplicar lógica.
- Ejecución exitosa de la suite de pruebas desde la terminal con código de salida 0.

### Requisitos de interfaz
- Ventana gráfica ordenada con tabla de productos y panel de registro de ventas.
- Indicador de stock disponible y desglose del descuento aplicado.
- Ausencia total de cálculos matemáticos dentro de los callbacks de los botones.

### Datos
- Producto: sku, nombre, precio, stock.
- Venta: sku, cantidad, precio_unitario, porcentaje_descuento, total_a_pagar.

### Estado
- Catálogo de inventario en memoria dentro de la instancia de `InventoryService`.

### Persistencia
No requiere persistencia en disco en esta fase (enfoque en testing de lógica).

### Validaciones
- SKU debe cumplir el patrón exacto `PROD-\d{4}`.
- No permitir ventas que superen el stock disponible (lanzar `InsufficientStockError`).
- Cantidad vendida debe ser entero mayor a cero.

### Casos límite
- Comprar exactamente 10 unidades (frontera del descuento del 10%).
- Comprar exactamente la cantidad total del stock disponible (el stock restante debe quedar en 0 exacto).
- Intentar vender un SKU inexistente.

### Manejo de errores
- La capa de servicio lanza excepciones semánticas (`InsufficientStockError`, `ProductNotFoundError`) que la GUI captura y traduce a mensajes de advertencia.

### Fundamentos de Python relacionados
- Módulo estándar `unittest` (`TestCase`, `assertEqual`, `assertRaises`, `setUp`).
- Principios de diseño para testabilidad (Design for Testability).
- Excepciones personalizadas orientadas al dominio.

### Conceptos Tkinter relacionados
- La GUI como capa delgada de presentación que solo delega al servicio.
- Cómo conectar una interfaz gráfica a un servicio probado previamente de forma segura.

### Herramientas para investigar
- Módulo `unittest` de la biblioteca estándar de Python.
- Métodos de aserción: `assertEqual`, `assertRaises`, `assertTrue`.

### Diseño de interfaz
¿Cómo estructurarías la ventana para que al ingresar una cantidad a vender, el descuento calculado por el servicio se muestre de inmediato en pantalla?

### Diseño de variables
Usa nombres como `inv_service`, `product_tree`, `sale_sku_entry`, `sale_qty_entry`, `discount_display_label`, `register_sale_btn`.

### Antes de programar
1. ¿Por qué es fundamental ejecutar `python -m unittest` en terminal antes de construir la interfaz gráfica de usuario?
2. ¿Cómo se utiliza `self.assertRaises(InsufficientStockError)` en `unittest` para verificar que el servicio rechace ventas sin stock?

### Arquitectura
```
ejercicio_086/
├── app.py                     # Interfaz gráfica Tkinter (capa delgada)
├── inventory_service.py       # Lógica pura de negocio y reglas de stock
├── exceptions.py              # Excepciones de dominio personalizadas
└── tests/
    ├── __init__.py
    └── test_inventory.py      # Suite de pruebas unitarias automatizadas con unittest
```

### Pruebas mínimas
1. Ejecutar en terminal: `python -m unittest tests/test_inventory.py` -> Todas las pruebas unitarias deben pasar con `OK`.
2. Abrir `app.py` -> Registrar una venta de 15 unidades de un producto con stock 20 -> Comprobar que aplique el 10% de descuento y reduzca el stock a 5.

### Pruebas de error
1. Ejecutar prueba unitaria intentando vender 25 unidades cuando el stock es 20 -> Debe lanzar y verificar `InsufficientStockError`.

### Experiencia de usuario
La interfaz debe ser reactiva y confiable, respaldada por la garantía de una lógica de negocio previamente validada por pruebas automáticas.

### Explicación posterior
¿Cómo demuestra este ejercicio que desacoplar la lógica de Tkinter permite verificar la robustez de un sistema en entornos automatizados sin interfaz gráfica?

### Aplicación profesional
Desarrollo de módulos comerciales empresariales, preparación de software para pipelines de CI/CD (GitHub Actions) y sistemas de misión crítica.

### Reto adicional
Añade una prueba unitaria adicional que valide el cálculo de reorden automático cuando el stock cae por debajo del umbral mínimo.

---
> [Índice General](../README.md) · [← Ejercicio 085](../ejercicio_085/README.md) · [Ejercicio 087 →](../ejercicio_087/README.md)
