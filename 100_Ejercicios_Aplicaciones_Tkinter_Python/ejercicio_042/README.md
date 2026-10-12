## Ejercicio 042 — Gestor de Preferencias y Configuración de Aplicación (`SettingsManagerApp`)

> [Índice General](../README.md) · [← Ejercicio 041](../ejercicio_041/README.md) · [Ejercicio 043 →](../ejercicio_043/README.md)

### Contexto profesional
En suites de software corporativo, los usuarios configuran parámetros de entorno como tema visual, directorio de trabajo predeterminado, idioma y opciones de inicio.

### Usuario objetivo
Usuario final o administrador de la aplicación.

### Problema
Hardcodear configuraciones en el código fuente obliga a recompilar la aplicación cada vez que un usuario desea cambiar su carpeta de trabajo o preferencias.

### Objetivo
Desarrollar una aplicación principal con barra de herramientas que incluya un botón 'Configuración', el cual abra una ventana modal `Toplevel` para modificar preferencias (Directorio por defecto, Tema Claro/Oscuro, Formato de Fecha, Notificaciones), persistiendo los ajustes en un archivo `config.json` y aplicándolos de inmediato.

### Flujo principal
El usuario abre la aplicación y visualiza su entorno según el archivo de configuración. Presiona 'Configuración', se abre la modal de ajustes. Modifica el tema visual de Claro a Oscuro y selecciona un nuevo directorio con `filedialog.askdirectory`. Al presionar 'Guardar y Aplicar', los ajustes se escriben en `config.json` y la ventana principal cambia inmediatamente sus colores y directorio activo.

### Requisitos funcionales
- Carga automática de `config.json` al arrancar (crear valores por defecto si no existe).
- Ventana modal `Toplevel` de preferencias con controles organizados: Directorio de trabajo (`Entry` + botón selector), Tema (`Radiobutton`: Claro / Oscuro), Formato de Fecha (`Combobox`), Sonidos activos (`Checkbutton`).
- Botón 'Examinar' en la modal para seleccionar el directorio de trabajo mediante `filedialog`.
- Persistencia de los cambios en `config.json` con formato legible (`indent=4`).
- Aplicación inmediata de los cambios en la ventana principal al guardar.

### Requisitos de interfaz
- Ventana principal con panel central que refleje el tema y muestre el directorio de trabajo activo.
- Ventana modal de ajustes ordenada con `LabelFrame`.
- Botones 'Guardar' y 'Cancelar' en la modal.

### Datos
- Esquema de configuración: `{'theme': 'dark'|'light', 'work_dir': str, 'date_format': str, 'sound_enabled': bool}`.

### Estado
- Diccionario de configuración en memoria.
- Tema visual aplicado actualmente.

### Persistencia
Archivo JSON (`config/config.json`).

### Validaciones
- Verificar que el directorio seleccionado exista en el sistema.
- Manejar archivos de configuración corruptos restableciendo valores por defecto.

### Casos límite
- El archivo `config.json` es editado externamente con sintaxis JSON inválida.
- El usuario selecciona una carpeta que luego es eliminada del sistema.

### Manejo de errores
- Capturar excepciones de lectura de JSON y restaurar la configuración predeterminada con diálogo informativo.

### Fundamentos de Python relacionados
- Módulo `json` para serialización de preferencias.
- Módulo `pathlib.Path` para validación de rutas existentes.

### Conceptos Tkinter relacionados
- Ventanas modales `Toplevel` con aplicación reactiva de cambios en la ventana padre.
- Cambio dinámico de propiedades visuales (`bg`, `fg`) según el tema seleccionado.

### Herramientas para investigar
- Módulo `json` de Python.
- Métodos de configuración de ventanas y widgets (`config(bg=...)`).

### Diseño de interfaz
¿Cómo asegurarías que el cambio de tema entre Claro y Oscuro se propague a todos los widgets sin dejar elementos ilegibles por falta de contraste?

### Diseño de variables
Usa nombres como `settings_modal`, `work_dir_entry`, `theme_radio_var`, `date_format_combo`, `sound_check_var`, `save_settings_btn`.

### Antes de programar
1. ¿Cómo se desacopla la carga y guardado de configuración en una clase de servicio para no mezclar lógica de archivos con widgets?
2. ¿Cómo notifica la ventana modal a la ventana principal que los ajustes han cambiado?

### Arquitectura
```
ejercicio_042/
├── app.py              # Ventana principal y aplicación de estilos
├── settings_dialog.py  # Modal Toplevel de configuración
├── config_service.py   # Carga, guardado y valores por defecto en config.json
└── config/
    └── config.json     # Archivo de configuración persistente
```

### Pruebas mínimas
1. Cambiar tema a Oscuro y guardar -> Comprobar que la ventana principal cambie a fondo oscuro y que `config.json` contenga `'theme': 'dark'`.
2. Reiniciar la app -> Verificar que arranque directamente con el tema oscuro guardado.

### Pruebas de error
1. Dañar intencionalmente el archivo `config.json` -> La app debe notificar el error y generar un archivo con valores por defecto sin romperse.

### Experiencia de usuario
Al abrir la modal de configuración, los campos deben reflejar fielmente los valores guardados actualmente en el JSON.

### Explicación posterior
¿Por qué es crucial centralizar la gestión de configuración en un módulo independiente y cómo se propagan las preferencias a la interfaz gráfica?

### Aplicación profesional
Diálogos de preferencias en herramientas de escritorio, suites de productividad y editores de código.

### Reto adicional
Añade un botón 'Restablecer Valores Predeterminados' en la modal que regrese todas las opciones a los valores de fábrica con confirmación.

---
> [Índice General](../README.md) · [← Ejercicio 041](../ejercicio_041/README.md) · [Ejercicio 043 →](../ejercicio_043/README.md)
