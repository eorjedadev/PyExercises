# Revisión de la colección

La revisión comprobó los 100 paquetes completos después de generar los datos.

| Elemento | Resultado |
| --- | ---: |
| Ejercicios consecutivos, del 001 al 100 | 100 |
| Apartados obligatorios por enunciado | 25 |
| Archivos de datos | 169 |
| Fuentes o tablas documentadas | 174 |
| Registros en fuentes principales | 156 573 |
| Registros en todas las fuentes | 184 912 |
| CSV | 146 |
| TXT tabulados | 5 |
| JSON de observaciones | 9 |
| Libros Excel | 4 |
| Bases SQLite | 5 |

Los recuentos incluyen las repeticiones suministradas. Los 100 archivos `procedencia.json` son metadatos y se contabilizan aparte de los archivos de datos.

Se comprobaron:

- Numeración, títulos, presencia y orden de los 25 apartados, y enlaces locales.
- Lectura de todos los archivos, cabeceras, número de filas y coincidencia con sus diccionarios y manifiestos.
- Huellas SHA-256 y tamaños de los archivos entregados.
- Integridad de las cinco bases SQLite mediante `PRAGMA integrity_check`.
- Estructura XML de los cuatro libros Excel y lectura independiente con openpyxl.
- Presencia de ambos brazos experimentales, muestras emparejadas para comparar instrumentos y suficientes observaciones de ambas clases en los encargos de clasificación revisados.
- Cruce de rutas con los tres transportistas, cohortes web recientes, dos años de cobertura nominal en los ejercicios energéticos temporales y disponibilidad del seguimiento de bajas al horizonte declarado.
- Ausencia de scripts de resolución, consultas resueltas y notebooks terminados en la colección.

La revisión editorial contrastó la progresión, las preguntas de los 100 encargos, la variedad de contextos y la disponibilidad de variables para el análisis solicitado. Los defectos didácticos permanecen en los datos para que el practicante los investigue y justifique sus decisiones. Las comprobaciones de integridad no certifican que una conclusión estadística sea correcta: esa evaluación requiere revisar el análisis del practicante.

[Volver al programa](README.md)
