# Ejercicio 026 — Throttling y Rate Limiting para Protección contra Abusos

[← Ejercicio 025](../ejercicio_025/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 027 →](../ejercicio_027/README.md)

---

### Contexto de negocio

Los endpoints de autenticación (`/users/token/`) y registro son blancos frecuentes de ataques de fuerza bruta y enumeración. Asimismo, usuarios anónimos podrían realizar scraping masivo del catálogo. Se requiere implementar limitación de tasa de peticiones (Rate Limiting / Throttling) diferenciado por tipo de usuario y endpoint.

### Estado actual del sistema

Endpoints de autenticación y catálogo operativos.

### Nueva necesidad

Configurar clases de Throttling en DRF (`AnonRateThrottle`, `UserRateThrottle`) y crear un throttle personalizado `AuthEndpointThrottle` para restringir intentos de login a 5 peticiones por minuto por IP.

### Objetivo

Proteger la API contra abusos, scraping y ataques de fuerza bruta mediante Throttling en DRF, comprendiendo el status code `429 Too Many Requests` y cabeceras `Retry-After`.

### Actor

Cliente de API / Potencial Atacante autenticado mediante credenciales válidas o consumidor de API REST.

### Módulo responsable

`apps/core` y aplicado en `apps/users` y `apps/catalog`

### Entidades involucradas

`AuthEndpointThrottle` (`SimpleRateThrottle`), configuración de `REST_FRAMEWORK['DEFAULT_THROTTLE_RATES']`.

### Reglas de negocio

1. Endpoints de autenticación (`/users/token/`, `/users/register/`): Máximo 5 peticiones por minuto por dirección IP (`5/minute`).
2. Usuarios anónimos en catálogo: Máximo 60 peticiones por minuto (`60/minute`).
3. Usuarios autenticados: Máximo 300 peticiones por minuto (`300/minute`).
4. Al exceder el límite, responder `429 Too Many Requests` con el tiempo de espera restante.

### Contrato esperado

Respuesta al Exceder Límite:
- Petición número 6 en menos de 1 minuto a `/users/token/`
  Response: `429 Too Many Requests`
  Header: `Retry-After: 48`
  ```json
  {
    "error": {
      "code": "THROTTLED",
      "message": "Se ha superado el límite de peticiones. Intente nuevamente en 48 segundos."
    }
  }
  ```

### Persistencia

DRF almacena las marcas de tiempo de las peticiones en la caché configurada de Django (LocMemCache o Redis).

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

Autenticación stateless obligatoria mediante tokens JWT (`rest_framework_simplejwt`). El cliente debe enviar la cabecera `Authorization: Bearer <access_token>` en cada petición HTTP.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Validación de IP de origen o identificador de usuario.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Usuarios detrás de un proxy inverso o balanceador de carga (debe leerse la IP real desde `X-Forwarded-For` o `REMOTE_ADDR` según la configuración de proxies seguros).

### Casos de error

- `400 Bad Request`: Payload JSON malformado o campos requeridos ausentes.
- `401 Unauthorized`: Token JWT expirado, revocado o ausente.
- `403 Forbidden`: Usuario sin permisos suficientes para la acción.
- `404 Not Found`: Identificador de recurso inexistente.
- `409 Conflict` / `422 Unprocessable`: Violación de invariantes de negocio o concurrencia.
- `500 Internal Server Error`: Errores no controlados capturados por el exception handler global.

### Consideraciones de seguridad

Protección fundamental contra ataques de diccionario y denegación de servicio a nivel de aplicación.

### Consideraciones de rendimiento

El backend de caché para throttling debe ser en memoria para no penalizar la latencia.

### Fundamentos de Python relacionados

Cálculo de ventanas de tiempo deslizantes. Tipado estricto con `typing` (`Optional`, `Dict`, `List`), decoradores, dataclasses, manejo estructurado de excepciones y programación modular.

### Conceptos Django relacionados

`CACHES` en settings, lectura de cabeceras HTTP de red.

### Conceptos DRF relacionados

`throttling.AnonRateThrottle`, `throttling.UserRateThrottle`, `throttling.SimpleRateThrottle`, `throttle_classes`, `DEFAULT_THROTTLE_RATES`.

### PostgreSQL

No requiere queries a PostgreSQL para evaluar el rate limit.

### Arquitectura

`apps/core/throttling.py` define los limitadores reutilizables.

### Dependencias entre módulos

`apps/users` y `apps/catalog` aplican las clases de throttling de `apps/core`.

### Antes de programar

1. ¿Por qué el throttling no reemplaza una contraseña segura ni el bloqueo de cuentas, pero es una capa indispensable de defensa?
2. ¿Cómo calcula DRF si una petición debe ser bloqueada usando la clave de caché y la tasa declarada?

### Pruebas mínimas

1. Enviar 5 peticiones consecutivas al endpoint de login y verificar que las 5 respondan con el status esperado.
2. Enviar la 6ta petición inmediata y verificar que responda `429 Too Many Requests` con cabecera `Retry-After`.

### Pruebas negativas

1. Comprobar que tras esperar el tiempo indicado en `Retry-After`, el acceso se restablezca normalmente.

### Documentación

Documentar los límites de tasa aplicados por endpoint en la documentación de la API.

### Explicación posterior

Explica cómo configurar `NUM_PROXIES` en `SECURE_PROXY_SSL_HEADER` o usar un middleware para obtener la IP real del cliente detrás de Nginx/Cloudflare.

### Aplicación profesional

Mitigación de ataques de fuerza bruta, protección de costos de infraestructura y cumplimiento de SLAs.

### Reto adicional

Implementar un `ScopedRateThrottle` en endpoints de descarga de reportes pesados para limitar a 3 descargas por hora por usuario.
