# Ejercicio 050 — Bitácora de cambios de estado

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_049.md) · [Siguiente](ejercicio_051.md)

### Contexto

Un equipo quiere dejar evidencia de cambios de incidencias en un archivo local.

### Situación

El encargo es **bitácora de cambios de estado**. Separa las reglas de transformación de los efectos externos que existan. Prepara ejemplos reproducibles y comprueba qué datos quedan después de un rechazo.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Estado final y bitácora cuyos registros válidos reflejan todos los intentos confirmados**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Estado inicial abierta, ruta de bitácora nueva y secuencia de comandos tomar, resolver, reabrir.

### Resultado esperado

Estado final y bitácora cuyos registros válidos reflejan todos los intentos confirmados.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Transiciones abierta→en curso por tomar, en curso→resuelta por resolver, resuelta→abierta por reabrir.
- Rechazar otras.
- Registrar cada intento como línea JSON con secuencia, comando, antes, después y aceptación.
- Detener ante fallo de escritura e informar el último estado confirmado.

### Casos especiales y límites

La operación no se considera confirmada si no se pudo registrar.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Serialización JSON y validación de esquema**. Tema para investigar: Comprende diferencias entre documento válido, tipos admitidos, campos requeridos y versión de esquema.
- **Rutas, archivos, codificación y gestión de recursos**. Tema para investigar: Comprende modos de apertura, cierre de recursos, UTF-8 y efectos de sobrescribir un archivo.
- **Modelado de estados, transiciones y efectos**. Tema para investigar: Relaciona condicionales, datos y funciones con invariantes; separa intento, validación y confirmación sin asumir una arquitectura única.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Permite transportar o guardar estructuras; la lectura sintáctica por sí sola no garantiza que cumplan el contrato.
- Conectan los datos del programa con recursos que pueden faltar o fallar.
- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.

### Variables y nombres

Identifica estas entidades: **estado anterior, comando recibido, estado confirmado, secuencia de auditoría**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué contrato vincula la confirmación en memoria con la evidencia escrita?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 019](ejercicio_019.md), [ejercicio 041](ejercicio_041.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Tomar,resolver,reabrir →abierta y tres líneas.
2. Resolver desde abierta →rechazo registrado.
3. Fallo al escribir primer intento →estado inicial y error.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Anunciar éxito aunque la escritura haya fallado.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON** (buscar ese título dentro del documento).
- [Universidad_Python.md — Archivos y Context Managers](../Universidad_Python.md#archivos-y-context-managers).
- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Tomar,resolver,reabrir →abierta y tres líneas**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué contrato vincula la confirmación en memoria con la evidencia escrita?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Bitácoras operativas permiten relacionar una decisión confirmada con la evidencia que quedó registrada. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Permitir reconstruir el estado a partir de una bitácora existente válida.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
