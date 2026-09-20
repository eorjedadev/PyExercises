# Ejercicio 028 — Resumen de respuestas de una encuesta

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_027.md) · [Siguiente](ejercicio_029.md)

### Contexto

Una organización quiere publicar resultados sin ocultar las respuestas inválidas.

### Situación

El encargo es **resumen de respuestas de una encuesta**. Expón la lógica principal mediante funciones con parámetros y retornos comprobables. La presentación por consola puede ser una adaptación; evita depender de variables globales para decidir.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Conteos de las tres opciones, inválidas y porcentajes o ausencia de porcentajes si no hay válidas**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Lista de respuestas textuales y opciones permitidas sí, no y abstención.

### Resultado esperado

Conteos de las tres opciones, inválidas y porcentajes o ausencia de porcentajes si no hay válidas.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Recortar extremos y convertir a minúsculas.
- Otras respuestas inválidas.
- Porcentajes sobre válidas.
- Presentar una cifra decimal.
- No forzar que los porcentajes redondeados sumen 100.

### Casos especiales y límites

Una opción con cero respuestas sigue apareciendo.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Cadenas, métodos de texto y comparaciones**. Tema para investigar: Investiga recorte, partición, pertenencia y diferencias entre igualdad textual y equivalencia definida por negocio.
- **Diccionarios, registros y colecciones anidadas**. Tema para investigar: Comprende claves únicas, ausencia de clave, valores por defecto y recorrido; justifica qué entidad merece ser una clave.
- **Enteros, operadores aritméticos y formato de resultados**. Tema para investigar: Comprende operaciones y precedencia; distingue valor, unidad y formato. Investiga división entera, resto o redondeo solo cuando las reglas los requieran.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Permiten separar el texto recibido de la forma usada para validarlo o compararlo.
- Relacionan identidades con atributos, estados o acumulados consultables.
- Representan cantidades y unidades sin mezclar el dato calculado con su presentación.

### Variables y nombres

Identifica estas entidades: **opciones admitidas, respuestas válidas, conteos, porcentaje por opción**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué población representa el denominador de cada porcentaje?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 016](ejercicio_016.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Sí, no, no, tal vez → sí 1, no 2, inválidas 1; 33.3 % y 66.7 %.
2. Solo inválidas → sin porcentajes.
3. Vacía → contadores cero.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Dividir entre todas las respuestas incluyendo inválidas.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Diccionario_Python.md — Métodos de Cadenas](../Diccionario_Python.md#m%C3%A9todos-de-cadenas).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [Universidad_Python.md — Operadores](../Universidad_Python.md#operadores).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Sí, no, no, tal vez → sí 1, no 2, inválidas 1; 33.3 % y 66.7 %**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué población representa el denominador de cada porcentaje?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Encuestas y reportes de aceptación deben publicar denominadores y registros excluidos para que sus métricas sean interpretables. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Comparar dos encuestas conservando sus denominadores separados.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
