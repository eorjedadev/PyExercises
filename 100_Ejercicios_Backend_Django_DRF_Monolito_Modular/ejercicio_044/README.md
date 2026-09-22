# Ejercicio 044 — Comando Personalizado de Gestión para Cancelar Pedidos Expirados

[← Ejercicio 043](../ejercicio_043/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 045 →](../ejercicio_045/README.md)

---

### Contexto de negocio

Muchos clientes inician un pedido (estado `PENDING`), reservan stock en el almacén, pero nunca completan el pago. Dejar ese stock reservado indefinidamente perjudica las ventas. Se requiere un comando de mantenimiento automatizable (`python manage.py cancel_expired_pending_orders --hours=24`) que identifique órdenes pendientes con más de X horas de antigüedad, las cancele y libere el stock automáticamente.

### Estado actual del sistema

Lógica de pedidos, inventario y cancelación operativa.

### Nueva necesidad

Crear el comando personalizado de Django en `apps/orders/management/commands/cancel_expired_orders.py`, aceptando argumentos de línea de comandos, ejecutando en lotes e imprimiendo un resumen en consola.

### Objetivo

Aprender a construir Custom Management Commands en Django para tareas de mantenimiento y automatización backend, procesando datos en lotes y reutilizando los servicios existentes del dominio.

### Actor

Sistema Automatizado (Cron / Scheduled Task) / Operador Backend

### Módulo responsable

`apps/orders` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`cancel_expired_orders` (Management Command), selector `get_expired_pending_orders`, servicio `cancel_order`.

### Reglas de negocio

1. El comando debe aceptar el argumento opcional `--hours=N` (por defecto 24 horas).
2. Debe buscar todas las órdenes en estado `PENDING` creadas hace más de N horas (`created_at <= now - N hours`).
3. Cada orden expirada debe cancelarse invocando el servicio oficial `orders.services.cancel_order` con motivo `'Expiración por tiempo límite de pago'` para asegurar la liberación del stock.
4. Debe soportar el flag `--dry-run` para simular y reportar cuántas órdenes se cancelarían sin aplicar cambios en base de datos.

### Contrato esperado

Ejecución en consola (PowerShell):
```powershell
python manage.py cancel_expired_orders --hours=12 --dry-run
[SIMULACION] Se encontraron 3 pedidos pendientes expirados para cancelar.
- ORD-2026-00010 (Creado: 2026-09-21 10:00 UTC)
- ORD-2026-00014 (Creado: 2026-09-21 11:30 UTC)

python manage.py cancel_expired_orders --hours=12
[PROCESADO] 2 pedidos cancelados exitosamente. Stock liberado en inventario.
```

### Persistencia

Actualización de estado en `orders_order` y liberación de stock en `inventory_stockitem`.

### Relaciones

`Order`, `StockItem`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validar que el argumento `--hours` sea un entero positivo mayor a cero.

### Transacciones

Cada cancelación de orden se ejecuta dentro de su propia transacción atómica.

### Casos límite

0 pedidos expirados encontrados (el comando debe finalizar limpiamente indicando 'No hay pedidos pendientes expirados').

### Casos de error

Manejo de errores por cada orden individual para que el fallo en una orden no aborte el procesamiento de las restantes.

### Consideraciones de seguridad

Los comandos de gestión tienen acceso irrestricto a la base de datos; proteger su ejecución en servidores de producción.

### Consideraciones de rendimiento

Usar `.iterator(chunk_size=100)` para iterar sobre miles de registros sin agotar la memoria RAM del servidor.

### Fundamentos de Python relacionados

Módulo `argparse`, cálculo de deltas de tiempo (`datetime.timedelta`).

### Conceptos Django relacionados

`core.management.base.BaseCommand`, `CommandError`, estructura de carpetas `management/commands/`.

### Conceptos DRF relacionados

Diseño de contratos REST con `serializers.Serializer` / `ModelSerializer`, vistas delegadoras `APIView` o `GenericAPIView`, normalización de respuestas JSON y documentación declarativa con `@extend_schema`.

### PostgreSQL

`SELECT ... FROM orders_order WHERE status = 'PENDING' AND created_at <= ...`.

### Arquitectura

El comando solo actúa como punto de entrada CLI, delegando la lógica de negocio a los servicios de `apps/orders` e `apps/inventory`.

### Dependencias entre módulos

`cancel_expired_orders` importa servicios de `apps.orders`.

### Antes de programar

1. ¿Por qué un Management Command debe reutilizar `services.cancel_order` en lugar de hacer un `Order.objects.filter(...).update(status='CANCELLED')` directo?
2. ¿Por qué el flag `--dry-run` es una práctica recomendada en herramientas de automatización backend?

### Pruebas mínimas

1. Crear 2 órdenes pendientes (una creada hace 2 días y otra hace 1 hora), ejecutar `call_command('cancel_expired_orders', hours=24)` -> Verificar que solo la orden antigua quede en estado `CANCELLED` y que su stock se libere.
2. Probar con `--dry-run` y comprobar que ninguna orden cambie de estado.

### Pruebas negativas

1. Ejecutar el comando pasando `--hours=-5` y verificar que lance `CommandError` con mensaje explicativo.

### Documentación

Documentar los argumentos del comando y su configuración sugerida en cron/task scheduler en el README del módulo.

### Explicación posterior

Explica cómo los Management Commands conectan las capacidades de un backend Django con la infraestructura de automatización de servidores (Linux Cron, Windows Task Scheduler, Kubernetes CronJobs).

### Aplicación profesional

Automatización de tareas de mantenimiento, facturación recurrente, purga de logs antiguos y conciliación bancaria.

### Reto adicional

Agregar una barra de progreso en consola mediante `tqdm` o salida estándar formateada si se procesan más de 50 órdenes.
