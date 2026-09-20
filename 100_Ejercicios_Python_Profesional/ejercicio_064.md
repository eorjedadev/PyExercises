# Ejercicio 064 — Caché con vencimiento comprobable

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_063.md) · [Siguiente](ejercicio_065.md)

### Contexto

Una aplicación reutiliza resultados mientras no excedan su vigencia.

### Situación

El encargo es **caché con vencimiento comprobable**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Resultado encontrado/ausente diferenciado del valor y estado observable de cada consulta**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Operaciones guardar clave/valor/TTL, consultar clave y avanzar tiempo; reloj inicial0 y avances enteros no negativos.

### Resultado esperado

Resultado encontrado/ausente diferenciado del valor y estado observable de cada consulta.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- TTL entero positivo.
- Valor puede ser None.
- Vigente mientras tiempo actual sea menor que vencimiento.
- Guardar reemplaza.
- Consulta no renueva.
- Sin reloj real.

### Casos especiales y límites

No confundir un valor None almacenado con falta de clave.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Encapsulación de estado y protección de invariantes.
- Invariantes y operaciones dependientes del estado vigente.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Pueden reunir estado y operaciones cuando esa unión protege reglas del dominio.
- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **valor almacenado, instante de expiración, reloj recibido, indicador de presencia**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué interfaz permite probar el tiempo sin esperar?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 055](ejercicio_055.md), [ejercicio 062](ejercicio_062.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Guardar A,None,5; consultar en4 →encontrado con None.
2. Consultar en5 →ausente.
3. Reemplazar en3 con TTL5 →vigente hasta antes de8.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Usar el valor como única señal de que la consulta tuvo éxito.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Programación Orientada a Objetos](../Universidad_Python.md#programaci%C3%B3n-orientada-a-objetos).
- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Guardar A,None,5; consultar en4 →encontrado con None**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué interfaz permite probar el tiempo sin esperar?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Cachés y permisos temporales necesitan separar ausencia, valor almacenado y pérdida de vigencia. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir invalidación explícita de una clave.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
