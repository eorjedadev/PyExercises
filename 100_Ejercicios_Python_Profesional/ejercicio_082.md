# Ejercicio 082 — Vista previa y confirmación de cambios de precios

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_081.md) · [Siguiente](ejercicio_083.md)

### Contexto

Un operador necesita revisar una importación antes de aplicarla a un catálogo que puede cambiar.

### Situación

El encargo es **vista previa y confirmación de cambios de precios**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Vista previa y resultado aplicado/conflicto con catálogo final**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Catálogo con revisión entera, propuesta de precios positivos por código y revisión esperada al confirmar.

### Resultado esperado

Vista previa y resultado aplicado/conflicto con catálogo final.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Vista previa muestra anteriores y nuevos sin mutar.
- Códigos desconocidos invalidan propuesta.
- Confirmación exige misma revisión que la vista previa.
- Aplicar todo o nada.
- Una aplicación exitosa aumenta revisión en1.
- Propuesta vacía no aumenta revisión.

### Casos especiales y límites

Confirmar dos veces la misma propuesta no debe aplicarla dos veces.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Invariantes y operaciones dependientes del estado vigente.
- Propiedad de los datos y modificaciones compartidas.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Explican por qué una modificación puede aparecer en otra parte del programa.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **revisión observada, propuesta pendiente, precio anterior, confirmación**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué dato vincula la revisión humana con el estado que realmente se cambia?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 042](ejercicio_042.md), [ejercicio 053](ejercicio_053.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Revisión4, A100, propuestaA120 →previa100→120; confirmar4 →A120,rev5.
2. Confirmar con catálogo ya rev5 →conflicto.
3. Propuesta vacía →sin cambios.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Aplicar una vista previa obsoleta sobre cambios posteriores.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md — Capítulo 6. Referencias, mutabilidad y ciclo de vida de objetos](../luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md#capitulo-6-referencias-mutabilidad-y-ciclo-de-vida-de-objetos).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Revisión4, A100, propuestaA120 →previa100→120; confirmar4 →A120,rev5**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué dato vincula la revisión humana con el estado que realmente se cambia?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Flujos de aprobación vinculan una vista previa con la revisión del estado que se pretende modificar. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Informar diferencias que ocurrieron desde la revisión observada.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
