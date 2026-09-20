# Ejercicio 001 — Confirmación de un pedido pequeño

[Índice](README.md#indice-de-ejercicios) · [Siguiente](ejercicio_002.md)

### Contexto

Una papelería confirma pedidos de un solo artículo antes de aceptar el pago.

### Situación

El encargo es **confirmación de un pedido pequeño**. Puedes empezar con valores preparados y una salida por consola. Mantén separadas las reglas del formato de los mensajes; no es obligatorio construir un menú.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Nombre limpio, cantidad y total en céntimos, o los campos rechazados**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Nombre del artículo, precio unitario entero en céntimos y cantidad entera.

### Resultado esperado

Nombre limpio, cantidad y total en céntimos, o los campos rechazados.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- El nombre se recorta en sus extremos y debe conservar contenido.
- Precio mayor que cero.
- Cantidad entre 1 y 20.
- No hay descuentos ni impuestos añadidos.

### Casos especiales y límites

Precio cero y nombres con espacios interiores.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Enteros, operadores aritméticos y formato de resultados**. Comprende operaciones y precedencia; distingue valor, unidad y formato. Investiga división entera, resto o redondeo solo cuando las reglas los requieran.
- **Cadenas, métodos de texto y comparaciones**. Investiga recorte, partición, pertenencia y diferencias entre igualdad textual y equivalencia definida por negocio.
- **Condicionales, booleanos y operadores de comparación**. Comprende límites inclusivos, condiciones compuestas y orden de evaluación antes de elegir ramas.

### ¿Por qué pueden ser útiles?

- Representan cantidades y unidades sin mezclar el dato calculado con su presentación.
- Permiten separar el texto recibido de la forma usada para validarlo o compararlo.
- Expresan las condiciones del contrato y la prioridad entre decisiones que pueden coincidir.

### Variables y nombres

Identifica estas entidades: **artículo, precio unitario, cantidad solicitada, importe total**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué diferencia hay entre una entrada inválida y un pedido válido de importe pequeño?
- ¿Cuáles son las entradas, sus unidades y el resultado que podrías comprobar a mano?
- ¿Qué entrada está justo en un límite y qué cambia al pasar al valor siguiente?
- ¿Cómo representarías un caso válido y un rechazo sin escribir aún el programa?

### Pruebas mínimas

1. Cuaderno, 350, 3 → total 1050.
2. Cantidad 20 → aceptada.
3. Nombre con solo espacios o cantidad 0 → rechazo sin total.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Confundir el precio de una unidad con el importe del pedido.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Operadores](../Universidad_Python.md#operadores).
- [Diccionario_Python.md — Métodos de Cadenas](../Diccionario_Python.md#m%C3%A9todos-de-cadenas).
- [Universidad_Python.md — Condicionales](../Universidad_Python.md#condicionales).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Cuaderno, 350, 3 → total 1050**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué diferencia hay entre una entrada inválida y un pedido válido de importe pequeño?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee tu código sin ejecutarlo y anota qué representa cada valor importante durante un caso mínimo. Comprueba después tu predicción.

### Aplicación profesional

Cotizadores y formularios de venta necesitan distinguir datos válidos, importes calculados y mensajes para el cliente. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Permitir precio cero solo para artículos marcados como muestra.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
