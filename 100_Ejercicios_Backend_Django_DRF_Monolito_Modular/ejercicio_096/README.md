# Ejercicio 096 — Desafío de Dominio: Billetera Digital (Wallets) con Contabilidad de Doble Entrada

[← Ejercicio 095](../ejercicio_095/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 097 →](../ejercicio_097/README.md)

---

### Contexto de negocio

Una aplicación FinTech permite a los usuarios tener una Billetera Digital (Digital Wallet) en USD. Los usuarios pueden recargar saldo, transferir dinero a otros usuarios en tiempo real y pagar servicios. En sistemas bancarios y financieros, almacenar el saldo simplemente como un campo `balance = Decimal(...)` que se suma y resta con `update` es inaceptable por falta de auditoría y riesgo de corrupción. Se requiere implementar Contabilidad de Doble Entrada (Double-Entry Ledger): cada transacción se compone de un Débito (DEBIT) y un Crédito (CREDIT) cuya suma total debe ser exactamente cero, con garantía absoluta de CERO saldos negativos.

### Estado actual del sistema

Monolito modular con usuarios y seguridad. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Diseñar de forma autónoma el módulo financiero de billeteras (`apps/wallets`), modelando cuentas (`WalletAccount`), transacciones de libro mayor (`LedgerTransaction`) y asientos contables (`LedgerEntry`), implementando transferencias atómicas P2P.

### Objetivo

Diseñar un sistema financiero de misión crítica aplicando el principio contable de Doble Entrada (Double-Entry Bookkeeping) en Django y PostgreSQL, garantizando consistencia matemática y prevención de saldos negativos.

### Actor

Usuario Titular de Billetera / Sistema Financiero

### Módulo responsable

Determinación autónoma por el practicante (`apps/wallets`)

### Entidades involucradas

El practicante debe modelar las entidades necesarias (`Wallet`, `LedgerTransaction`, `LedgerEntry`, `WalletHold`).

### Reglas de negocio

1. Toda transferencia entre dos usuarios crea 1 `LedgerTransaction` y exactamente 2 `LedgerEntry`: un DEBIT (-$Monto) en la cuenta origen y un CREDIT (+$Monto) en la cuenta destino.
2. Regla de Balance Cero: `SUM(amount)` de todos los asientos de una `LedgerTransaction` DEBE ser estrictamente 0.00.
3. Restricción física en PostgreSQL: El saldo de una billetera nunca puede ser menor a 0.00 (`CheckConstraint(balance >= 0)`).
4. Las transferencias P2P deben usar bloqueo pesimista `select_for_update()` ordenando las cuentas por ID para evitar interbloqueos (Deadlocks).
5. Los asientos contables son estrictamente inmutables (Append-Only); los errores se corrigen con una nueva transacción de reversión contable.

### Contrato esperado

El practicante debe diseñar los endpoints REST:
- `POST /api/v1/wallets/transfer/` (Transferencia P2P entre usuarios)
- `GET /api/v1/wallets/balance/` (Consultar saldo actual)
- `GET /api/v1/wallets/statement/` (Extracto de movimientos contables)

### Persistencia

Tablas `wallets_wallet`, `wallets_ledgertransaction`, `wallets_ledgerentry` en PostgreSQL con restricciones CHECK.

### Relaciones

Billeteras vinculadas a usuarios; Asientos vinculados a Billeteras y Transacciones.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Solo el titular de la billetera puede transferir sus fondos.

### Validaciones

Validar que el emisor tenga saldo disponible suficiente y que el receptor sea una cuenta válida activa.

### Transacciones

Transacción atómica obligatoria con `select_for_update()` sobre ambas cuentas.

### Casos límite

Usuario intentando transferirse dinero a sí mismo (debe ser bloqueado por regla de negocio).

### Casos de error

`400 Bad Request` si los fondos son insuficientes; `404 Not Found` si la cuenta destino no existe.

### Consideraciones de seguridad

Protección de máxima seguridad bancaria: no admitir saldos negativos bajo ninguna condición de carrera.

### Consideraciones de rendimiento

Bloqueos pesimistas ordenados alfabéticamente por UUID de cuenta (`min_id, max_id`) para prevenir Deadlocks en transferencias cruzadas simultáneas (A -> B y B -> A).

### Fundamentos de Python relacionados

Matemáticas financieras con `Decimal`, algoritmos de prevención de deadlocks.

### Conceptos Django relacionados

`CheckConstraint(check=Q(balance__gte=0))`, `transaction.atomic()`, `select_for_update()`.

### Conceptos DRF relacionados

Diseño de endpoints de transferencias financieras con soporte para `Idempotency-Key`.

### PostgreSQL

`ALTER TABLE wallets_wallet ADD CONSTRAINT check_non_negative_balance CHECK (balance >= 0);`.

### Arquitectura

`apps/wallets` como módulo FinTech de alta seguridad en el monolito.

### Dependencias entre módulos

`apps/wallets` interactúa con `apps/users` y `apps/audit`.

### Antes de programar

1. ¿Por qué la Contabilidad de Doble Entrada (Double-Entry) es el estándar universal de la banca mundial desde hace más de 500 años?
2. ¿Cómo se produce un Deadlock cuando el Usuario A le transfiere al Usuario B al mismo tiempo que B le transfiere a A, y cómo lo soluciona bloquear las cuentas siempre en orden de ID (`sorted([acc_a.id, acc_b.id])`)?

### Pruebas mínimas

1. Billetera A tiene $100.00, Billetera B tiene $0.00. Transferir $40.00 de A a B -> Verificar que A quede en $60.00, B en $40.00, y que existan exactamente 2 asientos contables cuya suma sea 0.00.
2. Ejecutar transferencias concurrentes simultáneas y comprobar que ningún saldo quede inconsistente.

### Pruebas negativas

1. Intentar transferir $150.00 desde una cuenta con $100.00 -> Verificar que lance `InsufficientFundsError` y que PostgreSQL impida cualquier saldo negativo.

### Documentación

Documentar la arquitectura contable del Ledger y la prevención de deadlocks en `docs/FINTECH_LEDGER.md`.

### Explicación posterior

Explica cómo los sistemas bancarios modernos (Revolut, Nubank, Stripe) implementan Ledgers inmutables y por qué la integridad contable nunca se delega a simples operaciones de suma/resta sin partida doble.

### Aplicación profesional

Bancos digitales, billeteras cripto/fiat, pasarelas de pago, procesamiento de nóminas y microcréditos.

### Reto adicional

Implementar un comando de auditoría `python manage.py verify_ledger_integrity` que compruebe que para el 100% de las transacciones históricas, la suma de débitos sea idéntica a la suma de créditos.
