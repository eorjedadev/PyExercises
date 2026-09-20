# Ejercicio 067 — Página de resultados con desempate

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_066.md) · [Siguiente](ejercicio_068.md)

### Contexto

Una herramienta interna muestra partes de un reporte ordenado.

### Situación

El encargo es **página de resultados con desempate**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Items de página, total de registros y total de páginas**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Registros con id único y puntaje entero; página desde1 y tamaño positivo.

### Resultado esperado

Items de página, total de registros y total de páginas.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Ordenar puntaje descendente e id ascendente.
- Página fuera del rango devuelve lista vacía.
- Conjunto vacío tiene cero páginas.
- No modificar registros originales.

### Casos especiales y límites

El mismo conjunto en diferente orden de entrada debe producir las mismas páginas.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Comparación total, estabilidad y desempates reproducibles.
- Orden, posiciones y conservación de relaciones.
- Contratos, parámetros explícitos y responsabilidades comprobables.

### ¿Por qué pueden ser útiles?

- Hacen reproducibles las prioridades y sus desempates.
- Representan grupos donde la posición, el orden o la asociación de varios valores tiene significado.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **orden total, número de página, tamaño de página, total de resultados**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué garantiza que un empate no haga saltar registros entre páginas?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 025](ejercicio_025.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. A10,B10,C5; tamaño2,página1 →A,B;2 páginas.
2. Página2 →C.
3. Página3 →vacío conservando total3.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Ordenar solo por puntaje y depender de un orden accidental.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Funciones Integradas](../Universidad_Python.md#funciones-integradas).
- [Universidad_Python.md — Listas](../Universidad_Python.md#listas).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A10,B10,C5; tamaño2,página1 →A,B;2 páginas**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué garantiza que un empate no haga saltar registros entre páginas?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Reportes paginados requieren un orden total para evitar que los empates cambien de página arbitrariamente. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir un filtro previo y distinguir total filtrado de total original.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
