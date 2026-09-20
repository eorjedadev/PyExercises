# Ejercicio 047 — Configuración con precedencia explícita

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_046.md) · [Siguiente](ejercicio_048.md)

### Contexto

Una herramienta combina configuración distribuida y preferencias locales.

### Situación

El encargo es **configuración con precedencia explícita**. Separa las reglas de transformación de los efectos externos que existan. Prepara ejemplos reproducibles y comprueba qué datos quedan después de un rechazo.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Configuración efectiva y origen de cada valor, o errores por capa y clave**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Tres mapas: predeterminado, archivo y argumentos; claves permitidas reintentos y modo.

### Resultado esperado

Configuración efectiva y origen de cada valor, o errores por capa y clave.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Valores posteriores prevalecen: argumentos sobre archivo sobre predeterminado.
- Reintentos entero de 0 a 5 excluyendo booleanos.
- Modo resumen/detalle.
- Validar todos los valores proporcionados aunque sean sobrescritos.
- Exigir ambas claves al final.

### Casos especiales y límites

Cero es un valor explícito, no una ausencia.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Diccionarios, registros y colecciones anidadas**. Tema para investigar: Comprende claves únicas, ausencia de clave, valores por defecto y recorrido; justifica qué entidad merece ser una clave.
- **Funciones, parámetros, retornos y contratos**. Tema para investigar: Distingue devolver un resultado de imprimirlo; identifica entradas explícitas y posibles efectos sobre argumentos.
- **Excepciones y resultados de validación**. Tema para investigar: Investiga qué fallos puedes recuperar, cuáles debes propagar y cómo conservar su causa.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Relacionan identidades con atributos, estados o acumulados consultables.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.
- Separan entradas rechazadas y problemas operativos de un resultado correcto.

### Variables y nombres

Identifica estas entidades: **capas de configuración, valor efectivo, procedencia, errores por capa**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué evidencia permite explicar por qué se eligió cada valor?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 012](ejercicio_012.md), [ejercicio 024](ejercicio_024.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Base2/resumen, archivo reintentos0, argumentos modo detalle →0/detalle.
2. Clave extra →error.
3. Archivo reintentos9 aunque argumento2 →error.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Ignorar un cero porque se evalúa como falso.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).
- [Universidad_Python.md — Manejo de Errores y Excepciones](../Universidad_Python.md#manejo-de-errores-y-excepciones).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Base2/resumen, archivo reintentos0, argumentos modo detalle →0/detalle**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué evidencia permite explicar por qué se eligió cada valor?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Configuración de aplicaciones debe explicar tanto el valor efectivo como la fuente que lo determinó. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Permitir restablecer una clave al valor predeterminado con una marca explícita.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
