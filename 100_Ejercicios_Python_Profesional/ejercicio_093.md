# Ejercicio 093 — Diagnóstico de fallos sin ocultar causas

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_092.md) · [Siguiente](ejercicio_094.md)

### Contexto

Una herramienta de importación debe explicar errores útiles para el operador y para mantenimiento.

### Situación

El encargo es **diagnóstico de fallos sin ocultar causas**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Reporte de resultado, registro diagnóstico y pruebas de fallos previsibles**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Solución del ejercicio42 y fallos simulados de archivo ausente, lectura denegada, cabecera inválida y fila incorrecta.

### Resultado esperado

Reporte de resultado, registro diagnóstico y pruebas de fallos previsibles.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Distinguir fallos globales de rechazos de fila.
- Respuesta pública incluye categoría y acción sugerida.
- Conservar causa técnica para diagnóstico local.
- No capturar y silenciar cualquier excepción.
- Ningún fallo global informa importación completa.

### Casos especiales y límites

Importación parcial es distinta de importación fallida o completa.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Clasificación, propagación y recuperación de fallos.
- Organización del programa y dependencias sustituibles.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Separan entradas rechazadas y problemas operativos de un resultado correcto.
- Permiten sustituir interacción o almacenamiento sin duplicar las reglas del problema.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **categoría pública, causa técnica, filas aceptadas, estado de importación**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué información necesita cada destinatario del error?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 042](ejercicio_042.md), [ejercicio 060](ejercicio_060.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Ausente →categoría origen_no_disponible, sugerir revisar ruta.
2. Cabecera errónea →contrato_invalido, sin catálogo.
3. Fila mala entre dos buenas →parcial con dos aceptadas.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Retornar un catálogo vacío tanto ante fallo como ante archivo válido vacío.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Manejo de Errores y Excepciones](../Universidad_Python.md#manejo-de-errores-y-excepciones).
- [Universidad_Python.md — Módulos y Paquetes](../Universidad_Python.md#m%C3%B3dulos-y-paquetes).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Ausente →categoría origen_no_disponible, sugerir revisar ruta**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué información necesita cada destinatario del error?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Diagnóstico operativo adapta mensajes a sus destinatarios sin ocultar causas ni confundir resultados parciales con éxitos completos. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Agregar identificador de ejecución a cada diagnóstico sin incluir datos sensibles de filas.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
