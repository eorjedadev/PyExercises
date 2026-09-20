# Ejercicio 094 — Pruebas de fallos durante una exportación

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_093.md) · [Siguiente](ejercicio_095.md)

### Contexto

Un equipo quiere evitar que una exportación fallida sustituya un reporte válido.

### Situación

El encargo es **pruebas de fallos durante una exportación**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Exportación confirmada o error con evidencia de conservación del archivo previo**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Registros de resumen y ruta destino que puede existir; componente de escritura sustituible durante pruebas.

### Resultado esperado

Exportación confirmada o error con evidencia de conservación del archivo previo.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Preparar salida en archivo temporal de la misma carpeta.
- Validar escritura y sustituir destino solo tras éxito.
- Fallos previos conservan destino byte por byte.
- Limpiar temporal cuando sea posible e informar si no se puede.
- Alcance: fallos controlados en un proceso, sin prometer resistencia a cualquier corte eléctrico.

### Casos especiales y límites

Una prueba que solo falla antes de empezar no demuestra protección frente a escritura parcial.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Persistencia, recursos externos y efectos observables.
- Clasificación, propagación y recuperación de fallos.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Conectan los datos del programa con recursos que pueden faltar o fallar.
- Separan entradas rechazadas y problemas operativos de un resultado correcto.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **archivo provisional, destino confirmado, fase fallida, limpieza pendiente**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿En qué punto se considera publicada la nueva versión?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 046](ejercicio_046.md), [ejercicio 093](ejercicio_093.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Fallo al escribir después de una fila →destino anterior intacto.
2. Fallo de sustitución →destino intacto y diagnóstico.
3. Éxito →destino con reporte nuevo completo.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Abrir el destino definitivo en modo de sobrescritura antes de tener el reporte completo.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Archivos y Context Managers](../Universidad_Python.md#archivos-y-context-managers).
- [Universidad_Python.md — Manejo de Errores y Excepciones](../Universidad_Python.md#manejo-de-errores-y-excepciones).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Fallo al escribir después de una fila →destino anterior intacto**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿En qué punto se considera publicada la nueva versión?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Publicación de archivos necesita proteger la versión confirmada frente a fallos ocurridos durante la preparación de otra. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Verificar el contenido temporal antes de permitir la publicación.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
