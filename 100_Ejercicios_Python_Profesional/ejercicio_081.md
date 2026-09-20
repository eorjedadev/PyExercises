# Ejercicio 081 — Plan de renombrado sin colisiones

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_080.md) · [Siguiente](ejercicio_082.md)

### Contexto

Un archivo documental quiere revisar cambios de nombres antes de realizarlos.

### Situación

El encargo es **plan de renombrado sin colisiones**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Plan validado con nombres finales o conflictos; ninguna operación real de archivos**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Lista de nombres actuales únicos y mapa de nombre actual a nombre propuesto; solo nombres, sin rutas.

### Resultado esperado

Plan validado con nombres finales o conflictos; ninguna operación real de archivos.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Simulación sin tocar disco.
- Nombres propuestos no vacíos, sin / ni barra inversa, distintos de . y ..
- Toda fuente debe existir.
- Comparar nombres con casefold.
- Estado final debe ser único.
- Intercambios A→B,B→A se permiten como plan.

### Casos especiales y límites

Validez del estado final no determina un orden seguro de ejecución real.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Pertenencia, unicidad y equivalencia entre grupos.
- Identidad textual, normalización y formatos admitidos.
- Contratos, parámetros explícitos y responsabilidades comprobables.

### ¿Por qué pueden ser útiles?

- Ayudan a expresar identidad, coincidencias y diferencias cuando las repeticiones no aportan significado.
- Permiten separar el texto recibido de la forma usada para validarlo o compararlo.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **nombre de origen, nombre propuesto, identidad comparable, colisión final**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué diferencia hay entre validar una propuesta y aplicarla sobre un sistema de archivos?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 030](ejercicio_030.md), [ejercicio 049](ejercicio_049.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. A.txt,B.txt; A→C →válido.
2. A→B sin mover B →conflicto.
3. A→B,B→A →plan válido.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Rechazar intercambios válidos por revisar movimientos aisladamente.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Conjuntos](../Universidad_Python.md#conjuntos).
- [Diccionario_Python.md — Métodos de Cadenas](../Diccionario_Python.md#m%C3%A9todos-de-cadenas).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A.txt,B.txt; A→C →válido**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué diferencia hay entre validar una propuesta y aplicarla sobre un sistema de archivos?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Herramientas de mantenimiento validan el resultado conjunto de un cambio antes de ejecutar acciones sobre archivos. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Diseñar, sin ejecutar, una estrategia de aplicación con nombres temporales.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
