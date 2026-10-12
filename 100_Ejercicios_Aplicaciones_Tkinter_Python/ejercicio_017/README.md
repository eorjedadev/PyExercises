## Ejercicio 017 — Validador y Probador Local de Expresiones Regulares (`RegexTesterApp`)

> [Índice General](../README.md) · [← Ejercicio 016](../ejercicio_016/README.md) · [Ejercicio 018 →](../ejercicio_018/README.md)

### Contexto profesional
En desarrollo de software y análisis forense de datos, los programadores necesitan probar patrones de expresiones regulares contra muestras de texto sin enviar datos confidenciales a evaluadores web públicos.

### Usuario objetivo
Desarrollador de software, analista de datos o auditor de seguridad.

### Problema
El uso de testers de regex en línea expone fragmentos de datos sensibles (PII, tokens, logs internos) a servidores de terceros no autorizados.

### Objetivo
Desarrollar un evaluador de expresiones regulares local con Tkinter que reciba un patrón, opciones de coincidencia (Ignore Case, Multiline) y un texto de prueba, resaltando visualmente todas las coincidencias encontradas dentro de un widget `Text` mediante tags.

### Flujo principal
El usuario escribe una expresión regular (ej. `\d{3}-\d{4}`), selecciona banderas opcionales y escribe o pega texto en el área de prueba. El sistema compila el regex, resalta en color amarillo todas las coincidencias en el texto e informa cuántas coincidencias se encontraron y sus posiciones.

### Requisitos funcionales
- Campo para patrón regex (`Entry`).
- Casillas para banderas de regex: `re.IGNORECASE`, `re.MULTILINE`, `re.DOTALL`.
- Área de texto para la muestra de prueba (`Text`).
- Resaltado de coincidencias mediante el sistema de tags del widget `Text` de Tkinter.
- Contador de coincidencias totales encontradas.
- Captura y visualización clara de errores de sintaxis (`re.error`) sin que la app falle.

### Requisitos de interfaz
- Barra superior con campo de patrón y checkboxes de flags.
- Área central amplia para el texto de prueba con barras de desplazamiento.
- Barra inferior de estado con el recuento de coincidencias o la descripción del error de sintaxis en color rojo.

### Datos
- Patrón regex: cadena.
- Muestra de texto: cadena multilínea.
- Coincidencias: lista de objetos `Match` o tuplas de índices `(inicio, fin)`.

### Estado
- Expresión compilada activa.
- Lista de rangos coincidentes.

### Persistencia
No requiere persistencia en disco.

### Validaciones
- Verificar que el patrón sea una expresión regular válida en Python antes de intentar buscar coincidencias.

### Casos límite
- Patrón regex vacío (no debe resaltar nada ni generar bucles infinitos).
- Patrones que coinciden con cadenas de longitud cero (ej. `^` o `.*`).
- Expresiones con sintaxis inválida (ej. corchetes no cerrados `[a-z`).

### Manejo de errores
- Capturar explícitamente `re.error` y mostrar el mensaje técnico de error en la barra de estado de forma legible.

### Fundamentos de Python relacionados
- Módulo `re` de Python (`re.compile`, `re.finditer`, `re.error`).
- Operador bitwise OR (`|`) para combinar flags de expresiones regulares (`re.I | re.M`).

### Conceptos Tkinter relacionados
- Sistema de tags en widget `Text`: `.tag_add(nombre, inicio, fin)`, `.tag_config(nombre, background=...)`, `.tag_remove(nombre, '1.0', 'end')`.
- Conversión de índices numéricos de Python a formato de coordenadas de texto en Tkinter (`'1.0 + {offset} chars'`).

### Herramientas para investigar
- Métodos de tags en `tkinter.Text`.
- Excepciones del módulo `re` (`re.error`).

### Diseño de interfaz
¿Cómo asegurarías que el color de resaltado de las coincidencias tenga buen contraste y no oculte el texto original?

### Diseño de variables
Usa nombres como `pattern_entry`, `case_flag_var`, `multi_flag_var`, `sample_text_widget`, `match_status_label`.

### Antes de programar
1. ¿Cómo se limpia un tag de resaltado anterior en un widget `Text` antes de aplicar uno nuevo?
2. ¿Cómo se traduce la posición numérica de un objeto `re.Match.start()` al sistema de coordenadas `'linea.columna'` de Tkinter?

### Arquitectura
```
ejercicio_017/
├── app.py          # Interfaz gráfica y gestión de tags en Text
└── regex_engine.py # Compilación de patrones y extracción de rangos de coincidencia
```

### Pruebas mínimas
1. Ingresar patrón `\d+` y muestra 'Tengo 25 manzanas y 10 peras' -> Debe encontrar 2 coincidencias y resaltarlas en amarillo.
2. Activar 'Ignore Case' y buscar `hola` en 'Hola HOLA' -> Debe encontrar 2 coincidencias.

### Pruebas de error
1. Ingresar patrón `[` (incompleto) -> Debe mostrar en rojo 'Error de sintaxis: unterminated character set' sin lanzar traceback no capturado.

### Experiencia de usuario
La actualización al escribir en el patrón o muestra debe ser ágil y borrar inmediatamente cualquier resaltado obsoleto.

### Explicación posterior
¿Cómo funciona el direccionamiento por tags en los widgets `Text` de Tkinter para formatear fragmentos específicos de texto?

### Aplicación profesional
Herramientas internas para desarrollo de pipelines de extracción de datos, linters y auditorías de seguridad.

### Reto adicional
Añade un panel lateral que muestre una lista con los grupos de captura (`group(1)`, `group(2)`) de cada coincidencia encontrada.

---
> [Índice General](../README.md) · [← Ejercicio 016](../ejercicio_016/README.md) · [Ejercicio 018 →](../ejercicio_018/README.md)
