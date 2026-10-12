## Ejercicio 039 — Gestor de Clientes con Ventana Modal de Edición (`CustomerDirectoryModalApp`)

> [Índice General](../README.md) · [← Ejercicio 038](../ejercicio_038/README.md) · [Ejercicio 040 →](../ejercicio_040/README.md)

### Contexto profesional
En departamentos de atención a clientes y ventas corporativas, los ejecutivos consultan un directorio de cuentas y necesitan editar datos de contacto mediante ventanas secundarias dedicadas sin perder el contexto de la tabla principal.

### Usuario objetivo
Ejecutivo de cuentas o asesor de servicio al cliente.

### Problema
Editar datos directamente sobre celdas diminutas en tablas complejas provoca errores de tipeo y cambios accidentales en columnas adyacentes.

### Objetivo
Desarrollar una aplicación de directorio de clientes con `ttk.Treeview` en la ventana principal y una ventana secundaria modal (`Toplevel`) para la creación y edición atómica de registros, implementando bloqueo modal con `grab_set()` y retorno seguro de datos.

### Flujo principal
El usuario ve la tabla de clientes. Selecciona un cliente y presiona 'Editar Cliente'. Se abre una ventana secundaria emergente (`Toplevel`) con los datos precargados en un formulario espacioso. La ventana principal queda bloqueada para interacción hasta que el usuario guarde o cancele. Al guardar, la tabla principal se actualiza inmediatamente.

### Requisitos funcionales
- Ventana principal con tabla `Treeview`: ID, Razón Social, RFC/Identificación, Contacto, Teléfono, Correo, Estatus.
- Ventana secundaria modal (`Toplevel`) para Nuevo Cliente y Editar Cliente.
- Precarga exacta de datos del cliente seleccionado al abrir la ventana de edición.
- Bloqueo modal estricto con `grab_set()` y asociación `transient(root)`.
- Actualización de la fila en la tabla principal al confirmar cambios.
- Botón para eliminar cliente de la lista con diálogo de confirmación.

### Requisitos de interfaz
- Ventana principal con barra de herramientas superior (Nuevo, Editar, Eliminar).
- Ventana modal con tamaño fijo, centrada respecto a la principal y sin botones de maximizar innecesarios.
- Botones 'Guardar Cambios' y 'Cancelar' en la ventana modal.

### Datos
- Cliente: id (`int`), nombre (`str`), id_fiscal (`str`), contacto (`str`), telefono (`str`), correo (`str`), estatus (`str`).

### Estado
- Lista de clientes en memoria.
- Referencia a la ventana `Toplevel` activa.

### Persistencia
No requiere persistencia en disco en esta fase (almacena en memoria de sesión).

### Validaciones
- Razón social y correo obligatorios.
- Formato válido de correo electrónico.
- Identificación fiscal única.

### Casos límite
- El usuario intenta hacer clic en la ventana principal mientras la modal está abierta (debe emitir aviso sonoro o ignorar clics).
- Cerrar la ventana modal con la 'X' superior (debe equivaler a presionar 'Cancelar' sin modificar los datos).

### Manejo de errores
- Manejar la destrucción limpia de la ventana modal liberando el grab con `grab_release()`.

### Fundamentos de Python relacionados
- Programación orientada a objetos: clases para representar ventanas secundarias.
- Paso de callbacks y referencias de objetos entre ventanas.

### Conceptos Tkinter relacionados
- Creación de ventanas secundarias con `Toplevel(master)`.
- Modalidad con `modal.grab_set()` y `modal.transient(root)`.
- Espera de cierre de ventana modal con `root.wait_window(modal)`.

### Herramientas para investigar
- Métodos de ventanas secundarias en Tkinter: `grab_set()`, `grab_release()`, `transient()`, `wait_window()`.
- Diferencia arquitectónica entre crear otra instancia de `Tk()` (incorrecto) vs `Toplevel()` (correcto).

### Diseño de interfaz
¿Por qué es crucial centrar la ventana modal respecto a la ventana principal para evitar que aparezca en esquinas lejanas de monitores grandes?

### Diseño de variables
Usa nombres como `customer_tree`, `add_customer_btn`, `edit_customer_btn`, `edit_modal_window`, `modal_name_entry`, `modal_save_btn`.

### Antes de programar
1. ¿Por qué NUNCA se debe instanciar una segunda vez `tk.Tk()` en una aplicación de Tkinter y qué errores graves provoca?
2. ¿Qué efecto tiene `grab_set()` sobre la interacción del usuario y por qué debe liberarse al cerrar la ventana?

### Arquitectura
```
ejercicio_039/
├── app.py                # Ventana principal y Treeview
├── customer_dialog.py    # Clase Toplevel modal para alta y edición
└── customer_service.py   # Colección de clientes y reglas de validación
```

### Pruebas mínimas
1. Seleccionar un cliente existente y presionar 'Editar' -> La modal debe abrirse con los datos correctos.
2. Modificar el teléfono y presionar 'Guardar' -> La tabla principal debe reflejar de inmediato el nuevo teléfono.

### Pruebas de error
1. Con la modal abierta, intentar hacer clic en los botones de la ventana principal -> La ventana principal debe estar inactiva y no responder hasta cerrar la modal.

### Experiencia de usuario
La ventana modal debe abrirse con el cursor enfocado en el primer campo editable y cerrarse suavemente al presionar 'Guardar' o 'Cancelar'.

### Explicación posterior
¿Cómo garantiza el trío de métodos `transient()`, `grab_set()` y `wait_window()` un comportamiento modal profesional en Tkinter?

### Aplicación profesional
Formularios de alta y edición en ERPs, aplicaciones de facturación y sistemas CRM comerciales.

### Reto adicional
Añade soporte para que al presionar la tecla `Escape` en la ventana modal, esta se cierre cancelando cualquier cambio.

---
> [Índice General](../README.md) · [← Ejercicio 038](../ejercicio_038/README.md) · [Ejercicio 040 →](../ejercicio_040/README.md)
