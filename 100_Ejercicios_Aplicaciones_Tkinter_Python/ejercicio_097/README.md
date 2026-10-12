## Ejercicio 097 — Terminal de Punto de Venta para Cafetería con Control de Caja (`CoffeeShopPosApp`)

> [Índice General](../README.md) · [← Ejercicio 096](../ejercicio_096/README.md) · [Ejercicio 098 →](../ejercicio_098/README.md)

### Contexto profesional
En cafeterías y barras de café de especialidad, los baristas y cajeros atienden pedidos rápidos de mostrador, gestionan el menú con personalizaciones (tipo de leche, tamaño, endulzante), cobran con diversos métodos de pago y realizan el arqueo de caja del turno.

### Usuario objetivo
Barista, cajero de cafetería o encargado de turno.

### Problema
La lentitud de registro en sistemas genéricos no adaptados a cafeterías provoca filas en mostrador y errores en el arqueo del efectivo al cierre del turno.

### Objetivo
Desarrollar de forma autónoma una terminal de punto de venta (POS) para cafetería con catálogo de productos por categorías (Café Caliente, Café Frío, Repostería), personalización de bebidas, cobro rápido, control de apertura y cierre de turno con arqueo de caja, y persistencia relacional.

### Flujo principal
El cajero inicia su turno registrando el fondo inicial de caja en efectivo. Durante el turno, selecciona bebidas y alimentos con un toque o clic; cada bebida permite seleccionar modificadores (ej. 'Leche de Avena +$15'). La orden calcula subtotales, IVA y total. Al cobrar, registra el método de pago (Efectivo, Tarjeta). Al finalizar el turno, presiona 'Cierre de Caja', donde ingresa el efectivo contado en el cajón y la aplicación calcula sobrantes o faltantes emitiendo el reporte del turno.

### Requisitos funcionales
- Control de turno de caja: Apertura de caja con fondo inicial en efectivo y Cierre con arqueo.
- Catálogo de productos con modificadores o extras que incrementan el precio unitario.
- Construcción rápida de la orden de venta en tabla o lista interactiva.
- Cobro con cálculo de cambio en efectivo y registro de pagos con tarjeta.
- Cálculo automático del arqueo de caja: $\text{Efectivo Esperado} = \text{Fondo Inicial} + \text{Ventas en Efectivo}$.
- Detección de descuadre: Faltante o Sobrante en el cierre de turno.
- Persistencia de ventas y turnos en base de datos SQLite.

### Requisitos de interfaz
- Interfaz optimizada para pantallas táctiles o ratón rápido con botones grandes de productos.
- Panel de orden actual claro y destacado a la derecha.
- Diálogo de cierre de turno con resumen financiero completo.

### Datos
- Producto, Extra/Modificador, Orden de Venta, Detalle de Venta, Turno de Caja.

### Estado
- Turno de caja activo (ID de turno).
- Orden en construcción en memoria.

### Persistencia
Base de datos relacional SQLite con tablas de turnos, ventas y catálogo.

### Validaciones
- No permitir registrar ventas si la caja no ha sido abierta con fondo inicial.
- Fondo inicial y efectivo contado deben ser números mayores o iguales a cero.

### Casos límite
- Turno cerrado con 0 ventas registradas.
- Efectivo contado menor al esperado (registrar faltante en el log contable).

### Manejo de errores
- Proteger las transacciones financieras con transacciones atómicas de base de datos.

### Fundamentos de Python relacionados
- Modelado de transacciones comerciales y contables.
- Cálculos de diferencias y balances de caja.

### Conceptos Tkinter relacionados
- Diseño de interfaces orientadas a punto de venta.
- Composición de paneles y diálogos modales.

### Herramientas para investigar
- Mejores prácticas en sistemas de punto de venta gastronómicos (POS).
- Procedimientos de apertura y corte de caja en comercio minorista.

### Diseño de interfaz
El estudiante diseña la distribución visual garantizando que el cobro pueda completarse en menos de 10 segundos.

### Diseño de variables
Nombres semánticos y profesionales en todos los módulos del proyecto.

### Antes de programar
1. ¿Cómo se diseña el flujo para que la aplicación impida cobrar si no hay un turno de caja abierto previamente?
2. ¿Cómo se calculan el efectivo esperado y la diferencia de arqueo en el cierre de caja?

### Arquitectura
Arquitectura limpia en tres capas con repositorio SQLite, servicios financieros y vistas modulares.

### Pruebas mínimas
1. Abrir caja con $1,000 -> Vender $500 en efectivo -> Cerrar caja con $1,500 contados -> Comprobar arqueo perfecto con $0 de diferencia.
2. Reiniciar la app -> El histórico de turnos y ventas debe persistir íntegro.

### Pruebas de error
1. Intentar vender con caja cerrada -> Debe advertir que debe abrirse el turno de caja primero.

### Experiencia de usuario
Experiencia ágil, tipografía de números grandes para el total y botones cómodos de pulsar.

### Explicación posterior
El estudiante debe explicar cómo modeló el ciclo de vida del turno de caja y cómo garantizó la coherencia de los saldos.

### Aplicación profesional
Puntos de venta en cafeterías, panaderías, heladerías y tiendas de conveniencia.

### Reto adicional
Añade la generación de un ticket de cierre de turno en formato de texto listo para simular impresión térmica.

---
> [Índice General](../README.md) · [← Ejercicio 096](../ejercicio_096/README.md) · [Ejercicio 098 →](../ejercicio_098/README.md)
