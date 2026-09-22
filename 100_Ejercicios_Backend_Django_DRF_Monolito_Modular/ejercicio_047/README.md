# Ejercicio 047 — Aislamiento de Pasarela Externa mediante Patrón Gateway / Adapter

[← Ejercicio 046](../ejercicio_046/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 048 →](../ejercicio_048/README.md)

---

### Contexto de negocio

El sistema no debe depender rígidamente del SDK de un único proveedor de pagos (ej. Stripe). Si el negocio decide mañana migrar a PayPal, Adyen o MercadoPago, no deberíamos tener que reescribir los modelos ni los servicios de `apps/payments`. Se requiere implementar el patrón Gateway / Adapter con una interfaz abstracta.

### Estado actual del sistema

Módulo `apps/payments` con modelo de transacciones creado.

### Nueva necesidad

Crear la interfaz abstracta `PaymentGatewayInterface` en `apps/payments/gateways/base.py` y una implementación simulada `SimulatedPaymentGateway` en `apps/payments/gateways/simulated.py` que permita emular cobros exitosos, denegaciones y timeouts.

### Objetivo

Aplicar el patrón Adapter / Gateway en Python y Django para desacoplar la lógica de negocio central de los detalles de implementación de APIs y SDKs de terceros.

### Actor

Servicio de Pagos en el contexto de las operaciones comerciales de la plataforma.

### Módulo responsable

`apps/payments` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`PaymentGatewayInterface` (Abstract Base Class), `SimulatedPaymentGateway`, `PaymentResult` (Dataclass), servicio `process_payment`.

### Reglas de negocio

1. Toda pasarela de pago debe implementar los métodos: `create_payment_intent(amount, currency, metadata) -> PaymentResult` y `refund(transaction_id, amount) -> RefundResult`.
2. El resultado debe ser un objeto estándar agnóstico (`PaymentResult` con `success: bool`, `provider_tx_id: str`, `error_message: Optional[str]`).
3. La pasarela simulada debe permitir inyectar escenarios de prueba (éxito garantizado, fallo por fondos insuficientes, error de red) mediante parámetros controlados.
4. La configuración de qué pasarela instanciar debe definirse mediante variable de entorno (`PAYMENT_GATEWAY_BACKEND`).

### Contrato esperado

Procesamiento exitoso o fallido mapeado uniformemente a `PaymentTransaction` independientemente del proveedor subyacente.

### Persistencia

Actualización de `status` (`CAPTURED` o `FAILED`) y `provider_reference` en `payments_paymenttransaction`.

### Relaciones

`PaymentTransaction`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación de divisas soportadas y montos positivos.

### Transacciones

Transacción atómica al registrar el resultado del cobro.

### Casos límite

Timeout o caída de la pasarela externa (debe capturarse con una excepción `GatewayTimeoutError` sin corromper la base de datos).

### Casos de error

`402 Payment Required` o `400 Bad Request` si la tarjeta es rechazada por fondos insuficientes.

### Consideraciones de seguridad

Aislar las claves secretas de la pasarela (`API_KEY`) en variables de entorno.

### Consideraciones de rendimiento

Establecer timeouts estrictos (ej. 5 segundos) en peticiones HTTP hacia pasarelas externas.

### Fundamentos de Python relacionados

Módulo `abc` (`ABC`, `@abstractmethod`), dataclasses (`@dataclass(frozen=True)`), inyección de dependencias.

### Conceptos Django relacionados

Instanciación dinámica de clases basada en strings de configuración (`django.utils.module_loading.import_string`).

### Conceptos DRF relacionados

Endpoint para confirmar cobro `POST /api/v1/payments/{id}/confirm/`.

### PostgreSQL

`UPDATE payments_paymenttransaction SET status = 'CAPTURED', provider_reference = 'tx_sim_999' WHERE id = ...`.

### Arquitectura

Patrón Puertos y Adaptadores (Hexagonal / Clean Architecture) dentro del módulo `apps/payments`.

### Dependencias entre módulos

Interno a `apps/payments`. La pasarela es un adaptador de infraestructura.

### Antes de programar

1. ¿Por qué llamar directamente a `stripe.Charge.create()` dentro de una vista de Django acopla peligrosamente todo el sistema a un proveedor específico?
2. ¿Cómo permite el uso de una clase abstracta intercambiar el proveedor en tests unitarios por un mock instantáneo sin costo de red?

### Pruebas mínimas

1. Invocar `process_payment` con la pasarela simulada en modo éxito -> Verificar que la transacción quede en `CAPTURED` y retorne `provider_reference`.
2. Invocar en modo rechazo -> Verificar que quede en `FAILED` y que se registre el motivo.

### Pruebas negativas

1. Simular un timeout de pasarela y verificar que la transacción pase a `FAILED` con mensaje de error de conectividad sin lanzar error 500.

### Documentación

Documentar la interfaz del Gateway y las instrucciones para implementar nuevos adaptadores en `apps/payments/gateways/README.md`.

### Explicación posterior

Explica el Principio de Inversión de Dependencias (DIP) de SOLID: los módulos de alto nivel (servicios de pago) no deben depender de módulos de bajo nivel (SDK de Stripe); ambos deben depender de abstracciones.

### Aplicación profesional

Arquitectura de pagos multi-proveedor, enrutamiento inteligente de pagos y resiliencia ante caídas de proveedores de pago.

### Reto adicional

Implementar una factoría `get_payment_gateway()` que retorne la instancia adecuada según `settings.PAYMENT_GATEWAY_BACKEND`.
