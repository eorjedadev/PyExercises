# Ejercicio 049 — Inspección de un directorio de entregas

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_048.md) · [Siguiente](ejercicio_050.md)

### Contexto

Una coordinadora necesita saber qué archivos recibió en una carpeta de trabajo.

### Situación

El encargo es **inspección de un directorio de entregas**. Separa las reglas de transformación de los efectos externos que existan. Prepara ejemplos reproducibles y comprueba qué datos quedan después de un rechazo.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Nombres y tamaños coincidentes, cantidad y bytes totales**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Ruta de carpeta y extensión buscada como .pdf.

### Resultado esperado

Nombres y tamaños coincidentes, cantidad y bytes totales.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Revisar solo hijos directos que sean archivos regulares, sin seguir enlaces simbólicos.
- Extensión comparada sin distinguir mayúsculas.
- Ordenar por nombre exacto.
- Informar tamaño en bytes.
- Carpeta ausente es error.

### Casos especiales y límites

Una carpeta con nombre terminado en .pdf no es un archivo recibido.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Rutas, archivos, codificación y gestión de recursos**. Tema para investigar: Comprende modos de apertura, cierre de recursos, UTF-8 y efectos de sobrescribir un archivo.
- **Ordenación, claves de comparación y estabilidad**. Tema para investigar: Investiga orden total, criterios compuestos y diferencia entre ordenar una copia y modificar la colección original.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Conectan los datos del programa con recursos que pueden faltar o fallar.
- Hacen reproducibles las prioridades y sus desempates.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **carpeta de entrada, extensión buscada, tamaño en bytes, archivos coincidentes**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué propiedades debes consultar sin leer el contenido de cada entrega?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 041](ejercicio_041.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. a.PDF de10 bytes y b.txt de5 → a.PDF, total10.
2. Solo subcarpeta c.pdf →ningún archivo.
3. Carpeta vacía →cero.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Confundir la extensión con cualquier coincidencia dentro del nombre.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Archivos y Context Managers](../Universidad_Python.md#archivos-y-context-managers).
- [Universidad_Python.md — Funciones Integradas](../Universidad_Python.md#funciones-integradas).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **a.PDF de10 bytes y b.txt de5 → a.PDF, total10**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué propiedades debes consultar sin leer el contenido de cada entrega?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Inventarios documentales inspeccionan metadatos de archivos sin confundir carpetas, enlaces y documentos recibidos. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir agrupación por extensión manteniendo la inspección sin recursión.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
