# Ejercicio 005 — Identificador de una solicitud

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_004.md) · [Siguiente](ejercicio_006.md)

### Contexto

Un área administrativa quiere comprobar referencias antes de buscarlas en su sistema.

### Situación

El encargo es **identificador de una solicitud**. Puedes empezar con valores preparados y una salida por consola. Mantén separadas las reglas del formato de los mensajes; no es obligatorio construir un menú.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Referencia válida conservada o causa de invalidez**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Una cadena con formato SOL- seguido de cuatro dígitos ASCII.

### Resultado esperado

Referencia válida conservada o causa de invalidez.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Recortar espacios externos.
- Prefijo exactamente SOL- en mayúsculas.
- Cuatro dígitos de 0 a 9.
- El número 0000 no está permitido.
- Conservar ceros iniciales.

### Casos especiales y límites

Los dígitos de otros alfabetos no pertenecen al formato acordado.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Cadenas, métodos de texto y comparaciones**. Investiga recorte, partición, pertenencia y diferencias entre igualdad textual y equivalencia definida por negocio.
- **Condicionales, booleanos y operadores de comparación**. Comprende límites inclusivos, condiciones compuestas y orden de evaluación antes de elegir ramas.

### ¿Por qué pueden ser útiles?

- Permiten separar el texto recibido de la forma usada para validarlo o compararlo.
- Expresan las condiciones del contrato y la prioridad entre decisiones que pueden coincidir.

### Variables y nombres

Identifica estas entidades: **referencia original, prefijo, segmento numérico, motivo de rechazo**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿El identificador es una cantidad o un texto con estructura?
- ¿Cuáles son las entradas, sus unidades y el resultado que podrías comprobar a mano?
- ¿Qué entrada está justo en un límite y qué cambia al pasar al valor siguiente?
- ¿Cómo representarías un caso válido y un rechazo sin escribir aún el programa?

### Pruebas mínimas

1. SOL-0007 → válida.
2. SOL-0000 → inválida.
3. sol-1234 y SOL-１２３４ → inválidas.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Convertir toda la referencia en un número y perder su formato.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Diccionario_Python.md — Métodos de Cadenas](../Diccionario_Python.md#m%C3%A9todos-de-cadenas).
- [Universidad_Python.md — Condicionales](../Universidad_Python.md#condicionales).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **SOL-0007 → válida**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿El identificador es una cantidad o un texto con estructura?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee tu código sin ejecutarlo y anota qué representa cada valor importante durante un caso mínimo. Comprueba después tu predicción.

### Aplicación profesional

Importadores de referencias preservan identificadores que contienen ceros y no representan cantidades aritméticas. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Aceptar el prefijo sin distinguir mayúsculas y producir un formato canónico.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
