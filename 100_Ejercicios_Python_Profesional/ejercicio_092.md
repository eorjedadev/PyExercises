# Ejercicio 092 — Repositorio intercambiable de contactos

[Índice](README.md#indice-de-ejercicios) · [Anterior](ejercicio_091.md) · [Siguiente](ejercicio_093.md)

### Contexto

Una aplicación quiere usar almacenamiento en memoria durante pruebas y JSON al trabajar localmente.

### Situación

El encargo es **repositorio intercambiable de contactos**. Define una interfaz comprobable y justifica la organización elegida. Automatiza las pruebas del contrato y evita dependencias externas que el problema no necesita.

### Objetivo

Producir este resultado a partir de las entradas indicadas: **Misma suite de comportamiento pasa con ambos repositorios y una prueba adicional de persistencia**. La solución debe distinguir los resultados válidos de los rechazos previstos.

### Requisitos

- Respeta las reglas y los formatos, órdenes o interfaces que se indiquen.
- Aplica las [convenciones comunes](README.md#convenciones-comunes) cuando no exista una excepción explícita.
- Entrega implementación, pruebas y una explicación de tus decisiones.

### Datos de entrada

Contactos con id y nombre no vacíos; operaciones crear, obtener y eliminar; dos implementaciones con mismo contrato.

### Resultado esperado

Misma suite de comportamiento pasa con ambos repositorios y una prueba adicional de persistencia.

Los mensajes son de redacción libre; las decisiones y los datos exigidos deben ser inequívocos.

### Reglas de negocio

- Crear id existente produce conflicto.
- Obtener/eliminar ausente produce no encontrado.
- Devolver datos que el consumidor no pueda alterar internamente.
- JSON persiste tras reinicio.
- Archivo corrupto produce error explícito.
- No se exige concurrencia.

### Casos especiales y límites

Uniformidad de interfaz no demuestra por sí sola uniformidad de comportamiento.

Comprueba las fronteras del contrato y explica cuándo un vacío es un resultado válido o una entrada rechazada.

### Fundamentos de Python relacionados

Elige y justifica tus herramientas antes de abrir las referencias. Debes relacionar estos conceptos, sin una estructura de datos impuesta:

- Organización del programa y dependencias sustituibles.
- Encapsulación de estado y protección de invariantes.
- Serialización, esquema y compatibilidad de datos persistidos.

### ¿Por qué pueden ser útiles?

- Permiten sustituir interacción o almacenamiento sin duplicar las reglas del problema.
- Pueden reunir estado y operaciones cuando esa unión protege reglas del dominio.
- Permite transportar o guardar estructuras; la lectura sintáctica por sí sola no garantiza que cumplan el contrato.

### Variables y nombres

Identifica estas entidades: **contrato del repositorio, contacto almacenado, copia devuelta, error de persistencia**. Diseña nombres para variables, colecciones, resultados intermedios, una función y sus parámetros; evita nombres como `dato1` o `temp`.

Comunica intención y unidades, distingue singular/plural y usa verbos para acciones. Identifica qué reglas merecen constantes con nombre. Explica un nombre que descartaste y por qué el elegido ayuda a leer el código.

### Antes de programar

- ¿Qué decisiones son dominio compartido y cuáles dependen del almacenamiento?
- Define por tu cuenta los contratos, invariantes y límites de responsabilidad; contrasta al menos dos diseños posibles antes de elegir.

Recupera razonamiento de [ejercicio 024](ejercicio_024.md), [ejercicio 043](ejercicio_043.md), [ejercicio 055](ejercicio_055.md): identifica una similitud y una diferencia de contrato antes de reutilizar algo.

### Pruebas mínimas

1. Crear A/Ana y obtener A →Ana en ambos.
2. Crear A otra vez →conflicto en ambos.
3. Reabrir repositorio JSON →A sigue disponible.

Añade un caso propio para el límite señalado en este enunciado. Escribe la expectativa antes de ejecutar y comprueba también los efectos sobre datos o archivos, si existen.

### Errores comunes

- Hacer que la aplicación consulte el tipo concreto de repositorio para decidir reglas.
- Dar por correcta la solución tras un solo ejemplo, sin comprobar límites y rechazos.

### Consulta recomendada

- [Universidad_Python.md — Módulos y Paquetes](../Universidad_Python.md#m%C3%B3dulos-y-paquetes).
- [Universidad_Python.md — Programación Orientada a Objetos](../Universidad_Python.md#programaci%C3%B3n-orientada-a-objetos).
- [NotasdePythonparaprofesionales.md](../NotasdePythonparaprofesionales.md) — **Capítulo 49: Módulo JSON** (buscar ese título dentro del documento).

Investiga el concepto que te falte; cierra los ejemplos resueltos antes de implementar tu diseño.

### Explicación posterior

- Explica qué hace tu programa y sigue los datos desde la entrada hasta el resultado en este escenario: **Crear A/Ana y obtener A →Ana en ambos**.
- ¿Por qué elegiste esas representaciones? ¿Qué significan tus variables, parámetros y resultados intermedios?
- Defiende tu respuesta a esta decisión de diseño: ¿Qué decisiones son dominio compartido y cuáles dependen del almacenamiento?
- ¿Qué validaciones realizaste, qué caso puede fallar todavía y qué parte sería reutilizable?
- ¿Podría otra persona explicar el contrato leyendo nombres, funciones y pruebas, sin volver al enunciado? Señala una mejora concreta.

Antes de modificar o reutilizar código anterior, léelo y predice el recorrido de un caso límite sin ejecutarlo. Registra la predicción y compruébala después.

### Aplicación profesional

Repositorios intercambiables permiten probar dominio y almacenamiento mediante un contrato de comportamiento compartido. Propón otro contexto donde reutilizarías el mecanismo y una regla que tendrías que adaptar.

### Reto adicional

Añadir una implementación de solo lectura que anuncie explícitamente su capacidad.

Es opcional. Señala qué pruebas deben conservar su resultado y cuáles cambian con el nuevo requisito.
