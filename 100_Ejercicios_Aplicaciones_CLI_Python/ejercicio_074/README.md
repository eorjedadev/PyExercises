## Ejercicio 074 — Generador de Semillas de Datos para PostgreSQL / SQLite (`db-seeder`)

> [← Ejercicio 073](../ejercicio_073/README.md) · [Índice General](../README.md) · [Ejercicio 075 →](../ejercicio_075/README.md)

### Contexto profesional
Durante el desarrollo y pruebas de rendimiento de aplicaciones web y bases de datos relacionales, los desarrolladores necesitan poblar las tablas con miles de registros ficticios realistas (usuarios, transacciones, órdenes de compra, productos) respetando restricciones de clave foránea (Foreign Keys), tipos de datos y unicidad.

### Problema
Construir una CLI que genere e inserte datos sintéticos realistas en bases de datos relacionales (PostgreSQL como motor principal, o SQLite local opcional) a partir de una receta declarativa en JSON/YAML, soportando relaciones uno-a-muchos, generación determinista mediante semillas aleatorias fijas (`--seed`), inserciones masivas por lotes y exportación de volcados SQL.

### Usuario objetivo
Desarrolladores backend, ingenieros de QA y DBAs.

### Objetivo
Crear un generador de semillas de base de datos relacional con generadores sintéticos realistas, resolución de dependencias de foreign keys e inserciones en batch.

### Ejemplo conceptual de uso
```bash
# Poblar base de datos PostgreSQL según la receta con semilla reproducible
python db_seeder.py seed --recipe recipe.json --db-url "postgresql://user:pass@localhost:5432/app_db" --seed 42

# Generar 5,000 usuarios y 20,000 órdenes exportando a archivo SQL
python db_seeder.py export-sql --recipe recipe.json -o seed_data.sql
```

### Requisitos funcionales
- Receta declarativa `recipe.json` que define tablas, cantidad de registros y tipos de generadores por columna:
  - Generadores soportados: `name`, `email`, `phone`, `address`, `uuid`, `timestamp_range`, `integer_range`, `decimal_range`, `choice_list`, `foreign_key`.
- Resolución de orden de inserción: insertar primero las tablas padre y luego las tablas hijas para no violar restricciones de Foreign Key.
- Modo determinista con `--seed <ENTERO>`: garantiza que la misma semilla genere exactamente los mismos datos sintéticos en cada ejecución.
- Inserciones masivas por lotes (batches de 1,000 registros usando `executemany` o `COPY` en PostgreSQL).
- Subcomando `seed`: inserta directamente en la base de datos dentro de una transacción atómica.
- Subcomando `export-sql`: genera sentencias `INSERT INTO` en un archivo SQL sin conectarse a la base de datos.
- Subcomando `clean`: vacía las tablas de la receta respetando el orden inverso de claves foráneas.

### Requisitos de CLI
- Subcomandos: `seed`, `export-sql`, `clean`.
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite` (SQLite opcional).
- Opción `--recipe <RUTA>` (default `recipe.json`).
- Opción `--seed <N>`: semilla de aleatoriedad determinista.
- Opción `--batch-size <N>` (default 1000).
- Exit code 0 en éxito, 1 si falló la inserción o se violaron restricciones relacionales, 2 en errores de receta.

### Entradas
- Archivo de receta de semillas y credenciales de base de datos.

### Salidas
- Resumen de registros insertados por tabla y tiempo transcurrido en STDOUT.

### Persistencia
Inserción directa en base de datos PostgreSQL / SQLite o guardado de archivo `.sql`.

### Validaciones
- Validar que la receta no contenga dependencias circulares entre tablas.
- Comprobar que los tipos de datos generados coincidan con el esquema relacional.

### Casos límite
- Generación de millones de filas (gestión estricta de memoria mediante generadores).
- Columnas con restricciones de unicidad (`UNIQUE`; garantizar que el generador no produzca duplicados en el lote).
- Valores nulos permitidos según probabilidad configurable (ej. `nullable_percent: 20`).

### Manejo de errores
- `psycopg.IntegrityError` / `sqlite3.IntegrityError` con reporte de la fila infractora.
- Errores de sintaxis en la receta.

### Fundamentos de Python relacionados
- Módulos `random` (con `random.seed()`), `uuid`, `datetime`, `decimal`.
- Generación de datos sintéticos realistas con listas léxicas o módulo `faker` (si se investiga).
- Conexión y transacciones por lotes en PostgreSQL / SQLite.
- Algoritmo de ordenamiento topológico para Foreign Keys.

### Conceptos CLI relacionados
- Generación determinista de datos de prueba.
- Optimización de operaciones de inserción masiva en bases de datos.

### Herramientas o módulos para investigar
- `random`.
- `psycopg`.
- `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías la opción para truncar las tablas antes de sembrar (`--truncate`) bajo confirmación?

### Diseño de argumentos
¿Cómo nombrarías la opción para multiplicar la cantidad de registros de toda la receta por un factor (ej. `--scale 10` para generar 10x datos)?

### Diseño de variables
`seeding_recipe_dict`, `table_dependency_order`, `synthetic_record_batch`, `random_generator_seed`, `inserted_rows_counter_map`.

### Antes de programar
1. ¿Cómo rastrear los IDs generados en una tabla padre (ej. `users`) para seleccionarlos aleatoriamente como Foreign Keys válidas en la tabla hija (`orders`)?
2. ¿Por qué el uso de `random.seed(42)` permite reproducir exactamente los mismos bugs de prueba en diferentes máquinas de desarrollo?

### Arquitectura
Generador de campos sintéticos (`fake_generators.py`), resolutor de dependencias (`fk_resolver.py`), motor de inserción (`batch_inserter.py`) y CLI.

### Pruebas mínimas
1. Ejecutar `seed` con una receta de 10 usuarios y 30 órdenes en PostgreSQL (o SQLite con `--driver sqlite`) y verificar que todas las órdenes tengan un `user_id` existente.
2. Ejecutar con `--seed 100` dos veces y verificar que los nombres generados sean idénticos.

### Pruebas de error
1. Pasar una receta con un generador no reconocido `generador_inventado` -> Exit code 2 con error de validación.

### Experiencia de usuario
Barra de progreso por tabla indicando: `Insertando 'users': [██████████] 1,000/1,000 (100%) en 0.4s`, `Insertando 'orders': [██████████] 5,000/5,000 (100%) en 1.1s`.

### Explicación posterior
Explica la diferencia entre pruebas con datos mock sintéticos y pruebas con volcados de datos anonimizados de producción (Data Masking).

### Aplicación profesional
Preparación de entornos de prueba para QA, pruebas de carga y estrés en bases de datos y desarrollo offline.

### Reto adicional
Implementar soporte para el comando nativo `COPY` de PostgreSQL (`psycopg.Cursor.copy`) para lograr velocidades de inserción superiores a 100,000 registros por segundo.

---
> [← Ejercicio 073](../ejercicio_073/README.md) · [Índice General](../README.md) · [Ejercicio 075 →](../ejercicio_075/README.md)
