# Investigación sin soluciones

[Volver al programa](README.md)

Las referencias siguientes se verificaron el 2026-09-22. Usa la versión de documentación que corresponda a tu entorno. Los enunciados son originales; las referencias son documentación conceptual y de herramientas, no fuentes de datos ni ejercicios resueltos.

- [Tutorial de Python](https://docs.python.org/es/3/tutorial/): estructuras, control de flujo, funciones, archivos y excepciones.
- [Guía de Pandas](https://pandas.pydata.org/docs/user_guide/index.html): tipos, datos ausentes, agrupaciones y combinación de tablas.
- [Introducción a NumPy](https://numpy.org/doc/stable/user/absolute_beginners.html): arrays, ejes y operaciones numéricas.
- [Guía de Matplotlib](https://matplotlib.org/stable/users/explain/quick_start.html): figura, ejes y representación de variables.
- [Estadística con SciPy](https://docs.scipy.org/doc/scipy/tutorial/stats.html): distribuciones, estimación y contrastes.
- [Manual estadístico NIST/SEMATECH](https://www.itl.nist.gov/div898/handbook/): supuestos, análisis exploratorio y diseño experimental.
- [SELECT en SQLite](https://www.sqlite.org/lang_select.html): selección, agrupación y semántica de uniones.
- [Documentación de Jupyter](https://docs.jupyter.org/en/latest/): cuadernos, kernel y ejecución ordenada.
- [Evaluación en scikit-learn](https://scikit-learn.org/stable/model_selection.html): particiones, validación y selección de métricas.
- [Errores habituales en scikit-learn](https://scikit-learn.org/stable/common_pitfalls.html): fuga de datos y preparación consistente.
- [Clustering en scikit-learn](https://scikit-learn.org/stable/modules/clustering.html): supuestos y criterios de agrupación.
- [Reestructuración en Pandas](https://pandas.pydata.org/docs/user_guide/reshaping.html): tablas anchas, largas y pivotes.

## Ruta de consulta

1. Escribe la duda antes de abrir una documentación: por ejemplo, qué ocurre con los nulos de una clave al agrupar.
2. Identifica el concepto y busca su contrato: entradas, salidas, unidades, supuestos y excepciones.
3. Construye una muestra pequeña propia para comprobar tu interpretación, sin copiar la solución del encargo.
4. Registra qué decisión permite tomar esa consulta y cuándo no sería aplicable.
5. Explica el resultado con palabras antes de ampliar el cálculo al dataset completo.

## Preguntas orientadoras

- Python: ¿qué estructura preserva la identidad de una observación? ¿Qué debe devolver una función ante un dato inválido?
- Tablas: ¿qué representa una fila después de agrupar o unir? ¿Qué claves deben ser únicas?
- Estadística: ¿cuál es el estimando, qué unidades son independientes y de qué población provienen?
- Visualización: ¿qué comparación debe leer la audiencia? ¿Qué escala o agrupación podría inducir una lectura engañosa?
- SQL: ¿qué filas conserva la consulta y qué efecto tienen NULL y la cardinalidad?
- Modelado: ¿qué información existe al predecir? ¿Cómo se simula el uso futuro sin contaminar evaluación?

No necesitas memorizar nombres de métodos. Debes poder explicar el problema que resuelven y comprobar sus resultados. Si buscas ayuda, presenta pregunta, razonamiento e intento: pide una pista o revisión de supuestos antes que una implementación terminada.
