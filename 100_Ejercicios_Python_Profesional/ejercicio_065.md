# Ejercicio 065 — Traducción entre dos contratos de proveedor

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_064.md) · [Siguiente](ejercicio_066.md)

### Contexto

Una aplicación recibe datos equivalentes con formatos distintos.

### Situación

El encargo es **traducción entre dos contratos de proveedor**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Registro común validado o errores de adaptación identificando proveedor y campo**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Proveedor A entrega sku y precio_centimos entero; B entrega code y amount como texto decimal positivo con dos cifras; ambos reciben una moneda literal PEN.

### Resultado esperado

Registro común validado o errores de adaptación identificando proveedor y campo.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Producir código recortado no vacío, precio entero positivo en céntimos y moneda.
- Rechazar moneda diferente, proveedor desconocido y campos faltantes.
- No consultar servicios externos.

### Casos especiales y límites

La lógica que consume el registro común no debe conocer el proveedor.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Organización del programa y dependencias sustituibles.
- Precisión numérica y políticas de redondeo.
- Contratos, parámetros explícitos y responsabilidades comprobables.

### ¿Por qué pueden ser útiles?

- Permiten sustituir interacción o almacenamiento sin duplicar las reglas del problema.
- Mantiene las cantidades monetarias coherentes con las unidades y reglas exigidas.
- Permiten probar decisiones sin depender de cómo se piden o muestran los datos.

### Variables y nombres

Identifica estas entidades: **registro externo, proveedor, precio canónico, error de contrato**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué variaciones pertenecen a la adaptación y cuáles al dominio compartido?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 040](ejercicio_040.md), [ejercicio 048](ejercicio_048.md), [ejercicio 051](ejercicio_051.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. A:sku X,precio_centimos125,PEN y B:code X,amount1.25,PEN →mismo registro.
2. B1.005 →rechazo.
3. USD →rechazo.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Propagar formatos de cada proveedor por todo el programa.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Módulos y Paquetes](../Universidad_Python.md#m%C3%B3dulos-y-paquetes).
- [Diccionario_Python.md — Imports para Ciencia de Datos](../Diccionario_Python.md#imports-para-ciencia-de-datos).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 8. Funciones](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-154).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **A:sku X,precio_centimos125,PEN y B:code X,amount1.25,PEN →mismo registro**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué variaciones pertenecen a la adaptación y cuáles al dominio compartido?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Después de implementar, lee una función sin ejecutarla y predice su salida y sus efectos para uno de los casos mínimos. Contrasta tu predicción con la ejecución.

### Aplicación profesional

Adaptadores de proveedores evitan que formatos externos distintos contaminen las reglas internas compartidas. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Incorporar un tercer proveedor sin cambiar las operaciones sobre el registro común.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
