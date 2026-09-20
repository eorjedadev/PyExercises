# Ejercicio 088 — Distribución proporcional de un descuento

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_087.md) · [Siguiente](ejercicio_089.md)

### Contexto

Una factura simulada reparte un descuento fijo entre líneas sin perder céntimos.

### Situación

El encargo es **distribución proporcional de un descuento**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Descuento e importe neto por línea y totales**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Líneas con id único e importe positivo en céntimos; descuento entero de0 al total.

### Resultado esperado

Descuento e importe neto por línea y totales.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Cuota ideal proporcional al importe.
- Asignar primero partes enteras y céntimos pendientes según mayor fracción restante, empate por id ascendente.
- Ningún descuento de línea supera su importe.
- Conservar total de descuento.

### Casos especiales y límites

Las fracciones deben compararse con precisión suficiente para no alterar empates.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Precisión numérica y políticas de redondeo.
- Unidades, exactitud y conservación de cantidades.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Mantiene las cantidades monetarias coherentes con las unidades y reglas exigidas.
- Representan cantidades y unidades sin mezclar el dato calculado con su presentación.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **cuota proporcional, fracción pendiente, descuento asignado, neto por línea**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué invariantes justifican la política de redondeo especificada por negocio?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 007](ejercicio_007.md), [ejercicio 021](ejercicio_021.md), [ejercicio 048](ejercicio_048.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. A100,B200, descuento100 →A33,B67.
2. A1,B1,C1, descuento1 →A1,B0,C0.
3. Descuento total →netos0.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Redondear cada cuota por separado y alterar el descuento total.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Diccionario_Python.md — Imports para Ciencia de Datos](../Diccionario_Python.md#imports-para-ciencia-de-datos).
- [Universidad_Python.md — Operadores](../Universidad_Python.md#operadores).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A100,B200, descuento100 →A33,B67**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué invariantes justifican la política de redondeo especificada por negocio?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Descuentos y prorrateos requieren conservar totales e implementar la política de redondeo definida por negocio. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Excluir ciertas líneas del reparto y validar el descuento contra el nuevo total elegible.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
