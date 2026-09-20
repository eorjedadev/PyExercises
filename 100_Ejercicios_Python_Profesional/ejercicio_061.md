# Ejercicio 061 — Consumo de páginas de una API simulada

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_060.md) · [Siguiente](ejercicio_062.md)

### Contexto

Un equipo debe reunir resultados de un servicio que entrega páginas enlazadas.

### Situación

El encargo es **consumo de páginas de una api simulada**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Items reunidos, páginas visitadas y estado completo/incompleto**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Mapa en memoria token→página con items y siguiente token o None; token inicial; items con id y contenido.

### Resultado esperado

Items reunidos, páginas visitadas y estado completo/incompleto.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Sin red.
- Recorrer hasta None.
- Token inexistente o repetido detiene con diagnóstico.
- Items repetidos por id conservan primera aparición.
- Mantener orden recibido.
- Devolver resultado parcial marcado incompleto ante fallo.

### Casos especiales y límites

Una página vacía puede tener una página siguiente.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Identidad de entidades y organización de datos relacionados.
- Clasificación, propagación y recuperación de fallos.
- Organización del programa y dependencias sustituibles.

### ¿Por qué pueden ser útiles?

- Relacionan identidades con atributos, estados o acumulados consultables.
- Separan entradas rechazadas y problemas operativos de un resultado correcto.
- Permiten sustituir interacción o almacenamiento sin duplicar las reglas del problema.

### Variables y nombres

Identifica estas entidades: **token de página, items reunidos, páginas visitadas, estado de completitud**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué condición indica fin y cuál indica un servicio inconsistente?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 033](ejercicio_033.md), [ejercicio 043](ejercicio_043.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. p1:[A], siguiente p2; p2:[A,B], None →A,B, completo.
2. p1 apunta a p1 →incompleto por ciclo.
3. p1 apunta a ausente →parcial incompleto.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Terminar al recibir una página sin items aunque tenga continuación.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Diccionarios](../Universidad_Python.md#diccionarios).
- [Universidad_Python.md — Manejo de Errores y Excepciones](../Universidad_Python.md#manejo-de-errores-y-excepciones).
- [Universidad_Python.md — Módulos y Paquetes](../Universidad_Python.md#m%C3%B3dulos-y-paquetes).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **p1:[A], siguiente p2; p2:[A,B], None →A,B, completo**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué condición indica fin y cuál indica un servicio inconsistente?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Clientes de servicios paginados deben distinguir final normal, resultados parciales y referencias inconsistentes. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Detectar si un id repetido trae contenido distinto.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
