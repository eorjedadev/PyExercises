# Ejercicio 063. Detector de productos mas vendidos

## Contexto

Este ejercicio representa una situacion practica donde no basta con escribir instrucciones sueltas. Debes pensar en piezas que colaboran: datos, reglas, funciones, clases, validaciones, errores y una salida clara para el usuario.

## Objetivo

Construir una solucion funcional para `Detector de productos mas vendidos` usando una estructura ordenada. El programa debe tener una entrada de datos, una capa de procesamiento y una salida verificable. Evita resolverlo todo dentro de un solo bloque.

## Area de entrenamiento

Ciencia de datos practica.

## Mision concreta

Tu solucion debe modelar una entidad principal llamada `FilaDato` y una estructura que administre muchos elementos, por ejemplo `Dataset`. No te quedes en imprimir datos: el programa debe recibir, validar, transformar y mostrar informacion util.

## Operaciones minimas

- cargar datos.
- limpiar valores.
- agrupar resultados.
- calcular metricas.
- visualizar o exportar.

## Reglas del dominio

- las columnas necesarias deben existir.
- los valores numericos deben convertirse con cuidado.
- los datos faltantes deben quedar reportados.

## Piezas que debes integrar

- Variables para representar estado temporal.
- Listas, diccionarios o conjuntos para agrupar datos.
- Condicionales para aplicar reglas.
- Ciclos para recorrer, buscar, filtrar o repetir acciones.
- Funciones para separar tareas pequeñas.
- Clases cuando exista una entidad clara del problema.
- Manejo de errores cuando pueda llegar un dato incorrecto.
- Persistencia o reporte cuando el ejercicio lo pida.

## Herramientas sugeridas

Puedes apoyarte en: csv, json, statistics.mean(), median(), Counter, defaultdict, matplotlib, plotly. No tienes que usarlas todas; el criterio esta en elegir las que realmente ordenan el problema.

## Funciones o metodos que deberias considerar

Piensa si tu solucion necesita funciones o metodos parecidos a estos: `cargar_dataset()`, `validar_columnas()`, `limpiar_fila()`, `calcular_metricas()`, `generar_reporte()`. No copies estos nombres sin pensar; usalos como pista para descubrir responsabilidades.

## Orientacion del profesor

Antes de programar, separa el problema en nombres concretos. Preguntate: que entidad principal existe, que datos debe guardar y que acciones puede realizar. Si el ejercicio habla de usuarios, productos, tickets, archivos, alertas o registros, probablemente hay una clase escondida esperando ser modelada.

Luego piensa en el flujo. Primero se recibe o carga informacion. Despues se valida. Luego se transforma o se guarda. Finalmente se muestra una respuesta. Si intentas hacer esas cuatro cosas al mismo tiempo, el programa se vuelve fragil. Trata cada parte como una pieza de un mecanismo: pequena, visible y comprobable.

## Logica que debes cuidar

- No aceptes datos vacios si son obligatorios.
- No repitas busquedas en varios lugares; crea una funcion o metodo para encontrar elementos.
- No guardes numeros como texto si despues vas a sumar, comparar o promediar.
- No mezcles interfaz, calculo y almacenamiento en la misma funcion.
- No confies en que el usuario escribira todo bien.

## Errores importantes a vigilar

- `ValueError` al convertir entradas numericas.
- `KeyError` al consultar claves inexistentes.
- `IndexError` al elegir una posicion de lista que no existe.
- Datos duplicados cuando deberian ser unicos.
- Estados imposibles, como cantidades negativas, fechas incoherentes o usuarios sin identificador.

## Pruebas que debes hacer

- Ejecuta el caso normal, con datos bien escritos.
- Ejecuta un caso con datos incompletos.
- Ejecuta un caso con valores extremos.
- Ejecuta un caso donde el elemento buscado no exista.
- Revisa si el resultado final se puede explicar con palabras simples.

## Pruebas especificas de este ejercicio

- fila incompleta.
- numero mal escrito.
- archivo vacio.
- grafico con etiquetas correctas.

## Reto extra

Agrega una funcion de exportacion, una opcion de busqueda avanzada o una pequena capa de pruebas. Si ya usaste consola, piensa como moverias la misma logica a Tkinter, Django o una API sin reescribirlo todo.
