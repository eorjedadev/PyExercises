# Ejercicio 087 — Edición por lotes con reversión completa

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_086.md) · [Siguiente](ejercicio_088.md)

### Contexto

Una aplicación actualiza varias fichas como una sola operación de trabajo.

### Situación

El encargo es **edición por lotes con reversión completa**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Nuevo estado independiente o rechazo sin efectos parciales**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Mapa de fichas id→nombre no vacío y lote ordenado de crear, renombrar o eliminar.

### Resultado esperado

Nuevo estado independiente o rechazo sin efectos parciales.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Crear exige id ausente.
- Renombrar/eliminar exigen presente.
- Nombre nuevo no vacío.
- Evaluar sobre estado provisional.
- Ante primera falla rechazar lote completo y devolver posición.
- Entradas originales intactas.

### Casos especiales y límites

Una operación posterior puede depender de una creación anterior del lote.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Propiedad de los datos y modificaciones compartidas.
- Invariantes y operaciones dependientes del estado vigente.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Explican por qué una modificación puede aparecer en otra parte del programa.
- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **estado confirmado, cambio provisional, posición fallida, lote rechazado**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Cómo demostrarás que no quedan efectos después de una falla tardía?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 053](ejercicio_053.md), [ejercicio 069](ejercicio_069.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Crear A,renombrar A Ana →A:Ana.
2. Crear A,eliminar X ausente →rechazo sin A.
3. Lote vacío →equivalente al original.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Restaurar solo el último cambio y dejar otros aplicados.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md — Capítulo 6. Referencias, mutabilidad y ciclo de vida de objetos](../luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md#capitulo-6-referencias-mutabilidad-y-ciclo-de-vida-de-objetos).
- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Crear A,renombrar A Ana →A:Ana**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Cómo demostrarás que no quedan efectos después de una falla tardía?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Edición de entidades por lotes protege el estado confirmado frente a fallos que aparecen después de varios cambios válidos. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Agregar validación final que prohíba nombres duplicados entre fichas.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
