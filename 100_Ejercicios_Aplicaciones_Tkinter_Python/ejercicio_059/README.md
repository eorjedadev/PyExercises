## Ejercicio 059 — Directorio de Propiedades Inmobiliarias (`RealEstateListingApp`)

> [Índice General](../README.md) · [← Ejercicio 058](../ejercicio_058/README.md) · [Ejercicio 060 →](../ejercicio_060/README.md)

### Contexto profesional
En agencias de bienes raíces y corredurías inmobiliarias, los asesores inmobiliarios buscan propiedades que coincidan con las preferencias específicas de presupuesto, zona y recámaras de sus clientes.

### Usuario objetivo
Agente inmobiliario o asesor de bienes raíces.

### Problema
La búsqueda manual en catálogos no estructurados retrasa la atención a compradores y provoca ofrecer inmuebles fuera del presupuesto del cliente.

### Objetivo
Desarrollar una aplicación de búsqueda inmobiliaria con SQLite (`inmuebles.db`), con catálogo de propiedades y un motor de filtros dinámicos multi-criterio en SQL seguro (Rango de Precios Mín/Máx, Zona, Tipo de Inmueble, Mínimo de Recámaras y Baños, Operación: Venta/Renta).

### Flujo principal
El asesor define los criterios del cliente en el panel de búsqueda: tipo 'Departamento', operación 'Renta', precio máximo $15,000 y al menos 2 recámaras. Presiona 'Buscar Propiedades'. La aplicación construye una consulta SQL dinámica segura con marcadores parametrizados, ejecuta la búsqueda y muestra los inmuebles en el `Treeview` con su estatus de disponibilidad.

### Requisitos funcionales
- Esquema SQLite con tabla `propiedades` (id, codigo, titulo, tipo, operacion, zona, precio, recamaras, banos, superficie_m2, disponible).
- Filtros combinables: Tipo (`Casa`, `Departamento`, `Oficina`, `Terreno`), Operación (`Venta`, `Renta`), Zona (`Combobox`), Precio Mínimo y Máximo, Mínimo de Habitaciones.
- Construcción segura de consultas SQL dinámicas añadiendo cláusulas `WHERE` y tuplas de parámetros según los filtros activos.
- Botón 'Limpiar Filtros' que restaure el catálogo completo.
- Formulario modal para dar de alta nuevas propiedades.
- Visualización en `ttk.Treeview` con formateo de moneda y superficies.

### Requisitos de interfaz
- Panel de filtros colapsable o bien organizado en cuadrícula superior.
- `Treeview` central amplio con columnas para todos los atributos del inmueble.
- Barra de estado inferior con total de propiedades encontradas y precio promedio.

### Datos
- Propiedad: id, codigo, titulo, tipo, operacion, zona, precio, recamaras, banos, superficie, disponible.

### Estado
- Criterios de filtro activos en memoria.
- Resultados de búsqueda listados.

### Persistencia
Base de datos relacional SQLite (`datos/inmuebles.db`).

### Validaciones
- Precio máximo debe ser mayor al precio mínimo si ambos se especifican.
- Campos numéricos deben ser valores positivos válidos.

### Casos límite
- Ninguna propiedad coincide con los criterios (la tabla debe quedar limpia con aviso '0 propiedades encontradas').
- Filtros sin seleccionar ningún criterio (debe retornar el catálogo completo).

### Manejo de errores
- Proteger la construcción de la consulta SQL dinámica contra inyecciones mediante el uso estricto de parámetros parametrizados `?`.

### Fundamentos de Python relacionados
- Construcción de consultas SQL dinámicas uniendo cláusulas condicionales con `AND`.
- Acumulación de listas de parámetros para pasar como tupla a `cursor.execute()`.

### Conceptos Tkinter relacionados
- Paneles de filtrado multi-control coordinados con un botón de ejecución.
- Formateo de columnas en `Treeview`.

### Herramientas para investigar
- Técnicas de construcción de consultas dinámicas seguras en Python.
- Cláusula `WHERE 1=1` en generación de consultas SQL.

### Diseño de interfaz
¿Cómo organizarías los 6 controles de filtro en la parte superior para que ocupen poco espacio vertical y dejen ver la tabla de resultados?

### Diseño de variables
Usa nombres como `properties_tree`, `type_combo`, `op_combo`, `zone_combo`, `min_price_entry`, `max_price_entry`, `min_rooms_spinbox`, `search_btn`, `db_realestate`.

### Antes de programar
1. ¿Cómo se construye una consulta SQL dinámica usando la técnica `'SELECT * FROM propiedades WHERE 1=1 '` agregando cláusulas condicionales seguras con `?`?
2. ¿Por qué nunca se deben concatenar los valores directamente en la cadena SQL?

### Arquitectura
```
ejercicio_059/
├── app.py             # Interfaz con formulario de filtros y catálogo
├── property_repo.py   # Motor de consultas SQL dinámicas y parametrizadas
└── datos/
    └── inmuebles.db   # Base de datos inmobiliaria
```

### Pruebas mínimas
1. Filtrar por Tipo 'Departamento' y Operación 'Renta' -> La tabla debe listar únicamente los registros que cumplan ambas condiciones.
2. Filtrar con Precio Máximo $10,000 -> Ninguna propiedad en el resultado debe costar más de $10,000.

### Pruebas de error
1. Ingresar Precio Mínimo $20,000 y Máximo $10,000 -> Debe advertir error en el rango de precios.

### Experiencia de usuario
Al presionar 'Limpiar Filtros', todos los selectores deben restablecerse a 'Todos' y la tabla debe refrescarse al catálogo completo.

### Explicación posterior
¿Cómo funciona la técnica de acumular cláusulas `WHERE` y una lista de parámetros para ejecutar consultas dinámicas seguras en SQLite?

### Aplicación profesional
Portales inmobiliarios locales, sistemas de corretaje de propiedades y catálogos de venta de vehículos usados.

### Reto adicional
Añade un selector para ordenar los resultados de la búsqueda por 'Precio (Menor a Mayor)' o 'Superficie (Mayor a Menor)'.

---
> [Índice General](../README.md) · [← Ejercicio 058](../ejercicio_058/README.md) · [Ejercicio 060 →](../ejercicio_060/README.md)
