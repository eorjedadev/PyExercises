# Ejercicio 016 — Palabras destacadas de una reseña

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_015.md) · [Siguiente](ejercicio_017.md)

### Contexto

Un equipo editorial identifica vocabulario repetido en comentarios cortos.

### Situación

El encargo es **palabras destacadas de una reseña**. Puedes empezar con valores preparados y una salida por consola. Mantén separadas las reglas del formato de los mensajes; no es obligatorio construir un menú.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Frecuencia por palabra, ordenada alfabéticamente**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Texto y conjunto de palabras excluidas, ya escritas en minúsculas.

### Resultado esperado

Frecuencia por palabra, ordenada alfabéticamente.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Separar por espacios.
- Recortar únicamente . ,.
- : ! ? de los extremos de cada fragmento.
- Convertir a minúsculas.
- Omitir vacías y excluidas.
- No quitar acentos.

### Casos especiales y límites

La puntuación interior y el signo ¿ se conservan intencionalmente.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Cadenas, métodos de texto y comparaciones**. Investiga recorte, partición, pertenencia y diferencias entre igualdad textual y equivalencia definida por negocio.
- **Diccionarios, registros y colecciones anidadas**. Comprende claves únicas, ausencia de clave, valores por defecto y recorrido; justifica qué entidad merece ser una clave.
- **Bucles, acumuladores y control de flujo**. Comprende inicialización, condición de terminación y significado de cada acumulador; no confundas una iteración con un resultado final.

### ¿Por qué pueden ser útiles?

- Permiten separar el texto recibido de la forma usada para validarlo o compararlo.
- Relacionan identidades con atributos, estados o acumulados consultables.
- Permiten examinar entradas sucesivas manteniendo la información necesaria para el resultado.

### Variables y nombres

Identifica estas entidades: **fragmento original, palabra comparable, palabras excluidas, frecuencia**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué definición de palabra está usando el programa?
- ¿Cuáles son las entradas, sus unidades y el resultado que podrías comprobar a mano?
- ¿Qué entrada está justo en un límite y qué cambia al pasar al valor siguiente?
- ¿Cómo representarías un caso válido y un rechazo sin escribir aún el programa?

### Pruebas mínimas

1. 'Hola, hola mundo!' y excluida mundo → hola: 2.
2. '¿Hola?' → ¿hola: 1 según el contrato.
3. Texto vacío → resultado vacío.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Aplicar una limpieza lingüística distinta de la especificada.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Diccionario_Python.md — Métodos de Cadenas](../Diccionario_Python.md#m%C3%A9todos-de-cadenas).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [Universidad_Python.md — Bucles](../Universidad_Python.md#bucles).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **'Hola, hola mundo!' y excluida mundo → hola: 2**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué definición de palabra está usando el programa?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee tu código sin ejecutarlo y anota qué representa cada valor importante durante un caso mínimo. Comprueba después tu predicción.

### Aplicación profesional

Análisis editorial y clasificación documental requieren definir qué se considera palabra antes de contarla. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Ampliar la puntuación admitida y revisar qué pruebas cambian.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
