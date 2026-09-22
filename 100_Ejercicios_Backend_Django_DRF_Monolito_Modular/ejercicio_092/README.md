# Ejercicio 092 — Desafío de Dominio: Plataforma B2B de Compras con Aprobación Jerárquica

[← Ejercicio 091](../ejercicio_091/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 093 →](../ejercicio_093/README.md)

---

### Contexto de negocio

Una corporación requiere una plataforma B2B para que sus empleados soliciten insumos y equipos. A diferencia del e-commerce B2C directo, una solicitud de compra corporativa (`PurchaseRequisition`) no se paga de inmediato: según el monto total, requiere un flujo de aprobación jerárquico por niveles: - Menos de $1,000: Aprobación de Jefe Directo (`TEAM_LEAD`). - Entre $1,000 y $10,000: Aprobación de Gerente de Área (`DEPARTMENT_MANAGER`). - Más de $10,000: Aprobación adicional de Dirección Financiera (`CFO`). Además, cada departamento tiene un presupuesto mensual asignado que no puede ser sobregirado.

### Estado actual del sistema

Monolito modular con catálogo de productos y usuarios.

### Nueva necesidad

Diseñar de forma autónoma el módulo B2B (`apps/procurement`), modelando organizaciones, departamentos, presupuestos mensuales, solicitudes de compra y el motor de flujo de aprobaciones jerárquicas.

### Objetivo

Diseñar un sistema empresarial B2B complejo con jerarquías organizacionales, presupuestos departamentales y flujos de aprobación multinivel basados en umbrales de dinero.

### Actor

Empleado Solicitante / Aprobador Jerárquico / Director Financiero

### Módulo responsable

Determinación autónoma por el practicante (`apps/procurement`)

### Entidades involucradas

El practicante debe modelar las entidades necesarias (`Organization`, `Department`, `DepartmentBudget`, `PurchaseRequisition`, `RequisitionApprovalStep`).

### Reglas de negocio

1. Cada departamento tiene un presupuesto asignado por mes (`budget_limit`, `spent_amount`, `committed_amount`).
2. Al crearse una solicitud, el monto pasa a comprometerse (`committed_amount += total`) para que solicitudes simultáneas no sobregiren el presupuesto.
3. El motor de aprobación debe calcular dinámicamente los pasos de aprobación requeridos según el monto total.
4. Si un aprobador rechaza la solicitud en cualquier nivel, el flujo se cancela y se libera el monto comprometido del presupuesto.
5. Solo cuando se aprueban todos los niveles requeridos, la solicitud pasa a `APPROVED` y se genera la orden de compra.

### Contrato esperado

El practicante debe diseñar los endpoints REST:
- `POST /api/v1/procurement/requisitions/` (Crear solicitud)
- `POST /api/v1/procurement/requisitions/{id}/approve/` (Aprobar paso actual)
- `POST /api/v1/procurement/requisitions/{id}/reject/` (Rechazar con motivo)

### Persistencia

Tablas relacionales en PostgreSQL con integridad referencial estricta.

### Relaciones

Jerarquías de organizaciones, departamentos, usuarios y solicitudes.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Verificación estricta de que el actor pertenezca al departamento y tenga el nivel jerárquico requerido para el paso actual.

### Validaciones

Validación de no sobregiro de presupuesto antes de admitir la solicitud.

### Transacciones

Transacciones atómicas obligatorias para comprometer/liberar presupuesto y avanzar aprobaciones.

### Casos límite

El jefe de departamento intenta aprobar su propia solicitud de compra (debe requerir aprobación de un nivel superior para evitar conflicto de interés).

### Casos de error

`400 Bad Request` si la solicitud supera el presupuesto disponible del departamento; `403 Forbidden` a usuarios sin nivel de firma suficiente.

### Consideraciones de seguridad

Segregación estricta de funciones y auditoría inmutable de firmas de aprobación.

### Consideraciones de rendimiento

Índices sobre `(department_id, month, year)` en presupuestos.

### Fundamentos de Python relacionados

Modelado de máquinas de estado compuestas y motores de reglas de negocio.

### Conceptos Django relacionados

`CheckConstraint`, `select_for_update()` en presupuestos departamentales.

### Conceptos DRF relacionados

Diseño de contratos REST con `serializers.Serializer` / `ModelSerializer`, vistas delegadoras `APIView` o `GenericAPIView`, normalización de respuestas JSON y documentación declarativa con `@extend_schema`.

### PostgreSQL

`UPDATE procurement_departmentbudget SET committed_amount = committed_amount + ... WHERE id = ... AND (spent_amount + committed_amount + ...) <= budget_limit;`.

### Arquitectura

`apps/procurement` como módulo B2B autónomo dentro del monolito.

### Dependencias entre módulos

Diseñar interfaces limpias hacia catálogo y usuarios.

### Antes de programar

1. ¿Por qué es vital comprometer el presupuesto (`committed_amount`) en el momento en que se solicita la compra y no esperar hasta que se apruebe 3 semanas después?
2. ¿Cómo se estructura un motor de aprobaciones para que los umbrales de dinero sean configurables sin modificar el código fuente?

### Pruebas mínimas

1. Crear una solicitud de $5,000 para el Departamento de IT -> Verificar que requiera 2 pasos de aprobación (Team Lead y Manager) y comprometa $5,000 del presupuesto.
2. Aprobar paso 1 y luego paso 2 -> Verificar que la solicitud pase a `APPROVED`.
3. Probar el rechazo en el paso 1 y verificar que el presupuesto comprometido se libere inmediatamente.

### Pruebas negativas

1. Intentar crear una solicitud que exceda el presupuesto mensual restante del departamento -> Verificar rechazo con error de presupuesto agotado.

### Documentación

Documentar el diagrama de flujo de aprobaciones y el cálculo de presupuestos en `docs/B2B_PROCUREMENT.md`.

### Explicación posterior

Justifica el diseño del modelo de datos de aprobaciones y cómo garantizaste que ninguna combinación de peticiones concurrentes pueda sobregirar el presupuesto departamental.

### Aplicación profesional

Sistemas ERP corporativos (SAP Ariba, Coupa), plataformas de compras públicas y portales de adquisiciones B2B.

### Reto adicional

Permitir delegación temporal de firma de aprobación a un suplente si el gerente está de vacaciones.
