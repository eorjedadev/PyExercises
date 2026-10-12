## Ejercicio 031 — Catálogo de Biblioteca y Préstamo de Libros (`BookCatalogApp`)

> [Índice General](../README.md) · [← Ejercicio 030](../ejercicio_030/README.md) · [Ejercicio 032 →](../ejercicio_032/README.md)

### Contexto profesional
En bibliotecas escolares y centros de documentación, los bibliotecarios deben gestionar el catálogo de libros y registrar préstamos a estudiantes.

### Usuario objetivo
Bibliotecario o asistente de biblioteca.

### Problema
El uso de fichas de cartón provoca extravío de ejemplares y desconocimiento de cuántos libros tiene prestados cada alumno.

### Objetivo
Desarrollar una aplicación de catálogo con `ttk.Treeview`, persistencia en JSON, búsqueda en vivo por título o autor, y control de disponibilidad (Disponible / Prestado) con registro del solicitante.

### Flujo principal
El bibliotecario busca un libro en la tabla por título o autor. Selecciona un libro disponible y presiona 'Prestar Libro', lo que abre un cuadro de diálogo para registrar el nombre del alumno y fecha. El libro pasa a estatus 'Prestado'. Al ser devuelto, presiona 'Registrar Devolución' y vuelve a 'Disponible'.

### Requisitos funcionales
- Carga y guardado en `catalogo_libros.json`.
- Columnas: ISBN, Título, Autor, Categoría, Estado ('Disponible' / 'Prestado'), Prestado A.
- Búsqueda en vivo insensible a mayúsculas por título o autor.
- Formulario para agregar nuevos libros al catálogo.
- Acción de préstamo con diálogo que solicite nombre del alumno.
- Acción de devolución con confirmación que restablezca disponibilidad.

### Requisitos de interfaz
- Treeview con dos colores: verde para disponibles, naranja/rojo para prestados.
- Barra de búsqueda superior prominente.
- Botones de préstamo y devolución contextuales.

### Datos
- Libro: ISBN, título, autor, categoria, estado, prestado_a, fecha_prestamo.

### Estado
- Lista maestra de libros.
- Lista mostrada en la tabla.

### Persistencia
Archivo JSON (`datos/catalogo_libros.json`).

### Validaciones
- ISBN único obligatorio.
- Título y autor obligatorios.
- No permitir prestar un libro que ya figura como prestado.

### Casos límite
- Devolución de un libro que ya está disponible.
- Búsqueda con caracteres acentuados.

### Manejo de errores
- Notificar con claridad cualquier intento de acción inválida sobre el estado del libro.

### Fundamentos de Python relacionados
- Manejo de diccionarios anidados en JSON.
- Métodos de cadenas para búsqueda insensible a mayúsculas (`query.lower() in libro['titulo'].lower()`).

### Conceptos Tkinter relacionados
- Diálogo simple para capturar texto con `simpledialog.askstring`.
- Modificación de elementos del Treeview.

### Herramientas para investigar
- Módulo `tkinter.simpledialog` (`askstring`).
- Formato y validación de ISBN básico.

### Diseño de interfaz
¿Cómo dispondrías los botones de acción para que no se confunda 'Agregar Libro al Catálogo' con 'Prestar Libro'?

### Diseño de variables
Usa nombres como `catalog_tree`, `search_var`, `isbn_entry`, `title_entry`, `author_entry`, `loan_btn`, `return_btn`.

### Antes de programar
1. ¿Qué ventajas ofrece `simpledialog.askstring` para solicitar un dato rápido sin diseñar una ventana completa?
2. ¿Cómo sincronizas los cambios en el archivo JSON para que no se pierdan si la app se cierra inesperadamente?

### Arquitectura
```
ejercicio_031/
├── app.py           # Vistas y tabla de catálogo
├── library_core.py  # Reglas de préstamo, devolución y búsquedas
└── datos/
    └── catalogo_libros.json # Archivo de catálogo
```

### Pruebas mínimas
1. Seleccionar libro disponible y presionar 'Prestar' -> Ingresar alumno 'Pedro' y verificar que cambie a 'Prestado' y se guarde en JSON.
2. Presionar 'Devolver' -> Verificar que regrese a 'Disponible' y se borre el alumno.

### Pruebas de error
1. Intentar prestar un libro que ya está prestado -> Debe advertir 'El libro ya se encuentra en préstamo'.

### Experiencia de usuario
El buscador debe responder inmediatamente mientras se teclea sin necesidad de presionar Enter.

### Explicación posterior
¿Cómo interactúa `simpledialog.askstring` con el bucle de eventos principal de la aplicación?

### Aplicación profesional
Gestores bibliotecarios, préstamos de herramientas en talleres universitarios y mediatecas.

### Reto adicional
Añade una validación que calcule automáticamente si un préstamo tiene más de 14 días y muestre una advertencia de 'Préstamo Vencido'.

---
> [Índice General](../README.md) · [← Ejercicio 030](../ejercicio_030/README.md) · [Ejercicio 032 →](../ejercicio_032/README.md)
