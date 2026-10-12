## Ejercicio 049 — Gestor CRUD de Alumnos y Matrícula Universitaria (`StudentEnrollmentSqliteApp`)

> [Índice General](../README.md) · [← Ejercicio 048](../ejercicio_048/README.md) · [Ejercicio 050 →](../ejercicio_050/README.md)

### Contexto profesional
En oficinas de control escolar y registro académico universitario, los secretarios académicos gestionan expedientes de alumnos y su estado de matrícula utilizando una base de datos local robusta.

### Usuario objetivo
Secretario académico o coordinador de registro escolar.

### Problema
Guardar registros escolares en archivos de texto o CSV expone la información a corrupción por cierres inesperados y carece de integridad referencial.

### Objetivo
Desarrollar una aplicación completa de gestión con persistencia en base de datos SQLite (`estudiantes.db`), implementando las cuatro operaciones CRUD (Crear, Consultar, Actualizar, Eliminar) mediante una capa de repositorio desacoplada de la interfaz gráfica de Tkinter.

### Flujo principal
El usuario abre la aplicación y visualiza a los alumnos en un `ttk.Treeview` cargados desde la base de datos SQLite. Puede registrar un nuevo alumno con el formulario lateral, seleccionar uno de la tabla para editar sus datos, eliminarlo con confirmación o buscar por matrícula o apellido. Todas las operaciones impactan directamente la base de datos relacional.

### Requisitos funcionales
- Creación automática de la tabla `estudiantes` en `estudiantes.db` si no existe al iniciar la app.
- Campos: ID (PK autoincremental), Matrícula (única), Nombre, Apellidos, Carrera (`Combobox`), Semestre (1 a 12), Correo, Estatus ('Activo', 'Inactivo', 'Egresado').
- Operación Create: Inserción de alumno con consulta parametrizada contra inyección SQL.
- Operación Read: Consulta general y búsqueda por matrícula o apellido.
- Operación Update: Edición de datos del alumno seleccionado en la tabla.
- Operación Delete: Eliminación física del registro con diálogo de confirmación.
- Separación estricta: ninguna sentencia SQL dentro de los callbacks de los widgets.

### Requisitos de interfaz
- Panel izquierdo: Formulario organizado para captura y edición con botones 'Guardar' y 'Limpiar'.
- Panel derecho: Barra de búsqueda superior, `ttk.Treeview` con scrollbar y botones 'Editar Seleccionado' y 'Eliminar'.
- Barra de estado con el total de alumnos registrados en la base de datos.

### Datos
- Registro de alumno: id (`int`), matricula (`str`), nombre (`str`), apellidos (`str`), carrera (`str`), semestre (`int`), correo (`str`), estatus (`str`).
- Base de datos: SQLite relacional.

### Estado
- Alumno en edición activa (ID o `None`).
- Registros consultados en memoria.

### Persistencia
Base de datos relacional SQLite local (`datos/estudiantes.db`).

### Validaciones
- Matrícula única y obligatoria.
- Nombre y apellidos obligatorios.
- Semestre entre 1 y 12.
- Correo con formato válido.

### Casos límite
- Intentar registrar una matrícula que ya existe en la base de datos (`sqlite3.IntegrityError`).
- Caracteres con tildes o caracteres especiales en nombres.
- Base de datos bloqueada por otro proceso.

### Manejo de errores
- Capturar `sqlite3.IntegrityError` y notificar que la matrícula ya pertenece a otro estudiante.
- Manejar excepciones de conexión mediante bloques `try/except` en la capa de datos.

### Fundamentos de Python relacionados
- Módulo estándar `sqlite3` (`sqlite3.connect`, transacciones con context managers, consultas parametrizadas con `?`).
- Patrón Repositorio (Repository Pattern) en Python.
- Clases de datos (`dataclass` o modelos) para representar entidades.

### Conceptos Tkinter relacionados
- Integración completa de Tkinter con una base de datos relacional.
- Sincronización del estado de formularios entre modos de 'Creación' y 'Edición'.

### Herramientas para investigar
- Módulo estándar `sqlite3` de Python.
- Buenas prácticas contra inyección SQL usando marcadores de posición (`?`).
- Patrón Repositorio y separación de capas.

### Diseño de interfaz
¿Cómo indicarías visualmente al usuario si el formulario lateral se encuentra en modo 'Nuevo Registro' o en modo 'Editando Registro Existente'?

### Diseño de variables
Usa nombres como `student_repo`, `students_tree`, `mat_entry`, `name_entry`, `career_combo`, `semester_entry`, `save_btn`, `edit_btn`, `delete_btn`.

### Antes de programar
1. ¿Por qué es una pésima práctica de seguridad formatear consultas SQL con f-strings (`f'SELECT * WHERE id={id}'`) y cómo se usan consultas parametrizadas con `?`?
2. ¿Por qué las operaciones SQL deben encapsularse en una clase repositorio separada de la ventana de Tkinter?

### Arquitectura
```
ejercicio_049/
├── app.py              # Interfaz gráfica y enlace de eventos
├── student_repo.py     # Capa DAO / Repositorio con consultas SQL a SQLite
├── models.py           # Entidad Alumno (dataclass)
└── datos/
    └── estudiantes.db  # Base de datos relacional SQLite
```

### Pruebas mínimas
1. Registrar un alumno nuevo -> Verificar que se inserte en `estudiantes.db` y aparezca en el Treeview.
2. Modificar el semestre del alumno y guardar -> Comprobar que la base de datos se actualice.
3. Reiniciar la app -> Verificar que los datos sigan intactos desde SQLite.

### Pruebas de error
1. Intentar registrar una matrícula duplicada -> Debe capturar `IntegrityError` y avisar 'La matrícula ya está registrada'.

### Experiencia de usuario
Al presionar 'Editar', los datos deben cargarse en el formulario, el botón debe cambiar a 'Actualizar Alumno' y resaltarse visualmente.

### Explicación posterior
¿Cómo garantiza el Patrón Repositorio que los cambios en el motor de base de datos no rompan la interfaz gráfica de usuario?

### Aplicación profesional
Sistemas de control escolar, módulos de expediente clínico y software administrativo empresarial.

### Reto adicional
Añade un selector de filtro en la tabla que permita ver únicamente a los alumnos de una carrera específica mediante una consulta SQL con cláusula `WHERE`.

---
> [Índice General](../README.md) · [← Ejercicio 048](../ejercicio_048/README.md) · [Ejercicio 050 →](../ejercicio_050/README.md)
