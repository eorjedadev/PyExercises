# Ejercicio 052 — Migración de fichas de clientes

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_051.md) · [Siguiente](ejercicio_053.md)

### Contexto

Un programa debe actualizar archivos históricos a un esquema nuevo sin perder información.

### Situación

El encargo es **migración de fichas de clientes**. Separa las reglas de transformación de los efectos externos que existan. Prepara ejemplos reproducibles y comprueba qué datos quedan después de un rechazo.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Documento versión2 y reporte de cuántas fichas se migraron**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Archivo JSON versión1 con clientes de id/nombre, o versión2 con id/nombre/activo; ruta de destino nueva.

### Resultado esperado

Documento versión2 y reporte de cuántas fichas se migraron.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Versión1 añade activo verdadero y pasa a versión2.
- Versión2 se valida y conserva.
- Identificadores únicos y nombres no vacíos.
- Versión desconocida o campos extra se rechazan.
- No sobrescribir origen ni destino existente.

### Casos especiales y límites

Ejecutar la migración sobre su resultado no debe alterar el significado.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Serialización JSON y validación de esquema**. Tema para investigar: Comprende diferencias entre documento válido, tipos admitidos, campos requeridos y versión de esquema.
- **Rutas, archivos, codificación y gestión de recursos**. Tema para investigar: Comprende modos de apertura, cierre de recursos, UTF-8 y efectos de sobrescribir un archivo.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Permite transportar o guardar estructuras; la lectura sintáctica por sí sola no garantiza que cumplan el contrato.
- Conectan los datos del programa con recursos que pueden faltar o fallar.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **versión de origen, ficha migrada, valor incorporado, destino**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Cómo demostrarás que la transformación no pierde datos admitidos?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 043](ejercicio_043.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. v1 con A/Ana →v2 con activo verdadero.
2. v2 válido →mismos datos, cero migradas.
3. v3 →error sin archivo de salida.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Modificar el único archivo disponible antes de validar todos sus registros.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON** (buscar ese título dentro del documento).
- [Universidad_Python.md — Archivos y Context Managers](../Universidad_Python.md#archivos-y-context-managers).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **v1 con A/Ana →v2 con activo verdadero**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Cómo demostrarás que la transformación no pierde datos admitidos?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Evolución de formatos requiere conservar significado y reconocer versiones desconocidas sin destruir el origen. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Agregar una migración v2→v3 con un nuevo campo opcional.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
