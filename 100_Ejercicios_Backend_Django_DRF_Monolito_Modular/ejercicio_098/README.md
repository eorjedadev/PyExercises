# Ejercicio 098 — Desafío de Dominio: Comisiones de Afiliados Multinivel y Liquidación Fiscal Mensual

[← Ejercicio 097](../ejercicio_097/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 099 →](../ejercicio_099/README.md)

---

### Contexto de negocio

Para impulsar el crecimiento, la empresa lanza un Programa de Afiliados Multinivel (Referral & Affiliate Network). Cuando un cliente compra mediante un enlace de afiliado: - El Afiliado Nivel 1 (referidor directo) recibe el 10% de la venta. - El Afiliado Nivel 2 (quien invitó al referidor directo) recibe el 3% de la venta. Las comisiones permanecen en estado `PENDING` durante el periodo de garantía de devolución (30 días). Al final de cada mes, un motor de liquidación consolida las comisiones confirmadas de cada afiliado, aplica retenciones de impuestos según el país fiscal del afiliado y genera la orden de liquidación de pago (`PayoutStatement`).

### Estado actual del sistema

Monolito modular con órdenes, pagos y facturación.

### Nueva necesidad

Diseñar de forma autónoma el módulo de afiliados (`apps/affiliates`), modelando la red de referidos (árbol genealógico), comisiones por venta (`CommissionEntry`), retenciones fiscales y el motor de liquidación mensual (`PayoutSettlementEngine`).

### Objetivo

Diseñar un sistema de comisiones multinivel y liquidación contable/fiscal en Django/DRF, modelando árboles jerárquicos de referidos, cálculos porcentuales escalonados y cierres mensuales.

### Actor

Afiliado / Motor de Liquidación Mensual / Administrador Financiero

### Módulo responsable

Determinación autónoma por el practicante (`apps/affiliates`)

### Entidades involucradas

El practicante debe modelar las entidades necesarias (`AffiliateProfile`, `ReferralRelationship`, `CommissionEntry`, `PayoutStatement`, `TaxWithholdingRule`).

### Reglas de negocio

1. Cada afiliado tiene un código de referencia único (`referral_code`).
2. Un afiliado puede haber sido referido por otro afiliado (árbol de referidos de máximo 2 niveles de profundidad).
3. Al crearse una orden pagada con código de afiliado, se generan automáticamente las comisiones correspondientes en estado `PENDING_MATURATION`.
4. Si la orden es devuelta o cancelada dentro de los 30 días, las comisiones pendientes asociadas se cancelan (`CANCELLED`).
5. El motor de liquidación mensual busca comisiones con más de 30 días (`MATURED`), calcula retenciones fiscales (ej. 10% de retención de impuestos) y genera el `PayoutStatement`.

### Contrato esperado

El practicante debe diseñar los endpoints REST:
- `GET /api/v1/affiliates/dashboard/` (Métricas de clics, ventas referidas y comisiones acumuladas)
- `POST /api/v1/affiliates/settlements/generate/` (Generar liquidación mensual)
- `GET /api/v1/affiliates/payouts/{id}/` (Detalle de liquidación con desglose fiscal)

### Persistencia

Tablas relacionales en PostgreSQL con precisión decimal para cálculos de porcentajes.

### Relaciones

Afiliados vinculados a Usuarios; Comisiones vinculadas a Órdenes y Afiliados.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Afiliado consulta sus propias comisiones; Dirección Financiera ejecuta liquidaciones.

### Validaciones

Validar que un usuario no pueda ser su propio referidor ni crear ciclos en la red.

### Transacciones

Transacciones atómicas en la generación de comisiones y en la liquidación mensual.

### Casos límite

El cliente compra usando un código de afiliado pero la orden se cancela antes de madurar (la comisión debe anularse automáticamente).

### Casos de error

`400 Bad Request` ante códigos de referido inválidos.

### Consideraciones de seguridad

Prevención de auto-referidos fraudulentos y lavado de comisiones.

### Consideraciones de rendimiento

Índices sobre `(affiliate_id, status, created_at)` para cálculo rápido de comisiones pendientes.

### Fundamentos de Python relacionados

Cálculos matemáticos de precisión fija con `Decimal`, árboles jerárquicos.

### Conceptos Django relacionados

`models.ForeignKey('self')`, agregaciones con `Sum()`, comandos de gestión.

### Conceptos DRF relacionados

Endpoints de analítica y comisiones para el panel de afiliados.

### PostgreSQL

`CREATE TABLE affiliates_commissionentry (id UUID PRIMARY KEY, affiliate_id UUID NOT NULL, order_id UUID NOT NULL, commission_level INT NOT NULL, amount NUMERIC(12,2) NOT NULL, ...);`.

### Arquitectura

`apps/affiliates` como módulo de monetización y marketing en el monolito.

### Dependencias entre módulos

`apps/affiliates` escucha eventos de `apps/orders` y genera facturación en `apps/billing`.

### Antes de programar

1. ¿Por qué las comisiones de afiliados deben tener un período de maduración de 30 días antes de ser liquidables?
2. ¿Cómo se calculan retenciones de impuestos y se redondean decimales para que la suma de comisiones brutas menos retenciones coincida al céntimo con el pago neto?

### Pruebas mínimas

1. Orden de $100 con afiliado N1 y N2 -> Verificar que se cree una comisión de $10.00 para N1 y $3.00 para N2 en estado `PENDING_MATURATION`.
2. Ejecutar el motor de liquidación sobre comisiones maduras con 10% de retención fiscal -> Verificar que la liquidación neta sea $9.00 y la retención $1.00.

### Pruebas negativas

1. Cancelar la orden antes de los 30 días y verificar que ambas comisiones pasen a estado `CANCELLED` y no se incluyan en la liquidación.

### Documentación

Documentar la estructura de la red de afiliados y las reglas fiscales en `docs/AFFILIATES_COMMISSIONS.md`.

### Explicación posterior

Explica cómo se estructuran los motores de compensación y comisiones en marketing de afiliados (Amazon Associates, Hotmart) y la gestión contable de pasivos acumulados.

### Aplicación profesional

Programas de referidos, comisiones de fuerza de ventas corporativa, redes de afiliados y liquidaciones a creadores de contenido.

### Reto adicional

Implementar un enlace de seguimiento de clics que registre la IP y User-Agent y asigne una cookie de referido con validez de 30 días.
