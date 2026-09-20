# Ejercicio 059 — Detección de archivos con contenido repetido

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_058.md) · [Siguiente](ejercicio_060.md)

### Contexto

Una herramienta local identifica entregas duplicadas sin borrar nada.

### Situación

El encargo es **detección de archivos con contenido repetido**. Separa las reglas de transformación de los efectos externos que existan. Prepara ejemplos reproducibles y comprueba qué datos quedan después de un rechazo.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Grupos de contenido idéntico y fallos de lectura; ninguna modificación de archivos**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Lista de rutas a archivos regulares dentro de una carpeta de práctica.

### Resultado esperado

Grupos de contenido idéntico y fallos de lectura; ninguna modificación de archivos.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Comparar contenido binario completo.
- Nombres diferentes pueden ser duplicados.
- Archivos vacíos también.
- Informar rutas ilegibles por separado.
- Ordenar rutas dentro de cada grupo.
- Grupos de al menos dos.
- Ordenar grupos por su primera ruta.

### Casos especiales y límites

El mismo tamaño no prueba que los contenidos sean iguales.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Rutas, archivos, codificación y gestión de recursos**. Tema para investigar: Comprende modos de apertura, cierre de recursos, UTF-8 y efectos de sobrescribir un archivo.
- **Diccionarios, registros y colecciones anidadas**. Tema para investigar: Comprende claves únicas, ausencia de clave, valores por defecto y recorrido; justifica qué entidad merece ser una clave.
- **Excepciones y resultados de validación**. Tema para investigar: Investiga qué fallos puedes recuperar, cuáles debes propagar y cómo conservar su causa.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Conectan los datos del programa con recursos que pueden faltar o fallar.
- Relacionan identidades con atributos, estados o acumulados consultables.
- Separan entradas rechazadas y problemas operativos de un resultado correcto.

### Variables y nombres

Identifica estas entidades: **ruta examinada, contenido binario, grupo de equivalencia, lectura fallida**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué evidencia suficiente usarás para afirmar igualdad de contenido?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 030](ejercicio_030.md), [ejercicio 049](ejercicio_049.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. a y b contienen bytes ABC, c contiene ABD →grupo a,b.
2. Dos archivos vacíos →grupo.
3. Una ruta ausente →fallo y restantes comparados.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Declarar duplicados por nombre o tamaño solamente.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Archivos y Context Managers](../Universidad_Python.md#archivos-y-context-managers).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [Universidad_Python.md — Manejo de Errores y Excepciones](../Universidad_Python.md#manejo-de-errores-y-excepciones).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **a y b contienen bytes ABC, c contiene ABD →grupo a,b**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué evidencia suficiente usarás para afirmar igualdad de contenido?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Auditorías documentales buscan equivalencia de contenido sin confundirla con coincidencia de nombre o tamaño. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Reducir memoria con lectura por bloques conservando la exactitud.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
