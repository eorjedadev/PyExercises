## Ejercicio 099 — Gestor Integral de Alquiler de Vehículos y Flota (`FleetRentalManagerApp`)

> [Índice General](../README.md) · [← Ejercicio 098](../ejercicio_098/README.md) · [Ejercicio 100 →](../ejercicio_100/README.md)

### Contexto profesional
En agencias de alquiler de vehículos (Rent-a-Car), los agentes de mostrador gestionan contratos de arrendamiento temporal, disponibilidad de la flota por categorías y liquidaciones de entrega con cargos por kilometraje excedente o retrasos.

### Usuario objetivo
Agente de mostrador de alquiler de autos o gerente de flota.

### Problema
La falta de control riguroso de kilometraje de salida/entrada y de fechas de retorno pactadas genera pérdidas por cobros omitidos y vehículos retenidos sin autorización.

### Objetivo
Desarrollar autónomamente un sistema integral de alquiler de vehículos con base de datos SQLite relacional. El estudiante debe diseñar de forma independiente la arquitectura, los modelos de flota y contratos, las validaciones de disponibilidad por fechas, las fórmulas de liquidación de entrega y la suite de pruebas automatizadas.

### Flujo principal
El agente consulta la disponibilidad de vehículos por categoría y rango de fechas. Registra un contrato de alquiler asignando un vehículo a un cliente, estipulando fecha de salida, fecha pactada de retorno, kilometraje inicial y depósito en garantía. Al devolver el vehículo, registra el kilometraje final y la fecha real; la aplicación calcula días efectivos, cargos por exceso de kilometraje o demora, aplica el depósito y emite la factura final de liquidación.

### Requisitos funcionales
- Catálogo de vehículos: Placa, Marca, Modelo, Categoría (`Económico`, `Sedán`, `SUV`, `Van`), Tarifa Diaria, Kilometraje Actual, Estado (`Disponible`, `Alquilado`, `En Mantenimiento`).
- Directorio de clientes con licencia de conducir y datos de contacto.
- Registro de contratos de alquiler con validación de disponibilidad del vehículo.
- Registro de liquidación de retorno: Kilometraje de entrada, inspección física de daños, cálculo de días reales y recargos por mora.
- Fórmula de liquidación: $(\text{Días} \times \text{Tarifa}) + \text{Cargos Km Excedente} + \text{Recargo Demora} - \text{Depósito}$.
- Actualización automática del kilometraje y estado del vehículo en la flota tras la devolución.
- Persistencia relacional completa en SQLite con claves foráneas.

### Requisitos de interfaz
- Sistema con múltiples vistas (Flota de Vehículos, Contratos Activos, Liquidaciones de Devolución).
- Tablas informativas con formateo monetario y estados cromáticos.
- Diálogo de liquidación detallado con el desglose de cobros antes de confirmar.

### Datos
- Vehículo, Cliente, Contrato de Alquiler, Liquidación de Retorno.

### Estado
- Flota de vehículos y contratos activos en memoria.

### Persistencia
Base de datos relacional SQLite (`datos/alquiler_autos.db`).

### Validaciones
- Kilometraje de retorno debe ser estrictamente mayor o igual al kilometraje de salida.
- Licencia de conducir del cliente obligatoria y vigente.
- No permitir alquilar un vehículo que no se encuentre en estado 'Disponible'.

### Casos límite
- Cliente devuelve el auto antes de la fecha pactada (reliquidar días reales según política).
- Cliente devuelve el auto 3 días después de la fecha pactada (aplicar tarifa diaria regular más recargo por mora).

### Manejo de errores
- Emplear transacciones atómicas para asegurar que la liquidación económica y el cambio de estado del vehículo a 'Disponible' ocurran conjuntamente.

### Fundamentos de Python relacionados
- Transacciones en SQLite y consultas relacionales complejas con `JOIN`.
- Cálculos de diferencias de fechas y tarifas compuestas.

### Conceptos Tkinter relacionados
- Arquitectura de interfaz multi-vista modular.
- Diálogos modales y actualización coordinada de tablas.

### Herramientas para investigar
- Modelos de tarificación en agencias de alquiler de vehículos (Hertz, Avis, etc.).
- Transacciones atómicas de base de datos en Python.

### Diseño de interfaz
El estudiante diseña autónomamente la disposición espacial de la aplicación y la jerarquía de las pantallas.

### Diseño de variables
Nombres estrictamente descriptivos y profesionales en todo el proyecto.

### Antes de programar
1. ¿Cómo estructurarás la consulta relacional para saber si un vehículo específico está libre en un rango de fechas dado?
2. ¿Cómo asegurarás en la base de datos que el kilometraje de un vehículo nunca disminuya tras una devolución?

### Arquitectura
Arquitectura limpia en tres capas con modelos, repositorio SQLite y vistas desacopladas.

### Pruebas mínimas
1. Alquilar vehículo por 3 días a $500/día -> Liquidar a tiempo con km dentro del límite -> Total debe ser $1,500 exactos y el vehículo volver a 'Disponible'.
2. Reiniciar la app -> Todos los contratos y estados de la flota deben persistir íntegros.

### Pruebas de error
1. Ingresar kilometraje de devolución menor al de salida (ej. salida 50,000 km, devolución 49,000 km) -> Debe rechazar la liquidación por inconsistencia.

### Experiencia de usuario
Experiencia fluida y profesional adaptada al ritmo de atención en mostrador de aeropuerto.

### Explicación posterior
El estudiante debe explicar cómo modeló el contrato de arrendamiento y cómo garantizó la integridad de los datos de la flota.

### Aplicación profesional
Software para agencias de alquiler de autos, leasing de maquinaria pesada y alquiler de equipos audiovisuales.

### Reto adicional
Añade un selector de seguro opcional (Cobertura Básica, Cobertura Total) que sume una tarifa fija diaria al costo del alquiler.

---
> [Índice General](../README.md) · [← Ejercicio 098](../ejercicio_098/README.md) · [Ejercicio 100 →](../ejercicio_100/README.md)
