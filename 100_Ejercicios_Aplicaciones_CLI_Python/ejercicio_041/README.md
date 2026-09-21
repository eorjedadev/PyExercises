## Ejercicio 041 — Registro de Inventario de Hardware y Activos IT (`asset-db`)

> [← Ejercicio 040](../ejercicio_040/README.md) · [Índice General](../README.md) · [Ejercicio 042 →](../ejercicio_042/README.md)

### Contexto profesional
Los departamentos de infraestructura y soporte de TI gestionan miles de activos físicos (servidores, laptops de empleados, switches, monitores) con números de serie, asignaciones de usuario, ubicaciones físicas y estados de garantía que deben registrarse y auditarse en una base de datos centralizada.

### Problema
Construir una CLI profesional conectada a una base de datos relacional para administrar el ciclo de vida de activos de hardware, permitiendo registrar nuevos equipos, asignar/desasignar a empleados, actualizar estado (Activo, En Reparación, Retirado), consultar inventario con filtros avanzados y exportar reportes de depreciación.

### Usuario objetivo
Administradores de sistemas, especialistas en soporte técnico y gestores de activos IT.

### Objetivo
Implementar una aplicación CLI conectada a PostgreSQL como motor relacional primario (con SQLite como alternativa local opcional), aplicando el patrón Repositorio y control de transacciones.

### Ejemplo conceptual de uso
```bash
# Registrar un nuevo activo en PostgreSQL
python asset_db.py register --tag "SRV-042" --serial "SN987654321" --type "Servidor" --model "Dell PowerEdge R750" --cost 4500.00

# Asignar un activo a un usuario
python asset_db.py assign --tag "SRV-042" --user "mario.gonzalez" --location "Rack B-12"

# Listar activos filtrando por tipo y estado usando SQLite local opcional
python asset_db.py list --type "Laptop" --status "Activo" --driver sqlite --sqlite-path ./assets_local.db
```

### Requisitos funcionales
- Subcomando `init-db`: crea el esquema de tablas relacionales (`assets`, `assignments`, `audit_log`) con índices y restricciones.
- Subcomando `register`: registra un activo con etiqueta patrimonial (`asset_tag` único), número de serie, tipo, modelo, costo de adquisición, fecha de compra y estado.
- Subcomando `assign`: crea un registro histórico de asignación vinculando el activo a un empleado y ubicación.
- Subcomando `status-change`: actualiza el estado (`ACTIVE`, `MAINTENANCE`, `RETIRED`) registrando el motivo.
- Subcomando `list`: consulta de activos con filtros múltiples (`--type`, `--status`, `--assigned-to`, `--location`).
- Subcomando `audit-history <TAG>`: muestra la línea de tiempo completa de asignaciones y cambios de estado del equipo.

### Requisitos de CLI
- Subcomandos: `init-db`, `register`, `assign`, `status-change`, `list`, `audit-history`.
- Opciones globales de conexión:
  - `--db-url <URL>` o variable de entorno `DATABASE_URL` (ej. `postgresql://user:pass@localhost:5432/it_assets`).
  - `--driver [postgresql|sqlite]` (default `postgresql`).
  - `--sqlite-path <RUTA>` (usado si el driver es `sqlite`).
- Exit code 0 en éxito, 1 si el activo no existe o viola unicidad, 2 en errores de conexión o argumentos.

### Entradas
- Parámetros de conexión a BD y datos de activos de hardware.

### Salidas
- Tablas formateadas con bordes en terminal, confirmaciones y mensajes de error.

### Persistencia
Base de datos relacional PostgreSQL (soporte para JSONB de especificaciones técnicas y UUID) como motor principal; SQLite como fallback local opcional.

### Validaciones
- `asset_tag` y `serial_number` deben ser únicos.
- El costo debe ser un valor decimal no negativo.
- El estado debe pertenecer al catálogo permitido.

### Casos límite
- Base de datos no inicializada o esquema desactualizado.
- Caída de la conexión de red hacia el servidor PostgreSQL durante una transacción.
- Intentar asignar un activo que se encuentra en estado `RETIRED` o `MAINTENANCE`.

### Manejo de errores
- Excepciones de conexión de base de datos (`psycopg.OperationalError` / `sqlite3.OperationalError`).
- Violaciones de integridad de clave única (`UniqueViolation`).

### Fundamentos de Python relacionados
- Patrón Repositorio (Repository Pattern) con interfaz abstracta (`BaseAssetRepository`, `PostgresAssetRepository`, `SqliteAssetRepository`).
- Manejo de transacciones con bloques `with connection:` (commit/rollback automático).
- Tipado estático con `dataclasses` o `Pydantic`.

### Conceptos CLI relacionados
- Configuración de conexiones vía variables de entorno vs flags CLI.
- Desacoplamiento de la capa de acceso a datos respecto a la interfaz de terminal.

### Herramientas o módulos para investigar
- Conector PostgreSQL: `psycopg` (v3) o `asyncpg`.
- Módulo estándar `sqlite3`.
- Módulo `os` y `argparse`.

### Diseño de comandos
Diseña la estructura de subcomandos para que las operaciones de auditoría no bloqueen las consultas regulares.

### Diseño de argumentos
¿Cómo permitirías pasar credenciales individuales (`--host`, `--port`, `--user`, `--password`, `--dbname`) si no se usa `--db-url`?

### Diseño de variables
`database_connection_url`, `db_driver_type`, `asset_record_dto`, `assignment_history_list`, `repository_instance`.

### Antes de programar
1. ¿Cómo diseñar la interfaz del repositorio para que la CLI ejecute exactamente el mismo código de negocio sin importar si el backend es PostgreSQL o SQLite?
2. ¿Cómo gestionar transacciones compuestas (ej. actualizar estado y registrar en la tabla de auditoría en la misma unidad atómica)?

### Arquitectura
Estructura profesional desacoplada:
```
ejercicio_041/
├── asset_db.py              # CLI y parsing de argumentos
├── config.py                # Carga de credenciales y variables de entorno
├── models.py                # Dataclasses de entidades (Asset, Assignment)
├── repositories/
│   ├── base.py              # Protocol/Abstract Base Class
│   ├── postgres_repo.py     # Implementación PostgreSQL
│   └── sqlite_repo.py       # Implementación SQLite opcional
└── views.py                 # Renderizado de tablas y formateo
```

### Pruebas mínimas
1. Inicializar esquema en PostgreSQL (o SQLite con `--driver sqlite`), registrar un activo y verificar que `list` lo devuelva con su ID y estado.
2. Asignar el activo a un usuario y verificar que `audit-history` muestre la asignación.

### Pruebas de error
1. Intentar registrar un activo con un `asset_tag` duplicado -> Exit code 1 con mensaje de conflicto de clave.

### Experiencia de usuario
Mensajes claros en terminal: `[OK] Activo SRV-042 registrado exitosamente (ID: 1)` y tablas con alineación perfecta.

### Explicación posterior
Explica la ventaja arquitectónica del patrón Repositorio y cómo permite cambiar de motor de base de datos sin alterar la interfaz CLI ni la lógica de negocio.

### Aplicación profesional
Sistemas CMDB (Configuration Management Database), gestión de inventarios corporativos y control de suministros.

### Reto adicional
Implementar un subcomando `export-csv` que ejecute una consulta con streaming desde PostgreSQL para exportar millones de registros sin saturar la RAM.

---
> [← Ejercicio 040](../ejercicio_040/README.md) · [Índice General](../README.md) · [Ejercicio 042 →](../ejercicio_042/README.md)
