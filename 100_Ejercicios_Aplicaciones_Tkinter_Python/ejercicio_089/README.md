## Ejercicio 089 — Aplicación con Motor de Temas Dinámicos y Soporte Claro/Oscuro (`ThemeEngineApp`)

> [Índice General](../README.md) · [← Ejercicio 088](../ejercicio_088/README.md) · [Ejercicio 090 →](../ejercicio_090/README.md)

### Contexto profesional
En suites de productividad modernas y software para entornos nocturnos (centros de control, terminales de despacho), los usuarios exigen la capacidad de alternar entre temas Claro (Light) y Oscuro (Dark) sin reiniciar la aplicación.

### Usuario objetivo
Operador de turno diurno/nocturno o usuario corporativo.

### Problema
Cambiar colores widget por widget recorriendo la jerarquía de forma artesanal genera código espagueti difícil de mantener y componentes con contrastes rotos.

### Objetivo
Desarrollar una aplicación de escritorio que implemente un motor formal de temas visuales utilizando la clase `ttk.Style`, definiendo paletas centralizadas de tokens de diseño (fondos, textos, acentos, selecciones) para temas 'Claro' y 'Oscuro', con cambio en caliente instantáneo y persistencia de la preferencia en `preferencias_tema.json`.

### Flujo principal
El usuario abre la aplicación y visualiza un panel con diversos widgets `ttk` (Botones, Entradas, Combobox, Treeview, Checkbuttons, Notebook). En la barra superior, hace clic en el interruptor de tema 'Modo Oscuro'. El motor de temas reconfigura los estilos globales de `ttk.Style` de inmediato: los fondos cambian a tonos carbón/gris oscuro, los textos a blanco/plata y los acentos a azul brillante, sin destruir ni recargar ninguna ventana. La preferencia se guarda en disco.

### Requisitos funcionales
- Definición centralizada de tokens de diseño en diccionarios de temas: Colores de Fondo Primario/Secundario, Texto Principal/Secundario, Borde, Acento Activo y Selección.
- Implementación formal mediante `ttk.Style()` configurando estilos derivados (`TLabel`, `TButton`, `TEntry`, `Treeview`, `TNotebook`).
- Selector o botón para alternar en caliente entre 'Modo Claro' y 'Modo Oscuro'.
- Actualización de elementos nativos de Tkinter (`Tk`, `Canvas`, `Text`) enlazados a la paleta centralizada.
- Persistencia automática de la selección de tema en archivo `preferencias_tema.json`.
- Carga del tema guardado al reiniciar la aplicación.

### Requisitos de interfaz
- Interfaz rica que incluya múltiples tipos de componentes para comprobar la consistencia del tema: pestañas, tablas, botones de acción, casillas y entradas de texto.
- Contraste tipográfico que cumpla con legibilidad visual en ambos modos.
- Interruptor de tema claramente identificable en la barra superior.

### Datos
- Paleta de tema: diccionario con tokens hexadecimales (`bg_primary`, `fg_primary`, `accent`, `tree_selected`, etc.).
- Archivo de preferencias: JSON.

### Estado
- Tema actualmente activo ('light' | 'dark').
- Instancia de `ttk.Style` configurada.

### Persistencia
Archivo JSON (`config/preferencias_tema.json`).

### Validaciones
- Verificar que los tokens de color sean códigos hexadecimales válidos de 7 caracteres (`#RRGGBB`).

### Casos límite
- Cambiar de tema con un menú desplegable abierto o una celda de tabla en selección.
- Archivo de preferencias inexistente (iniciar con el tema claro por defecto).

### Manejo de errores
- Manejar estilos no compatibles con el tema del sistema operativo garantizando la aplicación de colores sobre temas base como `'clam'` o `'alt'`.

### Fundamentos de Python relacionados
- Diccionarios de configuración y tokens de diseño estructurados.
- Persistencia JSON y lectura segura de ajustes.

### Conceptos Tkinter relacionados
- Uso profesional de `ttk.Style` (`theme_use('clam')`, `configure()`, `map()`).
- Mapeo de estados dinámicos en widgets con `style.map('TButton', background=[('active', ...), ('disabled', ...)])`.

### Herramientas para investigar
- Métodos `.configure()` y `.map()` en la clase `ttk.Style`.
- Temas base de ttk compatibles (`clam`, `alt`, `default`).

### Diseño de interfaz
¿Cómo asegurarías que los contrastes de texto sobre fondo cumplan con una lectura cómoda tanto en monitores de alto brillo como en salas oscuras?

### Diseño de variables
Usa nombres como `theme_engine`, `style_manager`, `toggle_theme_btn`, `current_theme_name`, `demo_treeview`, `demo_notebook`.

### Antes de programar
1. ¿Por qué es fundamental seleccionar un tema base como `'clam'` con `style.theme_use('clam')` antes de personalizar colores para asegurar compatibilidad en Windows y Linux?
2. ¿Cómo se utiliza `style.map()` para definir cómo debe verse un botón cuando el usuario pasa el ratón por encima o cuando está deshabilitado?

### Arquitectura
```
ejercicio_089/
├── app.py             # Ventana de demostración con múltiples widgets ttk
├── theme_engine.py    # Motor central de estilos, paletas y reconfiguración con ttk.Style
├── palettes.py        # Diccionarios de tokens para Modo Claro y Modo Oscuro
└── config/
    └── preferencias_tema.json # Persistencia del tema activo
```

### Pruebas mínimas
1. Cambiar a Modo Oscuro -> Todos los widgets (botones, entradas, Treeview y pestañas) deben tornarse oscuros con texto claro inmediatamente.
2. Reiniciar la aplicación -> Debe arrancar directamente en Modo Oscuro leyendo el archivo JSON.

### Pruebas de error
1. Dañar el archivo de preferencias -> Debe arrancar en Modo Claro por defecto sin arrojar excepciones.

### Experiencia de usuario
La transición debe ser instantánea y no debe dejar ningún widget con colores huérfanos del tema anterior.

### Explicación posterior
¿Cómo garantiza el uso centralizado de `ttk.Style` frente a colorear widgets manualmente la escalabilidad y mantenibilidad de temas visuales en aplicaciones grandes?

### Aplicación profesional
Consolas de monitoreo nocturno de seguridad, herramientas para desarrolladores, suites ofimáticas y software médico.

### Reto adicional
Añade un tercer tema temático de alto contraste (ej. 'Contraste Alto / Accesibilidad') con fondo negro puro y textos amarillo brillante.

---
> [Índice General](../README.md) · [← Ejercicio 088](../ejercicio_088/README.md) · [Ejercicio 090 →](../ejercicio_090/README.md)
