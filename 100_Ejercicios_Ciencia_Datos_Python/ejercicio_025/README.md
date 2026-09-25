# Ejercicio 025 — Datos que llegan como tabla ancha

[Índice](../README.md#indice-de-ejercicios) · [Anterior](../ejercicio_024/README.md) · [Siguiente](../ejercicio_026/README.md)

### Contexto

Un almacén exporta saldos diarios en columnas. Sector: **inventarios**. Todos los registros son sintéticos; las entidades y situaciones no describen organizaciones reales.

### Problema

La forma del archivo dificulta comparar cambios temporales. El encargo requiere comprobar esa lectura con evidencia, sin aceptar como conclusión lo que plantea la situación.

### Pregunta principal

¿Qué productos concentran cambios de saldo y días sin información?

### Preguntas secundarias

- ¿Qué días y almacenes quedan representados en la comparación?
- ¿Cuántas observaciones y entidades respaldan cada resultado? ¿Cambiaría la respuesta con otra regla justificada de inclusión?
- ¿Qué información adicional permitiría distinguir una diferencia real del proceso de una diferencia en cómo se registran los datos?

### Dataset disponible

La unidad de la fuente principal es **un producto-almacén-fecha**. Este paquete es independiente de los anteriores: entidades con el mismo código en otro ejercicio no deben unirse entre ejercicios.

- [registros](datos/registros.csv): **440 registros**, 9 campos. Fuente principal: un producto-almacén-fecha.
- [productos](datos/productos.csv): **12 registros**, 4 campos. Catálogo vigente para todo el período.
- [saldos_anchos](datos/saldos_anchos.csv): **40 registros**, 367 campos. Exportación por producto-almacén y fecha; no constituye movimientos de stock.

[Procedencia y huellas de archivos](datos/procedencia.json). CSV: UTF-8, coma, cabecera y punto decimal esperado. TXT: UTF-8 con tabuladores. JSON: lista de objetos con las mismas columnas. Excel: hoja `registros`. Vacío, celda vacía o `null` representan ausencia; no equivalen a cero. Los tipos del diccionario son el contrato esperado, no una garantía del tipo que llegará al lector.

Son observaciones muestreadas de inventario, no un libro completo de movimientos. Saldo es inicial, demanda y reposición se observan durante el día; no se conoce toda demanda perdida ni se impone conservación entre días no observados.

### Diccionario de datos

**registros**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `registro_id` | Identificador de instantánea | texto |
| `fecha` | Día de observación al inicio de jornada | fecha |
| `almacen` | Almacén | categoría |
| `producto` | Código de producto | texto |
| `saldo` | Unidades disponibles al inicio | entero |
| `demanda` | Unidades solicitadas durante ese día | entero |
| `reposicion` | Unidades recibidas durante el día | entero |
| `plazo_dias` | Plazo contractual de reposición en días | entero |
| `coste_unitario` | Coste unitario de referencia en PEN | real |

**productos**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `producto` | Clave de producto | texto |
| `familia` | Familia comercial | categoría |
| `coste_referencia` | PEN por unidad, fijo en el período, sin costes indirectos | real |
| `plazo_catalogo` | Días de reposición contractual | entero |

**saldos_anchos**

| Campo | Significado | Tipo esperado |
| --- | --- | --- |
| `almacen` | Almacén | texto |
| `producto` | Producto | texto |
| `2024-01-01` | Saldo observado el 2024-01-01; vacío si no consta lectura | entero |
| `2024-01-02` | Saldo observado el 2024-01-02; vacío si no consta lectura | entero |
| `2024-01-03` | Saldo observado el 2024-01-03; vacío si no consta lectura | entero |
| `2024-01-04` | Saldo observado el 2024-01-04; vacío si no consta lectura | entero |
| `2024-01-05` | Saldo observado el 2024-01-05; vacío si no consta lectura | entero |
| `2024-01-06` | Saldo observado el 2024-01-06; vacío si no consta lectura | entero |
| `2024-01-07` | Saldo observado el 2024-01-07; vacío si no consta lectura | entero |
| `2024-01-08` | Saldo observado el 2024-01-08; vacío si no consta lectura | entero |
| `2024-01-09` | Saldo observado el 2024-01-09; vacío si no consta lectura | entero |
| `2024-01-10` | Saldo observado el 2024-01-10; vacío si no consta lectura | entero |
| `2024-01-11` | Saldo observado el 2024-01-11; vacío si no consta lectura | entero |
| `2024-01-12` | Saldo observado el 2024-01-12; vacío si no consta lectura | entero |
| `2024-01-13` | Saldo observado el 2024-01-13; vacío si no consta lectura | entero |
| `2024-01-14` | Saldo observado el 2024-01-14; vacío si no consta lectura | entero |
| `2024-01-15` | Saldo observado el 2024-01-15; vacío si no consta lectura | entero |
| `2024-01-16` | Saldo observado el 2024-01-16; vacío si no consta lectura | entero |
| `2024-01-17` | Saldo observado el 2024-01-17; vacío si no consta lectura | entero |
| `2024-01-18` | Saldo observado el 2024-01-18; vacío si no consta lectura | entero |
| `2024-01-19` | Saldo observado el 2024-01-19; vacío si no consta lectura | entero |
| `2024-01-20` | Saldo observado el 2024-01-20; vacío si no consta lectura | entero |
| `2024-01-21` | Saldo observado el 2024-01-21; vacío si no consta lectura | entero |
| `2024-01-22` | Saldo observado el 2024-01-22; vacío si no consta lectura | entero |
| `2024-01-23` | Saldo observado el 2024-01-23; vacío si no consta lectura | entero |
| `2024-01-24` | Saldo observado el 2024-01-24; vacío si no consta lectura | entero |
| `2024-01-25` | Saldo observado el 2024-01-25; vacío si no consta lectura | entero |
| `2024-01-26` | Saldo observado el 2024-01-26; vacío si no consta lectura | entero |
| `2024-01-27` | Saldo observado el 2024-01-27; vacío si no consta lectura | entero |
| `2024-01-28` | Saldo observado el 2024-01-28; vacío si no consta lectura | entero |
| `2024-01-29` | Saldo observado el 2024-01-29; vacío si no consta lectura | entero |
| `2024-01-30` | Saldo observado el 2024-01-30; vacío si no consta lectura | entero |
| `2024-01-31` | Saldo observado el 2024-01-31; vacío si no consta lectura | entero |
| `2024-02-01` | Saldo observado el 2024-02-01; vacío si no consta lectura | entero |
| `2024-02-02` | Saldo observado el 2024-02-02; vacío si no consta lectura | entero |
| `2024-02-03` | Saldo observado el 2024-02-03; vacío si no consta lectura | entero |
| `2024-02-04` | Saldo observado el 2024-02-04; vacío si no consta lectura | entero |
| `2024-02-05` | Saldo observado el 2024-02-05; vacío si no consta lectura | entero |
| `2024-02-06` | Saldo observado el 2024-02-06; vacío si no consta lectura | entero |
| `2024-02-07` | Saldo observado el 2024-02-07; vacío si no consta lectura | entero |
| `2024-02-08` | Saldo observado el 2024-02-08; vacío si no consta lectura | entero |
| `2024-02-09` | Saldo observado el 2024-02-09; vacío si no consta lectura | entero |
| `2024-02-10` | Saldo observado el 2024-02-10; vacío si no consta lectura | entero |
| `2024-02-11` | Saldo observado el 2024-02-11; vacío si no consta lectura | entero |
| `2024-02-12` | Saldo observado el 2024-02-12; vacío si no consta lectura | entero |
| `2024-02-13` | Saldo observado el 2024-02-13; vacío si no consta lectura | entero |
| `2024-02-14` | Saldo observado el 2024-02-14; vacío si no consta lectura | entero |
| `2024-02-15` | Saldo observado el 2024-02-15; vacío si no consta lectura | entero |
| `2024-02-16` | Saldo observado el 2024-02-16; vacío si no consta lectura | entero |
| `2024-02-17` | Saldo observado el 2024-02-17; vacío si no consta lectura | entero |
| `2024-02-18` | Saldo observado el 2024-02-18; vacío si no consta lectura | entero |
| `2024-02-19` | Saldo observado el 2024-02-19; vacío si no consta lectura | entero |
| `2024-02-20` | Saldo observado el 2024-02-20; vacío si no consta lectura | entero |
| `2024-02-21` | Saldo observado el 2024-02-21; vacío si no consta lectura | entero |
| `2024-02-22` | Saldo observado el 2024-02-22; vacío si no consta lectura | entero |
| `2024-02-23` | Saldo observado el 2024-02-23; vacío si no consta lectura | entero |
| `2024-02-24` | Saldo observado el 2024-02-24; vacío si no consta lectura | entero |
| `2024-02-25` | Saldo observado el 2024-02-25; vacío si no consta lectura | entero |
| `2024-02-26` | Saldo observado el 2024-02-26; vacío si no consta lectura | entero |
| `2024-02-27` | Saldo observado el 2024-02-27; vacío si no consta lectura | entero |
| `2024-02-28` | Saldo observado el 2024-02-28; vacío si no consta lectura | entero |
| `2024-02-29` | Saldo observado el 2024-02-29; vacío si no consta lectura | entero |
| `2024-03-01` | Saldo observado el 2024-03-01; vacío si no consta lectura | entero |
| `2024-03-02` | Saldo observado el 2024-03-02; vacío si no consta lectura | entero |
| `2024-03-03` | Saldo observado el 2024-03-03; vacío si no consta lectura | entero |
| `2024-03-04` | Saldo observado el 2024-03-04; vacío si no consta lectura | entero |
| `2024-03-05` | Saldo observado el 2024-03-05; vacío si no consta lectura | entero |
| `2024-03-06` | Saldo observado el 2024-03-06; vacío si no consta lectura | entero |
| `2024-03-07` | Saldo observado el 2024-03-07; vacío si no consta lectura | entero |
| `2024-03-08` | Saldo observado el 2024-03-08; vacío si no consta lectura | entero |
| `2024-03-09` | Saldo observado el 2024-03-09; vacío si no consta lectura | entero |
| `2024-03-10` | Saldo observado el 2024-03-10; vacío si no consta lectura | entero |
| `2024-03-11` | Saldo observado el 2024-03-11; vacío si no consta lectura | entero |
| `2024-03-12` | Saldo observado el 2024-03-12; vacío si no consta lectura | entero |
| `2024-03-13` | Saldo observado el 2024-03-13; vacío si no consta lectura | entero |
| `2024-03-14` | Saldo observado el 2024-03-14; vacío si no consta lectura | entero |
| `2024-03-15` | Saldo observado el 2024-03-15; vacío si no consta lectura | entero |
| `2024-03-16` | Saldo observado el 2024-03-16; vacío si no consta lectura | entero |
| `2024-03-17` | Saldo observado el 2024-03-17; vacío si no consta lectura | entero |
| `2024-03-18` | Saldo observado el 2024-03-18; vacío si no consta lectura | entero |
| `2024-03-19` | Saldo observado el 2024-03-19; vacío si no consta lectura | entero |
| `2024-03-20` | Saldo observado el 2024-03-20; vacío si no consta lectura | entero |
| `2024-03-21` | Saldo observado el 2024-03-21; vacío si no consta lectura | entero |
| `2024-03-22` | Saldo observado el 2024-03-22; vacío si no consta lectura | entero |
| `2024-03-23` | Saldo observado el 2024-03-23; vacío si no consta lectura | entero |
| `2024-03-24` | Saldo observado el 2024-03-24; vacío si no consta lectura | entero |
| `2024-03-25` | Saldo observado el 2024-03-25; vacío si no consta lectura | entero |
| `2024-03-26` | Saldo observado el 2024-03-26; vacío si no consta lectura | entero |
| `2024-03-27` | Saldo observado el 2024-03-27; vacío si no consta lectura | entero |
| `2024-03-28` | Saldo observado el 2024-03-28; vacío si no consta lectura | entero |
| `2024-03-29` | Saldo observado el 2024-03-29; vacío si no consta lectura | entero |
| `2024-03-30` | Saldo observado el 2024-03-30; vacío si no consta lectura | entero |
| `2024-03-31` | Saldo observado el 2024-03-31; vacío si no consta lectura | entero |
| `2024-04-01` | Saldo observado el 2024-04-01; vacío si no consta lectura | entero |
| `2024-04-02` | Saldo observado el 2024-04-02; vacío si no consta lectura | entero |
| `2024-04-03` | Saldo observado el 2024-04-03; vacío si no consta lectura | entero |
| `2024-04-04` | Saldo observado el 2024-04-04; vacío si no consta lectura | entero |
| `2024-04-05` | Saldo observado el 2024-04-05; vacío si no consta lectura | entero |
| `2024-04-06` | Saldo observado el 2024-04-06; vacío si no consta lectura | entero |
| `2024-04-07` | Saldo observado el 2024-04-07; vacío si no consta lectura | entero |
| `2024-04-08` | Saldo observado el 2024-04-08; vacío si no consta lectura | entero |
| `2024-04-09` | Saldo observado el 2024-04-09; vacío si no consta lectura | entero |
| `2024-04-10` | Saldo observado el 2024-04-10; vacío si no consta lectura | entero |
| `2024-04-11` | Saldo observado el 2024-04-11; vacío si no consta lectura | entero |
| `2024-04-12` | Saldo observado el 2024-04-12; vacío si no consta lectura | entero |
| `2024-04-13` | Saldo observado el 2024-04-13; vacío si no consta lectura | entero |
| `2024-04-14` | Saldo observado el 2024-04-14; vacío si no consta lectura | entero |
| `2024-04-15` | Saldo observado el 2024-04-15; vacío si no consta lectura | entero |
| `2024-04-16` | Saldo observado el 2024-04-16; vacío si no consta lectura | entero |
| `2024-04-17` | Saldo observado el 2024-04-17; vacío si no consta lectura | entero |
| `2024-04-18` | Saldo observado el 2024-04-18; vacío si no consta lectura | entero |
| `2024-04-19` | Saldo observado el 2024-04-19; vacío si no consta lectura | entero |
| `2024-04-20` | Saldo observado el 2024-04-20; vacío si no consta lectura | entero |
| `2024-04-21` | Saldo observado el 2024-04-21; vacío si no consta lectura | entero |
| `2024-04-22` | Saldo observado el 2024-04-22; vacío si no consta lectura | entero |
| `2024-04-23` | Saldo observado el 2024-04-23; vacío si no consta lectura | entero |
| `2024-04-24` | Saldo observado el 2024-04-24; vacío si no consta lectura | entero |
| `2024-04-25` | Saldo observado el 2024-04-25; vacío si no consta lectura | entero |
| `2024-04-26` | Saldo observado el 2024-04-26; vacío si no consta lectura | entero |
| `2024-04-27` | Saldo observado el 2024-04-27; vacío si no consta lectura | entero |
| `2024-04-28` | Saldo observado el 2024-04-28; vacío si no consta lectura | entero |
| `2024-04-29` | Saldo observado el 2024-04-29; vacío si no consta lectura | entero |
| `2024-04-30` | Saldo observado el 2024-04-30; vacío si no consta lectura | entero |
| `2024-05-01` | Saldo observado el 2024-05-01; vacío si no consta lectura | entero |
| `2024-05-02` | Saldo observado el 2024-05-02; vacío si no consta lectura | entero |
| `2024-05-03` | Saldo observado el 2024-05-03; vacío si no consta lectura | entero |
| `2024-05-04` | Saldo observado el 2024-05-04; vacío si no consta lectura | entero |
| `2024-05-05` | Saldo observado el 2024-05-05; vacío si no consta lectura | entero |
| `2024-05-06` | Saldo observado el 2024-05-06; vacío si no consta lectura | entero |
| `2024-05-07` | Saldo observado el 2024-05-07; vacío si no consta lectura | entero |
| `2024-05-08` | Saldo observado el 2024-05-08; vacío si no consta lectura | entero |
| `2024-05-09` | Saldo observado el 2024-05-09; vacío si no consta lectura | entero |
| `2024-05-10` | Saldo observado el 2024-05-10; vacío si no consta lectura | entero |
| `2024-05-11` | Saldo observado el 2024-05-11; vacío si no consta lectura | entero |
| `2024-05-12` | Saldo observado el 2024-05-12; vacío si no consta lectura | entero |
| `2024-05-13` | Saldo observado el 2024-05-13; vacío si no consta lectura | entero |
| `2024-05-14` | Saldo observado el 2024-05-14; vacío si no consta lectura | entero |
| `2024-05-15` | Saldo observado el 2024-05-15; vacío si no consta lectura | entero |
| `2024-05-16` | Saldo observado el 2024-05-16; vacío si no consta lectura | entero |
| `2024-05-17` | Saldo observado el 2024-05-17; vacío si no consta lectura | entero |
| `2024-05-18` | Saldo observado el 2024-05-18; vacío si no consta lectura | entero |
| `2024-05-19` | Saldo observado el 2024-05-19; vacío si no consta lectura | entero |
| `2024-05-20` | Saldo observado el 2024-05-20; vacío si no consta lectura | entero |
| `2024-05-21` | Saldo observado el 2024-05-21; vacío si no consta lectura | entero |
| `2024-05-22` | Saldo observado el 2024-05-22; vacío si no consta lectura | entero |
| `2024-05-23` | Saldo observado el 2024-05-23; vacío si no consta lectura | entero |
| `2024-05-24` | Saldo observado el 2024-05-24; vacío si no consta lectura | entero |
| `2024-05-25` | Saldo observado el 2024-05-25; vacío si no consta lectura | entero |
| `2024-05-26` | Saldo observado el 2024-05-26; vacío si no consta lectura | entero |
| `2024-05-27` | Saldo observado el 2024-05-27; vacío si no consta lectura | entero |
| `2024-05-28` | Saldo observado el 2024-05-28; vacío si no consta lectura | entero |
| `2024-05-29` | Saldo observado el 2024-05-29; vacío si no consta lectura | entero |
| `2024-05-30` | Saldo observado el 2024-05-30; vacío si no consta lectura | entero |
| `2024-05-31` | Saldo observado el 2024-05-31; vacío si no consta lectura | entero |
| `2024-06-01` | Saldo observado el 2024-06-01; vacío si no consta lectura | entero |
| `2024-06-02` | Saldo observado el 2024-06-02; vacío si no consta lectura | entero |
| `2024-06-03` | Saldo observado el 2024-06-03; vacío si no consta lectura | entero |
| `2024-06-04` | Saldo observado el 2024-06-04; vacío si no consta lectura | entero |
| `2024-06-05` | Saldo observado el 2024-06-05; vacío si no consta lectura | entero |
| `2024-06-06` | Saldo observado el 2024-06-06; vacío si no consta lectura | entero |
| `2024-06-07` | Saldo observado el 2024-06-07; vacío si no consta lectura | entero |
| `2024-06-08` | Saldo observado el 2024-06-08; vacío si no consta lectura | entero |
| `2024-06-09` | Saldo observado el 2024-06-09; vacío si no consta lectura | entero |
| `2024-06-10` | Saldo observado el 2024-06-10; vacío si no consta lectura | entero |
| `2024-06-11` | Saldo observado el 2024-06-11; vacío si no consta lectura | entero |
| `2024-06-12` | Saldo observado el 2024-06-12; vacío si no consta lectura | entero |
| `2024-06-13` | Saldo observado el 2024-06-13; vacío si no consta lectura | entero |
| `2024-06-14` | Saldo observado el 2024-06-14; vacío si no consta lectura | entero |
| `2024-06-15` | Saldo observado el 2024-06-15; vacío si no consta lectura | entero |
| `2024-06-16` | Saldo observado el 2024-06-16; vacío si no consta lectura | entero |
| `2024-06-17` | Saldo observado el 2024-06-17; vacío si no consta lectura | entero |
| `2024-06-18` | Saldo observado el 2024-06-18; vacío si no consta lectura | entero |
| `2024-06-19` | Saldo observado el 2024-06-19; vacío si no consta lectura | entero |
| `2024-06-20` | Saldo observado el 2024-06-20; vacío si no consta lectura | entero |
| `2024-06-21` | Saldo observado el 2024-06-21; vacío si no consta lectura | entero |
| `2024-06-22` | Saldo observado el 2024-06-22; vacío si no consta lectura | entero |
| `2024-06-23` | Saldo observado el 2024-06-23; vacío si no consta lectura | entero |
| `2024-06-24` | Saldo observado el 2024-06-24; vacío si no consta lectura | entero |
| `2024-06-25` | Saldo observado el 2024-06-25; vacío si no consta lectura | entero |
| `2024-06-26` | Saldo observado el 2024-06-26; vacío si no consta lectura | entero |
| `2024-06-27` | Saldo observado el 2024-06-27; vacío si no consta lectura | entero |
| `2024-06-28` | Saldo observado el 2024-06-28; vacío si no consta lectura | entero |
| `2024-06-29` | Saldo observado el 2024-06-29; vacío si no consta lectura | entero |
| `2024-06-30` | Saldo observado el 2024-06-30; vacío si no consta lectura | entero |
| `2024-07-01` | Saldo observado el 2024-07-01; vacío si no consta lectura | entero |
| `2024-07-02` | Saldo observado el 2024-07-02; vacío si no consta lectura | entero |
| `2024-07-03` | Saldo observado el 2024-07-03; vacío si no consta lectura | entero |
| `2024-07-04` | Saldo observado el 2024-07-04; vacío si no consta lectura | entero |
| `2024-07-05` | Saldo observado el 2024-07-05; vacío si no consta lectura | entero |
| `2024-07-06` | Saldo observado el 2024-07-06; vacío si no consta lectura | entero |
| `2024-07-07` | Saldo observado el 2024-07-07; vacío si no consta lectura | entero |
| `2024-07-08` | Saldo observado el 2024-07-08; vacío si no consta lectura | entero |
| `2024-07-09` | Saldo observado el 2024-07-09; vacío si no consta lectura | entero |
| `2024-07-10` | Saldo observado el 2024-07-10; vacío si no consta lectura | entero |
| `2024-07-11` | Saldo observado el 2024-07-11; vacío si no consta lectura | entero |
| `2024-07-12` | Saldo observado el 2024-07-12; vacío si no consta lectura | entero |
| `2024-07-13` | Saldo observado el 2024-07-13; vacío si no consta lectura | entero |
| `2024-07-14` | Saldo observado el 2024-07-14; vacío si no consta lectura | entero |
| `2024-07-15` | Saldo observado el 2024-07-15; vacío si no consta lectura | entero |
| `2024-07-16` | Saldo observado el 2024-07-16; vacío si no consta lectura | entero |
| `2024-07-17` | Saldo observado el 2024-07-17; vacío si no consta lectura | entero |
| `2024-07-18` | Saldo observado el 2024-07-18; vacío si no consta lectura | entero |
| `2024-07-19` | Saldo observado el 2024-07-19; vacío si no consta lectura | entero |
| `2024-07-20` | Saldo observado el 2024-07-20; vacío si no consta lectura | entero |
| `2024-07-21` | Saldo observado el 2024-07-21; vacío si no consta lectura | entero |
| `2024-07-22` | Saldo observado el 2024-07-22; vacío si no consta lectura | entero |
| `2024-07-23` | Saldo observado el 2024-07-23; vacío si no consta lectura | entero |
| `2024-07-24` | Saldo observado el 2024-07-24; vacío si no consta lectura | entero |
| `2024-07-25` | Saldo observado el 2024-07-25; vacío si no consta lectura | entero |
| `2024-07-26` | Saldo observado el 2024-07-26; vacío si no consta lectura | entero |
| `2024-07-27` | Saldo observado el 2024-07-27; vacío si no consta lectura | entero |
| `2024-07-28` | Saldo observado el 2024-07-28; vacío si no consta lectura | entero |
| `2024-07-29` | Saldo observado el 2024-07-29; vacío si no consta lectura | entero |
| `2024-07-30` | Saldo observado el 2024-07-30; vacío si no consta lectura | entero |
| `2024-07-31` | Saldo observado el 2024-07-31; vacío si no consta lectura | entero |
| `2024-08-01` | Saldo observado el 2024-08-01; vacío si no consta lectura | entero |
| `2024-08-02` | Saldo observado el 2024-08-02; vacío si no consta lectura | entero |
| `2024-08-03` | Saldo observado el 2024-08-03; vacío si no consta lectura | entero |
| `2024-08-04` | Saldo observado el 2024-08-04; vacío si no consta lectura | entero |
| `2024-08-05` | Saldo observado el 2024-08-05; vacío si no consta lectura | entero |
| `2024-08-06` | Saldo observado el 2024-08-06; vacío si no consta lectura | entero |
| `2024-08-07` | Saldo observado el 2024-08-07; vacío si no consta lectura | entero |
| `2024-08-08` | Saldo observado el 2024-08-08; vacío si no consta lectura | entero |
| `2024-08-09` | Saldo observado el 2024-08-09; vacío si no consta lectura | entero |
| `2024-08-10` | Saldo observado el 2024-08-10; vacío si no consta lectura | entero |
| `2024-08-11` | Saldo observado el 2024-08-11; vacío si no consta lectura | entero |
| `2024-08-12` | Saldo observado el 2024-08-12; vacío si no consta lectura | entero |
| `2024-08-13` | Saldo observado el 2024-08-13; vacío si no consta lectura | entero |
| `2024-08-14` | Saldo observado el 2024-08-14; vacío si no consta lectura | entero |
| `2024-08-15` | Saldo observado el 2024-08-15; vacío si no consta lectura | entero |
| `2024-08-16` | Saldo observado el 2024-08-16; vacío si no consta lectura | entero |
| `2024-08-17` | Saldo observado el 2024-08-17; vacío si no consta lectura | entero |
| `2024-08-18` | Saldo observado el 2024-08-18; vacío si no consta lectura | entero |
| `2024-08-19` | Saldo observado el 2024-08-19; vacío si no consta lectura | entero |
| `2024-08-20` | Saldo observado el 2024-08-20; vacío si no consta lectura | entero |
| `2024-08-21` | Saldo observado el 2024-08-21; vacío si no consta lectura | entero |
| `2024-08-22` | Saldo observado el 2024-08-22; vacío si no consta lectura | entero |
| `2024-08-23` | Saldo observado el 2024-08-23; vacío si no consta lectura | entero |
| `2024-08-24` | Saldo observado el 2024-08-24; vacío si no consta lectura | entero |
| `2024-08-25` | Saldo observado el 2024-08-25; vacío si no consta lectura | entero |
| `2024-08-26` | Saldo observado el 2024-08-26; vacío si no consta lectura | entero |
| `2024-08-27` | Saldo observado el 2024-08-27; vacío si no consta lectura | entero |
| `2024-08-28` | Saldo observado el 2024-08-28; vacío si no consta lectura | entero |
| `2024-08-29` | Saldo observado el 2024-08-29; vacío si no consta lectura | entero |
| `2024-08-30` | Saldo observado el 2024-08-30; vacío si no consta lectura | entero |
| `2024-08-31` | Saldo observado el 2024-08-31; vacío si no consta lectura | entero |
| `2024-09-01` | Saldo observado el 2024-09-01; vacío si no consta lectura | entero |
| `2024-09-02` | Saldo observado el 2024-09-02; vacío si no consta lectura | entero |
| `2024-09-03` | Saldo observado el 2024-09-03; vacío si no consta lectura | entero |
| `2024-09-04` | Saldo observado el 2024-09-04; vacío si no consta lectura | entero |
| `2024-09-05` | Saldo observado el 2024-09-05; vacío si no consta lectura | entero |
| `2024-09-06` | Saldo observado el 2024-09-06; vacío si no consta lectura | entero |
| `2024-09-07` | Saldo observado el 2024-09-07; vacío si no consta lectura | entero |
| `2024-09-08` | Saldo observado el 2024-09-08; vacío si no consta lectura | entero |
| `2024-09-09` | Saldo observado el 2024-09-09; vacío si no consta lectura | entero |
| `2024-09-10` | Saldo observado el 2024-09-10; vacío si no consta lectura | entero |
| `2024-09-11` | Saldo observado el 2024-09-11; vacío si no consta lectura | entero |
| `2024-09-12` | Saldo observado el 2024-09-12; vacío si no consta lectura | entero |
| `2024-09-13` | Saldo observado el 2024-09-13; vacío si no consta lectura | entero |
| `2024-09-14` | Saldo observado el 2024-09-14; vacío si no consta lectura | entero |
| `2024-09-15` | Saldo observado el 2024-09-15; vacío si no consta lectura | entero |
| `2024-09-16` | Saldo observado el 2024-09-16; vacío si no consta lectura | entero |
| `2024-09-17` | Saldo observado el 2024-09-17; vacío si no consta lectura | entero |
| `2024-09-18` | Saldo observado el 2024-09-18; vacío si no consta lectura | entero |
| `2024-09-19` | Saldo observado el 2024-09-19; vacío si no consta lectura | entero |
| `2024-09-20` | Saldo observado el 2024-09-20; vacío si no consta lectura | entero |
| `2024-09-21` | Saldo observado el 2024-09-21; vacío si no consta lectura | entero |
| `2024-09-22` | Saldo observado el 2024-09-22; vacío si no consta lectura | entero |
| `2024-09-23` | Saldo observado el 2024-09-23; vacío si no consta lectura | entero |
| `2024-09-24` | Saldo observado el 2024-09-24; vacío si no consta lectura | entero |
| `2024-09-25` | Saldo observado el 2024-09-25; vacío si no consta lectura | entero |
| `2024-09-26` | Saldo observado el 2024-09-26; vacío si no consta lectura | entero |
| `2024-09-27` | Saldo observado el 2024-09-27; vacío si no consta lectura | entero |
| `2024-09-28` | Saldo observado el 2024-09-28; vacío si no consta lectura | entero |
| `2024-09-29` | Saldo observado el 2024-09-29; vacío si no consta lectura | entero |
| `2024-09-30` | Saldo observado el 2024-09-30; vacío si no consta lectura | entero |
| `2024-10-01` | Saldo observado el 2024-10-01; vacío si no consta lectura | entero |
| `2024-10-02` | Saldo observado el 2024-10-02; vacío si no consta lectura | entero |
| `2024-10-03` | Saldo observado el 2024-10-03; vacío si no consta lectura | entero |
| `2024-10-04` | Saldo observado el 2024-10-04; vacío si no consta lectura | entero |
| `2024-10-05` | Saldo observado el 2024-10-05; vacío si no consta lectura | entero |
| `2024-10-06` | Saldo observado el 2024-10-06; vacío si no consta lectura | entero |
| `2024-10-07` | Saldo observado el 2024-10-07; vacío si no consta lectura | entero |
| `2024-10-08` | Saldo observado el 2024-10-08; vacío si no consta lectura | entero |
| `2024-10-09` | Saldo observado el 2024-10-09; vacío si no consta lectura | entero |
| `2024-10-10` | Saldo observado el 2024-10-10; vacío si no consta lectura | entero |
| `2024-10-11` | Saldo observado el 2024-10-11; vacío si no consta lectura | entero |
| `2024-10-12` | Saldo observado el 2024-10-12; vacío si no consta lectura | entero |
| `2024-10-13` | Saldo observado el 2024-10-13; vacío si no consta lectura | entero |
| `2024-10-14` | Saldo observado el 2024-10-14; vacío si no consta lectura | entero |
| `2024-10-15` | Saldo observado el 2024-10-15; vacío si no consta lectura | entero |
| `2024-10-16` | Saldo observado el 2024-10-16; vacío si no consta lectura | entero |
| `2024-10-17` | Saldo observado el 2024-10-17; vacío si no consta lectura | entero |
| `2024-10-18` | Saldo observado el 2024-10-18; vacío si no consta lectura | entero |
| `2024-10-19` | Saldo observado el 2024-10-19; vacío si no consta lectura | entero |
| `2024-10-20` | Saldo observado el 2024-10-20; vacío si no consta lectura | entero |
| `2024-10-21` | Saldo observado el 2024-10-21; vacío si no consta lectura | entero |
| `2024-10-22` | Saldo observado el 2024-10-22; vacío si no consta lectura | entero |
| `2024-10-23` | Saldo observado el 2024-10-23; vacío si no consta lectura | entero |
| `2024-10-24` | Saldo observado el 2024-10-24; vacío si no consta lectura | entero |
| `2024-10-25` | Saldo observado el 2024-10-25; vacío si no consta lectura | entero |
| `2024-10-26` | Saldo observado el 2024-10-26; vacío si no consta lectura | entero |
| `2024-10-27` | Saldo observado el 2024-10-27; vacío si no consta lectura | entero |
| `2024-10-28` | Saldo observado el 2024-10-28; vacío si no consta lectura | entero |
| `2024-10-29` | Saldo observado el 2024-10-29; vacío si no consta lectura | entero |
| `2024-10-30` | Saldo observado el 2024-10-30; vacío si no consta lectura | entero |
| `2024-10-31` | Saldo observado el 2024-10-31; vacío si no consta lectura | entero |
| `2024-11-01` | Saldo observado el 2024-11-01; vacío si no consta lectura | entero |
| `2024-11-02` | Saldo observado el 2024-11-02; vacío si no consta lectura | entero |
| `2024-11-03` | Saldo observado el 2024-11-03; vacío si no consta lectura | entero |
| `2024-11-04` | Saldo observado el 2024-11-04; vacío si no consta lectura | entero |
| `2024-11-05` | Saldo observado el 2024-11-05; vacío si no consta lectura | entero |
| `2024-11-06` | Saldo observado el 2024-11-06; vacío si no consta lectura | entero |
| `2024-11-07` | Saldo observado el 2024-11-07; vacío si no consta lectura | entero |
| `2024-11-08` | Saldo observado el 2024-11-08; vacío si no consta lectura | entero |
| `2024-11-09` | Saldo observado el 2024-11-09; vacío si no consta lectura | entero |
| `2024-11-10` | Saldo observado el 2024-11-10; vacío si no consta lectura | entero |
| `2024-11-11` | Saldo observado el 2024-11-11; vacío si no consta lectura | entero |
| `2024-11-12` | Saldo observado el 2024-11-12; vacío si no consta lectura | entero |
| `2024-11-13` | Saldo observado el 2024-11-13; vacío si no consta lectura | entero |
| `2024-11-14` | Saldo observado el 2024-11-14; vacío si no consta lectura | entero |
| `2024-11-15` | Saldo observado el 2024-11-15; vacío si no consta lectura | entero |
| `2024-11-16` | Saldo observado el 2024-11-16; vacío si no consta lectura | entero |
| `2024-11-17` | Saldo observado el 2024-11-17; vacío si no consta lectura | entero |
| `2024-11-18` | Saldo observado el 2024-11-18; vacío si no consta lectura | entero |
| `2024-11-19` | Saldo observado el 2024-11-19; vacío si no consta lectura | entero |
| `2024-11-20` | Saldo observado el 2024-11-20; vacío si no consta lectura | entero |
| `2024-11-21` | Saldo observado el 2024-11-21; vacío si no consta lectura | entero |
| `2024-11-22` | Saldo observado el 2024-11-22; vacío si no consta lectura | entero |
| `2024-11-23` | Saldo observado el 2024-11-23; vacío si no consta lectura | entero |
| `2024-11-24` | Saldo observado el 2024-11-24; vacío si no consta lectura | entero |
| `2024-11-25` | Saldo observado el 2024-11-25; vacío si no consta lectura | entero |
| `2024-11-26` | Saldo observado el 2024-11-26; vacío si no consta lectura | entero |
| `2024-11-27` | Saldo observado el 2024-11-27; vacío si no consta lectura | entero |
| `2024-11-28` | Saldo observado el 2024-11-28; vacío si no consta lectura | entero |
| `2024-11-29` | Saldo observado el 2024-11-29; vacío si no consta lectura | entero |
| `2024-11-30` | Saldo observado el 2024-11-30; vacío si no consta lectura | entero |
| `2024-12-01` | Saldo observado el 2024-12-01; vacío si no consta lectura | entero |
| `2024-12-02` | Saldo observado el 2024-12-02; vacío si no consta lectura | entero |
| `2024-12-03` | Saldo observado el 2024-12-03; vacío si no consta lectura | entero |
| `2024-12-04` | Saldo observado el 2024-12-04; vacío si no consta lectura | entero |
| `2024-12-05` | Saldo observado el 2024-12-05; vacío si no consta lectura | entero |
| `2024-12-06` | Saldo observado el 2024-12-06; vacío si no consta lectura | entero |
| `2024-12-07` | Saldo observado el 2024-12-07; vacío si no consta lectura | entero |
| `2024-12-08` | Saldo observado el 2024-12-08; vacío si no consta lectura | entero |
| `2024-12-09` | Saldo observado el 2024-12-09; vacío si no consta lectura | entero |
| `2024-12-10` | Saldo observado el 2024-12-10; vacío si no consta lectura | entero |
| `2024-12-11` | Saldo observado el 2024-12-11; vacío si no consta lectura | entero |
| `2024-12-12` | Saldo observado el 2024-12-12; vacío si no consta lectura | entero |
| `2024-12-13` | Saldo observado el 2024-12-13; vacío si no consta lectura | entero |
| `2024-12-14` | Saldo observado el 2024-12-14; vacío si no consta lectura | entero |
| `2024-12-15` | Saldo observado el 2024-12-15; vacío si no consta lectura | entero |
| `2024-12-16` | Saldo observado el 2024-12-16; vacío si no consta lectura | entero |
| `2024-12-17` | Saldo observado el 2024-12-17; vacío si no consta lectura | entero |
| `2024-12-18` | Saldo observado el 2024-12-18; vacío si no consta lectura | entero |
| `2024-12-19` | Saldo observado el 2024-12-19; vacío si no consta lectura | entero |
| `2024-12-20` | Saldo observado el 2024-12-20; vacío si no consta lectura | entero |
| `2024-12-21` | Saldo observado el 2024-12-21; vacío si no consta lectura | entero |
| `2024-12-22` | Saldo observado el 2024-12-22; vacío si no consta lectura | entero |
| `2024-12-23` | Saldo observado el 2024-12-23; vacío si no consta lectura | entero |
| `2024-12-24` | Saldo observado el 2024-12-24; vacío si no consta lectura | entero |
| `2024-12-25` | Saldo observado el 2024-12-25; vacío si no consta lectura | entero |
| `2024-12-26` | Saldo observado el 2024-12-26; vacío si no consta lectura | entero |
| `2024-12-27` | Saldo observado el 2024-12-27; vacío si no consta lectura | entero |
| `2024-12-28` | Saldo observado el 2024-12-28; vacío si no consta lectura | entero |
| `2024-12-29` | Saldo observado el 2024-12-29; vacío si no consta lectura | entero |
| `2024-12-30` | Saldo observado el 2024-12-30; vacío si no consta lectura | entero |

### Objetivo

Producir un diagnóstico que responda a la pregunta principal con resultados verificables y una decisión justificada. Incluye una tabla de evidencia con tamaños, un registro de decisiones de calidad y la representación solicitada; el código por sí solo no constituye la entrega.

### Antes de programar

- ¿Qué representa **un producto-almacén-fecha** y qué dejaría de representar si agregas por `producto`?
- ¿Qué significan `saldo` y `demanda`? ¿Son cantidades, categorías, estados o medidas de exposición?
- ¿Qué población pretendes describir y qué casos podrían quedar fuera antes de empezar?
- ¿Qué resultado podría refutar la interpretación planteada en el problema?

### Inspección inicial

Comprueba dimensiones, claves candidatas, tipos observados, categorías, unidades y cobertura de fechas. Revisa muestras del inicio y del final, además de una muestra elegida por ti. Examina si una entidad aparece varias veces y qué significa esa repetición. Informa lo observado sin convertir todavía cada sospecha en una corrección.

### Calidad de datos

Evalúa ausencias, repeticiones, formatos, rangos y coherencia entre campos. En este contexto debes considerar: **Un espacio vacío es distinto de saldo cero; sumar saldos a través del tiempo carece de sentido.** Para cada problema encontrado, registra evidencia, decisión —conservar, marcar, corregir, investigar, imputar o excluir—, justificación y efecto sobre la población. No borres nulos ni extremos por una regla universal. Mantén los originales y contrasta el resultado bajo una decisión alternativa razonable.

### Requisitos del análisis

Relaciona la exportación ancha con los registros, transforma su estructura y conserva producto, almacén y fecha.

La pregunta está delimitada, pero debes elegir transformaciones, métricas y representación. Compara al menos dos decisiones plausibles de preparación y explica si alteran el mensaje.

Cada métrica debe indicar unidad, población y denominador; separa dato observado de supuesto y resultado simulado. Separa lectura, validación, transformación y análisis en funciones; registra dependencias, parámetros y semillas si hay azar. Ejecuta desde una sesión limpia sin depender del orden accidental de celdas. Comprueba al menos una conservación relevante: conteo de entidades, suma de categorías, importe conciliado o coherencia de ventanas. Si no hay observaciones suficientes, informa la imposibilidad de estimar en vez de inventar un valor.

### Fundamentos de Python relacionados

Funciones reutilizables con nombres que expliquen su intención; parámetros para filtros y umbrales; rutas con pathlib, fechas, excepciones específicas y módulos. Evita capturar cualquier excepción y continuar silenciosamente.

### Conceptos de Ciencia de Datos relacionados

**Formato ancho y largo; pivotes; granularidad.** Estudia qué pregunta responde cada concepto, bajo qué supuestos y qué puede ocultar. Relaciona su significado con la unidad de observación del paquete antes de elegir una función de biblioteca.

### Herramientas que podría investigar

Elige las operaciones de selección, transformación y resumen que respondan al encargo. Revisa en la documentación sus supuestos sobre tipos, valores ausentes e índices. Justifica cuándo una operación vectorizada aporta claridad respecto a un ciclo. No se prescribe un gráfico ni una cadena de métodos.

### Diseño de variables

Identifica nombres para la fuente de **un producto-almacén-fecha**, el subconjunto elegible, la comparación por `producto`, una medida derivada y una función de validación. Propón nombres descriptivos en `snake_case`, conserva unidades en las magnitudes y diferencia observaciones de resúmenes. Explica un nombre descartado; evita `df1`, `df2`, `data`, `temp` o `x` cuando el dominio permita expresar la intención.

### Análisis requerido

Convierte el encargo en evidencia sobre **datos que llegan como tabla ancha**. Presenta la comparación principal y una alternativa que pueda cuestionarla; indica el tamaño de cada grupo o ventana y explica qué cambió al preparar los datos. ¿Qué días y almacenes quedan representados en la comparación? Expón al menos una explicación rival antes de redactar una recomendación.

### Visualización

Diseña una figura que permita responder «¿Qué productos concentran cambios de saldo y días sin información?». Elige la representación según tipo de variable y audiencia. Incluye población, unidades, período y denominadores; añade incertidumbre cuando sea parte de tu metodología. Escribe una observación y una afirmación que esa figura no demuestra.

### Interpretación

Explica qué significa el resultado para la pregunta principal, qué observaciones lo sostienen y qué tan sensible es a tu metodología. Distingue asociación de causalidad: una relación estadística no demuestra que una variable cause otra. Si el diseño permite una interpretación causal, identifica los supuestos y amenazas concretas que aún debes revisar.

### Casos límite

- Un espacio vacío es distinto de saldo cero; sumar saldos a través del tiempo carece de sentido.
- Un grupo sin observaciones elegibles o con una sola observación: ¿qué métricas dejan de tener sentido?
- Una clave repetida con valores diferentes: ¿es una nueva observación, una revisión o una inconsistencia?
- Un resultado que cambia al incluir un extremo o un registro incompleto: ¿cómo comunicarías esa fragilidad?

### Errores comunes

Aceptar la afirmación del problema sin comprobarla; confundir filas con entidades independientes; cambiar un denominador sin documentarlo; sumar o promediar sin revisar unidades; elegir el gráfico o la prueba que más favorezca una conclusión. En particular, explica cómo evitarías este riesgo: **Un espacio vacío es distinto de saldo cero; sumar saldos a través del tiempo carece de sentido.**

### Consulta recomendada

- [Reestructuración en Pandas](https://pandas.pydata.org/docs/user_guide/reshaping.html): consulta tablas anchas, largas y pivotes.
- [Guía de Pandas](https://pandas.pydata.org/docs/user_guide/index.html): consulta tipos, datos ausentes, agrupaciones y combinación de tablas.
- [Guía de Matplotlib](https://matplotlib.org/stable/users/explain/quick_start.html): consulta figura, ejes y representación de variables.

Antes de consultar, escribe una pregunta concreta sobre **formato ancho y largo**. Después registra el apartado leído, su supuesto principal y cómo lo aplicaste. Consulta también la [guía de investigación](../RECURSOS.md); no busques un notebook resuelto del encargo.

### Conclusión

Entrega una conclusión de 120–180 palabras con una cifra, su denominador o unidad, la decisión que respalda y una limitación. La conclusión debe basarse exclusivamente en los resultados que obtengas; el enunciado no anticipa si habrá diferencias, relaciones o un método superior.

Completa también la [explicación posterior y bitácora](../REGISTRO_APRENDIZAJE.md): problema, datos, calidad, transformaciones y sus razones, análisis, hallazgos, evidencia, límites, información que falta, reproducción y explicación a otra audiencia.

### Limitaciones

¿Qué observaciones, variables o mecanismos de selección faltan para sostener una conclusión más fuerte? ¿Qué parte de la pregunta queda sin responder? Revisa especialmente: **Un espacio vacío es distinto de saldo cero; sumar saldos a través del tiempo carece de sentido.** Los datos sintéticos sirven para entrenar razonamiento; sus patrones no estiman parámetros de una población real.

### Aplicación profesional

Revisión de abastecimiento y cobertura de demanda. Describe quién usaría tu resultado, qué decisión podría tomar y qué comprobación necesitaría antes de actuar.

### Reto adicional

Produce una tabla de comparación semanal preservando días no observados. Conserva la primera versión, cambia solo las condiciones declaradas y compara evidencia y conclusión. Documenta qué componentes de tu código pudiste reutilizar y qué supuesto dejó de ser válido.
