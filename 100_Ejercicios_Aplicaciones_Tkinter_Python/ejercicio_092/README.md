## Ejercicio 092 — Formulario Accesible por Teclado con Atajos y Navegación Universal (`AccessibleFormApp`)

> [Índice General](../README.md) · [← Ejercicio 091](../ejercicio_091/README.md) · [Ejercicio 093 →](../ejercicio_093/README.md)

### Contexto profesional
En dependencias públicas y empresas que atienden estándares de accesibilidad universal (WCAG para aplicaciones de escritorio), los operadores con discapacidades motrices o visuales parciales deben poder operar formularios completos exclusivamente mediante el teclado.

### Usuario objetivo
Operador de datos con discapacidad visual/motriz o digitador intensivo de alta velocidad.

### Problema
Formularios diseñados sin orden lógico de foco (`focus traversal`), sin etiquetas asociadas ni atajos universales de teclado ralentizan el trabajo y excluyen a usuarios que no pueden utilizar el ratón.

### Objetivo
Desarrollar un formulario corporativo de alta velocidad y accesibilidad universal con Tkinter, que garantice orden estricto de navegación con `Tab` y `Shift+Tab`, atajos de teclado mnemónicos con `Alt+Letra` para cada control, confirmación con `Enter`, cancelación con `Escape`, retroalimentación visual destacada de foco activo (borde de alto contraste) y mensajes de estado legibles.

### Flujo principal
El operador abre el formulario. El foco se sitúa de inmediato en el primer campo con un contorno visual llamativo. El usuario llena los campos y navega fluidamente con la tecla `Tab` sin tocar el ratón. Puede usar combinaciones `Alt+N` para saltar directamente al campo Nombre o `Alt+G` para presionar el botón Guardar. Al presionar `Enter`, se valida y envía el formulario; con `Escape` se cancela la captura.

### Requisitos funcionales
- Orden estricto y predecible de tabulación entre todos los controles interactivos (`Tab` para avanzar, `Shift+Tab` para retroceder).
- Resalte visual de foco activo: cuando un campo recibe el foco (`<FocusIn>`), su borde cambia a color azul brillante de alto contraste; al perderlo (`<FocusOut>`), vuelve a su estado normal.
- Teclas mnemónicas con `Alt`: cada etiqueta debe tener una letra subrayada asociada a su campo mediante bindings (ej. `Alt+N` para Nombre, `Alt+C` para Correo, `Alt+G` para Guardar).
- Teclas de acción universales: `Enter` envía el formulario desde cualquier campo; `Escape` limpia y cancela con confirmación.
- Todos los widgets interactivos deben tener etiquetas legibles y fuentes con contraste cromático superior a 4.5:1 (estándar WCAG AA).
- Confirmación sonora sutil opcional al guardar o cometer un error.

### Requisitos de interfaz
- Formulario limpio con espaciado vertical generoso (mínimo 8 px entre filas).
- Tipografías legibles con tamaño no menor a 11 puntos.
- Indicadores mnemónicos claros en el texto de las etiquetas.

### Datos
- Ficha de operador: nombre, identificacion, departamento, telefono, notas.

### Estado
- Widget que posee el foco activo actualmente.
- Estado del formulario.

### Persistencia
No requiere persistencia en disco en esta fase (almacena en memoria de sesión).

### Validaciones
- Validaciones obligatorias de campos al presionar `Enter` o el botón Guardar.

### Casos límite
- Navegar con `Tab` desde el último widget de la ventana (el foco debe ciclar ordenadamente al primer widget sin perderse).
- Presionar un atajo mnemónico mientras se redacta texto en un área multilínea.

### Manejo de errores
- Al fallar la validación, el foco del teclado debe trasladarse automáticamente al campo específico que contiene el error.

### Fundamentos de Python relacionados
- Manejo de accesibilidad y diseño centrado en el usuario.
- Mapeo de atajos y eventos de teclado universales.

### Conceptos Tkinter relacionados
- Eventos de foco `<FocusIn>` y `<FocusOut>`.
- Enlaces de atajos con modificador Alt (`<Alt-Key-n>`, `<Alt-Key-g>`).
- Métodos de manipulación de foco: `widget.focus_set()`, `widget.focus_get()`.
- Propiedad `underline` en widgets `Label` para indicar mnemónicos.

### Herramientas para investigar
- Pautas de accesibilidad para software de escritorio (WCAG 2.1 aplicadas a desktop).
- Manejo de foco y parámetro `underline` en Tkinter.

### Diseño de interfaz
¿Cómo asegurarías que el resalte visual del campo con foco activo sea lo suficientemente notorio para personas con debilidad visual?

### Diseño de variables
Usa nombres como `name_field_entry`, `id_field_entry`, `dept_field_combo`, `save_action_btn`, `cancel_action_btn`, `focus_highlighter`.

### Antes de programar
1. ¿Cómo se asocia el parámetro `underline=0` en una `Label` con un evento `<Alt-n>` para que al presionar la tecla el cursor salte automáticamente al `Entry` contiguo?
2. ¿Cómo se asegura en Tkinter que el orden de tabulación siga exactamente el orden de creación o empaquetado de los widgets?

### Arquitectura
```
ejercicio_092/
├── app.py             # Formulario accesible y navegación universal
├── focus_helper.py    # Gestor de efectos visuales de foco (FocusIn / FocusOut)
└── key_bindings.py    # Centralización de atajos mnemónicos y teclas Enter/Escape
```

### Pruebas mínimas
1. Abrir la app y presionar `Tab` 5 veces -> El foco debe recorrer ordenadamente cada campo y volver al primero.
2. Presionar `Alt+N` -> El cursor debe situarse de inmediato en el campo Nombre.
3. Presionar `Enter` con datos válidos -> Debe guardar y limpiar el formulario.

### Pruebas de error
1. Presionar `Enter` con campos vacíos -> El cursor debe saltar automáticamente al primer campo vacío y resaltarse en rojo.

### Experiencia de usuario
La experiencia de llenado de formularios debe ser sumamente veloz y fluida para operadores que trabajan exclusivamente con el teclado sin tocar el ratón.

### Explicación posterior
¿Cómo contribuyen el orden riguroso de foco, los mnemónicos y el resaltado visual a la accesibilidad e inclusión en el desarrollo de software de escritorio?

### Aplicación profesional
Sistemas de captura masiva de datos en dependencias gubernamentales, terminales de facturación de alta velocidad en aduanas y aplicaciones certificadas en accesibilidad.

### Reto adicional
Añade una opción para agrandar toda la tipografía de la interfaz a 'Modo Fuente Grande (14 pt)' con reajuste automático de espaciados.

---
> [Índice General](../README.md) · [← Ejercicio 091](../ejercicio_091/README.md) · [Ejercicio 093 →](../ejercicio_093/README.md)
