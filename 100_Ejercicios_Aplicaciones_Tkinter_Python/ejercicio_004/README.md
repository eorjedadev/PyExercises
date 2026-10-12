## Ejercicio 004 — Generador Seguro de Contraseñas Corporativas (`PassGenApp`)

> [Índice General](../README.md) · [← Ejercicio 003](../ejercicio_003/README.md) · [Ejercicio 005 →](../ejercicio_005/README.md)

### Contexto profesional
Los administradores de sistemas y analistas de ciberseguridad necesitan generar credenciales seguras para nuevos colaboradores según políticas corporativas de longitud y complejidad.

### Usuario objetivo
Administrador de sistemas (SysAdmin) o técnico de soporte de identidades.

### Problema
Los usuarios tienden a inventar claves débiles o predecibles si no disponen de una herramienta local y rápida que además permita copiarla al portapapeles sin pasar por sitios web externos potencialmente inseguros.

### Objetivo
Construir una aplicación que genere contraseñas criptográficamente seguras con longitud parametrizable (8 a 64 caracteres), opciones de inclusión de mayúsculas, minúsculas, números y caracteres especiales, indicador visual de entropía y copiado con un clic.

### Flujo principal
El usuario ajusta la longitud deseada con un control deslizante (`Scale`), activa o desactiva casillas de verificación (`Checkbutton`) para los juegos de caracteres requeridos, presiona 'Generar', observa la contraseña generada y una barra o etiqueta que indica la fuerza de la clave, y hace clic en 'Copiar al portapapeles'.

### Requisitos funcionales
- Deslizador o selector numérico de longitud de clave (mínimo 8, máximo 64, por defecto 16).
- Casillas de selección para: Mayúsculas (A-Z), Minúsculas (a-z), Dígitos (0-9) y Símbolos especiales (!@#$%^&*).
- Opción para excluir caracteres visualmente ambiguos (ej. 0, O, l, 1, I).
- Generación utilizando generador criptográfico (`secrets` de Python).
- Botón para copiar la contraseña generada directamente al portapapeles del sistema operativo.

### Requisitos de interfaz
- Control `ttk.Scale` acoplado a una etiqueta numérica que muestre el valor actual de la longitud.
- Grupo de `ttk.Checkbutton` alineados en un marco rotulado ('Opciones de Complejidad').
- Campo de texto o `Entry` de sólo lectura (`state='readonly'`) para la contraseña generada.
- Etiqueta o barra coloreada de fortaleza (Débil = rojo, Media = amarillo, Fuerte = verde).
- Botón con feedback visual temporal ('¡Copiado!') tras enviar al portapapeles.

### Datos
- Longitud: entero (8 a 64).
- Banderas booleanas para cada conjunto de caracteres.
- Contraseña generada: cadena de texto (`str`).
- Nivel de entropía calculado en bits: flotante.

### Estado
- Variables `BooleanVar` para las casillas de verificación.
- Variable `IntVar` para la longitud de contraseña.
- Variable `StringVar` para el texto de la clave generada.

### Persistencia
No persiste contraseñas en disco por motivos elementales de seguridad.

### Validaciones
- Verificar que al menos un conjunto de caracteres esté seleccionado antes de intentar generar una contraseña.
- La longitud debe ser mayor o igual a 8.

### Casos límite
- El usuario desmarca todas las casillas de verificación y presiona 'Generar'.
- El usuario selecciona exclusión de ambiguos en una longitud grande.
- Intentar copiar al portapapeles cuando aún no se ha generado ninguna contraseña.

### Manejo de errores
- Mostrar mensaje de error si ninguna opción de caracteres está seleccionada, impidiendo la generación.

### Fundamentos de Python relacionados
- Módulo `secrets` de la biblioteca estándar (`secrets.choice`).
- Módulo `string` (`string.ascii_uppercase`, `string.digits`, etc.).
- Cálculo de entropía de contraseñas: $E = L \times \log_2(N)$ donde $L$ es la longitud y $N$ el tamaño del alfabeto.

### Conceptos Tkinter relacionados
- Widgets `ttk.Checkbutton`, `ttk.Scale`, `ttk.LabelFrame`.
- Manipulación del portapapeles del sistema mediante `root.clipboard_clear()` y `root.clipboard_append()`.
- Control de estado de widgets (`state='readonly'` y `state='normal'`).

### Herramientas para investigar
- Métodos de clipboard en Tkinter.
- Documentación del módulo `secrets` en Python 3.

### Diseño de interfaz
¿Cómo asegurarías que el campo de la contraseña sea visiblemente prominente y no se pueda modificar accidentalmente con el teclado?

### Diseño de variables
Usa nombres como `length_var`, `use_upper_var`, `use_digits_var`, `use_symbols_var`, `exclude_ambiguous_var`, `password_display_var`.

### Antes de programar
1. ¿Por qué nunca se debe utilizar el módulo `random` para contraseñas de seguridad corporativa?
2. ¿Cómo garantizas que la contraseña incluya al menos un carácter de cada tipo seleccionado?

### Arquitectura
```
ejercicio_004/
├── app.py           # Vistas y eventos de Tkinter
└── generator.py     # Lógica criptográfica y cálculo de entropía pura
```

### Pruebas mínimas
1. Seleccionar longitud 20 con todos los tipos habilitados -> Comprobar que la longitud sea 20 y contenga caracteres de cada familia.
2. Presionar 'Copiar' -> Pegar en un bloc de notas y verificar coincidencia exacta.

### Pruebas de error
1. Desmarcar todas las opciones y presionar 'Generar' -> Debe advertir al usuario que debe seleccionar al menos una categoría de caracteres.

### Experiencia de usuario
Tras presionar 'Copiar', el botón debe mostrar '¡Copiado al portapapeles!' durante 2 segundos antes de volver a su texto habitual mediante `.after()`.

### Explicación posterior
¿Qué métodos de Tkinter permiten interactuar con el portapapeles del sistema operativo y qué precauciones deben tomarse al manipularlo?

### Aplicación profesional
Módulos de creación de usuarios en paneles de administración interna, gestores locales de credenciales y terminales de provisioning.

### Reto adicional
Agrega una opción para generar contraseñas en formato frase de contraseña (*Passphrase*) compuesta por 4 o 5 palabras aleatorias en español separadas por guiones.

---
> [Índice General](../README.md) · [← Ejercicio 003](../ejercicio_003/README.md) · [Ejercicio 005 →](../ejercicio_005/README.md)
