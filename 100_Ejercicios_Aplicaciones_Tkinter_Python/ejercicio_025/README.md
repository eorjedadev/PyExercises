## Ejercicio 025 — Agenda Telefónica y Directorio Profesional (`ContactBookApp`)

> [Índice General](../README.md) · [← Ejercicio 024](../ejercicio_024/README.md) · [Ejercicio 026 →](../ejercicio_026/README.md)

### Contexto profesional
En recepciones de corporativos y despachos jurídicos, los secretarios gestionan un directorio telefónico interno que debe permitir búsquedas inmediatas y persistir contactos en disco.

### Usuario objetivo
Secretario ejecutivo o recepcionista corporativo.

### Problema
La búsqueda manual en listas estáticas retrasa la transferencia de llamadas urgentes a socios y directores.

### Objetivo
Construir una agenda de contactos de escritorio con `Listbox` y `Scrollbar`, búsqueda incremental en tiempo real al escribir en un campo, formulario lateral para agregar y eliminar contactos, y persistencia en un archivo de texto estructurado (`contactos.txt`).

### Flujo principal
El usuario abre la aplicación y ve la lista de contactos cargados automáticamente desde el archivo de texto. Al teclear en la barra de búsqueda superior, la lista se filtra al instante. Puede seleccionar un contacto para ver sus detalles, registrar uno nuevo mediante el formulario lateral o eliminar el contacto seleccionado con confirmación.

### Requisitos funcionales
- Carga inicial automática de contactos desde archivo de texto plano delimitado por punto y coma (`nombre;telefono;correo;departamento`).
- Visualización en widget `Listbox` con barra de desplazamiento vertical sincronizada.
- Filtrado incremental en vivo al escribir en la barra de búsqueda (`<KeyRelease>`).
- Formulario lateral para captura de nuevo contacto (Nombre, Teléfono, Correo, Departamento).
- Guardado automático de los cambios en el archivo `contactos.txt` al agregar o eliminar.
- Botón de eliminación que requiera confirmación con `messagebox.askyesno`.

### Requisitos de interfaz
- Panel izquierdo: Barra de búsqueda superior, `Listbox` amplio y botones de acción (Eliminar, Ver Detalles).
- Panel derecho: Formulario rotulado para registrar un nuevo contacto con botón 'Guardar Contacto'.
- Barra de estado inferior que indique 'Total de contactos: X'.

### Datos
- Contacto: diccionario con nombre, teléfono, correo y departamento.
- Colección completa: lista de diccionarios.

### Estado
- Lista maestra completa de contactos en memoria.
- Lista de contactos actualmente filtrados y mostrados en el `Listbox`.
- Contacto actualmente seleccionado.

### Persistencia
Persistencia en archivo de texto plano delimitado (`datos/contactos.txt`).

### Validaciones
- Nombre y teléfono son campos obligatorios.
- No permitir nombres duplicados exactos.
- Validar que el archivo exista o crearlo si no existe al iniciar la app.

### Casos límite
- Archivo `contactos.txt` no existe en la primera ejecución (debe crearse vacío sin fallar).
- Búsqueda que no arroja ningún resultado (la lista queda vacía y muestra estado '0 coincidencias').
- Intentar presionar 'Eliminar' sin haber seleccionado ningún elemento en la lista.

### Manejo de errores
- Manejar `FileNotFoundError` y `PermissionError` al leer o escribir en disco.
- Notificar con diálogo amigable si se intenta eliminar sin selección.

### Fundamentos de Python relacionados
- Manejo de archivos con context managers (`with open(..., 'r', encoding='utf-8')`).
- Métodos de cadenas (`split(';')`, `join(';')`, `strip()`).
- Filtrado de listas con comprensiones de listas (`[c for c in contactos if query in c['nombre'].lower()]`).

### Conceptos Tkinter relacionados
- Widget `Listbox` y métodos `.insert()`, `.delete()`, `.curselection()`, `.get()`.
- Widget `Scrollbar` acoplado al comando `yscrollcommand` del `Listbox`.
- Enlace de eventos de teclado `<KeyRelease>` en el campo de búsqueda.

### Herramientas para investigar
- Métodos de manipulación de `tkinter.Listbox`.
- Manejo de rutas con `pathlib.Path`.

### Diseño de interfaz
¿Cómo asegurarías que el `Listbox` ocupe la mayor parte del espacio horizontal disponible cuando la ventana se expanda?

### Diseño de variables
Usa nombres como `search_entry`, `contacts_listbox`, `contact_scrollbar`, `name_entry`, `phone_entry`, `email_entry`, `dept_entry`, `status_label`.

### Antes de programar
1. ¿Por qué debes mantener una lista maestra original separada de la lista que se muestra en el `Listbox` durante una búsqueda?
2. ¿Cómo sincronizas la selección del `Listbox` filtrado con el índice del contacto en la lista maestra?

### Arquitectura
```
ejercicio_025/
├── app.py              # Interfaz con Listbox, formulario y búsqueda
├── storage.py          # Lectura y escritura en contactos.txt
└── datos/
    └── contactos.txt   # Archivo de persistencia de texto plano
```

### Pruebas mínimas
1. Agregar un contacto 'Laura Gómez' -> Comprobar que aparezca en la lista y que se guarde en `datos/contactos.txt`.
2. Escribir 'laura' en el buscador -> Verificar que solo se muestre Laura en la lista.

### Pruebas de error
1. Presionar 'Eliminar' sin tener ningún contacto seleccionado -> Debe advertir 'Seleccione un contacto primero'.

### Experiencia de usuario
Al teclear en el campo de búsqueda, la actualización de la lista debe ser instantánea y no perder el foco del teclado.

### Explicación posterior
¿Por qué es crucial separar la lista maestra de datos en memoria de la representación visual contenida en el widget `Listbox`?

### Aplicación profesional
Agendas internas en conmutadores telefónicos corporativos, libretas de direcciones y directorios locales de personal.

### Reto adicional
Añade la opción de ordenar alfabéticamente la lista de contactos de forma ascendente o descendente mediante un botón de ordenamiento.

---
> [Índice General](../README.md) · [← Ejercicio 024](../ejercicio_024/README.md) · [Ejercicio 026 →](../ejercicio_026/README.md)
