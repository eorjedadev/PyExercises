# Ejercicio 087 — Dockerización Profesional del Monolito Modular con PostgreSQL y Windows

[← Ejercicio 086](../ejercicio_086/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 088 →](../ejercicio_088/README.md)

---

### Contexto de negocio

Para garantizar que la aplicación se ejecute de manera 100% idéntica en el entorno de desarrollo en Windows de cualquier programador, en los servidores de staging y en producción, se requiere dockerizar profesionalmente el monolito modular. Se debe construir un `Dockerfile` multi-stage optimizado y un `docker-compose.yml` que orqueste el servicio backend Django y el contenedor de base de datos PostgreSQL con volúmenes persistentes.

### Estado actual del sistema

Monolito modular completo con múltiples aplicaciones operativas.

### Nueva necesidad

Crear el `Dockerfile`, `.dockerignore`, `docker-compose.yml` y script de entrada `entrypoint.sh` (compatible con Windows y Linux) para levantar todo el entorno con un solo comando: `docker compose up --build`.

### Objetivo

Dominar la contenerización profesional de aplicaciones Django + PostgreSQL con Docker y Docker Compose, aplicando compilación multi-etapa (Multi-Stage Build), usuarios no root por seguridad, persistencia de volúmenes y variables de entorno.

### Actor

Ingeniero de DevOps / Desarrollador Backend

### Módulo responsable

Raíz del proyecto (`Dockerfile`, `docker-compose.yml`)

### Entidades involucradas

`Dockerfile`, `docker-compose.yml`, `.dockerignore`, `entrypoint.sh`.

### Reglas de negocio

1. El `Dockerfile` debe usar una imagen base ligera oficial (`python:3.12-slim` o similar).
2. Debe utilizar un usuario de sistema sin privilegios (`appuser` no root) para ejecutar el proceso Django en el contenedor.
3. `docker-compose.yml` debe definir el servicio `db` (PostgreSQL 16) con volumen persistente (`postgres_data`) y healthcheck de base de datos (`pg_isready`).
4. El servicio `web` debe esperar a que la base de datos esté saludable (`depends_on` con `condition: service_healthy`) antes de aplicar migraciones e iniciar el servidor.
5. El script de entrada debe ser compatible con saltos de línea LF para evitar errores al construirse desde Windows (CRLF).

### Contrato esperado

Comandos de Ejecución en PowerShell / Terminal:
```powershell
docker compose up -d --build
docker compose logs -f web
docker compose exec web python manage.py check
```
Servidor disponible en `http://localhost:8000/api/v1/health/` respondiendo `200 OK`.

### Persistencia

Volumen persistente `postgres_data` en Docker para que los datos no se borren al apagar contenedores.

### Relaciones

Entidad o proceso autónomo sin dependencias foráneas directas en esta operación; mantiene aislamiento estricto de dominio respecto a otros agregados.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Validación de sintaxis de Docker Compose con `docker compose config`.

### Transacciones

Operación de solo lectura (SELECT). Se ejecuta bajo el autocommit estándar de PostgreSQL, optimizando el pooling de conexiones sin abrir transacciones de escritura innecesarias.

### Casos límite

Problema de saltos de línea Windows CRLF en scripts `entrypoint.sh` (debe normalizarse a LF en `.gitattributes` o Dockerfile con `dos2unix`).

### Casos de error

Contenedor web que reintenta conexión a PostgreSQL si la base de datos tarda unos segundos en iniciar.

### Consideraciones de seguridad

No ejecutar contenedores como `root`; no copiar archivos `.env` reales dentro de la imagen en el `Dockerfile` (usar `.dockerignore`).

### Consideraciones de rendimiento

Optimizar el orden de las capas de Docker (copiar `requirements.txt` e instalar dependencias antes de copiar el código fuente para aprovechar la caché de Docker).

### Fundamentos de Python relacionados

Gestión de dependencias con `pip` y entornos virtuales en contenedores.

### Conceptos Django relacionados

Variables de entorno inyectadas desde Docker, comandos de migración en el entrypoint.

### Conceptos DRF relacionados

Diseño de contratos REST con `serializers.Serializer` / `ModelSerializer`, vistas delegadoras `APIView` o `GenericAPIView`, normalización de respuestas JSON y documentación declarativa con `@extend_schema`.

### PostgreSQL

Contenedor oficial `postgres:16-alpine` con variables `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`.

### Arquitectura

Empaquetado y aislamiento de la unidad de despliegue del Monolito Modular.

### Dependencias entre módulos

Orquesta todos los módulos y la base de datos PostgreSQL.

### Antes de programar

1. ¿Por qué ejecutar procesos dentro de un contenedor Docker como usuario `root` es un riesgo de seguridad crítico?
2. ¿Por qué copiar `requirements.txt` y ejecutar `pip install` antes de `COPY . .` acelera la construcción de imágenes en Docker gracias a la caché de capas?

### Pruebas mínimas

1. Ejecutar `docker compose up -d`, esperar el arranque y consultar `GET http://localhost:8000/api/v1/health/ready/` -> Verificar status `200 OK` con base de datos conectada.
2. Ejecutar `docker compose down` y luego `docker compose up -d` -> Verificar que los datos creados previamente sigan existiendo (volumen persistente verificado).

### Pruebas negativas

1. Verificar que el archivo `.dockerignore` impida que `.env`, `__pycache__` y `.git` se copien dentro de la imagen de Docker.

### Documentación

Documentar los comandos de arranque con Docker para Windows (PowerShell) y Linux en el `README.md` principal.

### Explicación posterior

Explica la arquitectura de contenedores Docker, cómo `docker-compose` crea una red virtual aislada (Bridge Network) donde Django resuelve el host de PostgreSQL por su nombre de servicio (`db`), y cómo los volúmenes garantizan la durabilidad de los datos.

### Aplicación profesional

Estándar de facto en la industria para desarrollo local consistente, integración continua (CI) y despliegue en Kubernetes / AWS ECS.

### Reto adicional

Agregar un servicio de pruebas en `docker-compose.yml` que ejecute la suite completa de `pytest` en un contenedor efímero aislado.
