# Ejercicio 052 — Generación de Reportes PDF y CSV sin Bloquear el Servidor

[← Ejercicio 051](../ejercicio_051/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 053 →](../ejercicio_053/README.md)

---

### Contexto de negocio

Los gerentes y administradores necesitan exportar reportes periódicos de ventas en formato CSV y generar facturas electrónicas en formato PDF descargable para los clientes. La generación de un reporte con miles de registros en CSV o la renderización de un PDF con gráficos debe optimizarse para consumir la mínima memoria posible mediante Streaming de respuestas HTTP.

### Estado actual del sistema

Módulo de facturación y órdenes operativos. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Implementar dos endpoints de exportación: `GET /api/v1/billing/reports/sales-csv/` usando `StreamingHttpResponse` con generadores en Python para exportar CSV en tiempo real, y `GET /api/v1/billing/invoices/{id}/pdf/` para renderizar el PDF de la factura.

### Objetivo

Dominar la generación y transmisión de archivos dinámicos (CSV/PDF) en Django/DRF, utilizando `StreamingHttpResponse` y generadores iteradores para manejar grandes volúmenes de datos con consumo de memoria O(1).

### Actor

Administrador (CSV de ventas) / Cliente (PDF de su factura)

### Módulo responsable

`apps/billing` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`SalesCsvExportView`, `InvoicePdfView`, `StreamingHttpResponse`, `csv.writer`.

### Reglas de negocio

1. El reporte CSV debe incluir columnas: `order_number`, `customer_email`, `total_amount`, `status`, `created_at`.
2. El archivo CSV debe transmitirse en chunks mediante streaming sin cargar todos los registros en una lista en memoria RAM.
3. La cabecera HTTP `Content-Disposition` debe configurar `attachment; filename="reporte_ventas_YYYYMMDD.csv"`.
4. El PDF de factura solo puede ser descargado por el propietario de la orden o un Administrador.

### Contrato esperado

Descargar CSV de Ventas:
- `GET /api/v1/billing/reports/sales-csv/?from=2026-01-01&to=2026-09-22`
  Header: `Authorization: Bearer <token_admin>`
  Response: `200 OK`
  Headers: `Content-Type: text/csv; charset=utf-8`, `Content-Disposition: attachment; filename="sales_report.csv"`
  Body: Stream de datos CSV en texto plano.

### Persistencia

Consultas al ORM con `.iterator()` para procesar en lotes.

### Relaciones

`Order`, `Invoice`, `CustomerProfile`. Relaciones foráneas protegidas mediante `on_delete=models.PROTECT` y restricciones relacionales en el motor PostgreSQL.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Solo rol `ADMIN` para el CSV global; propietario para el PDF individual.

### Validaciones

Validar formato de fechas en parámetros query.

### Transacciones

No requerida para exportación de solo lectura.

### Casos límite

Exportación de 100,000 registros (debe procesarse fluidamente sin provocar errores Out-Of-Memory (OOM)).

### Casos de error

`403 Forbidden` si un cliente no autorizado intenta descargar el reporte global.

### Consideraciones de seguridad

Prevenir inyecciones de fórmulas CSV (CSV Injection / Formula Injection) si los nombres de productos contienen caracteres `=`, `+`, `-`, `@`.

### Consideraciones de rendimiento

Uso de `QuerySet.iterator(chunk_size=2000)` combinado con generadores `yield` de Python.

### Fundamentos de Python relacionados

Generadores (`yield`), módulo `csv`, manipulación de buffers en memoria (`io.StringIO`).

### Conceptos Django relacionados

`django.http.StreamingHttpResponse`, `QuerySet.iterator()`, configuración de headers HTTP.

### Conceptos DRF relacionados

Integración de vistas de streaming con permisos de DRF.

### PostgreSQL

PostgreSQL ejecuta un cursor del lado del servidor para transmitir las filas por lotes.

### Arquitectura

Los servicios de generación de reportes residen en `apps/billing/reports.py`.

### Dependencias entre módulos

`apps/billing` consulta órdenes de `apps/orders`.

### Antes de programar

1. ¿Por qué hacer `list(Order.objects.all())` y luego escribir todo en un string antes de responder provoca caídas por memoria RAM en servidores con bases de datos grandes?
2. ¿Cómo funciona un generador con `yield` para producir datos fila por fila a medida que el cliente los descarga?

### Pruebas mínimas

1. Crear 10 órdenes, solicitar el endpoint de CSV como Admin -> Verificar status `200`, cabecera `Content-Type: text/csv` y contenido de filas.
2. Solicitar el PDF de una factura como cliente propietario -> Verificar status `200` y cabecera de archivo adjunto.

### Pruebas negativas

1. Solicitar el CSV de ventas como cliente estándar sin rol admin -> Verificar `403 Forbidden`.

### Documentación

Documentar los parámetros de exportación y el formato de los reportes en la documentación interna.

### Explicación posterior

Explica la diferencia entre `HttpResponse` (bufferiza toda la respuesta en memoria antes de enviar el primer byte) y `StreamingHttpResponse` (transmite chunks en tiempo real manteniendo la memoria constante).

### Aplicación profesional

Generación de extractos bancarios, reportes contables masivos, facturas electrónicas y exportación de Big Data.

### Reto adicional

Sanitizar las celdas del CSV anteponiendo un apóstrofe si comienzan con `=`, `+`, `-` o `@` para neutralizar ataques de CSV Injection en Microsoft Excel.
