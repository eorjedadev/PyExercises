## Ejercicio 040 — Sistema de Punto de Venta Simple con Selector de Productos (`SimplePosApp`)

> [Índice General](../README.md) · [← Ejercicio 039](../ejercicio_039/README.md) · [Ejercicio 041 →](../ejercicio_041/README.md)

### Contexto profesional
En tiendas de conveniencia y mostradores de venta minorista, los cajeros registran las compras de los clientes agregando productos a una orden de venta con cálculo de impuestos y vuelto.

### Usuario objetivo
Cajero de tienda o dependiente de mostrador.

### Problema
La lentitud al buscar productos por código y los errores en el cálculo manual del cambio generan filas de clientes molestos en caja.

### Objetivo
Construir una aplicación de punto de venta (POS) de dos paneles con tabla de orden actual, diálogo modal de búsqueda rápida de catálogo de productos, cálculo automático de subtotal, IVA (16%), total y cálculo del cambio a entregar según el monto recibido en efectivo.

### Flujo principal
El cajero presiona 'Buscar Producto' (`F2`). Se abre un selector modal con el catálogo de artículos. Selecciona uno, define cantidad y se agrega a la orden actual. En la ventana principal visualiza el desglose financiero. Ingresa el dinero entregado por el cliente en efectivo y la aplicación calcula al instante el cambio a devolver.

### Requisitos funcionales
- Catálogo en memoria con 10 productos de prueba (Código, Nombre, Precio Unitario, Stock).
- Tabla principal de la orden de venta: Código, Descripción, Cantidad, Precio Unitario, Importe.
- Diálogo secundario de selección rápida de productos con buscador incremental.
- Cálculo automático continuo: Subtotal, IVA desglosado (16%) y Total a pagar.
- Campo de 'Efectivo Recibido' con cálculo inmediato del cambio a devolver.
- Botón 'Cobrar y Finalizar Venta' que emite confirmación y limpia la orden.

### Requisitos de interfaz
- Panel izquierdo: Tabla de productos en la orden con botones para modificar cantidad o quitar ítem.
- Panel derecho: Totales financieros con números grandes y destacados, entradas de efectivo y cambio.
- Botón prominente de cobro.

### Datos
- Línea de venta: producto, cantidad (int), precio (float), importe (float).
- Transacción: subtotal, iva, total, efectivo, cambio.

### Estado
- Lista de líneas agregadas a la orden activa.
- Desglose financiero calculado en memoria.

### Persistencia
No requiere persistencia en disco en esta fase (opera en memoria de sesión).

### Validaciones
- Cantidad agregada debe ser entero positivo mayor o igual a 1.
- Efectivo recibido debe ser mayor o igual al total a pagar para permitir finalizar la venta.

### Casos límite
- Intentar cobrar una orden con 0 productos agregados.
- Efectivo recibido menor al total de la venta (el cambio debe mostrar $0.00 o advertencia de 'Monto insuficiente').
- Agregar múltiples veces el mismo producto (debe incrementar la cantidad de la fila existente en lugar de duplicar la fila).

### Manejo de errores
- Notificar con claridad si el efectivo recibido no cubre el importe total de la compra.

### Fundamentos de Python relacionados
- Manipulación de listas de objetos y búsqueda de elementos existentes por ID.
- Fórmulas de cálculo de impuestos y redondeo a centavos.

### Conceptos Tkinter relacionados
- Comunicación bidireccional entre la ventana principal y el diálogo modal de selección.
- Eventos de teclado reactivos `<KeyRelease>` en el campo de efectivo recibido.

### Herramientas para investigar
- Patrones de diseño de interfaces de Punto de Venta (POS).
- Enlace de eventos de teclado en campos de pago.

### Diseño de interfaz
¿Cómo asegurarías que el total a pagar sea el elemento visual más llamativo de la pantalla para el cajero?

### Diseño de variables
Usa nombres como `order_tree`, `add_item_btn`, `subtotal_label`, `tax_label`, `total_label`, `cash_received_entry`, `change_due_label`, `checkout_btn`.

### Antes de programar
1. ¿Cómo agrupas productos repetidos para que al agregar 2 veces el mismo ítem la cantidad pase a 2 en la misma fila?
2. ¿Cómo sincronizas el diálogo modal para que al seleccionar un producto retorne el objeto a la ventana principal?

### Arquitectura
```
ejercicio_040/
├── app.py             # Pantalla de venta principal y totales
├── product_lookup.py  # Ventana modal de búsqueda de catálogo
└── pos_engine.py      # Lógica de cálculo de orden, impuestos y cambio
```

### Pruebas mínimas
1. Agregar 2 ítems de $50 y 1 de $100 -> Subtotal $200, IVA $32, Total $232.00.
2. Ingresar efectivo $250.00 -> Comprobar que el cambio calculado sea exactamente $18.00.

### Pruebas de error
1. Ingresar efectivo $200 cuando el total es $232 -> Debe indicar que el efectivo es insuficiente para cobrar.

### Experiencia de usuario
El foco del cursor debe trasladarse automáticamente al campo de efectivo recibido en cuanto se agregue el primer producto.

### Explicación posterior
¿Cómo se implementa la comunicación de datos entre una ventana modal de búsqueda y la ventana principal de la aplicación?

### Aplicación profesional
Terminales de cobro en farmacias, restaurantes de comida rápida y tiendas de abarrotes.

### Reto adicional
Añade un botón que imprima o muestre en pantalla una simulación de ticket de compra en texto formateado con fecha, hora y detalle de productos.

---
> [Índice General](../README.md) · [← Ejercicio 039](../ejercicio_039/README.md) · [Ejercicio 041 →](../ejercicio_041/README.md)
