# Ejercicio 042 — Carga de precios desde CSV

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_041.md) · [Siguiente](ejercicio_043.md)

### Contexto

Un comercio recibe precios desde una hoja de cálculo exportada.

### Situación

El encargo es **carga de precios desde csv**. Separa las reglas de transformación de los efectos externos que existan. Prepara ejemplos reproducibles y comprueba qué datos quedan después de un rechazo.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Catálogo aceptado y rechazos numerados por registro de datos desde 1**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Archivo UTF-8 con cabecera exacta codigo,precio_centimos; filas de dos campos; precios como enteros positivos.

### Resultado esperado

Catálogo aceptado y rechazos numerados por registro de datos desde 1.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Usar reglas CSV para comillas y comas.
- Código recortado no vacío.
- Primer precio válido de un código prevalece.
- Filas inválidas o códigos repetidos se reportan.
- Cabecera incorrecta aborta.

### Casos especiales y límites

Un campo entre comillas puede contener una coma.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Intercambio tabular y módulo csv**. Tema para investigar: Ubica csv en el diccionario y explora reader, writer y DictReader con la ayuda local del módulo; diferencia registro CSV y línea física.
- **Excepciones y resultados de validación**. Tema para investigar: Investiga qué fallos puedes recuperar, cuáles debes propagar y cómo conservar su causa.
- **Diccionarios, registros y colecciones anidadas**. Tema para investigar: Comprende claves únicas, ausencia de clave, valores por defecto y recorrido; justifica qué entidad merece ser una clave.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Preserva campos que pueden incluir delimitadores o comillas sin confundirlos con columnas adicionales.
- Separan entradas rechazadas y problemas operativos de un resultado correcto.
- Relacionan identidades con atributos, estados o acumulados consultables.

### Variables y nombres

Identifica estas entidades: **cabecera esperada, registro CSV, precio convertido, rechazos de importación**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué error invalida el archivo y cuál solo una fila?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 012](ejercicio_012.md), [ejercicio 017](ejercicio_017.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. A,100 seguido A,200 → A100 y segundo rechazado.
2. Precio 'abc' → fila rechazada.
3. Cabecera incorrecta → sin catálogo importado.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Separar cada línea por comas sin respetar el formato CSV.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Diccionario_Python.md — Imports Importantes por Área](../Diccionario_Python.md#imports-importantes-por-%C3%A1rea).
- [Universidad_Python.md — Manejo de Errores y Excepciones](../Universidad_Python.md#manejo-de-errores-y-excepciones).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A,100 seguido A,200 → A100 y segundo rechazado**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué error invalida el archivo y cuál solo una fila?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Importadores tabulares separan errores del documento, filas rechazadas y colisiones de identidad. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Comparar el catálogo importado con uno anterior antes de aprobar cambios.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
