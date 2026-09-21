## Ejercicio 059 — Conciliador de Datos entre CSV y Base de Datos (`data-reconcile`)

> [← Ejercicio 058](../ejercicio_058/README.md) · [Índice General](../README.md) · [Ejercicio 060 →](../ejercicio_060/README.md)

### Contexto profesional
En procesos de auditoría financiera, migración de sistemas ERP o sincronización de pasarelas de pago, los ingenieros deben comparar periódicamente extractos en archivos CSV provistos por bancos o proveedores externos contra los registros reales almacenados en la base de datos de producción (PostgreSQL o SQLite), detectando transacciones faltantes, discrepancias en montos y registros duplicados.

### Problema
Construir una CLI que concilie un archivo CSV contra una tabla de base de datos relacional PostgreSQL (o SQLite opcional) mediante una clave primaria o compuesta (ej. `transaction_id` o `date + reference`), identifique discrepancias en campos numéricos y textuales, reporte registros presentes solo en CSV, solo en BD o con diferencias de valor, y genere un reporte de conciliación exportable.

### Usuario objetivo
Auditores de datos, desarrolladores backend y analistas financieros.

### Objetivo
Desarrollar un motor de conciliación y cruce de datos bidireccional con tolerancia numérica, mapeo de columnas y persistencia de reportes.

### Ejemplo conceptual de uso
```bash
# Conciliar extracto bancario CSV contra tabla 'transactions' en PostgreSQL
python data_reconcile.py reconcile extracto_banco.csv --db-table "transactions" --key "tx_id" --map "monto=amount,fecha=created_at"

# Conciliar con tolerancia de redondeo de 1 centavo y exportar discrepancias
python data_reconcile.py reconcile pagos.csv --db-table "payments" --key "payment_ref" --tolerance 0.01 --output-diffs discrepancias.csv
```

### Requisitos funcionales
- Leer y validar archivo CSV externo.
- Conectar a la base de datos relacional PostgreSQL (o SQLite opcional) y consultar los registros de la tabla objetivo.
- Mapeo flexible de nombres de columnas (`--map "col_csv=col_db,col2_csv=col2_db"`).
- Comparar conjuntos de datos en base a una clave primaria o compuesta (`--key`).
- Categorizar resultados de conciliación:
  - `MATCH`: Registros idénticos en ambos lados.
  - `CSV_ONLY`: Registros en el CSV que no existen en la base de datos.
  - `DB_ONLY`: Registros en la base de datos que no están en el CSV.
  - `VALUE_MISMATCH`: Registros presentes en ambos lados pero con diferencias en uno o más campos.
- Parámetro `--tolerance <VALOR>` para permitir variaciones numéricas mínimas por redondeo (ej. diferencias de $0.01).
- Generar resumen con porcentajes de conciliación y montos totales conciliados vs discrepantes.

### Requisitos de CLI
- Subcomando `reconcile`.
- Argumento posicional: archivo CSV.
- Opción `--db-table <TABLA>`.
- Opción `--key <COLUMNAS>`.
- Opción `--map <MAPEO>`.
- Opción `--tolerance <DELTA>` (default 0.00).
- Opciones de conexión: `--db-url` (PostgreSQL) o `--driver sqlite`.
- Opción `--output-diffs <RUTA>`.
- Exit code 0 si la conciliación es 100% exitosa sin discrepancias, 1 si existen registros no conciliados, 2 en errores.

### Entradas
- Archivo CSV, credenciales de base de datos y parámetros de mapeo.

### Salidas
- Reporte de conciliación en terminal y archivo de diferencias exportado.

### Persistencia
PostgreSQL como motor principal (o SQLite local opcional) y guardado de resultados de conciliación en disco.

### Validaciones
- Validar que las columnas clave existan tanto en el CSV como en la tabla de la base de datos.
- Comprobar que los tipos de datos a comparar sean compatibles.

### Casos límite
- Conciliación de cientos de miles de registros (usar streaming y diccionarios indexados por clave para no hacer consultas $N+1$).
- Fechas con formatos diferentes (ej. `YYYY-MM-DD` en BD vs `DD/MM/YYYY` en CSV; requerir normalización).
- Valores numéricos con signos o símbolos de moneda en el CSV.

### Manejo de errores
- Errores de base de datos (`psycopg.Error`).
- `csv.Error` en datos mal formados.

### Fundamentos de Python relacionados
- Módulos `decimal.Decimal` y `csv`.
- Algoritmos de unión y diferencia de conjuntos (`set.difference`, `set.intersection`).
- Normalización de tipos de datos y formatos de fecha.
- Conexión y transacciones en PostgreSQL / SQLite.

### Conceptos CLI relacionados
- Diseño de motores de reconciliación de datos en terminal.
- Gestión de tolerancias y reglas de negocio complejas.

### Herramientas o módulos para investigar
- `decimal`.
- `csv` y `datetime`.
- `psycopg` / `sqlite3`.
- `argparse`.

### Diseño de comandos
¿Cómo diseñarías el subcomando `auto-fix` para insertar automáticamente en la BD los registros faltantes identificados en el CSV previa confirmación?

### Diseño de argumentos
¿Cómo nombrarías la opción para ignorar mayúsculas/minúsculas en la comparación de campos de texto (`--ignore-case`)?

### Diseño de variables
`csv_records_index_map`, `db_records_index_map`, `matched_keys_set`, `value_mismatches_list`, `csv_only_keys_set`, `db_only_keys_set`.

### Antes de programar
1. ¿Por qué es fundamental indexar ambos conjuntos de datos en diccionarios en memoria basados en la clave de conciliación en lugar de ejecutar un `SELECT WHERE key = ...` por cada fila del CSV?
2. ¿Cómo normalizar fechas de diferentes zonas horarias y formatos antes de compararlas?

### Arquitectura
Lector CSV (`csv_reader.py`), repositorio de base de datos (`db_reader.py`), motor de conciliación (`reconciliation_engine.py`) y CLI.

### Pruebas mínimas
1. Conciliar un CSV de 5 registros contra una base de datos con 4 registros idénticos y 1 con monto diferente; verificar que clasifique 4 MATCH y 1 VALUE_MISMATCH.
2. Probar `--tolerance 0.05` en una diferencia de $0.02 y verificar que clasifique como MATCH.

### Pruebas de error
1. Especificar una tabla de base de datos inexistente -> Exit code 2 con error claro.

### Experiencia de usuario
Resumen ejecutivo en terminal con métricas: `% Conciliado`, `Total Registros CSV`, `Total Registros BD`, `Discrepancias` y tabla detallada de errores.

### Explicación posterior
Explica la importancia de los procesos de conciliación bancaria y contable en sistemas de pago para detectar fraudes, fugas de dinero o bugs de sincronización.

### Aplicación profesional
Auditorías de pasarelas de pago (Stripe, Adyen), conciliaciones contables ERP y validación de migraciones de bases de datos.

### Reto adicional
Generar un archivo SQL con las sentencias `UPDATE` e `INSERT` necesarias para corregir automáticamente las discrepancias detectadas en la base de datos.

---
> [← Ejercicio 058](../ejercicio_058/README.md) · [Índice General](../README.md) · [Ejercicio 060 →](../ejercicio_060/README.md)
