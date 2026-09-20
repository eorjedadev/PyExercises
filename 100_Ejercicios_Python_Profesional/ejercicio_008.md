# Ejercicio 008 — Resumen de una cesta

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_007.md) · [Siguiente](ejercicio_009.md)

### Contexto

Un pequeño comercio necesita revisar las líneas de una cesta antes de cobrar.

### Situación

El encargo es **resumen de una cesta**. Puedes empezar con valores preparados y una salida por consola. Mantén separadas las reglas del formato de los mensajes; no es obligatorio construir un menú.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Número de líneas, unidades totales y nombres de líneas con cantidad de al menos 5, en orden de entrada**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Lista de pares nombre y cantidad entera, con cantidades positivas.

### Resultado esperado

Número de líneas, unidades totales y nombres de líneas con cantidad de al menos 5, en orden de entrada.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Recortar nombres.
- Rechazar toda la cesta si una línea no es válida.
- Nombres repetidos se permiten como líneas separadas.
- Cesta vacía válida.

### Casos especiales y límites

No confundir líneas con productos distintos.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Listas, tuplas, índices y recorridos**. Compara secuencias mutables e inmutables; comprueba cómo se representa una secuencia vacía.
- **Bucles, acumuladores y control de flujo**. Comprende inicialización, condición de terminación y significado de cada acumulador; no confundas una iteración con un resultado final.
- **Cadenas, métodos de texto y comparaciones**. Investiga recorte, partición, pertenencia y diferencias entre igualdad textual y equivalencia definida por negocio.

### ¿Por qué pueden ser útiles?

- Representan grupos donde la posición, el orden o la asociación de varios valores tiene significado.
- Permiten examinar entradas sucesivas manteniendo la información necesaria para el resultado.
- Permiten separar el texto recibido de la forma usada para validarlo o compararlo.

### Variables y nombres

Identifica estas entidades: **líneas de cesta, unidades acumuladas, líneas voluminosas**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué estás contando en cada resultado?
- ¿Cuáles son las entradas, sus unidades y el resultado que podrías comprobar a mano?
- ¿Qué entrada está justo en un límite y qué cambia al pasar al valor siguiente?
- ¿Cómo representarías un caso válido y un rechazo sin escribir aún el programa?

### Pruebas mínimas

1. Lápiz 2 y Papel 5 → 2 líneas, 7 unidades, Papel.
2. Dos líneas Lápiz 1 → 2 líneas, 2 unidades.
3. Lista vacía → tres resultados vacíos o cero.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Deduplicar sin que el contrato lo pida.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Listas](../Universidad_Python.md#listas).
- [Universidad_Python.md — Bucles](../Universidad_Python.md#bucles).
- [Diccionario_Python.md — Métodos de Cadenas](../Diccionario_Python.md#m%C3%A9todos-de-cadenas).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Lápiz 2 y Papel 5 → 2 líneas, 7 unidades, Papel**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué estás contando en cada resultado?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee tu código sin ejecutarlo y anota qué representa cada valor importante durante un caso mínimo. Comprueba después tu predicción.

### Aplicación profesional

Reportes de pedidos distinguen cantidad de registros, unidades físicas y subconjuntos que requieren atención. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir un resumen de unidades por nombre normalizado.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
