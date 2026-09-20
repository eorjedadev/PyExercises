# Ejercicio 002 — Etiqueta para un envío interno

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_001.md) · [Siguiente](ejercicio_003.md)

### Contexto

Recepción necesita etiquetas legibles para distribuir sobres dentro de una oficina.

### Situación

El encargo es **etiqueta para un envío interno**. Puedes empezar con valores preparados y una salida por consola. Mantén separadas las reglas del formato de los mensajes; no es obligatorio construir un menú.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Etiqueta con destinatario, sede normalizada y piso, o motivos de rechazo**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Destinatario, sede y número de piso entero; sedes permitidas: norte y sur.

### Resultado esperado

Etiqueta con destinatario, sede normalizada y piso, o motivos de rechazo.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Recortar espacios externos.
- Comparar sede sin distinguir mayúsculas.
- Destinatario no vacío.
- Pisos de 0 a 12.
- Piso 0 se presenta como recepción.

### Casos especiales y límites

Un destinatario puede tener varios apellidos y no debe perderlos.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Cadenas, métodos de texto y comparaciones**. Investiga recorte, partición, pertenencia y diferencias entre igualdad textual y equivalencia definida por negocio.
- **Condicionales, booleanos y operadores de comparación**. Comprende límites inclusivos, condiciones compuestas y orden de evaluación antes de elegir ramas.
- **Enteros, operadores aritméticos y formato de resultados**. Comprende operaciones y precedencia; distingue valor, unidad y formato. Investiga división entera, resto o redondeo solo cuando las reglas los requieran.

### ¿Por qué pueden ser útiles?

- Permiten separar el texto recibido de la forma usada para validarlo o compararlo.
- Expresan las condiciones del contrato y la prioridad entre decisiones que pueden coincidir.
- Representan cantidades y unidades sin mezclar el dato calculado con su presentación.

### Variables y nombres

Identifica estas entidades: **destinatario, sede admitida, piso, etiqueta**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué texto puede normalizarse y cuál debe conservar la escritura del usuario?
- ¿Cuáles son las entradas, sus unidades y el resultado que podrías comprobar a mano?
- ¿Qué entrada está justo en un límite y qué cambia al pasar al valor siguiente?
- ¿Cómo representarías un caso válido y un rechazo sin escribir aún el programa?

### Pruebas mínimas

1. Ana, NORTE, 0 → Ana / norte / recepción.
2. Luis, sur, 12 → piso 12.
3. Sede este o piso 13 → rechazo.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Aplicar una normalización que altere nombres personales.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Diccionario_Python.md — Métodos de Cadenas](../Diccionario_Python.md#m%C3%A9todos-de-cadenas).
- [Universidad_Python.md — Condicionales](../Universidad_Python.md#condicionales).
- [Universidad_Python.md — Operadores](../Universidad_Python.md#operadores).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Ana, NORTE, 0 → Ana / norte / recepción**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué texto puede normalizarse y cuál debe conservar la escritura del usuario?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee tu código sin ejecutarlo y anota qué representa cada valor importante durante un caso mínimo. Comprueba después tu predicción.

### Aplicación profesional

Generadores de etiquetas y credenciales separan datos visibles de valores normalizados para enrutar una entrega. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir una sede con su propio límite de pisos.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
