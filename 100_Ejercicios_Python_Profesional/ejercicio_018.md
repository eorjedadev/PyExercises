# Ejercicio 018 — Cruce de invitados y asistentes

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_017.md) · [Siguiente](ejercicio_019.md)

### Contexto

Organización quiere saber quién acudió a un evento y quién entró sin invitación.

### Situación

El encargo es **cruce de invitados y asistentes**. Puedes empezar con valores preparados y una salida por consola. Mantén separadas las reglas del formato de los mensajes; no es obligatorio construir un menú.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Tres grupos y número de escaneos repetidos dentro de asistentes**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Dos listas de identificadores únicos por persona; repeticiones de escaneo permitidas.

### Resultado esperado

Tres grupos y número de escaneos repetidos dentro de asistentes.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Identificadores no vacíos y exactos.
- Informar invitados presentes, invitados ausentes y presentes no invitados.
- Cada persona una sola vez.
- Ordenar cada grupo por identificador.

### Casos especiales y límites

No usar los nombres personales como identificadores únicos.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Conjuntos, pertenencia y operaciones entre grupos**. Investiga qué información de orden o multiplicidad se pierde al representar datos como conjunto.
- **Diccionarios, registros y colecciones anidadas**. Comprende claves únicas, ausencia de clave, valores por defecto y recorrido; justifica qué entidad merece ser una clave.
- **Funciones, parámetros, retornos y contratos**. Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

### ¿Por qué pueden ser útiles?

- Ayudan a expresar identidad, coincidencias y diferencias cuando las repeticiones no aportan significado.
- Relacionan identidades con atributos, estados o acumulados consultables.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **personas invitadas, personas presentes, ausencias, repeticiones de escaneo**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué diferencia distingue ausencia de entrada no prevista?
- ¿Cuáles son las entradas, sus unidades y el resultado que podrías comprobar a mano?
- ¿Qué entrada está justo en un límite y qué cambia al pasar al valor siguiente?
- ¿Cómo representarías un caso válido y un rechazo sin escribir aún el programa?

### Pruebas mínimas

1. Invitados A,B; asistentes B,C,B → presentes B, ausentes A, no invitado C, 1 repetición.
2. Sin asistentes → todos ausentes.
3. Sin invitados y asistente C → C no invitado.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Comparar posiciones de las dos listas como si representaran a la misma persona.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Conjuntos](../Universidad_Python.md#conjuntos).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Invitados A,B; asistentes B,C,B → presentes B, ausentes A, no invitado C, 1 repetición**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué diferencia distingue ausencia de entrada no prevista?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee tu código sin ejecutarlo y anota qué representa cada valor importante durante un caso mínimo. Comprueba después tu predicción.

### Aplicación profesional

Conciliación de accesos compara colectivos sin confundir duplicados de registro con personas diferentes. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Incorporar acompañantes autorizados en una tercera lista.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
