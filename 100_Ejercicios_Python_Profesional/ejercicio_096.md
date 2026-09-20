# Ejercicio 096 — Plantillas de mensajes con contrato acotado

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_095.md) · [Siguiente](ejercicio_097.md)

### Contexto

Un equipo redacta avisos reutilizables sin permitir expresiones ejecutables.

### Situación

El encargo es **plantillas de mensajes con contrato acotado**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Mensaje renderizado o diagnóstico, y claves no utilizadas**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Plantilla y mapa de valores textuales; marcadores con forma {{nombre}}, nombre compuesto por letras ASCII y guion bajo, al menos un carácter.

### Resultado esperado

Mensaje renderizado o diagnóstico, y claves no utilizadas.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Sustituir marcadores existentes.
- Clave ausente produce error sin salida parcial.
- Claves sobrantes se informan.
- Cualquier par de llaves mal formado se rechaza.
- Llaves sueltas se rechazan.
- Valores insertados son literales y no se vuelven a interpretar.

### Casos especiales y límites

Un reemplazo no debe convertirse en una segunda plantilla.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Identidad textual, normalización y formatos admitidos.
- Contratos, parámetros explícitos y responsabilidades comprobables.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Permiten separar el texto recibido de la forma usada para validarlo o compararlo.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **plantilla original, marcador reconocido, valor literal, clave faltante**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué distingue datos de una instrucción dentro de este contrato?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 005](ejercicio_005.md), [ejercicio 016](ejercicio_016.md), [ejercicio 068](ejercicio_068.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. 'Hola {{nombre}}' con nombre Ana →Hola Ana.
2. Nombre ausente →error.
3. Valor '{{otro}}' →se inserta literalmente.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Usar evaluación de código para resolver marcadores textuales.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Diccionario_Python.md — Métodos de Cadenas](../Diccionario_Python.md#m%C3%A9todos-de-cadenas).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **'Hola {{nombre}}' con nombre Ana →Hola Ana**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué distingue datos de una instrucción dentro de este contrato?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Generación de mensajes separa sustitución literal de interpretación y valida un lenguaje deliberadamente acotado. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Permitir escapar llaves con una sintaxis nueva y pruebas de ambigüedad.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
