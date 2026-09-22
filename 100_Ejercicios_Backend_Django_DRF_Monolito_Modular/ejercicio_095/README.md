# Ejercicio 095 — Desafío de Dominio: Plataforma de Cursos con Prerrequisitos y Certificación Automática

[← Ejercicio 094](../ejercicio_094/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 096 →](../ejercicio_096/README.md)

---

### Contexto de negocio

Una plataforma de educación online (E-Learning LMS) necesita gestionar cursos estructurados en módulos y lecciones, con un grafo de prerrequisitos (ej. para inscribirse en 'Django Avanzado' se debe haber aprobado previamente 'Python Profesional'). Al completar todas las lecciones y aprobar la evaluación final con nota >= 80%, el sistema debe emitir automáticamente un Certificado Digital con código único de validación pública y fecha de expiración.

### Estado actual del sistema

Monolito modular con usuarios y pagos. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Diseñar de forma autónoma el módulo de educación (`apps/learning`), modelando cursos, prerrequisitos, lecciones, progreso del estudiante (`Enrollment`), evaluaciones y emisión automática de certificados digitales.

### Objetivo

Diseñar un sistema de E-Learning completo en Django/DRF, modelando grafos de prerrequisitos acíclicos, seguimiento de progreso y certificación automatizada con validación pública.

### Actor

Estudiante / Instructor / Evaluador Público de Certificados

### Módulo responsable

Determinación autónoma por el practicante (`apps/learning`)

### Entidades involucradas

El practicante debe modelar las entidades necesarias (`Course`, `CoursePrerequisite`, `Lesson`, `Enrollment`, `LessonProgress`, `Certificate`).

### Reglas de negocio

1. Un curso puede tener N cursos prerrequisitos que el estudiante debe haber completado antes de inscribirse.
2. No se permiten ciclos en los prerrequisitos (Curso A no puede requerir B si B requiere A).
3. El progreso del estudiante se calcula como `(lecciones_completadas / total_lecciones) * 100`.
4. Al alcanzar el 100% de progreso y aprobar el examen, el servicio de aprendizaje genera automáticamente un `Certificate` con código criptográfico único de 16 caracteres.
5. Debe existir un endpoint público `GET /api/v1/learning/certificates/verify/{code}/` para que empleadores validen la autenticidad del diploma.

### Contrato esperado

El practicante debe diseñar los endpoints REST:
- `POST /api/v1/learning/courses/{id}/enroll/` (Inscripción con chequeo de prerrequisitos)
- `POST /api/v1/learning/lessons/{id}/complete/` (Marcar lección completada y actualizar progreso)
- `GET /api/v1/learning/certificates/verify/{code}/` (Verificación pública de certificado)

### Persistencia

Tablas relacionales en PostgreSQL. Persistencia física garantizada mediante tablas relacionales en PostgreSQL, con tipos de datos nativos e integridad referencial protegida.

### Relaciones

Cursos, Lecciones, Estudiantes, Progreso y Certificados.

### Autenticación

`IsAuthenticated` para estudiar; público para verificar certificados.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación de cumplimiento de prerrequisitos y no ciclos en el grafo de cursos.

### Transacciones

Transacción atómica al completar la última lección y emitir el certificado.

### Casos límite

El instructor agrega una nueva lección a un curso que un estudiante ya había completado al 100% (el progreso debe recalcularse dinámicamente sin revocar el certificado ya emitido).

### Casos de error

`400 Bad Request` si el estudiante intenta inscribirse sin haber aprobado los cursos previos obligatorios.

### Consideraciones de seguridad

Generación segura de códigos de certificado no predecibles.

### Consideraciones de rendimiento

Índice único sobre `code` en `Certificate` e índices sobre `(student_id, course_id)` en `Enrollment`.

### Fundamentos de Python relacionados

Algoritmos de detección de ciclos en grafos (DFS / Topological Sort), cálculo de porcentajes.

### Conceptos Django relacionados

`UniqueConstraint`, señales o servicios de dominio para emisión automática de certificados.

### Conceptos DRF relacionados

Serializadores de progreso y verificación pública.

### PostgreSQL

`CREATE TABLE learning_certificate (id UUID PRIMARY KEY, verification_code VARCHAR(32) UNIQUE NOT NULL, ...);`.

### Arquitectura

`apps/learning` encapsula todo el dominio educativo en el monolito.

### Dependencias entre módulos

`apps/learning` consulta `apps/users` y se integra con `apps/notifications`.

### Antes de programar

1. ¿Cómo se detecta que un árbol de prerrequisitos no contenga una dependencia circular infinita en Python?
2. ¿Por qué el código de verificación del certificado debe ser único, pseudoaleatorio e inmutable?

### Pruebas mínimas

1. Intentar inscribirse en Curso B (requiere Curso A) sin haber aprobado A -> Verificar rechazo `400`.
2. Aprobar Curso A, inscribirse en B -> Inscripción exitosa.
3. Completar todas las lecciones de B -> Verificar que el progreso llegue al 100% y se genere automáticamente el `Certificate` con su código único.

### Pruebas negativas

1. Consultar el endpoint de verificación pública con un código falso -> Verificar respuesta `404 Not Found` (certificado no válido).

### Documentación

Documentar la estructura del LMS y la verificación de diplomas en `docs/LEARNING_DOMAIN.md`.

### Explicación posterior

Explica cómo el modelado de grafos acíclicos de prerrequisitos y la emisión automática de credenciales digitales se integran limpiamente en una arquitectura modular.

### Aplicación profesional

Plataformas de educación online (Coursera, Udemy, Platzi), sistemas de certificación corporativa y universidades digitales.

### Reto adicional

Generar dinámicamente un PDF del diploma con el nombre del estudiante y código QR de validación.
