# Ejercicio 086 — Seguimiento de un envío por eventos

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_085.md) · [Siguiente](ejercicio_087.md)

### Contexto

Logística necesita validar la historia de un paquete sin permitir estados imposibles.

### Situación

El encargo es **seguimiento de un envío por eventos**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Estado final e historial de decisiones con estado previo y posterior**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Estado inicial preparado y eventos recoger, entregar, devolver, cancelar con id único.

### Resultado esperado

Estado final e historial de decisiones con estado previo y posterior.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Preparado admite recoger→en tránsito o cancelar→cancelado.
- En tránsito admite entregar→entregado o devolver→devuelto.
- Estados finales no admiten nuevos cambios.
- Eventos inválidos se registran como rechazados.
- No detener todo el historial.

### Casos especiales y límites

Un evento conocido puede ser inválido para el estado actual.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Invariantes y operaciones dependientes del estado vigente.
- Organización del programa y dependencias sustituibles.
- Evidencia automatizada y detección de regresiones.

### ¿Por qué pueden ser útiles?

- Hace explícito qué operaciones son válidas y qué cambia al aceptarlas.
- Permiten sustituir interacción o almacenamiento sin duplicar las reglas del problema.
- Aportan evidencia repetible de comportamientos y de fallos que deben permanecer controlados.

### Variables y nombres

Identifica estas entidades: **estado del envío, evento recibido, transición admitida, historial**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué reglas pertenecen al evento y cuáles a la combinación evento/estado?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 050](ejercicio_050.md), [ejercicio 055](ejercicio_055.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Recoger,entregar →entregado.
2. Entregar desde preparado →rechazo.
3. Cancelar,recoger →cancelado y segundo rechazo.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Aceptar cualquier evento solo porque su nombre es conocido.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Funciones](../Universidad_Python.md#funciones).
- [Universidad_Python.md — Módulos y Paquetes](../Universidad_Python.md#m%C3%B3dulos-y-paquetes).
- [INTENSIVO DE PYTHON (Eric Matthes).md — 11. Probar el código](../INTENSIVO%20DE%20PYTHON%20%28Eric%20Matthes%29.md#toc-236).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Recoger,entregar →entregado**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué reglas pertenecen al evento y cuáles a la combinación evento/estado?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Seguimiento logístico conserva historia y rechaza transiciones incompatibles con el estado del envío. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir incidencia en tránsito que no cambie el estado y sí deje evidencia.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
