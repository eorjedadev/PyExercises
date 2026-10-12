## Ejercicio 006 — Bloc de Notas Rápido con Selector de Formato (`ScratchPadApp`)

> [Índice General](../README.md) · [← Ejercicio 005](../ejercicio_005/README.md) · [Ejercicio 007 →](../ejercicio_007/README.md)

### Contexto profesional
En mesas de ayuda telefónica y soporte técnico, los analistas necesitan tomar notas efímeras durante las llamadas sin abrir herramientas complejas, con detección de cambios no guardados.

### Usuario objetivo
Operador de soporte técnico o analista de operaciones.

### Problema
El cierre accidental de ventanas provoca la pérdida de notas temporales sobre números de ticket o datos de clientes recopilados en la llamada.

### Objetivo
Desarrollar una ventana de bloc de notas con campo de título, selector de formato de texto (Plano, Registro con Fecha/Hora, Lista de Tareas), botón de limpieza con diálogo de confirmación y detección de estado modificado.

### Flujo principal
El operador escribe un título y redacta notas. Puede pulsar un botón 'Insertar Marca de Tiempo' para estampar la hora actual. Al intentar limpiar o salir, si existen notas, se solicita confirmación explícita para evitar pérdida de datos.

### Requisitos funcionales
- Campo de título de la nota.
- Área de texto multilínea con barra de desplazamiento.
- Botón 'Insertar Marca de Tiempo' que inserta la fecha y hora actual en la posición del cursor.
- Botón de limpieza que verifica si hay texto escrito antes de reiniciar el formulario.
- Detección de cambios no guardados para solicitar confirmación.

### Requisitos de interfaz
- Estructura visual dividida en: Barra superior (Título y controles de formato), Centro (Área de texto), Barra inferior (Estado y botón de limpieza).
- Uso de `messagebox.askyesno` para confirmaciones críticas.

### Datos
- Título: cadena (`str`).
- Contenido: texto multilínea (`str`).
- Marca de tiempo: cadena ISO o formato legible local.

### Estado
- Bandera booleana `is_dirty` que indica si el documento ha sido modificado desde la última acción de guardado o limpieza.

### Persistencia
No requiere persistencia en disco (es un borrador de sesión).

### Validaciones
- Validar antes de limpiar si el área de texto contiene información no vacía.

### Casos límite
- Intentar insertar marca de tiempo cuando el cursor no está en el foco del área de texto.
- El usuario presiona limpiar cuando el bloc ya está vacío (no debe pedir confirmación innecesaria).

### Manejo de errores
- Controlar el protocolo de cierre `WM_DELETE_WINDOW` para evitar salida accidental si `is_dirty` es verdadero.

### Fundamentos de Python relacionados
- Módulo `datetime` para generación de marcas de tiempo formateadas (`datetime.now().strftime(...)`).
- Métodos de inserción y manipulación de texto en memoria.

### Conceptos Tkinter relacionados
- Widget `Text` y método `.insert(tk.INSERT, texto)`.
- Módulo `tkinter.messagebox` (`askyesno`, `showwarning`).
- Manejo de protocolo de cierre de ventana `root.protocol('WM_DELETE_WINDOW', ...)`. 

### Herramientas para investigar
- Índice especial `tk.INSERT` en widgets `Text`.
- Métodos de `tkinter.messagebox`.

### Diseño de interfaz
¿Cómo posicionarías los botones superiores para que la inserción de fecha y hora esté accesible con un solo clic sin estorbar la escritura?

### Diseño de variables
Usa nombres como `title_entry`, `content_text`, `insert_timestamp_btn`, `clear_btn`, `is_dirty_state`.

### Antes de programar
1. ¿Cómo interceptas el botón de la 'X' de la ventana para que ejecute tu propia lógica de validación?
2. ¿Cómo se inserta texto exactamente en la posición donde el usuario tiene el cursor?

### Arquitectura
```
ejercicio_006/
├── app.py           # Ventana gráfica y gestión de eventos
└── notepad_core.py  # Reglas de negocio y gestión de estado sucio
```

### Pruebas mínimas
1. Escribir texto en el área y presionar 'Insertar Marca de Tiempo' -> Comprobar que la fecha/hora aparezca en la posición actual.
2. Presionar 'Limpiar' -> Responder 'No' en el diálogo y verificar que el texto se conserve.

### Pruebas de error
1. Con texto en pantalla, hacer clic en la 'X' de cerrar ventana -> Debe aparecer el diálogo de advertencia preguntando si realmente desea salir.

### Experiencia de usuario
Si el bloc está vacío, el botón de 'Limpiar' puede permanecer deshabilitado (`state='disabled'`) para evitar clics inútiles.

### Explicación posterior
¿Qué papel cumple el interceptor `WM_DELETE_WINDOW` en la prevención de pérdida accidental de datos en aplicaciones de escritorio?

### Aplicación profesional
Blocs de notas flotantes en aplicaciones de contact center, consolas de despacho de emergencias y notas rápidas de CRM.

### Reto adicional
Agrega un botón que convierta las líneas seleccionadas del texto en una lista de viñetas ('- ') automáticamente.

---
> [Índice General](../README.md) · [← Ejercicio 005](../ejercicio_005/README.md) · [Ejercicio 007 →](../ejercicio_007/README.md)
