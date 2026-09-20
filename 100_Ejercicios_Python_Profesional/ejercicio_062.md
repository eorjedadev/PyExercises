# Ejercicio 062 — Plan de reintentos de una operación

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_061.md) · [Siguiente](ejercicio_063.md)

### Contexto

Una integración necesita decidir qué hacer ante fallos transitorios sin esperar realmente.

### Situación

El encargo es **plan de reintentos de una operación**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Estado final, intentos consumidos y demoras que habrían ocurrido**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Lista de resultados simulados: éxito, temporal o permanente; máximo de intentos positivo; demora base positiva en segundos.

### Resultado esperado

Estado final, intentos consumidos y demoras que habrían ocurrido.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Cada resultado consume un intento.
- Éxito o permanente detienen.
- Temporal permite reintento si quedan intentos, con demoras base, doble, cuádruple.
- No dormir ni llamar a la red.
- Falta de resultados antes de terminar produce estado simulación incompleta.

### Casos especiales y límites

No planificar una espera después del último intento.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Invariantes y operaciones dependientes del estado vigente.
- Contratos, parámetros explícitos y responsabilidades comprobables.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **intento actual, causa de fallo, demora prevista, presupuesto de intentos**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué diferencia hay entre número de intentos y número de reintentos?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 050](ejercicio_050.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Temporal,temporal,éxito; máximo3, base2 →éxito,3 intentos, demoras2,4.
2. Permanente →1 intento sin demoras.
3. Temporal con máximo1 →agotado sin demora.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Reintentar errores permanentes o contar mal el primer intento.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Temporal,temporal,éxito; máximo3, base2 →éxito,3 intentos, demoras2,4**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué diferencia hay entre número de intentos y número de reintentos?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Integraciones tolerantes a fallos necesitan políticas acotadas y comprobables para errores transitorios. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir un tope de demora y comprobar que no altera el límite de intentos.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
