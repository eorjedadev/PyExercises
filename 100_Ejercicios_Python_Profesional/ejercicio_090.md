# Ejercicio 090 — Reporte reproducible de cierre

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_089.md) · [Siguiente](ejercicio_091.md)

### Contexto

Una organización debe poder regenerar un reporte con idénticos datos y reglas.

### Situación

El encargo es **reporte reproducible de cierre**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Reporte determinista y evidencia de igualdad entre ejecuciones**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Movimientos con id único, fecha ISO e importe entero en céntimos; intervalo de fechas inclusivo; versión de reglas literal v1.

### Resultado esperado

Reporte determinista y evidencia de igualdad entre ejecuciones.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Seleccionar intervalo.
- Ordenar fecha e id.
- Devolver total y detalle.
- Incorporar parámetros y versión en el reporte JSON.
- No incluir hora real de ejecución.
- Mismas entradas equivalentes generan los mismos bytes UTF-8.

### Casos especiales y límites

El orden de claves y el formato de serialización también afectan la comparación de bytes.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Serialización, esquema y compatibilidad de datos persistidos.
- Calendario, tiempo de referencia e intervalos.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Permite transportar o guardar estructuras; la lectura sintáctica por sí sola no garantiza que cumplan el contrato.
- Evitan interpretar meses y días como cantidades con longitud fija.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **periodo de cierre, versión de reglas, detalle ordenado, representación estable**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué dependencias ocultas impedirían repetir exactamente el resultado?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 045](ejercicio_045.md), [ejercicio 046](ejercicio_046.md), [ejercicio 067](ejercicio_067.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Mismos movimientos en otro orden →mismos bytes.
2. Movimiento en fecha final →incluido.
3. Intervalo invertido o versión desconocida →error.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Agregar una marca temporal real que cambie en cada ejecución.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON** (buscar ese título dentro del documento).
- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 5: Fecha y hora** (buscar ese título dentro del documento).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Mismos movimientos en otro orden →mismos bytes**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué dependencias ocultas impedirían repetir exactamente el resultado?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Cierres reproducibles necesitan datos, parámetros, orden y versión de reglas que determinen por completo la salida. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir una versión v2 manteniendo reproducibles los reportes v1.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
