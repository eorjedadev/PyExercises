# Ejercicio 066 — Procesamiento incremental de un registro extenso

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_065.md) · [Siguiente](ejercicio_067.md)

### Contexto

Operaciones debe resumir un archivo que puede ser mayor que la memoria disponible.

### Situación

El encargo es **procesamiento incremental de un registro extenso**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Resumen por servicio y cantidad total de rechazadas, más reporte de errores**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Archivo UTF-8 con una línea por evento, formato servicio;duracion_ms, duración entera no negativa.

### Resultado esperado

Resumen por servicio y cantidad total de rechazadas, más reporte de errores.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Leer incrementalmente.
- Cada línea debe tener exactamente dos campos no vacíos.
- Acumular cantidad, suma y máximo por servicio.
- Rechazos con número y motivo pueden escribirse incrementalmente.
- No conservar todas las líneas ni todos los errores en memoria.

### Casos especiales y límites

El tamaño del estado debe depender de servicios distintos, no de cantidad de eventos.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Consumo incremental y límites de memoria.
- Persistencia, recursos externos y efectos observables.
- Identidad de entidades y organización de datos relacionados.

### ¿Por qué pueden ser útiles?

- Permiten consumir datos sin materializar todo el origen en memoria.
- Conectan los datos del programa con recursos que pueden faltar o fallar.
- Relacionan identidades con atributos, estados o acumulados consultables.

### Variables y nombres

Identifica estas entidades: **evento actual, acumulado por servicio, duración máxima, conteo de rechazos**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué datos debes conservar para calcular cada métrica y cuáles puedes descartar?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 041](ejercicio_041.md), [ejercicio 044](ejercicio_044.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. A;10 y A;20 →cantidad2,suma30,máximo20.
2. A;-1 →rechazo.
3. Archivo vacío →resumen vacío.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Convertir el iterador completo en lista por comodidad.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md — Capítulo 17. Iteradores, generadores y corrutinas clásicas](../luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.md#capitulo-17-iteradores-generadores-y-corrutinas-clasicas).
- [Universidad_Python.md — Archivos y Context Managers](../Universidad_Python.md#archivos-y-context-managers).
- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A;10 y A;20 →cantidad2,suma30,máximo20**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué datos debes conservar para calcular cada métrica y cuáles puedes descartar?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Procesamiento de archivos extensos reduce memoria conservando solo los datos necesarios para sus métricas. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir media por servicio sin almacenar todas sus duraciones.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
