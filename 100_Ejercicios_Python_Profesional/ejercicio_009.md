# Ejercicio 009 — Lecturas de temperatura de una sala

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_008.md) · [Siguiente](ejercicio_010.md)

### Contexto

Mantenimiento revisa una serie corta de mediciones de una sala de equipos.

### Situación

El encargo es **lecturas de temperatura de una sala**. Puedes empezar con valores preparados y una salida por consola. Mantén separadas las reglas del formato de los mensajes; no es obligatorio construir un menú.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Cantidad válida, cantidad confortable, índices inválidos desde 1 y media con una cifra decimal; sin válidas, media ausente**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Lista de temperaturas enteras en grados Celsius.

### Resultado esperado

Cantidad válida, cantidad confortable, índices inválidos desde 1 y media con una cifra decimal; sin válidas, media ausente.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Rango admisible de sensor: -40 a 80.
- Separar lecturas fuera de rango.
- Considerar confortable de 18 a 26 inclusive.
- Media solo de lecturas válidas.

### Casos especiales y límites

No presentar cero como media cuando faltan observaciones.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Listas, tuplas, índices y recorridos**. Compara secuencias mutables e inmutables; comprueba cómo se representa una secuencia vacía.
- **Bucles, acumuladores y control de flujo**. Comprende inicialización, condición de terminación y significado de cada acumulador; no confundas una iteración con un resultado final.
- **Condicionales, booleanos y operadores de comparación**. Comprende límites inclusivos, condiciones compuestas y orden de evaluación antes de elegir ramas.

### ¿Por qué pueden ser útiles?

- Representan grupos donde la posición, el orden o la asociación de varios valores tiene significado.
- Permiten examinar entradas sucesivas manteniendo la información necesaria para el resultado.
- Expresan las condiciones del contrato y la prioridad entre decisiones que pueden coincidir.

### Variables y nombres

Identifica estas entidades: **lecturas válidas, índices rechazados, rango confortable, media**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué diferencia hay entre una lectura extrema válida y una lectura descartada?
- ¿Cuáles son las entradas, sus unidades y el resultado que podrías comprobar a mano?
- ¿Qué entrada está justo en un límite y qué cambia al pasar al valor siguiente?
- ¿Cómo representarías un caso válido y un rechazo sin escribir aún el programa?

### Pruebas mínimas

1. 18, 26, 30 → 3 válidas, 2 confortables, media 24.7.
2. 81, -41 → 0 válidas, media ausente.
3. Lista vacía → contadores cero.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Incluir lecturas descartadas en el denominador.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Listas](../Universidad_Python.md#listas).
- [Universidad_Python.md — Bucles](../Universidad_Python.md#bucles).
- [Universidad_Python.md — Condicionales](../Universidad_Python.md#condicionales).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **18, 26, 30 → 3 válidas, 2 confortables, media 24.7**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué diferencia hay entre una lectura extrema válida y una lectura descartada?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee tu código sin ejecutarlo y anota qué representa cada valor importante durante un caso mínimo. Comprueba después tu predicción.

### Aplicación profesional

Tableros de sensores separan observaciones válidas, valores fuera de rango y ausencia de información suficiente. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Informar también cuántas lecturas válidas quedaron bajo el rango confortable.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
