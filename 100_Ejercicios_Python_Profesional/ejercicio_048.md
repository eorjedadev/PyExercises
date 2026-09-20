# Ejercicio 048 — Lectura de movimientos con decimales exactos

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_047.md) · [Siguiente](ejercicio_049.md)

### Contexto

Un registro de gastos usa importes decimales escritos por personas.

### Situación

El encargo es **lectura de movimientos con decimales exactos**. Separa las reglas de transformación de los efectos externos que existan. Prepara ejemplos reproducibles y comprueba qué datos quedan después de un rechazo.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Importes aceptados, posiciones rechazadas y suma**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Lista de textos con formato opcional signo menos, dígitos ASCII, punto y exactamente dos decimales; sin espacios.

### Resultado esperado

Importes aceptados, posiciones rechazadas y suma.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Aceptar negativos y cero.
- Rechazar comas, exponentes, NaN, infinito y decimales adicionales.
- Separar inválidos.
- Total exacto presentado con dos decimales.

### Casos especiales y límites

El formato válido debe comprobarse además de poder convertir el texto.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

- **Representación exacta de importes y política de redondeo**. Tema para investigar: Ubica decimal y fractions en el diccionario; compara céntimos enteros y representaciones exactas. Investiga conversión desde texto y cuantización en la ayuda local.
- **Cadenas, métodos de texto y comparaciones**. Tema para investigar: Investiga recorte, partición, pertenencia y diferencias entre igualdad textual y equivalencia definida por negocio.
- **Excepciones y resultados de validación**. Tema para investigar: Investiga qué fallos puedes recuperar, cuáles debes propagar y cómo conservar su causa.

Son alternativas de estudio, no una lista de herramientas obligatorias. Justifica cuáles eliges.

### ¿Por qué pueden ser útiles?

- Mantiene las cantidades monetarias coherentes con las unidades y reglas exigidas.
- Permiten separar el texto recibido de la forma usada para validarlo o compararlo.
- Separan entradas rechazadas y problemas operativos de un resultado correcto.

### Variables y nombres

Identifica estas entidades: **importe textual, importe exacto, movimientos rechazados, saldo calculado**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué garantía necesita la representación elegida para sumar dinero?
- ¿Qué contratos separarías para comprobar las reglas sin depender de la presentación?
- ¿Qué datos pueden cambiar y qué evidencia mostraría una modificación no deseada?

Recupera razonamiento de [ejercicio 007](ejercicio_007.md), [ejercicio 026](ejercicio_026.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. 0.10,0.20,-0.05 →0.25.
2. 1.005 y 1,20 →rechazados.
3. Lista vacía →0.00.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Usar un tipo que introduzca errores binarios y luego ocultarlos al mostrar.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Diccionario_Python.md — Imports para Ciencia de Datos](../Diccionario_Python.md#imports-para-ciencia-de-datos).
- [Diccionario_Python.md — Métodos de Cadenas](../Diccionario_Python.md#m%C3%A9todos-de-cadenas).
- [Universidad_Python.md — Manejo de Errores y Excepciones](../Universidad_Python.md#manejo-de-errores-y-excepciones).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **0.10,0.20,-0.05 →0.25**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué garantía necesita la representación elegida para sumar dinero?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Procesamiento de importes exige exactitud y un contrato textual más estricto que la mera posibilidad de conversión. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Aceptar símbolo monetario mediante una regla de formato nueva y explícita.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
