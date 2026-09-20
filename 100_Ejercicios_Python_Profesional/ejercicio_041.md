# Ejercicio 041 — Importación de una lista de tareas

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_040.md) · [Siguiente](ejercicio_042.md)

### Contexto

Una oficina recibe cada mañana un archivo de texto con tareas para revisar.

### Situación

El encargo es **importación de una lista de tareas**. Separa las reglas de transformación de los efectos externos que existan. Prepara ejemplos reproducibles y comprueba qué datos quedan después de un rechazo.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Tareas con número de línea original y cantidad de líneas omitidas**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Ruta de archivo UTF-8; una tarea por línea física.

### Resultado esperado

Tareas con número de línea original y cantidad de líneas omitidas.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Recortar extremos.
- Omitir líneas vacías y líneas cuyo primer carácter tras recortar sea #.
- Conservar duplicados y orden.
- Archivo inexistente se informa sin crear nada.

### Casos especiales y límites

Los números de línea no deben reiniciarse tras filtrar.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Rutas, archivos, codificación y gestión de recursos**. Tema para investigar: Comprende modos de apertura, cierre de recursos, UTF-8 y efectos de sobrescribir un archivo.
- **Cadenas, métodos de texto y comparaciones**. Tema para investigar: Investiga recorte, partición, pertenencia y diferencias entre igualdad textual y equivalencia definida por negocio.
- **Excepciones y resultados de validación**. Tema para investigar: Investiga qué fallos puedes recuperar, cuáles debes propagar y cómo conservar su causa.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Conectan los datos del programa con recursos que pueden faltar o fallar.
- Permiten separar el texto recibido de la forma usada para validarlo o compararlo.
- Separan entradas rechazadas y problemas operativos de un resultado correcto.

### Variables y nombres

Identifica estas entidades: **ruta de origen, línea física, tarea limpia, líneas omitidas**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué responsabilidades son distintas entre leer un archivo y decidir si una línea es tarea?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 010](ejercicio_010.md), [ejercicio 020](ejercicio_020.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Líneas '# nota', ' Llamar ', '', 'Llamar' → tareas en 2 y 4, dos omitidas.
2. Archivo vacío → cero tareas.
3. Ruta ausente → error legible.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Perder la posición original al filtrar antes de numerar.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Archivos y Context Managers](../Universidad_Python.md#archivos-y-context-managers).
- [Diccionario_Python.md — Métodos de Cadenas](../Diccionario_Python.md#m%C3%A9todos-de-cadenas).
- [Universidad_Python.md — Manejo de Errores y Excepciones](../Universidad_Python.md#manejo-de-errores-y-excepciones).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Líneas '# nota', ' Llamar ', '', 'Llamar' → tareas en 2 y 4, dos omitidas**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué responsabilidades son distintas entre leer un archivo y decidir si una línea es tarea?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Automatizaciones administrativas filtran archivos de texto conservando posiciones para revisar el origen de cada dato. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir un informe separado de tareas repetidas conservando todas las líneas.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
