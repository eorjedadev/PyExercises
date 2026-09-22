# Ejercicio 053 — Descarga Segura de Archivos Privados mediante URLs Firmadas / Endpoints Autorizados

[← Ejercicio 052](../ejercicio_052/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 054 →](../ejercicio_054/README.md)

---

### Contexto de negocio

Las facturas, contratos y comprobantes fiscales contienen datos privados y financieros sensibles. Servir estos archivos directamente mediante URLs estáticas públicas (ej. `http://servidor/media/invoices/factura_123.pdf`) permitiría que cualquier persona que adivine o capture el enlace descargue documentos confidenciales. Los archivos deben ser estrictamente privados y accesibles solo mediante autorización o URLs temporales firmadas.

### Estado actual del sistema

Módulo de facturación con archivos adjuntos operativos.

### Nueva necesidad

Implementar un endpoint seguro de descarga `GET /api/v1/billing/invoices/{id}/download/` que verifique la propiedad del recurso y sirva el archivo mediante `FileResponse` de Django o redirija a una URL temporal con firma criptográfica y expiración corta (Signed URL).

### Objetivo

Proteger el acceso a archivos privados en aplicaciones backend, implementando control de acceso granular antes de servir archivos y evitando la exposición accidental de directorios de almacenamiento.

### Actor

Cliente Propietario / Auditor Fiscal autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/billing` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`InvoiceDownloadAPIView`, `django.core.signing.TimestampSigner`, `FileResponse`.

### Reglas de negocio

1. Ningún archivo del módulo de facturación puede ser accesible públicamente sin autenticación.
2. El endpoint de descarga debe verificar que el usuario autenticado sea el dueño de la factura o tenga rol `ADMIN`.
3. Opcionalmente, se puede generar un enlace de un solo uso con firma criptográfica (`TimestampSigner`) que expire en 60 segundos.
4. La descarga debe incluir cabeceras de seguridad `X-Content-Type-Options: nosniff`.

### Contrato esperado

Descarga de Factura Autorizada:
- `GET /api/v1/billing/invoices/{id}/download/`
  Header: `Authorization: Bearer <token_propietario>`
  Response: `200 OK`
  Headers: `Content-Type: application/pdf`, `Content-Disposition: inline; filename="invoice_ORD-2026-00001.pdf"`
  Body: Stream binario del archivo PDF.

### Persistencia

No aplica cambios de esquema; lectura de archivo desde almacenamiento seguro.

### Relaciones

`Invoice` vinculado a `Order` y `CustomerProfile`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Verificación de ownership mediante `has_object_permission`.

### Validaciones

Validar que el archivo físico exista en el sistema de almacenamiento antes de intentar servirlo.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

El registro de factura existe en base de datos pero el archivo físico fue borrado del disco (responder `404 Not Found` con mensaje amigable en lugar de error 500 crudo).

### Casos de error

`403 Forbidden` si un usuario intenta descargar la factura de otro cliente; `404 Not Found` si el archivo no existe.

### Consideraciones de seguridad

Prevenir Path Traversal (evitar que un atacante use `../../etc/passwd` como nombre de archivo).

### Consideraciones de rendimiento

Uso de `FileResponse` que delega la transmisión eficiente de bloques binarios.

### Fundamentos de Python relacionados

Firmas con timestamp (`signing.TimestampSigner`), validación de firmas temporales.

### Conceptos Django relacionados

`django.http.FileResponse`, `django.core.signing`, configuración de almacenamiento privado fuera de `STATIC_ROOT`.

### Conceptos DRF relacionados

Vistas de DRF que retornan `FileResponse` manteniendo la pila de autenticación y permisos.

### PostgreSQL

Consulta ORM para validar la propiedad de la factura.

### Arquitectura

El control de acceso a archivos privados se gestiona en la capa de vistas de `apps/billing`.

### Dependencias entre módulos

`apps/billing` consulta la relación de usuario con `apps.customers`.

### Antes de programar

1. ¿Por qué configurar `MEDIA_URL` con Nginx o Apache para servir todos los archivos directamente sin pasar por Django es un agujero de seguridad crítico para documentos privados?
2. ¿Cómo funciona una Signed URL temporal para permitir que un cliente descargue un archivo pesado directamente sin sobrecargar el proceso de Django?

### Pruebas mínimas

1. Crear una factura con archivo para el Usuario 1, autenticarse como Usuario 1 y solicitar la descarga -> Verificar status `200` y recepción del stream binario.
2. Autenticarse como Admin y solicitar la misma descarga -> Verificar status `200`.

### Pruebas negativas

1. Autenticarse como Usuario 2 e intentar descargar la factura del Usuario 1 -> Verificar `403 Forbidden` / `404 Not Found`.
2. Intentar descargar sin token de autenticación -> Verificar `401 Unauthorized`.

### Documentación

Documentar la política de protección de archivos privados en la guía de seguridad del proyecto.

### Explicación posterior

Explica cómo arquitecturas de almacenamiento en la nube (AWS S3, Google Cloud Storage) implementan Presigned URLs con expiración y cómo Django interactúa con ellas de manera segura.

### Aplicación profesional

Descarga de nóminas de sueldos, historiales clínicos médicos, contratos legales y diplomas certificados.

### Reto adicional

Implementar la generación de una URL firmada de descarga temporal `GET /api/v1/billing/invoices/{id}/signed-url/` que retorne un enlace con token válido por 10 minutos.
