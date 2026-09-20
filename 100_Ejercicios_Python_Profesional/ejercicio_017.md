# Ejercicio 017 — Consolidación de materiales solicitados

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_016.md) · [Siguiente](ejercicio_018.md)

### Contexto

Varios equipos piden materiales y compras necesita una lista conjunta.

### Situación

El encargo es **consolidación de materiales solicitados**. Puedes empezar con valores preparados y una salida por consola. Mantén separadas las reglas del formato de los mensajes; no es obligatorio construir un menú.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Totales por código en orden alfabético e índices y motivos de solicitudes rechazadas**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Lista de solicitudes con código de material y cantidad positiva entera.

### Resultado esperado

Totales por código en orden alfabético e índices y motivos de solicitudes rechazadas.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Códigos recortados y en mayúsculas.
- Código vacío invalida la solicitud.
- Separar inválidas conservando su posición.
- Sumar válidas del mismo código.

### Casos especiales y límites

Una fila incorrecta no debe borrar aportes válidos anteriores.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Diccionarios, registros y colecciones anidadas**. Comprende claves únicas, ausencia de clave, valores por defecto y recorrido; justifica qué entidad merece ser una clave.
- **Bucles, acumuladores y control de flujo**. Comprende inicialización, condición de terminación y significado de cada acumulador; no confundas una iteración con un resultado final.
- **Funciones, parámetros, retornos y contratos**. Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

### ¿Por qué pueden ser útiles?

- Relacionan identidades con atributos, estados o acumulados consultables.
- Permiten examinar entradas sucesivas manteniendo la información necesaria para el resultado.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **código canónico, cantidad solicitada, total por material, filas rechazadas**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿La identidad del material depende de cómo se escribió el código?
- ¿Cuáles son las entradas, sus unidades y el resultado que podrías comprobar a mano?
- ¿Qué entrada está justo en un límite y qué cambia al pasar al valor siguiente?
- ¿Cómo representarías un caso válido y un rechazo sin escribir aún el programa?

Recupera razonamiento de [ejercicio 008](ejercicio_008.md), [ejercicio 010](ejercicio_010.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. ' ab ' 2 y AB 3 → AB: 5.
2. AB 0 y CD 1 → CD: 1, rechazo de fila 1.
3. Vacío → totales vacíos.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Sobrescribir la cantidad previa en vez de consolidar solicitudes.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [Universidad_Python.md — Bucles](../Universidad_Python.md#bucles).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **' ab ' 2 y AB 3 → AB: 5**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿La identidad del material depende de cómo se escribió el código?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee tu código sin ejecutarlo y anota qué representa cada valor importante durante un caso mínimo. Comprueba después tu predicción.

### Aplicación profesional

Compras consolidadas y planificación de materiales agregan solicitudes sin perder rechazos ni procedencia. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir un límite máximo por material y señalar excesos sin recortar totales.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
