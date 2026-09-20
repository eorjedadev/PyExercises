# Ejercicio 007 — Reparto del coste de una comida

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_006.md) · [Siguiente](ejercicio_008.md)

### Contexto

Un equipo reparte un gasto común sin perder céntimos por redondeo.

### Situación

El encargo es **reparto del coste de una comida**. Puedes empezar con valores preparados y una salida por consola. Mantén separadas las reglas del formato de los mensajes; no es obligatorio construir un menú.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Aporte de cada persona y comprobación del total repartido**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Total no negativo en céntimos y lista ordenada de participantes con nombres distintos y no vacíos.

### Resultado esperado

Aporte de cada persona y comprobación del total repartido.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Debe haber al menos un participante.
- Diferencias entre aportes como máximo de un céntimo.
- Quienes aparecen primero asumen los céntimos sobrantes.
- Conservar el orden.

### Casos especiales y límites

El total puede ser menor que el número de participantes.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Enteros, operadores aritméticos y formato de resultados**. Comprende operaciones y precedencia; distingue valor, unidad y formato. Investiga división entera, resto o redondeo solo cuando las reglas los requieran.
- **Listas, tuplas, índices y recorridos**. Compara secuencias mutables e inmutables; comprueba cómo se representa una secuencia vacía.
- **Bucles, acumuladores y control de flujo**. Comprende inicialización, condición de terminación y significado de cada acumulador; no confundas una iteración con un resultado final.

### ¿Por qué pueden ser útiles?

- Representan cantidades y unidades sin mezclar el dato calculado con su presentación.
- Representan grupos donde la posición, el orden o la asociación de varios valores tiene significado.
- Permiten examinar entradas sucesivas manteniendo la información necesaria para el resultado.

### Variables y nombres

Identifica estas entidades: **total de la cuenta, participantes, aporte individual, sobrante**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué condiciones deben cumplir todos los aportes juntos?
- ¿Cuáles son las entradas, sus unidades y el resultado que podrías comprobar a mano?
- ¿Qué entrada está justo en un límite y qué cambia al pasar al valor siguiente?
- ¿Cómo representarías un caso válido y un rechazo sin escribir aún el programa?

### Pruebas mínimas

1. 100 entre Ana, Beto, Cora → 34, 33, 33.
2. 0 entre dos personas → 0, 0.
3. Lista vacía → rechazo.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Usar redondeos independientes que alteren el total.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Operadores](../Universidad_Python.md#operadores).
- [Universidad_Python.md — Listas](../Universidad_Python.md#listas).
- [Universidad_Python.md — Bucles](../Universidad_Python.md#bucles).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **100 entre Ana, Beto, Cora → 34, 33, 33**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué condiciones deben cumplir todos los aportes juntos?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee tu código sin ejecutarlo y anota qué representa cada valor importante durante un caso mínimo. Comprueba después tu predicción.

### Aplicación profesional

Repartos de gastos y asignación de unidades indivisibles deben conservar el total y explicitar desempates. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Permitir excluir del reparto a participantes invitados.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
