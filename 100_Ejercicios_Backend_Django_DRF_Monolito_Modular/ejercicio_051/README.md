# Ejercicio 051 — Módulo de Facturación (apps/billing) y Validación Estricta de Archivos

[← Ejercicio 050](../ejercicio_050/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 052 →](../ejercicio_052/README.md)

---

### Contexto de negocio

Los clientes corporativos necesitan adjuntar comprobantes de retención fiscal o comprobantes de pago bancario en formato PDF o imagen. El módulo de facturación (`apps/billing`) debe recibir estos archivos mediante `multipart/form-data`. Permitir subidas sin control expone al servidor a ejecución de código malicioso (Web Shells), agotamiento de disco (Denial of Service) y vulnerabilidades de tipo MIME spoofing.

### Estado actual del sistema

Módulos de órdenes y pagos operativos. El monolito modular se encuentra operativo y estructurado con sus aplicaciones registradas en `config/settings/base.py`.

### Nueva necesidad

Crear el módulo `apps/billing`, modelar `Invoice` y `TaxDocumentAttachment`, e implementar validación estricta de archivos comprobando tamaño máximo (5 MB), extensiones permitidas (`.pdf`, `.png`, `.jpg`) y verificación de bytes mágicos (MIME real con `python-magic` o inspección de encabezados de archivo).

### Objetivo

Dominar la carga segura de archivos en Django REST Framework, implementando validaciones a nivel de bytes para evitar ataques de manipulación de extensiones y almacenamiento seguro.

### Actor

Cliente Corporativo Autenticado autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/billing` (Módulo de Dominio encapsulado dentro del namespace `apps/`).

### Entidades involucradas

`Invoice` (`id` UUID, `order_id` UUID, `invoice_number`, `tax_amount`, `pdf_file`, `created_at`), `TaxDocumentAttachment` (`id` UUID, `file`, `file_name`, `file_size_bytes`, `mime_type`, `uploaded_at`).

### Reglas de negocio

1. El archivo no puede superar los 5 MB (5,242,880 bytes).
2. Solo se admiten tipos MIME reales: `application/pdf`, `image/jpeg`, `image/png`.
3. La validación no debe confiar únicamente en `file.name` o `file.content_type` enviado por el navegador; debe inspeccionar los primeros bytes del archivo (Magic Bytes).
4. Los archivos guardados deben renombrarse con un UUID aleatorio para evitar colisiones y sobrescritura de archivos.

### Contrato esperado

Subir Comprobante Fiscal:
- `POST /api/v1/billing/attachments/`
  Header: `Authorization: Bearer <token>`, `Content-Type: multipart/form-data`
  Form-Data: `file=@comprobante_fiscal.pdf`, `order_id=uuid-orden`
  Response: `201 Created`
  ```json
  {
    "id": "uuid-adjunto",
    "file_name": "comprobante_fiscal.pdf",
    "file_size_bytes": 245120,
    "mime_type": "application/pdf",
    "uploaded_at": "2026-09-22T17:00:00Z"
  }
  ```

### Persistencia

Tabla `billing_taxdocumentattachment` en PostgreSQL y archivo almacenado en `MEDIA_ROOT` o almacenamiento de objetos.

### Relaciones

`TaxDocumentAttachment` vinculado a `Invoice` u `Order`.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

Control de acceso granular verificando que el usuario autenticado sea el propietario del recurso (`IsOwner` o `has_object_permission`) o cuente con roles autorizados en el sistema.

### Validaciones

Validación de tamaño con `file.size` y validación de cabecera binaria con `file.read(2048)`.

### Transacciones

Transacción atómica al guardar metadatos en base de datos.

### Casos límite

Archivo malicioso renombrado como `script.php.pdf` o archivo de 0 bytes (vacío).

### Casos de error

`400 Bad Request` si el tamaño supera 5 MB o el tipo MIME no está permitido.

### Consideraciones de seguridad

Nunca ejecutar ni servir archivos subidos directamente desde directorios con permisos de ejecución de scripts.

### Consideraciones de rendimiento

Restablecer el puntero del archivo con `file.seek(0)` tras la lectura de validación binaria.

### Fundamentos de Python relacionados

Lectura de streams de bytes binarios (`rb`), punteros de archivo (`seek`, `tell`), manipulación de nombres de archivo seguros (`pathlib.Path`).

### Conceptos Django relacionados

`models.FileField`, función de ruta `upload_to=custom_file_path`, configuración de `MEDIA_ROOT` y `MEDIA_URL`.

### Conceptos DRF relacionados

`MultiPartParser`, `FormParser`, `serializers.FileField` con validadores personalizados.

### PostgreSQL

`INSERT INTO billing_taxdocumentattachment (id, file_path, file_size_bytes, mime_type, ...) ...`.

### Arquitectura

El módulo `apps/billing` encapsula el procesamiento contable y documental.

### Dependencias entre módulos

`apps/billing` referencia órdenes de `apps/orders`.

### Antes de programar

1. ¿Por qué un atacante puede engañar al servidor enviando un ejecutable `.exe` renombrado como `.jpg` si el backend solo valida la extensión de la cadena de texto?
2. ¿Por qué es obligatorio hacer `file.seek(0)` después de leer los primeros bytes para validar el tipo MIME?

### Pruebas mínimas

1. Crear un archivo PDF sintético en memoria (`SimpleUploadedFile('test.pdf', b'%PDF-1.4 ...', content_type='application/pdf')`) y enviarlo mediante el cliente de API -> Verificar `201 Created`.
2. Verificar que el archivo persista en disco y se registre su tamaño exacto en PostgreSQL.

### Pruebas negativas

1. Enviar un archivo que exceda 5 MB -> Verificar rechazo `400 Bad Request` con mensaje de límite de tamaño excedido.
2. Enviar un archivo de texto plano `.txt` o script `.py` disfrazado -> Verificar rechazo `400 Bad Request`.

### Documentación

Documentar los límites de subida de archivos y los tipos MIME permitidos en el README de `apps/billing`.

### Explicación posterior

Explica cómo funcionan los Magic Numbers en formatos binarios (ej. `%PDF` para PDF, `ÿØÿ` para JPEG, `PNG` para PNG) y por qué la inspección binaria es el único método seguro para verificar archivos.

### Aplicación profesional

Carga de documentos de identidad KYC en banca, facturas electrónicas, imágenes de perfil y comprobantes fiscales.

### Reto adicional

Generar un hash SHA-256 del archivo cargado y almacenarlo en la base de datos para verificar integridad documental y evitar duplicados.
