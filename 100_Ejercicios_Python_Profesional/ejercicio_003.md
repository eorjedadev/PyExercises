# Ejercicio 003 — Control de aforo de un taller

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_002.md) · [Siguiente](ejercicio_004.md)

### Contexto

La persona que organiza un taller decide si puede aceptar a un grupo completo.

### Situación

El encargo es **control de aforo de un taller**. Puedes empezar con valores preparados y una salida por consola. Mantén separadas las reglas del formato de los mensajes; no es obligatorio construir un menú.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Decisión, ocupación resultante y plazas libres**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Capacidad, asistentes confirmados y tamaño del grupo; todos enteros.

### Resultado esperado

Decisión, ocupación resultante y plazas libres.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Capacidad positiva.
- Confirmados entre 0 y capacidad.
- Grupo positivo.
- Aceptar solo si cabe completo.
- No modificar confirmados cuando se rechaza.

### Casos especiales y límites

Distinguir taller lleno de datos incoherentes.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Condicionales, booleanos y operadores de comparación**. Comprende límites inclusivos, condiciones compuestas y orden de evaluación antes de elegir ramas.
- **Enteros, operadores aritméticos y formato de resultados**. Comprende operaciones y precedencia; distingue valor, unidad y formato. Investiga división entera, resto o redondeo solo cuando las reglas los requieran.

### ¿Por qué pueden ser útiles?

- Expresan las condiciones del contrato y la prioridad entre decisiones que pueden coincidir.
- Representan cantidades y unidades sin mezclar el dato calculado con su presentación.

### Variables y nombres

Identifica estas entidades: **capacidad, ocupación actual, plazas solicitadas, plazas disponibles**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué igualdad representa exactamente el último grupo que cabe?
- ¿Cuáles son las entradas, sus unidades y el resultado que podrías comprobar a mano?
- ¿Qué entrada está justo en un límite y qué cambia al pasar al valor siguiente?
- ¿Cómo representarías un caso válido y un rechazo sin escribir aún el programa?

### Pruebas mínimas

1. 10, 7, 3 → aceptado, ocupación 10, libres 0.
2. 10, 7, 4 → rechazado, ocupación 7.
3. 10, 11, 1 → entrada inválida.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Rechazar un grupo que ocupa exactamente el aforo restante.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Condicionales](../Universidad_Python.md#condicionales).
- [Universidad_Python.md — Operadores](../Universidad_Python.md#operadores).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **10, 7, 3 → aceptado, ocupación 10, libres 0**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué igualdad representa exactamente el último grupo que cabe?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee tu código sin ejecutarlo y anota qué representa cada valor importante durante un caso mínimo. Comprueba después tu predicción.

### Aplicación profesional

Inscripciones y admisión de lotes comparten la regla de aceptar una solicitud completa dentro de una capacidad. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Informar cuántas personas del grupo quedarían sin plaza, sin aceptarlo parcialmente.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
