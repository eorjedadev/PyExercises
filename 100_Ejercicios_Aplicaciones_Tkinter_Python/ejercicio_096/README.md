## Ejercicio 096 — Sistema Integral de Gestión de Clínica Veterinaria (`VetCareClinicApp`)

> [Índice General](../README.md) · [← Ejercicio 095](../ejercicio_095/README.md) · [Ejercicio 097 →](../ejercicio_097/README.md)

### Contexto profesional
En clínicas veterinarias y hospitales de mascotas, los médicos veterinarios y recepcionistas administran expedientes clínicos de pacientes, citas de consulta, registros de vacunación y emisión de comprobantes de atención médica.

### Usuario objetivo
Médico veterinario o recepcionista de clínica de animales.

### Problema
La dispersión de historiales médicos en fichas de papel provoca extravío de antecedentes de alergias a medicamentos y olvido de esquemas de vacunación de mascotas.

### Objetivo
Desarrollar con total autonomía profesional un sistema integral de gestión de clínica veterinaria. El estudiante debe diseñar la arquitectura, el esquema relacional de datos, las vistas de interfaz gráfica, las validaciones y los flujos operativos de consulta médica.

### Flujo principal
El usuario gestiona el padrón de clientes (dueños) y sus mascotas asociadas (Nombre, Especie, Raza, Edad, Peso). Puede agendar consultas médicas, registrar diagnósticos, tratamientos y recetas, consultar el carnet de vacunación de la mascota y emitir una nota de servicio consolidada.

### Requisitos funcionales
- Registro de dueños y mascotas vinculadas (relación uno a muchos).
- Expediente clínico: historial de consultas médicas por mascota con fecha, peso, temperatura, diagnóstico y tratamiento prescrito.
- Carnet digital de vacunación: registro de vacunas aplicadas y fecha de próximo refuerzo.
- Agenda de citas del día con estados de atención.
- Búsqueda rápida por nombre de mascota, nombre de dueño o número de expediente.
- Emisión de resumen clínico o comprobante de atención médica en archivo de texto o reporte.

### Requisitos de interfaz
- Sistema multi-vista o multi-pestaña estructurado profesionalmente.
- Visualización clara del historial clínico de la mascota seleccionada.
- Formularios accesibles y ordenados.

### Datos
- Dueño, Mascota, Consulta Médica, Vacunación, Ficha de Pago.

### Estado
- Paciente activo en consulta en memoria.
- Citas del día consultadas.

### Persistencia
Base de datos relacional SQLite diseñada con claves foráneas e integridad referencial.

### Validaciones
- Datos obligatorios de dueño y mascota.
- Signos vitales numéricos válidos (peso en kg, temperatura en °C).
- Fechas cronológicamente coherentes.

### Casos límite
- Dueño con múltiples mascotas registradas en la misma clínica.
- Mascota sin historial previo de vacunación.

### Manejo de errores
- Manejo seguro de transacciones en base de datos y control de excepciones sin cierres inesperados.

### Fundamentos de Python relacionados
- Modelado relacional avanzado en SQLite.
- Separación estricta de capas de software.
- Programación orientada a objetos.

### Conceptos Tkinter relacionados
- Selección autónoma de componentes (`ttk.Notebook`, `Treeview`, `Toplevel`, `Canvas`).
- Diálogos y validaciones.

### Herramientas para investigar
- Esquemas relacionales para software de clínicas médicas/veterinarias.
- Buenas prácticas de experiencia de usuario en software de salud.

### Diseño de interfaz
El estudiante diseña conceptualmente los bocetos y jerarquías visuales antes de programar.

### Diseño de variables
Nombres profesionales, descriptivos y semánticos en la totalidad del proyecto.

### Antes de programar
1. ¿Cómo estructurarás la base de datos relacional para que un dueño pueda tener varias mascotas y cada mascota múltiples consultas y vacunas?
2. ¿Cómo separarás la lógica de negocio de la interfaz gráfica para poder probarla de forma independiente?

### Arquitectura
Arquitectura modular profesional en tres capas con repositorio SQLite, servicios y vistas independientes.

### Pruebas mínimas
1. Registrar dueño con 2 mascotas -> Registrar consulta médica para una de ellas -> Verificar que la consulta quede asociada a la mascota correcta en la base de datos.
2. Reiniciar la app -> Todos los expedientes deben consultarse íntegros.

### Pruebas de error
1. Intentar registrar temperatura corporal negativa o fuera de rango biológico -> Debe rechazar el registro con advertencia clínica.

### Experiencia de usuario
Interfaz intuitiva, ordenada y agradable adaptada a la velocidad de atención en consultorio.

### Explicación posterior
El estudiante debe defender sus decisiones de diseño de interfaz, modelo de base de datos relacional y cómo garantizó la separación de responsabilidades.

### Aplicación profesional
Sistemas de gestión veterinaria (PMS veterinario), clínicas odontológicas y centros de atención médica ambulatoria.

### Reto adicional
Añade un módulo de recordatorios que liste automáticamente todas las mascotas que tienen una vacuna de refuerzo pendiente para los próximos 7 días.

---
> [Índice General](../README.md) · [← Ejercicio 095](../ejercicio_095/README.md) · [Ejercicio 097 →](../ejercicio_097/README.md)
