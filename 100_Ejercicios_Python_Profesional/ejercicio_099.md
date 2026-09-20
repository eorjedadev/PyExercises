# Ejercicio 099 — Cola de trabajo con reintentos diferidos

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_098.md) · [Siguiente](ejercicio_100.md)

### Contexto

Una automatización procesa trabajos pendientes sin bloquearse por un fallo transitorio.

### Situación

El encargo es **cola de trabajo con reintentos diferidos**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Historial con tiempos, resultado final por trabajo y número de intentos; sin esperas reales**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Trabajos con id único y secuencia de resultados simulados éxito/temporal/permanente; reloj inicial0; máximo3 intentos.

### Resultado esperado

Historial con tiempos, resultado final por trabajo y número de intentos; sin esperas reales.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Un intento por decisión.
- Elegir menor instante de elegibilidad y luego id.
- Primer temporal pospone2 segundos, segundo4.
- Tercer temporal agota.
- Éxito/permanente finalizan.
- Avanzar reloj simulado si no hay elegibles.
- Resultado faltante produce error de simulación para ese trabajo.

### Casos especiales y límites

Un trabajo pospuesto no debe impedir atender a otro ya elegible.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Invariantes y operaciones dependientes del estado vigente.
- Comparación total, estabilidad y desempates reproducibles.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Hacen reproducibles las prioridades y sus desempates.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **instante elegible, intento consumido, resultado transitorio, trabajo finalizado**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué diferencia hay entre orden de entrada, prioridad de ejecución y estado final?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 062](ejercicio_062.md), [ejercicio 063](ejercicio_063.md), [ejercicio 072](ejercicio_072.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. A:temporal,éxito →intentos en0 y2.
2. A:temporal,temporal,temporal →0,2,6 y agotado.
3. B:permanente →un intento.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Dormir el proceso entero cuando solo un trabajo espera.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [Universidad_Python.md — Funciones Integradas](../Universidad_Python.md#funciones-integradas).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A:temporal,éxito →intentos en0 y2**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué diferencia hay entre orden de entrada, prioridad de ejecución y estado final?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Procesadores de trabajo diferido combinan elegibilidad temporal, límites de intentos y atención de otras tareas disponibles. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Permitir cancelar un trabajo pendiente antes de su próximo intento.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
