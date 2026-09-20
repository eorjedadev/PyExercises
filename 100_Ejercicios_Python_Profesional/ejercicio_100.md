# Ejercicio 100 — Entrega de un importador profesional acotado

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_099.md)

### Contexto

Un equipo te encarga unir validación, revisión y persistencia en una entrega pequeña que otra persona pueda mantener.

### Situación

El encargo es **entrega de un importador profesional acotado**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Herramienta con contratos separados, reporte de ejecución, pruebas, guía de uso y breve memoria de decisiones; reutilizar razonamiento previo sin copiar módulos innecesarios**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Catálogo JSON con revision entera no negativa y productos como lista de registros codigo/precio_centimos; códigos únicos no vacíos y precios enteros positivos. CSV de cambios con cabecera exacta codigo,precio_centimos y códigos existentes. Revisión esperada entera no negativa para aplicar.

### Resultado esperado

Herramienta con contratos separados, reporte de ejecución, pruebas, guía de uso y breve memoria de decisiones; reutilizar razonamiento previo sin copiar módulos innecesarios.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Solo simular y aplicar.
- CSV inválido o con códigos repetidos rechaza todo el lote.
- Vista previa no escribe.
- Aplicación verifica revisión esperada, cambia todo o nada y aumenta revisión en1 solo si algún precio cambia.
- Escritura fallida conserva archivo previo.
- Reporte determinista con cambiados, sin_cambio o rechazo.
- Sin red ni concurrencia entre procesos.
- Códigos CSV recortados y comparados exactamente.
- Precios CSV solo dígitos ASCII que representen un entero positivo.
- Catálogo inválido impide ambos modos.
- CSV solo con cabecera es válido y no cambia revisión.
- Reporte ordenado por código.

### Casos especiales y límites

Una simulación correcta no garantiza que la aplicación posterior use el mismo estado; el contrato debe hacer visible ese límite.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Organización del programa y dependencias sustituibles.
- Persistencia, recursos externos y efectos observables.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Permiten sustituir interacción o almacenamiento sin duplicar las reglas del problema.
- Conectan los datos del programa con recursos que pueden faltar o fallar.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **catálogo confirmado, propuesta validada, revisión esperada, resultado publicado**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué partes puedes reemplazar o probar aisladamente y qué evidencia demuestra el comportamiento de extremo a extremo?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 042](ejercicio_042.md), [ejercicio 076](ejercicio_076.md), [ejercicio 082](ejercicio_082.md), [ejercicio 090](ejercicio_090.md), [ejercicio 094](ejercicio_094.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Catálogo rev2 A100,B200; CSV A120 →previa A100→120; aplicar rev2 →rev3 y B200 intacto.
2. Revisión esperada1 →rechazo sin cambios.
3. Fila inválida o fallo de escritura →archivo previo idéntico.
4. CSV A100 sobre A100 →sin cambio ni nueva revisión.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Unir piezas que funcionaban por separado sin revisar sus contratos compartidos.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Módulos y Paquetes](../Universidad_Python.md#m%C3%B3dulos-y-paquetes).
- [Universidad_Python.md — Archivos y Context Managers](../Universidad_Python.md#archivos-y-context-managers).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Catálogo rev2 A100,B200; CSV A120 →previa A100→120; aplicar rev2 →rev3 y B200 intacto**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué partes puedes reemplazar o probar aisladamente y qué evidencia demuestra el comportamiento de extremo a extremo?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Una entrega mantenible integra contratos de validación, revisión y publicación sin ampliar innecesariamente el alcance del producto. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Permitir incorporar códigos nuevos mediante una opción explícita y actualizar contratos, pruebas y guía de uso.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
