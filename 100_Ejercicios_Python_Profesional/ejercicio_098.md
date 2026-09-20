# Ejercicio 098 — Actualización incremental de un tablero

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_097.md) · [Siguiente](ejercicio_099.md)

### Contexto

Un tablero incorpora operaciones y correcciones sin reconstruir siempre todos los totales.

### Situación

El encargo es **actualización incremental de un tablero**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Decisión por evento, operaciones vigentes y totales por categoría**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Eventos ordenados de alta id/categoría/importe, corregir id/categoría/importe y anular id; importes enteros no negativos.

### Resultado esperado

Decisión por evento, operaciones vigentes y totales por categoría.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Alta exige id nunca usado.
- Corregir exige operación vigente.
- Anular vigente una vez.
- Ids anulados no se reutilizan.
- Total por categoría debe corresponder a operaciones vigentes.
- Categorías sin operaciones se omiten, incluso si su total era0.

### Casos especiales y límites

Cambiar categoría implica retirar el aporte de una y añadirlo a otra.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Invariantes y operaciones dependientes del estado vigente.
- Identidad de entidades y organización de datos relacionados.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Relacionan identidades con atributos, estados o acumulados consultables.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **operación vigente, aporte anterior, categoría nueva, total derivado**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Cómo comprobarías los totales incrementales contra una reconstrucción independiente?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 054](ejercicio_054.md), [ejercicio 079](ejercicio_079.md), [ejercicio 084](ejercicio_084.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Alta A norte100,corregir A sur80 →solo sur80.
2. Anular A →sin categorías.
3. Anular A otra vez →rechazo sin cambio.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Sumar la corrección como si fuese una operación adicional.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Alta A norte100,corregir A sur80 →solo sur80**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Cómo comprobarías los totales incrementales contra una reconstrucción independiente?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Tableros incrementales deben retirar aportes anteriores al corregir operaciones y contrastar sus totales con el estado vigente. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Persistir eventos y reconstruir el tablero para auditar su coherencia.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
