# Ejercicio 079 — Conciliación de cargos y devoluciones

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_078.md) · [Siguiente](ejercicio_080.md)

### Contexto

Una tienda comprueba que sus devoluciones registradas no exceden los cargos originales.

### Situación

El encargo es **conciliación de cargos y devoluciones**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Devuelto y pendiente de devolución por cargo, y decisiones por devolución**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Cargos de id único e importe positivo en céntimos; devoluciones ordenadas con id único, cargo referido e importe positivo.

### Resultado esperado

Devuelto y pendiente de devolución por cargo, y decisiones por devolución.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Cargo inexistente rechaza devolución.
- Suma de devoluciones aceptadas no puede superar cargo.
- Rechazos no consumen saldo.
- Identificadores duplicados invalidan entrada antes de procesar.

### Casos especiales y límites

No aplicar reglas fiscales ni bancarias ajenas al contrato simulado.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Identidad de entidades y organización de datos relacionados.
- Invariantes y operaciones dependientes del estado vigente.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Relacionan identidades con atributos, estados o acumulados consultables.
- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **cargo original, devolución solicitada, acumulado devuelto, saldo reembolsable**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué vínculo permite atribuir cada devolución al cargo correcto?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 019](ejercicio_019.md), [ejercicio 032](ejercicio_032.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Cargo C100; devoluciones60,50 →acepta60,rechaza50,pendiente40.
2. Devolver100 →pendiente0.
3. Referencia desconocida →rechazo.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Validar cada devolución aisladamente contra el importe completo.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Cargo C100; devoluciones60,50 →acepta60,rechaza50,pendiente40**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué vínculo permite atribuir cada devolución al cargo correcto?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Conciliación de operaciones relacionadas limita acumulados por entidad original y conserva rechazos auditables. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Admitir cancelación de una devolución aceptada mediante evento explícito.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
