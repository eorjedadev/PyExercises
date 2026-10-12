## Ejercicio 095 — Centro de Despachos y Enrutamiento Logístico (`DispatchHubApp`)

> [Índice General](../README.md) · [← Ejercicio 094](../ejercicio_094/README.md) · [Ejercicio 096 →](../ejercicio_096/README.md)

### Contexto profesional
En empresas de distribución de mercancías y paquetería urbana, los coordinadores logísticos asignan pedidos pendientes a vehículos de la flota según su capacidad de carga volumétrica y ruta de entrega.

### Usuario objetivo
Coordinador de despachos o despachador de flota logística.

### Problema
Asignar pedidos manualmente sin validar la capacidad de carga máxima de cada furgoneta provoca sobrecargas ilegales, multas de tránsito y entregas retrasadas.

### Objetivo
Desarrollar de forma autónoma una aplicación integral de centro de despachos y asignación de pedidos a vehículos de flota. El estudiante debe decidir de manera independiente la arquitectura del proyecto, el diseño visual de la interfaz, los widgets necesarios, el esquema de persistencia (SQLite o JSON), las reglas de validación y la suite de pruebas a implementar.

### Flujo principal
El despachador visualiza dos paneles principales: los pedidos pendientes de entrega y los vehículos de la flota disponibles con su capacidad de carga (kg y volumen m3). Selecciona un vehículo y le asigna pedidos seleccionados. La aplicación valida que la suma de pesos de los pedidos no supere la capacidad máxima del vehículo asignado. Al confirmar la ruta, el vehículo pasa a estado 'En Ruta' y se emite la hoja de despacho consolidada.

### Requisitos funcionales
- Gestión de catálogo de vehículos de la flota (Placa, Modelo, Capacidad Peso kg, Capacidad Volumen m3, Estado).
- Gestión de pedidos pendientes de entrega (Folio, Destinatario, Dirección, Peso kg, Volumen m3, Zona).
- Asignación interactiva de pedidos a vehículos.
- Validación estricta en tiempo real de sobrecarga: advertir y bloquear la asignación si el peso acumulado excede la capacidad del vehículo.
- Visualización del porcentaje de ocupación del vehículo asignado (barra de capacidad).
- Generación de hoja de ruta consolidada de entrega en archivo imprimible o texto plano.
- Persistencia robusta de datos decidida por el estudiante.

### Requisitos de interfaz
- Interfaz profesional de despacho de grado corporativo diseñada con criterios ergonómicos.
- El estudiante decide si utiliza múltiples vistas, pestañas (`Notebook`) o diseño maestro-detalle.
- Retroalimentación visual evidente de capacidad ocupada vs capacidad libre en cada vehículo.

### Datos
- Flota de vehículos, lista de pedidos, rutas consolidadas y métricas de carga.

### Estado
- Estado de asignación en tiempo real en memoria.

### Persistencia
Estrategia de persistencia elegida y justificada autónomamente por el estudiante (SQLite relacional recomendada).

### Validaciones
- Capacidad de peso y volumen del vehículo no rebasable.
- Pedidos asignados no pueden asignarse a dos vehículos simultáneamente.

### Casos límite
- Pedido individual cuyo peso excede la capacidad total del vehículo más grande de la flota.
- Cancelar la asignación de un pedido y devolverlo a la lista de pendientes.

### Manejo de errores
- Manejo integral y profesional de errores de usuario, datos y sistema sin abortos inesperados.

### Fundamentos de Python relacionados
- Modelado de entidades orientadas a objetos.
- Arquitectura modular desacoplada en paquetes de software.
- Algoritmos de empaquetado y cálculo de capacidades.

### Conceptos Tkinter relacionados
- Selección autónoma de widgets y gestores de geometría (`grid`, `pack`, `Canvas`, `Treeview`).
- Manejo de estado y eventos.

### Herramientas para investigar
- Patrones arquitectónicos para software logístico.
- Problema de la mochila (Knapsack Problem) simple para optimización de carga.

### Diseño de interfaz
El estudiante debe diseñar y justificar la disposición espacial de la aplicación antes de implementar.

### Diseño de variables
Aplicación estricta de nomenclatura semántica y profesional en todo el código.

### Antes de programar
1. ¿Qué arquitectura de paquetes (`ui/`, `services/`, `models/`, `storage/`) adoptarás y por qué?
2. ¿Cómo presentarás visualmente la ocupación de cada vehículo para que el despachador tome decisiones en segundos?

### Arquitectura
Estructura modular completa diseñada autónomamente por el practicante respetando la separación de responsabilidades.

### Pruebas mínimas
1. Asignar 3 pedidos a un vehículo sin rebasar su capacidad -> Comprobar que cambie a 'En Ruta' y se descuenten de pendientes.
2. Reiniciar la app -> Los datos deben persistir íntegros.

### Pruebas de error
1. Intentar asignar un pedido que haga que el vehículo supere el 100% de su capacidad -> La aplicación debe bloquear la asignación e informar la sobrecarga.

### Experiencia de usuario
Experiencia de usuario de nivel profesional con navegación ágil y tiempos de respuesta inmediatos.

### Explicación posterior
El estudiante debe explicar detalladamente sus decisiones de arquitectura, widgets seleccionados, modelo de persistencia y cómo probó su lógica.

### Aplicación profesional
Centros de distribución logística (Hubs de última milla), empresas de transporte de carga y flotas de comercio electrónico.

### Reto adicional
Añade un algoritmo de sugerencia automática que proponga el vehículo óptimo para un conjunto de pedidos minimizando el espacio desperdiciado.

---
> [Índice General](../README.md) · [← Ejercicio 094](../ejercicio_094/README.md) · [Ejercicio 096 →](../ejercicio_096/README.md)
