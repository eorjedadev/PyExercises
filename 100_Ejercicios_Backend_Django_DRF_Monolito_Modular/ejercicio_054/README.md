# Ejercicio 054 — Gestión de Datos Iniciales y Fixtures Profesionales con Seeds

[← Ejercicio 053](../ejercicio_053/README.md) · [Índice General](../README.md#índice-general-de-ejercicios) · [Mapa de Aprendizaje](../MAPA_APRENDIZAJE.md) · [Mapa de Arquitectura](../MAPA_ARQUITECTURA.md) · [Ejercicio 055 →](../ejercicio_055/README.md)

---

### Contexto de negocio

Cuando un nuevo desarrollador se une al equipo o cuando se despliega un entorno de staging/demo, se requiere poblar la base de datos con un conjunto coherente y realista de datos iniciales: categorías base, catálogo de productos con imágenes ficticias, usuarios con diferentes roles, stock de inventario y cupones activos. El uso de fixtures JSON estáticas frágiles suele romperse al cambiar modelos; se requiere un comando de Seed programático.

### Estado actual del sistema

Sistema completo con módulos de catálogo, inventario, usuarios, órdenes y promociones.

### Nueva necesidad

Crear el comando de gestión `python manage.py seed_demo_data --clean` en `apps/core/management/commands/seed_demo_data.py` que utilice los servicios oficiales de cada módulo para poblar un entorno completo y reproducible.

### Objetivo

Dominar la inicialización y siembra de datos (Data Seeding) en Django, entendiendo por qué los comandos basados en servicios son más robustos que los archivos `fixtures.json` estáticos ante migraciones de esquema.

### Actor

Desarrollador / Entorno de Testing / CI Pipeline

### Módulo responsable

`apps/core` coordinando con todos los módulos

### Entidades involucradas

`seed_demo_data` (BaseCommand), servicios de todos los módulos.

### Reglas de negocio

1. El comando debe crear: 1 Superusuario Admin, 2 Gestores de Catálogo, 5 Clientes de prueba, 10 Categorías jerárquicas, 30 Productos con stock y 3 Cupones promocionales.
2. Las contraseñas de todos los usuarios de prueba deben ser consistentes y documentadas (ej. `Password123!`).
3. El flag `--clean` debe purgar previamente los datos de prueba sin alterar esquemas.
4. El comando debe ser idempotente: si se ejecuta dos veces seguidas sin `--clean`, no debe duplicar registros ni fallar por unicidad.

### Contrato esperado

Ejecución en Consola (PowerShell):
```powershell
python manage.py seed_demo_data --clean
[SEED] Purgando datos de prueba existentes...
[SEED] Creando usuarios y roles...
[SEED] Creando categorias y catalogo...
[SEED] Inicializando stock de inventario...
[SEED] Creando cupones de descuento...
[OK] Base de datos poblada exitosamente con 30 productos y 8 usuarios.
```

### Persistencia

Inserción masiva controlada en todas las tablas de PostgreSQL.

### Relaciones

Relaciones coherentes entre todas las entidades del sistema.

### Autenticación

No aplica contexto de autenticación HTTP; la ejecución se realiza de forma interna mediante comandos CLI de administración, workers asíncronos o eventos de dominio en memoria.

### Autorización

No aplica autorización de capa HTTP. El control de acceso está delegado a los permisos del sistema operativo y roles del proceso de fondo que ejecuta la rutina.

### Validaciones

Validación de datos iniciales mediante los propios servicios del negocio.

### Transacciones

Transacción atómica global para garantizar que el seed se aplique completo o se revierta.

### Casos límite

Ejecución sobre una base de datos de producción (debe bloquearse si `settings.ENVIRONMENT == 'production'`).

### Casos de error

`CommandError` si se intenta ejecutar en entorno de producción sin flag explícito de confirmación.

### Consideraciones de seguridad

Garantizar que los comandos de seed nunca se ejecuten automáticamente en bases de datos con clientes reales.

### Consideraciones de rendimiento

Uso de operaciones por lotes cuando sea aplicable.

### Fundamentos de Python relacionados

Generación de datos estructurados, iteraciones, formato de mensajes en terminal con colores.

### Conceptos Django relacionados

`BaseCommand.style.SUCCESS`, `django.conf.settings`, validación de entorno de ejecución.

### Conceptos DRF relacionados

Diseño de contratos REST con `serializers.Serializer` / `ModelSerializer`, vistas delegadoras `APIView` o `GenericAPIView`, normalización de respuestas JSON y documentación declarativa con `@extend_schema`.

### PostgreSQL

`TRUNCATE ... CASCADE` o borrado ordenado respetando claves foráneas.

### Arquitectura

El comando de seed demuestra la ventaja de tener una Capa de Servicios: el script invoca `create_product()`, `register_user()`, `adjust_stock()` asegurando que todas las reglas de negocio se cumplan.

### Dependencias entre módulos

`apps/core` orquesta la llamada a servicios de todos los módulos.

### Antes de programar

1. ¿Por qué los archivos `dumpdata` / `loaddata` en formato JSON de Django se rompen frecuentemente cuando los modelos evolucionan con nuevas columnas obligatorias?
2. ¿Cómo protege la verificación `if not settings.DEBUG` contra el borrado accidental de una base de datos real?

### Pruebas mínimas

1. Ejecutar `call_command('seed_demo_data', clean=True)` en una base de datos vacía y verificar que se creen las entidades esperadas.
2. Ejecutar el comando por segunda vez y comprobar que finalice exitosamente sin violar constraints de unicidad.

### Pruebas negativas

1. Simular `settings.DEBUG = False` y verificar que el comando exija confirmación obligatoria o aborte la ejecución por seguridad.

### Documentación

Documentar los usuarios de prueba creados y sus credenciales en el `README.md` principal para facilitar el onboarding de nuevos desarrolladores.

### Explicación posterior

Explica la estrategia de Seeding Programático (Database Seeding) frente a Fixtures estáticas y cómo acelera el desarrollo local y las pruebas de frontend.

### Aplicación profesional

Inicialización de entornos de demostración para clientes, ambientes de staging para QA y pipelines de CI/CD.

### Reto adicional

Integrar la biblioteca `faker` (si está disponible) para generar nombres, descripciones y direcciones con variedad realista.
