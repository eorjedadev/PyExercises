# Ejercicio 015 — Comparación de dos presupuestos

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_014.md) · [Siguiente](ejercicio_016.md)

### Contexto

Compras compara ofertas que incluyen precio por unidad y transporte fijo.

### Situación

El encargo es **comparación de dos presupuestos**. Puedes empezar con valores preparados y una salida por consola. Mantén separadas las reglas del formato de los mensajes; no es obligatorio construir un menú.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Totales, oferta u ofertas elegidas y diferencia de coste**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Dos ofertas con nombre, precio unitario positivo en céntimos, transporte no negativo y una cantidad común positiva.

### Resultado esperado

Totales, oferta u ofertas elegidas y diferencia de coste.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Calcular total de cada oferta para toda la cantidad.
- Seleccionar menor total.
- Conservar ambos nombres en empate.

### Casos especiales y límites

La oferta más barata por unidad puede resultar más costosa.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Enteros, operadores aritméticos y formato de resultados**. Comprende operaciones y precedencia; distingue valor, unidad y formato. Investiga división entera, resto o redondeo solo cuando las reglas los requieran.
- **Condicionales, booleanos y operadores de comparación**. Comprende límites inclusivos, condiciones compuestas y orden de evaluación antes de elegir ramas.
- **Funciones, parámetros, retornos y contratos**. Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

### ¿Por qué pueden ser útiles?

- Representan cantidades y unidades sin mezclar el dato calculado con su presentación.
- Expresan las condiciones del contrato y la prioridad entre decisiones que pueden coincidir.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **coste unitario, transporte fijo, coste comparable, diferencia**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué dato cambia entre ofertas y cuál es compartido?
- ¿Cuáles son las entradas, sus unidades y el resultado que podrías comprobar a mano?
- ¿Qué entrada está justo en un límite y qué cambia al pasar al valor siguiente?
- ¿Cómo representarías un caso válido y un rechazo sin escribir aún el programa?

Recupera razonamiento de [ejercicio 001](ejercicio_001.md), [ejercicio 004](ejercicio_004.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. A: 100+500 de envío; B: 150+0; cantidad 10 → empate en 1500.
2. Cantidad 1 con mismas ofertas → B, diferencia 450.
3. Cantidad 0 → rechazo.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Sumar transporte una vez por unidad.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Operadores](../Universidad_Python.md#operadores).
- [Universidad_Python.md — Condicionales](../Universidad_Python.md#condicionales).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A: 100+500 de envío; B: 150+0; cantidad 10 → empate en 1500**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué dato cambia entre ofertas y cuál es compartido?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee tu código sin ejecutarlo y anota qué representa cada valor importante durante un caso mínimo. Comprueba después tu predicción.

### Aplicación profesional

Comparadores comerciales calculan un coste comparable antes de tomar decisiones sobre alternativas. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Aceptar una lista de ofertas y devolver todos los empates.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
