# Ejercicio 074 — Presupuesto de recursos indivisibles

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_073.md) · [Siguiente](ejercicio_075.md)

### Contexto

Una cuadrilla debe seleccionar trabajos dentro de un límite de horas y maximizar su valor estimado.

### Situación

El encargo es **presupuesto de recursos indivisibles**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Ids elegidos, horas consumidas y valor total**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Hasta 12 trabajos con id único, horas enteras positivas y valor entero no negativo; capacidad entera no negativa.

### Resultado esperado

Ids elegidos, horas consumidas y valor total.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Cada trabajo se toma completo una sola vez.
- Maximizar suma de valores sin exceder horas.
- Empate: menor total de horas y luego lista de ids ordenados lexicográficamente.
- Conjunto vacío permitido.

### Casos especiales y límites

Elegir siempre el mayor valor individual puede fallar.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Orden, posiciones y conservación de relaciones.
- Contratos, parámetros explícitos y responsabilidades comprobables.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Representan grupos donde la posición, el orden o la asociación de varios valores tiene significado.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **combinación candidata, horas disponibles, valor conjunto, criterio de desempate**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Cómo demostrarías que tu selección es la mejor para el dominio acotado?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 015](ejercicio_015.md), [ejercicio 034](ejercicio_034.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Capacidad4; A:3h/5, B:2h/4, C:2h/4 →B,C con valor8.
2. Capacidad0 →vacío.
3. A y B:1h/2, capacidad1 →A.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Confundir una estrategia intuitiva con una garantía de máximo.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Listas](../Universidad_Python.md#listas).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Capacidad4; A:3h/5, B:2h/4, C:2h/4 →B,C con valor8**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Cómo demostrarías que tu selección es la mejor para el dominio acotado?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Selección acotada de trabajos permite contrastar intuiciones con un resultado óptimo bajo un contrato explícito. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Permitir pares de trabajos incompatibles manteniendo el límite de 12.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
