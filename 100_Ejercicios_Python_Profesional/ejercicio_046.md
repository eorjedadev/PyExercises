# Ejercicio 046 — Exportación de un resumen comercial

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_045.md) · [Siguiente](ejercicio_047.md)

### Contexto

Una empresa entrega un resumen CSV que otras herramientas deben poder leer.

### Situación

El encargo es **exportación de un resumen comercial**. Separa las reglas de transformación de los efectos externos que existan. Prepara ejemplos reproducibles y comprueba qué datos quedan después de un rechazo.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Archivo CSV verificable y cantidad de regiones exportadas**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Registros válidos con región textual no vacía e importe no negativo en céntimos; ruta de salida nueva.

### Resultado esperado

Archivo CSV verificable y cantidad de regiones exportadas.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Agrupar por región exacta.
- Ordenar regiones.
- Cabecera region,total_centimos.
- UTF-8.
- No sobrescribir un destino existente.
- Entrada vacía produce solo cabecera.

### Casos especiales y límites

Las comillas y comas del nombre de región deben sobrevivir al intercambio.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Intercambio tabular y módulo csv**. Tema para investigar: Ubica csv en el diccionario y explora reader, writer y DictReader con la ayuda local del módulo; diferencia registro CSV y línea física.
- **Rutas, archivos, codificación y gestión de recursos**. Tema para investigar: Comprende modos de apertura, cierre de recursos, UTF-8 y efectos de sobrescribir un archivo.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Preserva campos que pueden incluir delimitadores o comillas sin confundirlos con columnas adicionales.
- Conectan los datos del programa con recursos que pueden faltar o fallar.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **región comercial, importe agregado, ruta de exportación, filas escritas**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Cómo comprobarás el contenido sin depender de cómo se ve en un editor?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 017](ejercicio_017.md), [ejercicio 042](ejercicio_042.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Norte100,Norte50,Sur0 → Norte150,Sur0.
2. Región 'Costa, norte' → un único campo al releer.
3. Destino existente → error sin cambios.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Confundir un CSV visualmente plausible con uno válido.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Diccionario_Python.md — Imports Importantes por Área](../Diccionario_Python.md#imports-importantes-por-%C3%A1rea).
- [Universidad_Python.md — Archivos y Context Managers](../Universidad_Python.md#archivos-y-context-managers).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Norte100,Norte50,Sur0 → Norte150,Sur0**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Cómo comprobarás el contenido sin depender de cómo se ve en un editor?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Intercambio de reportes necesita formatos que otras herramientas puedan leer sin perder comas, comillas o caracteres. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Incluir cantidad de operaciones por región.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
