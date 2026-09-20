# Ejercicio 013 — Lista de preparación de paquetes

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_012.md) · [Siguiente](ejercicio_014.md)

### Contexto

Un almacén necesita dividir unidades idénticas en cajas de capacidad fija.

### Situación

El encargo es **lista de preparación de paquetes**. Puedes empezar con valores preparados y una salida por consola. Mantén separadas las reglas del formato de los mensajes; no es obligatorio construir un menú.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Cantidad de cajas y unidades contenidas en cada una**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Unidades enteras no negativas y capacidad entera positiva de cada caja.

### Resultado esperado

Cantidad de cajas y unidades contenidas en cada una.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Usar cajas completas salvo la última.
- No crear cajas vacías.
- Orden de salida por número de caja desde 1.

### Casos especiales y límites

Una última caja exacta no implica otra caja adicional.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Enteros, operadores aritméticos y formato de resultados**. Comprende operaciones y precedencia; distingue valor, unidad y formato. Investiga división entera, resto o redondeo solo cuando las reglas los requieran.
- **Bucles, acumuladores y control de flujo**. Comprende inicialización, condición de terminación y significado de cada acumulador; no confundas una iteración con un resultado final.
- **Listas, tuplas, índices y recorridos**. Compara secuencias mutables e inmutables; comprueba cómo se representa una secuencia vacía.

### ¿Por qué pueden ser útiles?

- Representan cantidades y unidades sin mezclar el dato calculado con su presentación.
- Permiten examinar entradas sucesivas manteniendo la información necesaria para el resultado.
- Representan grupos donde la posición, el orden o la asociación de varios valores tiene significado.

### Variables y nombres

Identifica estas entidades: **unidades pendientes, capacidad por caja, número de caja, contenido**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué relación debe existir entre la suma del contenido y la entrada?
- ¿Cuáles son las entradas, sus unidades y el resultado que podrías comprobar a mano?
- ¿Qué entrada está justo en un límite y qué cambia al pasar al valor siguiente?
- ¿Cómo representarías un caso válido y un rechazo sin escribir aún el programa?

### Pruebas mínimas

1. 10 unidades, capacidad 4 → 4, 4, 2.
2. 8 y 4 → 4, 4.
3. 0 y 4 → ninguna caja; capacidad 0 → error.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Interpretar el resto cero como una caja vacía obligatoria.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Operadores](../Universidad_Python.md#operadores).
- [Universidad_Python.md — Bucles](../Universidad_Python.md#bucles).
- [Universidad_Python.md — Listas](../Universidad_Python.md#listas).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **10 unidades, capacidad 4 → 4, 4, 2**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué relación debe existir entre la suma del contenido y la entrada?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee tu código sin ejecutarlo y anota qué representa cada valor importante durante un caso mínimo. Comprueba después tu predicción.

### Aplicación profesional

Preparación de lotes y paginación de trabajos distribuyen elementos sin generar contenedores vacíos adicionales. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Agregar un límite de cajas e informar unidades que quedarían pendientes.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
