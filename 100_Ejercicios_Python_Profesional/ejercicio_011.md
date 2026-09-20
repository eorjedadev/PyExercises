# Ejercicio 011 — Prioridad de una incidencia

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_010.md) · [Siguiente](ejercicio_012.md)

### Contexto

Soporte quiere aplicar la misma política inicial a todas sus incidencias.

### Situación

El encargo es **prioridad de una incidencia**. Puedes empezar con valores preparados y una salida por consola. Mantén separadas las reglas del formato de los mensajes; no es obligatorio construir un menú.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Prioridad y regla que la justifica**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Impacto bajo o alto, servicio detenido como booleano y antigüedad entera en horas.

### Resultado esperado

Prioridad y regla que la justifica.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Antigüedad no negativa.
- Urgente si servicio detenido e impacto alto.
- En otro caso alta si detenido o antigüedad al menos 24.
- Resto normal.

### Casos especiales y límites

Varias condiciones pueden cumplirse a la vez.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Condicionales, booleanos y operadores de comparación**. Comprende límites inclusivos, condiciones compuestas y orden de evaluación antes de elegir ramas.
- **Funciones, parámetros, retornos y contratos**. Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.
- **Cadenas, métodos de texto y comparaciones**. Investiga recorte, partición, pertenencia y diferencias entre igualdad textual y equivalencia definida por negocio.

### ¿Por qué pueden ser útiles?

- Expresan las condiciones del contrato y la prioridad entre decisiones que pueden coincidir.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.
- Permiten separar el texto recibido de la forma usada para validarlo o compararlo.

### Variables y nombres

Identifica estas entidades: **impacto, interrupción del servicio, antigüedad, prioridad asignada**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué regla debe prevalecer cuando coinciden dos categorías?
- ¿Cuáles son las entradas, sus unidades y el resultado que podrías comprobar a mano?
- ¿Qué entrada está justo en un límite y qué cambia al pasar al valor siguiente?
- ¿Cómo representarías un caso válido y un rechazo sin escribir aún el programa?

Recupera razonamiento de [ejercicio 003](ejercicio_003.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Alto, detenido, 0 → urgente.
2. Bajo, activo, 24 → alta.
3. Alto, activo, 23 → normal.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Evaluar una regla general antes de una más específica.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Condicionales](../Universidad_Python.md#condicionales).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).
- [Diccionario_Python.md — Métodos de Cadenas](../Diccionario_Python.md#m%C3%A9todos-de-cadenas).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Alto, detenido, 0 → urgente**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué regla debe prevalecer cuando coinciden dos categorías?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee tu código sin ejecutarlo y anota qué representa cada valor importante durante un caso mínimo. Comprueba después tu predicción.

### Aplicación profesional

Sistemas de soporte aplican políticas de prioridad con reglas superpuestas y explicaciones auditables. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Introducir prioridad alta por impacto alto aunque el servicio siga activo.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
