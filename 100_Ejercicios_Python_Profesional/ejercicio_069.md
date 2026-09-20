# Ejercicio 069 — Combinación de propuestas de edición

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_068.md) · [Siguiente](ejercicio_070.md)

### Contexto

Dos personas editan campos distintos de una ficha y el sistema debe detectar conflictos.

### Situación

El encargo es **combinación de propuestas de edición**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Propuesta combinada para campos no conflictivos y detalles base/A/B de cada conflicto**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Tres mapas con las mismas claves: base, propuesta A y propuesta B; valores escalares.

### Resultado esperado

Propuesta combinada para campos no conflictivos y detalles base/A/B de cada conflicto.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Si solo una propuesta difiere de base, tomarla.
- Si ambas cambian al mismo valor, aceptarlo.
- Si cambian a valores distintos, marcar conflicto.
- No guardar una ficha final mientras haya conflictos.

### Casos especiales y límites

Volver al valor base en una rama cuenta como no cambiar ese campo.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Identidad de entidades y organización de datos relacionados.
- Propiedad de los datos y modificaciones compartidas.
- Contratos, parámetros explícitos y responsabilidades comprobables.

### ¿Por qué pueden ser útiles?

- Relacionan identidades con atributos, estados o acumulados consultables.
- Explican por qué una modificación puede aparecer en otra parte del programa.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **valor base, propuesta de cada editor, campo en conflicto, combinación provisional**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué aporta la versión base que no aportaría comparar solo A y B?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 020](ejercicio_020.md), [ejercicio 030](ejercicio_030.md), [ejercicio 053](ejercicio_053.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Base nombre Ana,ciudad Lima; A cambia nombre, B cambia ciudad →combina ambos.
2. Ambas cambian ciudad a Cusco →sin conflicto.
3. A Cusco,B Piura →conflicto.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Elegir siempre la última propuesta y perder cambios válidos.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md — Capítulo 6. Referencias, mutabilidad y ciclo de vida de objetos](../luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md#capitulo-6-referencias-mutabilidad-y-ciclo-de-vida-de-objetos).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Base nombre Ana,ciudad Lima; A cambia nombre, B cambia ciudad →combina ambos**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué aporta la versión base que no aportaría comparar solo A y B?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Edición colaborativa necesita una versión base para distinguir cambios compatibles de conflictos reales. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Permitir claves añadidas o eliminadas con una marca explícita de ausencia.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
