# ============================================================
# CURSO COMPLETO DE PYTHON: 500 EJERCICIOS + 200 SISTEMAS
# ============================================================
# 
# Este documento contiene 500 ejercicios organizados en:
# - NIVEL BÁSICO (1-200): Fundamentos de Python
# - NIVEL INTERMEDIO (201-400): POO, estructuras de datos, funciones
# - NIVEL AVANZADO (401-500): Temas avanzados, decoradores, generadores
#
# Además, 200 sistemas prácticos en archivo separado.
#
# ============================================================

"""
═══════════════════════════════════════════════════════════════════
                        NIVEL BÁSICO (1-200)
═══════════════════════════════════════════════════════════════════

═══════════════════════════════════════════════════════════════════
                    MÓDULO 1: INTRODUCCIÓN
═══════════════════════════════════════════════════════════════════

EJERCICIO 1 - HOLA MUNDO BÁSICO
────────────────────────────────
Descripción: Escribe tu primer programa en Python que muestre "¡Hola, Mundo!" en pantalla.

Concepto: La función print() es la forma más básica de mostrar salida en Python.
         Todo lo que coloques dentro de los paréntesis se mostrará en la consola.

Código:
"""
print("¡Hola, Mundo!")

"""
────────────────────────────────
EJERCICIO 2 - MÚLTIPLES SALIDAS
────────────────────────────────
Descripción: Muestra tu nombre y tu edad en líneas separadas usando print().

Concepto: Cada llamada a print() crea una nueva línea automáticamente.
         Puedes pasar múltiples argumentos separados por comas.

Código:
"""
nombre = "Juan"
edad = 25
print(nombre)
print(edad)

# Versión en una sola línea
print(nombre, edad)

"""
────────────────────────────────
EJERCICIO 3 - SEPARADORES PERSONALIZADOS
────────────────────────────────
Descripción: Usa el parámetro sep para cambiar el separador entre palabras.

Concepto: El parámetro sep (separador) permite definir qué carácter
         se usa entre los argumentos de print().

Código:
"""
# Por defecto usa espacio
print("Hola", "Mundo")  # Hola Mundo

# Con separador personalizado
print("Hola", "Mundo", sep="-")  # Hola-Mundo
print("2024", "01", "15", sep="/")  # 2024/01/15

"""
────────────────────────────────
EJERCICIO 4 - SIN SALTO DE LÍNEA
────────────────────────────────
Descripción: Muestra varios mensajes en la misma línea.

Concepto: El parámetro end define qué se muestra al final del print().
         Por defecto es "\n" (nueva línea).

Código:
"""
print("Esto ", end="")
print("está ", end="")
print("en la misma línea")

"""
────────────────────────────────
EJERCICIO 5 - COMENTARIOS EN PYTHON
────────────────────────────────
Descripción: Aprende a usar comentarios para documentar tu código.

Concepto: Los comentarios开始 con # y son ignorados por Python.
         Son esenciales para entender el código.

Código:
"""
# Este es un comentario de una línea

"""
Este es un
comentario de
múltiples líneas
"""

# ============================================================
#                    MÓDULO 2: VARIABLES
# ============================================================

"""
────────────────────────────────
EJERCICIO 6 - CREAR VARIABLES SIMPLES
────────────────────────────────
Descripción: Crea variables de diferentes tipos y muestra sus valores.

Concepto: Una variable es un contenedor que almacena un valor.
         No necesitas declarar el tipo; Python lo deduce automáticamente.

Código:
"""
# Variables de diferentes tipos
nombre = "María"           # str (cadena de texto)
edad = 30                  # int (número entero)
altura = 1.65              # float (número decimal)
es_estudiante = True      # bool (booleano)

print(nombre)
print(edad)
print(altura)
print(es_estudiante)

"""
────────────────────────────────
EJERCICIO 7 - CONOCER EL TIPO DE VARIABLE
────────────────────────────────
Descripción: Usa type() para conocer el tipo de dato de una variable.

Concepto: La función type() devuelve el tipo de dato de una variable.
         Es útil para depuración y validación.

Código:
"""
x = 10
y = "Hola"
z = 3.14

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'float'>

"""
────────────────────────────────
EJERCICIO 8 - CONVERSIÓN DE TIPOS (CASTING)
────────────────────────────────
Descripción: Convierte entre diferentes tipos de datos.

Concepto: Puedes convertir un tipo a otro usando: int(), float(), str(), bool()

Código:
"""
# String a entero
numero = int("25")
print(numero)  # 25

# String a float
decimal = float("3.14")
print(decimal)  # 3.14

# Número a string
texto = str(100)
print(texto)  # "100"

# Float a entero (redondea hacia abajo)
entero = int(3.7)
print(entero)  # 3

# Entero a booleano
print(bool(1))   # True
print(bool(0))   # False
print(bool(""))  # False
print(bool("texto"))  # True

"""
────────────────────────────────
EJERCICIO 9 - NOMBRADO DE VARIABLES
────────────────────────────────
Descripción: Practica las reglas de nombrado de variables.

Concepto: 
- Debe comenzar con letra o guión bajo
- No puede comenzar con número
- Sensible a mayúsculas (edad ≠ Edad)
- No puede ser palabra reservada

Código:
"""
# Válido
nombre = "Juan"
_privado = "secreto"
PI = 3.14159
nombreUsuario = "juan123"

# Inválido (comentado para evitar error)
# 2nombre = "Juan"     # Error: comienza con número
# mi-variable = "hola" # Error: contiene guión
# class = "hola"       # Error: palabra reservada

print("Reglas de nombrado aprendidas")

"""
────────────────────────────────
EJERCICIO 10 - CONVENCIONES DE NOMBRADO
────────────────────────────────
Descripción: Usa las convenciones correctas para nombrar variables.

Concepto:
- snake_case: nombre_usuario (para variables y funciones)
- UPPER_CASE: PI, MAXIMO (para constantes)
- PascalCase: Usuario, Calculadora (para clases)

Código:
"""
# snake_case (recomendado para variables)
nombre_usuario = "Juan"
edad_maxima = 100
precio_producto = 49.99

# UPPER_CASE (para constantes)
PI = 3.14159
MAXIMO_INTENTOS = 3
SALUDO = "Hola"

# No recomendado (pero válido)
nombreUsuario = "Juan"  # camelCase
NombreUsuario = "María"  # PascalCase

print("Convenciones de nombrado practicadas")

# ============================================================
#                    MÓDULO 3: OPERADORES
# ============================================================

"""
────────────────────────────────
EJERCICIO 11 - OPERADORES ARITMÉTICOS
────────────────────────────────
Descripción: Practica las operaciones matemáticas básicas.

Concepto: Python soporta: + (suma), - (resta), * (multiplicación),
         / (división), // (división entera), % (módulo), ** (potencia)

Código:
"""
a = 10
b = 3

print("Suma:", a + b)           # 13
print("Resta:", a - b)           # 7
print("Multiplicación:", a * b)  # 30
print("División:", a / b)        # 3.333...
print("División entera:", a // b) # 3
print("Módulo:", a % b)           # 1
print("Potencia:", a ** b)       # 1000

"""
────────────────────────────────
EJERCICIO 12 - OPERADORES DE COMPARACIÓN
────────────────────────────────
Descripción: Compara valores y entiende los booleanos.

Concepto: Los operadores de comparación devuelven True o False:
         ==, !=, >, <, >=, <=

Código:
"""
x = 5
y = 10

print(x == y)   # False (igual a)
print(x != y)   # True (diferente de)
print(x > y)    # False (mayor que)
print(x < y)    # True (menor que)
print(x >= y)   # False (mayor o igual)
print(x <= y)   # True (menor o igual)

"""
────────────────────────────────
EJERCICIO 13 - OPERADORES LÓGICOS
────────────────────────────────
Descripción: Combina condiciones con and, or, not.

Concepto:
- and: True si ambos son True
- or: True si al menos uno es True
- not: Invierte el valor booleano

Código:
"""
edad = 25
tiene_licencia = True

# and: ambas condiciones deben ser verdaderas
if edad >= 18 and tiene_licencia:
    print("Puedes conducir")

# or: al menos una condición debe ser verdadera
es_estudiante = True
es_beneficiario = False
if es_estudiante or es_beneficiario:
    print("Tienes descuento")

# not: invierte el valor
es_mayor = True
if not es_mayor:
    print("Es menor de edad")
else:
    print("Es mayor de edad")

"""
────────────────────────────────
EJERCICIO 14 - OPERADORES DE ASIGNACIÓN COMPUESTA
────────────────────────────────
Descripción: Usa operadores abreviados para modificar variables.

Concepto: x += 3 es lo mismo que x = x + 3

Código:
"""
x = 10
print(f"Valor inicial: {x}")

x += 5  # x = x + 5
print(f"Después de += 5: {x}")

x -= 3  # x = x - 3
print(f"Después de -= 3: {x}")

x *= 2  # x = x * 2
print(f"Después de *= 2: {x}")

x //= 4  # x = x // 4
print(f"Después de //= 4: {x}")

"""
────────────────────────────────
EJERCICIO 15 - PRECEDENCIA DE OPERADORES
────────────────────────────────
Descripción: Entiende el orden de evaluación de operaciones.

Concepto: El orden es:
1. ** (potencia)
2. * / // % (multiplicación/división)
3. + - (suma/resta)
4. == != < > (comparación)
5. not
6. and
7. or

Código:
"""
# Sin paréntesis
resultado = 2 + 3 * 4  # 14 (primero multiplicación)
print(f"2 + 3 * 4 = {resultado}")

# Con paréntesis
resultado = (2 + 3) * 4  # 20 (primero suma)
print(f"(2 + 3) * 4 = {resultado}")

# Más complejo
resultado = 2 ** 3 * 4 - 10 // 2 + 5
print(f"2 ** 3 * 4 - 10 // 2 + 5 = {resultado}")
# Explicación: 8*4 - 5 + 5 = 32 - 5 + 5 = 32

# ============================================================
#               MÓDULO 4: ENTRADA Y SALIDA
# ============================================================

"""
────────────────────────────────
EJERCICIO 16 - ENTRADA BÁSICA CON INPUT()
────────────────────────────────
Descripción: Aprende a obtener datos del usuario.

Concepto: input() siempre devuelve una cadena de texto (str).
         Debes convertir al tipo que necesites.

Código:
"""
# input() básico (devuelve string)
# nombre = input("¿Cómo te llamas? ")
# print(f"Hola {nombre}!")

# Simulando entrada para el ejemplo
nombre = "Juan"
print(f"Hola {nombre}!")

# input() como número (debes convertir)
# edad = int(input("¿Cuántos años tienes? "))
# print(f"Tienes {edad} años")

# Simulando
edad = 25
print(f"Tienes {edad} años")

"""
────────────────────────────────
EJERCICIO 17 - F-STRINGS (CADENAS FORMATEADAS)
────────────────────────────────
Descripción: Inserta variables dentro de cadenas de forma legible.

Concepto: Las f-strings permiten escribir {variable} dentro de una cadena
         precedida por 'f' o 'F'.

Código:
"""
nombre = "Ana"
edad = 28
altura = 1.70

# F-string básico
print(f"Me llamo {nombre} y tengo {edad} años")

# Con expresiones
print(f"El año que viene tendré {edad + 1} años")

# Con formatos
print(f"Mi altura es {altura:.2f} metros")  # 2 decimales
print(f"Mi altura es {altura:.1f} metros")  # 1 decimal

# Con alineación
print(f"{'Nombre':<10} | {'Edad':>5}")  # align left/right
print(f"{nombre:<10} | {edad:>5}")

"""
────────────────────────────────
EJERCICIO 18 - CONCATENACIÓN DE CADENAS
────────────────────────────────
Descripción: Une cadenas de diferentes formas.

Concepto: Puedes concatenar con + o con join()

Código:
"""
nombre = "Juan"
apellido = "Pérez"

# Con operador +
nombre_completo = nombre + " " + apellido
print(nombre_completo)  # Juan Pérez

# Con join()
partes = ["Hola", "a", "todos"]
mensaje = " ".join(partes)
print(mensaje)  # Hola a todos

# Con join y separador personalizado
palabras = ["uno", "dos", "tres"]
print("-".join(palabras))  # uno-dos-tres

# ============================================================
#               MÓDULO 5: CONDICIONALES
# ============================================================

"""
────────────────────────────────
EJERCICIO 19 - CONDICIONAL IF BÁSICO
────────────────────────────────
Descripción: Usa if para ejecutar código condicionalmente.

Concepto: if condición: ejecuta el bloque si la condición es True

Código:
"""
edad = 18

if edad >= 18:
    print("Eres mayor de edad")

print("Programa terminado")

"""
────────────────────────────────
EJERCICIO 20 - IF-ELSE
────────────────────────────────
Descripción: Ejecuta diferente código según la condición.

Concepto: else se ejecuta cuando if es False

Código:
"""
temperatura = 25

if temperatura > 30:
    print("Hace calor")
else:
    print("Temperatura agradable")

"""
────────────────────────────────
EJERCICIO 21 - IF-ELIF-ELSE
────────────────────────────────
Descripción: Maneja múltiples condiciones.

Concepto: elif permite verificar múltiples condiciones en cadena

Código:
"""
nota = 75

if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy bueno")
elif nota >= 70:
    print("Bueno")
elif nota >= 60:
    print("Suficiente")
else:
    print("Reprobado")

"""
────────────────────────────────
EJERCICIO 22 - CONDICIONES ANIDADAS
────────────────────────────────
Descripción: Usa condiciones dentro de condiciones.

Concepto: Puedes anidar if dentro de otros if

Código:
"""
edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes comprar el producto")
    else:
        print("No tienes suficiente dinero")
else:
    print("Eres menor de edad")

# Equivalente con and
if edad >= 18 and tiene_dinero:
    print("Puedes comprar el producto")

"""
────────────────────────────────
EJERCICIO 23 - OPERADORES EN CONDICIONES
────────────────────────────────
Descripción: Combina múltiples condiciones.

Concepto: Usa and, or, not para condiciones complejas

Código:
"""
usuario = "admin"
password = "123456"
sesion_activa = True

# Verificar credenciales
if usuario == "admin" and password == "123456":
    print("Acceso concedido")
else:
    print("Credenciales incorrectas")

# Verificar con or
tipo = "invitado"
es_premium = False

if tipo == "admin" or tipo == "premium" or es_premium:
    print("Tienes acceso especial")
else:
    print("Acceso estándar")

"""
────────────────────────────────
EJERCICIO 24 - EVALUACIÓN BOOLEANA
────────────────────────────────
Descripción: Entiende qué valores se evalúan como False.

Concepto: En Python, estos valores son "falsy":
         None, False, 0, 0.0, "", [], {}, ()

Código:
"""
# Valores que evaluan a False
if not None:
    print("None es False")

if not 0:
    print("0 es False")

if not "":
    print("Cadena vacía es False")

if not []:
    print("Lista vacía es False")

if not {}:
    print("Diccionario vacío es False")

# Valores que evaluan a True
if "texto":
    print("Cualquier texto no vacío es True")

if [1, 2]:
    print("Lista no vacía es True")

if 42:
    print("Cualquier número no cero es True")

"""
────────────────────────────────
EJERCICIO 25 - OPERADOR TERNARIO
────────────────────────────────
Descripción: Condicional en una sola línea.

Concepto: valor_if_true if condicion else valor_if_false

Código:
"""
edad = 20

# Forma tradicional
if edad >= 18:
    mensaje = "Mayor de edad"
else:
    mensaje = "Menor de edad"

# Con operador ternario
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)

# Otro ejemplo
es_premium = True
cuenta = "Premium" if es_premium else "Gratis"
print(cuenta)

# ============================================================
#                    MÓDULO 6: BUCLES
# ============================================================

"""
────────────────────────────────
EJERCICIO 26 - BUCLE WHILE BÁSICO
────────────────────────────────
Descripción: Repite código mientras una condición sea verdadera.

Concepto: while condición: ejecuta mientras sea True
         ¡Cuidado de no crear un bucle infinito!

Código:
"""
contador = 0

while contador < 5:
    print(contador)
    contador += 1  # Importante: evita bucle infinito

print("Bucle terminado")

"""
────────────────────────────────
EJERCICIO 27 - WHILE CON BREAK
────────────────────────────────
Descripción: Usa break para salir del bucle prematuramente.

Concepto: break termina inmediatamente el bucle

Código:
"""
while True:
    respuesta = input("¿Continuar? (s/n): ")
    
    if respuesta == "n":
        print("Saliendo...")
        break
    
    print("Continuando...")

print("Programa terminado")

# Simulando para que no pida entrada
respuesta = "s"
while respuesta != "n":
    print("Ejecutando tarea...")
    respuesta = "n"  # Para salir del bucle
print("Bucle terminado con break")

"""
────────────────────────────────
EJERCICIO 28 - WHILE CON CONTINUE
────────────────────────────────
Descripción: Usa continue para saltar iteraciones.

Concepto: continue salta el resto del código y pasa a la siguiente iteración

Código:
"""
# Imprimir solo números pares del 0 al 10
i = 0

while i <= 10:
    i += 1
    if i % 2 == 1:  # Si es impar
        continue    # Saltar
    print(i)        # Solo mostrar pares

"""
────────────────────────────────
EJERCICIO 29 - BUCLE FOR BÁSICO
────────────────────────────────
Descripción: Itera sobre una secuencia de elementos.

Concepto: for elemento in secuencia: iterable sobre cada elemento

Código:
"""
# Iterar sobre una cadena
for letra in "Python":
    print(letra)

# Iterar sobre una lista
frutas = ["manzana", "banano", "cereza"]
for fruta in frutas:
    print(fruta)

"""
────────────────────────────────
EJERCICIO 30 - FUNCIÓN RANGE()
────────────────────────────────
Descripción: Genera secuencias de números.

Concepto: range(inicio, fin, paso) genera números desde inicio hasta fin-1

Código:
"""
# range(n): 0 hasta n-1
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()

# range(inicio, fin)
print("range(2, 8):")
for i in range(2, 8):
    print(i, end=" ")
print()

# range(inicio, fin, paso)
print("range(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# range inverso
print("range(10, 0, -1):")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# ============================================================
#        EJERCICIOS 31-60: ESTRUCTURAS DE DATOS BÁSICAS
# ============================================================

"""
────────────────────────────────
EJERCICIO 31 - CREAR Y ACCEDER A LISTAS
────────────────────────────────
Descripción: Las listas son colecciones ordenadas y mutables.

Concepto: Lista = [elem1, elem2, ...]
         Acceso por índice: lista[0] (primer elemento)

Código:
"""
# Crear lista
frutas = ["manzana", "banano", "cereza", "naranja"]

# Acceder por índice
print(frutas[0])   # Primera
print(frutas[-1])  # Última
print(frutas[-2])  # Segunda desde el final

# Modificar
frutas[0] = "uva"
print(frutas)  # ['uva', 'banano', 'cereza', 'naranja']

# Longitud
print(len(frutas))  # 4

"""
────────────────────────────────
EJERCICIO 32 - MÉTODOS DE LISTAS
────────────────────────────────
Descripción: Aprende los métodos más útiles de listas.

Concepto: Las listas tienen métodos para agregar, eliminar, buscar, ordenar

Código:
"""
numeros = [1, 2, 3]

# Agregar elementos
numeros.append(4)      # Al final
print(numeros)  # [1, 2, 3, 4]

numeros.insert(0, 0)   # En posición específica
print(numeros)  # [0, 1, 2, 3, 4]

numeros.extend([5, 6])  # Múltiples elementos
print(numeros)  # [0, 1, 2, 3, 4, 5, 6]

# Eliminar elementos
numeros.remove(3)     # Elimina primera aparición
print(numeros)  # [0, 1, 2, 4, 5, 6]

ultimo = numeros.pop()  # Elimina y retorna el último
print(ultimo)  # 6
print(numeros)  # [0, 1, 2, 4, 5]

# Buscar
print(numeros.index(2))  # 2
print(numeros.count(1))  # 1

# Ordenar
numeros.sort()
print(numeros)  # [0, 1, 2, 4, 5]

numeros.reverse()
print(numeros)  # [5, 4, 2, 1, 0]

"""
────────────────────────────────
EJERCICIO 33 - SLICING DE LISTAS
────────────────────────────────
Descripción: Extrae porciones de una lista.

Concepto: lista[inicio:fin:paso]
         El elemento fin NO se incluye

Código:
"""
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numeros[2:7])     # [2, 3, 4, 5, 6]
print(numeros[:5])     # [0, 1, 2, 3, 4] (desde el inicio)
print(numeros[5:])     # [5, 6, 7, 8, 9] (hasta el final)
print(numeros[::2])    # [0, 2, 4, 6, 8] (cada 2)
print(numeros[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (inverso)

# Copiar lista
copia = numeros[:]
print(copia)

"""
────────────────────────────────
EJERCICIO 34 - DICCIONARIOS BÁSICOS
────────────────────────────────
Descripción: Los diccionarios almacenan pares clave-valor.

Concepto: diccionario = {clave1: valor1, clave2: valor2}
         Acceso: diccionario[clave] o diccionario.get(clave)

Código:
"""
# Crear diccionario
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder a valores
print(persona["nombre"])  # Juan
print(persona.get("edad"))  # 30
print(persona.get("pais", "No especificado"))  # Valor por defecto

# Modificar
persona["edad"] = 31
persona["pais"] = "España"
print(persona)

# Agregar nuevo par
persona["profesion"] = "Ingeniero"
print(persona)

# Eliminar
del persona["ciudad"]
print(persona)

"""
────────────────────────────────
EJERCICIO 35 - MÉTODOS DE DICCIONARIOS
────────────────────────────────
Descripción: Métodos útiles para trabajar con diccionarios.

Código:
"""
producto = {
    "nombre": "Laptop",
    "precio": 999,
    "stock": 5
}

# Keys, values, items
print(producto.keys())    # dict_keys(['nombre', 'precio', 'stock'])
print(producto.values())  # dict_values(['Laptop', 999, 5])
print(producto.items())  # dict_items([('nombre', 'Laptop'), ...])

# Iterar
for clave, valor in producto.items():
    print(f"{clave}: {valor}")

# Actualizar
producto.update({"precio": 899, "marca": "Dell"})
print(producto)

# pop (eliminar y retornar)
stock = producto.pop("stock")
print(stock)  # 5
print(producto)

"""
────────────────────────────────
EJERCICIO 36 - CONJUNTOS (SETS)
────────────────────────────────
Descripción: Los sets son colecciones sin duplicados y sin orden.

Concepto: set = {elem1, elem2, ...}
         Útiles para eliminar duplicados y operaciones de conjuntos

Código:
"""
# Crear set
frutas = {"manzana", "banano", "cereza", "manzana"}  # Duplicate removed

print(frutas)  # {'manzana', 'banano', 'cereza'}

# Agregar
frutas.add("naranja")
print(frutas)

frutas.update(["uva", "pera"])
print(frutas)

# Eliminar
frutas.discard("banano")  # No error si no existe
print(frutas)

# Operaciones de conjuntos
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 | set2)  # Union: {1, 2, 3, 4, 5, 6}
print(set1 & set2)  # Intersección: {3, 4}
print(set1 - set2)  # Diferencia: {1, 2}
print(set1 ^ set2)  # Diferencia simétrica: {1, 2, 5, 6}

"""
────────────────────────────────
EJERCICIO 37 - TUPLAS
────────────────────────────────
Descripción: Las tuplas son listas inmutables.

Concepto: tupla = (elem1, elem2, ...)
         No se pueden modificar después de creadas

Código:
"""
# Crear tupla
coordenadas = (10, 20, 30)
print(coordenadas)
print(coordenadas[0])  # 10

# Desempaquetar
x, y, z = coordenadas
print(f"x={x}, y={y}, z={z}")

# Tupla de un elemento (coma necesaria)
tupla_unica = (5,)  # No es lo mismo que (5)
print(type(tupla_unica))

# Inmutabilidad
# coordenadas[0] = 15  # ¡Error! No se puede modificar

# Métodos
print(coordenadas.count(10))  # 1
print(coordenadas.index(20))  # 1

"""
────────────────────────────────
EJERCICIO 38 - ENUMERATE
────────────────────────────────
Descripción: Obtiene índice y valor al iterar.

Concepto: enumerate(iterable) devuelve (índice, valor)

Código:
"""
frutas = ["manzana", "banano", "cereza"]

# Con enumerate
for indice, valor in enumerate(frutas):
    print(f"Índice {indice}: {valor}")

# Enumerar desde otro índice
for indice, valor in enumerate(frutas, start=1):
    print(f"Fruta #{indice}: {valor}")

# Convertir a lista de tuplas
print(list(enumerate(frutas)))

"""
────────────────────────────────
EJERCICIO 39 - ZIP
────────────────────────────────
Descripción: Combina múltiples iterables.

Concepto: zip(iter1, iter2) combina elementos en tuplas

Código:
"""
nombres = ["Juan", "Ana", "Luis"]
edades = [25, 30, 35]

# Combinar
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# Convertir a diccionario
diccionario = dict(zip(nombres, edades))
print(diccionario)

# Diferentes longitudes (se usa la menor)
nombres2 = ["Juan", "Ana"]
print(list(zip(nombres2, edades)))  # Solo 2 elementos

"""
────────────────────────────────
EJERCICIO 40 - LIST COMPREHENSION BÁSICO
────────────────────────────────
Descripción: Crear listas de forma concisa.

Concepto: [expresion for elemento in iterable]

Código:
"""
# Tradicional
cuadrados = []
for i in range(10):
    cuadrados.append(i ** 2)

# Con list comprehension
cuadrados = [i ** 2 for i in range(10)]
print(cuadrados)

# Con condición (filtrar)
pares = [i for i in range(20) if i % 2 == 0]
print(pares)

# Con transformación
palabras = ["hola", "mundo", "python"]
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)

# ============================================================
#        EJERCICIOS 41-80: FUNCIONES BÁSICAS
# ============================================================

"""
────────────────────────────────
EJERCICIO 41 - FUNCIÓN BÁSICA
────────────────────────────────
Descripción: Crea tu primera función.

Concepto: def nombre_funcion(parametros): return valor

Código:
"""
def saludar():
    """Esta función muestra un saludo"""
    print("¡Hola!")

# Llamar función
saludar()

# Función con return
def obtener_saludo():
    return "¡Hola, Mundo!"

mensaje = obtener_saludo()
print(mensaje)

"""
────────────────────────────────
EJERCICIO 42 - FUNCIONES CON PARÁMETROS
────────────────────────────────
Descripción: Pasa datos a las funciones.

Concepto: Los parámetros son variables en la definición
         Los argumentos son los valores reales

Código:
"""
def saludar_persona(nombre):
    """Saluda a una persona específica"""
    print(f"¡Hola {nombre}!")

saludar_persona("Juan")
saludar_persona("María")

# Múltiples parámetros
def presentar(nombre, edad):
    print(f"Soy {nombre} y tengo {edad} años")

presentar("Juan", 25)

"""
────────────────────────────────
EJERCICIO 43 - PARÁMETROS POR DEFECTO
────────────────────────────────
Descripción: Define valores por defecto para parámetros.

Concepto: parametro=valor por defecto

Código:
"""
def saludar(nombre, mensaje="¡Hola!"):
    print(f"{mensaje}, {nombre}!")

saludar("Juan")  # Usa el mensaje por defecto
saludar("María", "Buenos días")  # Usa mensaje personalizado

# Varios parámetros con valores por defecto
def crear_usuario(nombre, edad=18, pais="España"):
    return {"nombre": nombre, "edad": edad, "pais": pais}

print(crear_usuario("Juan"))
print(crear_usuario("Ana", 25))
print(crear_usuario("Luis", pais="México"))

"""
────────────────────────────────
EJERCICIO 44 - ARGUMENTOS VARIABLES *ARGS
────────────────────────────────
Descripción: Acepta múltiples argumentos posicionales.

Concepto: *args captura argumentos como tupla

Código:
"""
def suma(*numeros):
    """Suma todos los números dados"""
    total = 0
    for n in numeros:
        total += n
    return total

print(suma(1, 2))         # 3
print(suma(1, 2, 3, 4))   # 10
print(suma())             # 0

# Función con args y otros parámetros
def mostrar_info(nombre, *cursos):
    print(f"{nombre} está cursando:")
    for curso in cursos:
        print(f"  - {curso}")

mostrar_info("Juan", "Python", "JavaScript", "SQL")

"""
────────────────────────────────
EJERCICIO 45 - ARGUMENTOS NOMBRADOS **KWARGS
────────────────────────────────
Descripción: Acepta múltiples argumentos como clave-valor.

Concepto: **kwargs captura argumentos como diccionario

Código:
"""
def configurar_usuario(**datos):
    """Muestra la configuración del usuario"""
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

configurar_usuario(nombre="Juan", edad=25, ciudad="Madrid")

# Combinar *args y **kwargs
def funcion_completa(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

funcion_completa(1, 2, 3, 4, nombre="Juan", edad=25)

"""
────────────────────────────────
EJERCICIO 46 - FUNCIONES LAMBDA
────────────────────────────────
Descripción: Funciones anónimas de una línea.

Concepto: lambda parametros: expresión

Código:
"""
# Función lambda básica
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # 25

# Lambda con múltiples parámetros
suma = lambda a, b: a + b
print(suma(3, 4))  # 7

# Lambda con filter
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]

# Lambda con map
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Lambda con sorted
nombres = ["Carlos", "Ana", "Pedro", "Beatriz"]
print(sorted(nombres, key=lambda x: len(x)))  # Por longitud
print(sorted(nombres, key=lambda x: x[-1]))  # Por última letra

"""
────────────────────────────────
EJERCICIO 47 - DESEMPAQUETADO DE VARIABLES
────────────────────────────────
Descripción: Asigna valores a múltiples variables a la vez.

Concepto: a, b = valor1, valor2

Código:
"""
# Desempaquetado básico
a, b = 1, 2
print(f"a={a}, b={b}")

# Intercambiar valores
a, b = b, a
print(f"a={a}, b={b}")

# Desempaquetar secuencia
primero, segundo, tercero = [1, 2, 3]
print(f"{primero}, {segundo}, {tercero}")

# Desempaquetar con *
numeros = [1, 2, 3, 4, 5]
primero, *resto = numeros
print(f"Primero: {primero}")  # 1
print(f"Resto: {resto}")      # [2, 3, 4, 5]

# Desempaquetar diccionario
dic = {"a": 1, "b": 2}
print(*dic.items())  # ('a', 1) ('b', 2)

"""
────────────────────────────────
EJERCICIO 48 - ALCANCE DE VARIABLES (SCOPE)
────────────────────────────────
Descripción: Entiende las variables locales y globales.

Concepto: 
- Variables locales: solo existen dentro de la función
- Variables globales: accesibles en todo el programa

Código:
"""
# Variable global
mensaje = "Hola"

def funcion1():
    # Variable local
    mensaje_local = "Mundo"
    print(f"{mensaje} {mensaje_local}")

# print(mensaje_local)  # Error: no existe fuera

# Modificar variable global
contador = 0

def incrementar():
    global contador
    contador += 1
    print(f"Contador: {contador}")

incrementar()
incrementar()
print(f"Contador final: {contador}")

"""
────────────────────────────────
EJERCICIO 49 - RETURN MÚLTIPLE
────────────────────────────────
Descripción: Las funciones pueden retornar múltiples valores.

Concepto: return valor1, valor2 crea una tupla

Código:
"""
def operaciones(a, b):
    """Retorna múltiples resultados"""
    suma = a + b
    resta = a - b
    producto = a * b
    return suma, resta, producto

resultado = operaciones(10, 5)
print(resultado)  # (15, 5, 50)

# Desempaquetar
s, r, p = operaciones(10, 5)
print(f"Suma: {s}, Resta: {r}, Producto: {p}")

"""
────────────────────────────────
EJERCICIO 50 - FUNCIONES ANIDADAS
────────────────────────────────
Descripción: Define funciones dentro de funciones.

Concepto: Las funciones anidadas pueden acceder a variables del scope exterior

Código:
"""
def exterior():
    mensaje = "Hola desde exterior"
    
    def interior():
        print(mensaje)  # Accede a variable de exterior
    
    interior()

exterior()

# Con closure
def crear_multiplicador(factor):
    def multiplicar(numero):
        return numero * factor
    return multiplicar

duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)

print(duplicar(5))  # 10
print(triplicar(5))  # 15

# ============================================================
#        EJERCICIOS 51-100: CASOS PRÁCTICOS BÁSICOS
# ============================================================

"""
────────────────────────────────
EJERCICIO 51 - CALCULADORA BÁSICA
────────────────────────────────
Descripción: Crea una calculadora que realize operaciones básicas.

Concepto: Uso de funciones, condicionales y entrada/salida

Código:
"""
def calculadora():
    print("=== CALCULADORA BÁSICA ===")
    print("Operaciones: +, -, *, /")
    
    num1 = float(input("Primer número: "))
    operador = input("Operador: ")
    num2 = float(input("Segundo número: "))
    
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Error: División por cero"
    else:
        return "Operador inválido"
    
    return f"Resultado: {resultado}"

# Demo (sin pedir entrada real)
print("Calculadora creada")
print("Para usar: calculadora()")

"""
────────────────────────────────
EJERCICIO 52 - CONVERSOR DE TEMPERATURA
────────────────────────────────
Descripción: Convierte entre Celsius, Fahrenheit y Kelvin.

Concepto: Fórmulas de conversión de temperatura

Código:
"""
def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def celsius_a_kelvin(c):
    return c + 273.15

def kelvin_a_celsius(k):
    return k - 273.15

# Ejemplos
print(f"25°C = {celsius_a_fahrenheit(25)}°F")
print(f"77°F = {fahrenheit_a_celsius(77)}°C")
print(f"100°C = {celsius_a_kelvin(100)}K")

"""
────────────────────────────────
EJERCICIO 53 - DETERMINAR MAYOR DE 3 NÚMEROS
────────────────────────────────
Descripción: Encuentra el número mayor de tres valores.

Concepto: Comparaciones y condicionales

Código:
"""
def mayor_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(mayor_de_tres(10, 25, 15))  # 25
print(mayor_de_tres(100, 50, 75))  # 100

# Con max()
def mayor_max(a, b, c):
    return max(a, b, c)

print(mayor_max(10, 25, 15))  # 25

"""
────────────────────────────────
EJERCICIO 54 - VALIDADOR DE CONTRASEÑA
────────────────────────────────
Descripción: Verifica si una contraseña cumple requisitos.

Concepto: Cadenas, longitudes, condicionales

Código:
"""
def validar_contraseña(password):
    """
    Valida contraseña:
    - Mínimo 8 caracteres
    - Al menos una mayúscula
    - Al menos un número
    """
    errores = []
    
    if len(password) < 8:
        errores.append("Mínimo 8 caracteres")
    
    if not any(c.isupper() for c in password):
        errores.append("Al menos una mayúscula")
    
    if not any(c.isdigit() for c in password):
        errores.append("Al menos un número")
    
    if errores:
        return False, errores
    return True, ["Contraseña válida"]

# Pruebas
print(validar_contraseña("abc"))  # Inválida
print(validar_contraseña("Password1"))  # Válida

"""
────────────────────────────────
EJERCICIO 55 - GENERADOR DE NÚMEROS PRIMOS
────────────────────────────────
Descripción: Verifica si un número es primo.

Concepto: Números primos (solo divisibles por 1 y ellos mismos)

Código:
"""
def es_primo(n):
    """Verifica si n es número primo"""
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Pruebas
for i in range(1, 20):
    if es_primo(i):
        print(i, end=" ")
print()  # 2 3 5 7 11 13 17 19

# Listar primos en rango
def primos_hasta(n):
    return [i for i in range(2, n+1) if es_primo(i)]

print(primos_hasta(30))

"""
────────────────────────────────
EJERCICIO 56 - TABLA DE MULTIPLICAR
────────────────────────────────
Descripción: Genera la tabla de multiplicar de un número.

Concepto: Bucles for y range

Código:
"""
def tabla_multiplicar(numero, hasta=10):
    """Muestra la tabla de multiplicar"""
    print(f"Tabla del {numero}:")
    for i in range(1, hasta + 1):
        print(f"{numero} x {i} = {numero * i}")

tabla_multiplicar(5)
print()
tabla_multiplicar(7, 12)

"""
────────────────────────────────
EJERCICIO 57 - CONTADOR DE PALABRAS
────────────────────────────────
Descripción: Cuenta palabras y caracteres en un texto.

Concepto: Métodos de strings, split, len

Código:
"""
def analizar_texto(texto):
    """Analiza un texto y devuelve estadísticas"""
    palabras = texto.split()
    
    return {
        "palabras": len(palabras),
        "caracteres": len(texto),
        "caracteres_sin_espacios": len(texto.replace(" ", "")),
        "oraciones": texto.count(".") + texto.count("!") + texto.count("?"),
        "palabra_mas_larga": max(palabras, key=len) if palabras else ""
    }

# Prueba
texto = "Python es un lenguaje de programación increíble."
resultado = analizar_texto(texto)
print(resultado)

"""
────────────────────────────────
EJERCICIO 58 - FIBONACCI
────────────────────────────────
Descripción: Genera la serie de Fibonacci.

Concepto: Sucesión donde cada número es la suma de los dos anteriores

Código:
"""
def fibonacci(n):
    """Retorna lista con n números de Fibonacci"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    serie = [0, 1]
    while len(serie) < n:
        serie.append(serie[-1] + serie[-2])
    
    return serie

print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Versión recursiva
def fib_recursivo(n):
    if n <= 1:
        return n
    return fib_recursivo(n-1) + fib_recursivo(n-2)

print([fib_recursivo(i) for i in range(10)])

"""
────────────────────────────────
EJERCICIO 59 - INVERTIR CADENA
────────────────────────────────
Descripción: Invierte una cadena de texto.

Concepto: Strings, slicing, bucles

Código:
"""
# Método 1: slicing
def invertir_cadena(cadena):
    return cadena[::-1]

print(invertir_cadena("Python"))  # nohtyP

# Método 2: reversed
def invertir_reversed(cadena):
    return "".join(reversed(cadena))

print(invertir_reversed("Hola"))  # aloH

# Método 3: bucle
def invertir_bucle(cadena):
    invertida = ""
    for letra in cadena:
        invertida = letra + invertida
    return invertida

print(invertir_bucle("Mundo"))  # odnuM

"""
────────────────────────────────
EJERCICIO 60 - DETECTOR DE PALÍNDROMOS
────────────────────────────────
Descripción: Verifica si una palabra es un palíndromo.

Concepto: Palabras que se leen igual al derecho y al revés

Código:
"""
def es_palindromo(palabra):
    """Verifica si una palabra es palíndromo"""
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

# Pruebas
print(es_palindromo("radar"))      # True
print(es_palindromo("python"))    # False
print(es_palindromo("A man a plan a canal Panama"))  # True

# Versión con comparación de índices
def es_palindromo_indices(palabra):
    palabra = palabra.lower().replace(" ", "")
    izquierda = 0
    derecha = len(palabra) - 1
    
    while izquierda < derecha:
        if palabra[izquierda] != palabra[derecha]:
            return False
        izquierda += 1
        derecha -= 1
    return True

print(es_palindromo_indices("radar"))

# ============================================================
#        EJERCICIOS 61-100: MÁS PRÁCTICA
# ============================================================

"""
────────────────────────────────
EJERCICIO 61 - FACTORIAL
────────────────────────────────
Descripción: Calcula el factorial de un número.

Concepto: n! = n * (n-1) * (n-2) * ... * 1

Código:
"""
def factorial(n):
    """Calcula el factorial de n"""
    if n < 0:
        return "Error: número negativo"
    if n <= 1:
        return 1
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

print(factorial(5))   # 120
print(factorial(0))   # 1
print(factorial(10))  # 3628800

# Versión recursiva
def factorial_recursivo(n):
    if n < 0:
        return "Error"
    if n <= 1:
        return 1
    return n * factorial_recursivo(n - 1)

print(factorial_recursivo(5))  # 120

"""
────────────────────────────────
EJERCICIO 62 - SUMA DE DÍGITOS
────────────────────────────────
Descripción: Suma todos los dígitos de un número.

Concepto: Conversión a string o operaciones matemáticas

Código:
"""
def suma_digitos(numero):
    """Suma los dígitos de un número"""
    return sum(int(d) for d in str(abs(numero)))

print(suma_digitos(12345))   # 15
print(suma_digitos(999))      # 27
print(suma_digitos(100))     # 1

# Versión sin convertir a string
def suma_digitos_mat(numero):
    suma = 0
    numero = abs(numero)
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma

print(suma_digitos_mat(12345))  # 15

"""
────────────────────────────────
EJERCICIO 63 - NÚMERO MÁGICO
────────────────────────────────
Descripción: Encuentra un número que elevados a sus dígitos suman el número.

Concepto: Números que son suma de sus dígitos elevados a una potencia

Código:
"""
def encontrar_magicos(hasta):
    """Encuentra números que son suma de sus dígitos elevados al número de dígitos"""
    resultados = []
    
    for num in range(1, hasta + 1):
        num_str = str(num)
        suma = sum(int(d) ** len(num_str) for d in num_str)
        if suma == num:
            resultados.append(num)
    
    return resultados

print(encontrar_magicos(1000))  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407

"""
────────────────────────────────
EJERCICIO 64 - APLANAR LISTA
────────────────────────────────
Descripción: Convierte una lista de listas en una lista plana.

Concepto: List comprehension, iterables anidados

Código:
"""
# Con list comprehension
def aplanar(lista):
    return [item for sublist in lista for item in sublist]

matriz = [[1, 2], [3, 4], [5, 6]]
print(aplanar(matriz))  # [1, 2, 3, 4, 5, 6]

# Versión que maneja cualquier nivel de anidación
def aplanar_profundo(lista):
    resultado = []
    for item in lista:
        if isinstance(item, list):
            resultado.extend(aplanar_profundo(item))
        else:
            resultado.append(item)
    return resultado

matriz_anidada = [1, [2, [3, [4, [5]]]]]
print(aplanar_profundo(matriz_anidada))  # [1, 2, 3, 4, 5]

"""
────────────────────────────────
EJERCICIO 65 - ELIMINAR DUPLICADOS
────────────────────────────────
Descripción: Elimina elementos duplicados manteniendo orden.

Concepto: Sets, diccionarios (mantienen orden desde Python 3.7)

Código:
"""
def eliminar_duplicados(lista):
    """Elimina duplicados manteniendo el orden"""
    seen = set()
    resultado = []
    for item in lista:
        if item not in seen:
            seen.add(item)
            resultado.append(item)
    return resultado

numeros = [1, 2, 2, 3, 1, 4, 3, 5]
print(eliminar_duplicados(numeros))  # [1, 2, 3, 4, 5]

# Método simple con dict (mantiene orden desde Python 3.7)
def eliminar_duplicados_dict(lista):
    return list(dict.fromkeys(lista))

print(eliminar_duplicados_dict(numeros))

"""
────────────────────────────────
EJERCICIO 66 - PROMEDIO DE LISTA
────────────────────────────────
Descripción: Calcula el promedio de una lista de números.

Concepto: Funciones integradas sum(), len()

Código:
"""
def promedio(lista):
    """Calcula el promedio de una lista"""
    if not lista:
        return 0
    return sum(lista) / len(lista)

numeros = [10, 20, 30, 40, 50]
print(promedio(numeros))  # 30.0

# Promedio ponderado
def promedio_ponderado(valores, pesos):
    return sum(v * p for v, p in zip(valores, pesos)) / sum(pesos)

notas = [85, 90, 78]
pesos = [0.3, 0.5, 0.2]
print(promedio_ponderado(notas, pesos))  # 86.1

"""
────────────────────────────────
EJERCICIO 67 - ORDENAR LISTA MANUALMENTE
────────────────────────────────
Descripción: Implementa algoritmos de ordenamiento.

Concepto: Burbuja, selección, inserción

Código:
"""
# Ordenamiento Burbuja
def burbuja(lista):
    """Ordena lista usando bubble sort"""
    n = len(lista)
    lista = lista.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista

print(burbuja([64, 34, 25, 12, 22, 11, 90]))

# Ordenamiento por Selección
def seleccion(lista):
    lista = lista.copy()
    n = len(lista)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    
    return lista

print(seleccion([64, 25, 12, 22, 11]))

"""
────────────────────────────────
EJERCICIO 68 - NÚMEROS AMIGOS
────────────────────────────────
Descripción: Encuentra números amigos.

Concepto: Dos números son amigos si la suma de divisores de uno equals al otro

Código:
"""
def suma_divisores(n):
    """Suma los divisores propios de n"""
    suma = 1  # 1 siempre es divisor propio
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            suma += i
            if i != n // i:
                suma += n // i
    return suma

def son_amigos(a, b):
    """Verifica si dos números son amigos"""
    return suma_divisores(a) == b and suma_divisores(b) == a

print(son_amigos(220, 284))  # True (números amigos clásicos)
print(son_amigos(1184, 1210))  # True

# Encontrar amigos en rango
def encontrar_amigos(hasta):
    amigos = []
    for a in range(2, hasta):
        b = suma_divisores(a)
        if b > a and b <= hasta and son_amigos(a, b):
            amigos.append((a, b))
    return amigos

print(encontrar_amigos(2000))

"""
────────────────────────────────
EJERCICIO 69 - GENERADOR DE CONTRASEÑAS
────────────────────────────────
Descripción: Genera contraseñas aleatorias seguras.

Concepto: Módulo random, strings, elección aleatoria

Código:
"""
import random
import string

def generar_contraseña(longitud=12, mayusculas=True, numeros=True, especiales=True):
    """Genera una contraseña aleatoria segura"""
    
    # Caracteres base
    caracteres = string.ascii_lowercase
    
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if especiales:
        caracteres += string.punctuation
    
    # Generar contraseña
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    # Asegurar que tenga al menos un carácter de cada tipo
    if mayusculas and not any(c.isupper() for c in contraseña):
        contraseña = random.choice(string.ascii_uppercase) + contraseña[1:]
    if numeros and not any(c.isdigit() for c in contraseña):
        contraseña = random.choice(string.digits) + contraseña[1:]
    if especiales and not any(c in string.punctuation for c in contraseña):
        contraseña = random.choice(string.punctuation) + contraseña[1:]
    
    return contraseña

print(generar_contraseña(16))

# Versión con símbolospersonalizables
def generar_contraseña_personal(personal, longitud=12):
    return ''.join(random.choice(personal) for _ in range(longitud))

caracteres_personal = string.ascii_letters + string.digits
print(generar_contraseña_personal(caracteres_personal, 10))

"""
────────────────────────────────
EJERCICIO 70 - VALIDADOR DE EMAIL
────────────────────────────────
Descripción: Verifica si un email tiene formato válido.

Concepto: Expresiones regulares básicas, strings

Código:
"""
def validar_email(email):
    """Valida formato básico de email"""
    
    # Verificar elementos básicos
    if not email or "@" not in email:
        return False
    
    partes = email.split("@")
    if len(partes) != 2:
        return False
    
    usuario, dominio = partes
    
    # Usuario no vacío
    if not usuario:
        return False
    
    # Dominio debe tener punto
    if "." not in dominio:
        return False
    
    # No debe empezar o terminar con punto
    if dominio.startswith(".") or dominio.endswith("."):
        return False
    
    return True

# Pruebas
emails = ["juan@gmail.com", "juan@.com", "@gmail.com", "juan", "juan@dominio.es"]
for email in emails:
    print(f"{email}: {validar_email(email)}")

"""
────────────────────────────────
EJERCICIO 71 - JUEGO DE ADIVINAR NÚMERO
────────────────────────────────
Descripción: Crea un juego donde el usuario debe adivinar un número.

Concepto: Bucles, condicionales, random, entrada/salida

Código:
"""
import random

def juego_adivinar():
    """Juego de adivinar el número"""
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 10
    
    print("=== ADIVINA EL NÚMERO ===")
    print("Estoy pensando en un número entre 1 y 100")
    print(f"Tienes {max_intentos} intentos\n")
    
    while intentos < max_intentos:
        try:
            guess = int(input(f"Intento {intentos + 1}: "))
            intentos += 1
            
            if guess < numero_secreto:
                print("Más alto...")
            elif guess > numero_secreto:
                print("Más bajo...")
            else:
                print(f"¡Felicidades! Adivinaste en {intentos} intentos")
                return True
                
        except ValueError:
            print("Por favor, ingresa un número válido")
    
    print(f"Perdiste. El número era {numero_secreto}")
    return False

# Descomenta para jugar:
# juego_adivinar()

print("Juego creado - llama a juego_adivinar() para jugar")

"""
────────────────────────────────
EJERCICIO 72 - CALCULADORA DE IMC
────────────────────────────────
Descripción: Calcula el Índice de Masa Corporal.

Concepto: Fórmula IMC = peso / altura², clasificación de resultados

Código:
"""
def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal
    peso en kg, altura en metros
    """
    if altura <= 0 or peso <= 0:
        return None, "Valores inválidos"
    
    imc = peso / (altura ** 2)
    
    # Clasificación OMS
    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif imc < 25:
        clasificacion = "Peso normal"
    elif imc < 30:
        clasificador = "Sobrepeso"
    else:
        clasificacion = "Obesidad"
    
    return imc, clasificacion

# Pruebas
resultado = calcular_imc(70, 1.75)
print(f"IMC: {resultado[0]:.2f} - {resultado[1]}")

resultado = calcular_imc(90, 1.70)
print(f"IMC: {resultado[0]:.2f} - {resultado[1]}")

"""
────────────────────────────────
EJERCICIO 73 - CONVERSOR DE MONEDAS
────────────────────────────────
Descripción: Convierte entre diferentes monedas.

Concepto: Diccionarios, tasas de cambio, funciones

Código:
"""
tasas = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 149.50,
    "MXN": 17.15,
    "PEN": 3.75
}

def convertir(monto, desde, hacia):
    """Convierte monto de una moneda a otra"""
    if desde not in tasas or hacia not in tasas:
        return None, "Moneda no válida"
    
    # Convertir a USD primero, luego a la moneda destino
    monto_usd = monto / tasas[desde]
    resultado = monto_usd * tasas[hacia]
    
    return resultado

# Ejemplos
print(f"100 USD = {convertir(100, 'USD', 'EUR')[0]:.2f} EUR")
print(f"100 EUR = {convertir(100, 'EUR', 'USD')[0]:.2f} USD")
print(f"1000 PEN = {convertir(1000, 'PEN', 'USD')[0]:.2f} USD")

# Función para mostrar todas las conversiones
def convertir_todas(monto, desde):
    print(f"\n{monto} {desde} equivalen a:")
    for moneda, tasa in tasas.items():
        if moneda != desde:
            resultado = convertir(monto, desde, moneda)[0]
            print(f"  {resultado:.2f} {moneda}")

convertir_todas(100, "USD")

"""
────────────────────────────────
EJERCICIO 74 - GENERADOR DE SEUDOALEATORIOS
────────────────────────────────
Descripción: Implementa un generador de números pseudoaleatorios simple.

Concepto: Algoritmo de generación de números aleatorios

Código:
"""
class GeneradorAleatorio:
    """Generador lineal congruencial simple"""
    
    def __init__(self, semilla=None):
        if semilla is None:
            import time
            self.estado = int(time.time() * 1000) % 1000000
        else:
            self.estado = semilla
    
    def random(self):
        """Retorna número entre 0 y 1"""
        # Parámetros del algoritmo LCG
        self.estado = (self.estado * 1103515245 + 12345) % 2**31
        return self.estado / 2**31
    
    def randint(self, a, b):
        """Retorna entero entre a y b (inclusive)"""
        return int(a + self.random() * (b - a))
    
    def choice(self, secuencia):
        """Retorna elemento aleatorio de secuencia"""
        return secuencia[self.randint(0, len(secuencia) - 1)]
    
    def shuffle(self, lista):
        """Mezcla lista in-place"""
        for i in range(len(lista) - 1, 0, -1):
            j = self.randint(0, i)
            lista[i], lista[j] = lista[j], lista[i]

# Uso
gen = GeneradorAleatorio(42)
print([gen.random() for _ in range(5)])
print(gen.randint(1, 10))
print(gen.choice(["a", "b", "c"]))

"""
────────────────────────────────
EJERCICIO 75 - CIFRADO CÉSAR
────────────────────────────────
Descripción: Implementa el cifrado César para encriptar mensajes.

Concepto: Cifrado por desplazamiento de caracteres

Código:
"""
def cifrar_cesar(texto, desplazamiento):
    """Cifra texto usando el cifrado César"""
    resultado = ""
    
    for char in texto:
        if char.isalpha():
            # Determinar si es mayúscula o minúscula
            codigo_base = ord('A') if char.isupper() else ord('a')
            
            # Desplazar carácter
            nuevo_codigo = (ord(char) - codigo_base + desplazamiento) % 26
            resultado += chr(codigo_base + nuevo_codigo)
        else:
            resultado += char
    
    return resultado

def descifrar_cesar(texto, desplazamiento):
    """Descifra texto cifrado con César"""
    return cifrar_cesar(texto, -desplazamiento)

# Pruebas
mensaje = "HOLA MUNDO"
cifrado = cifrar_cesar(mensaje, 3)
descifrado = descifrar_cesar(cifrado, 3)

print(f"Original: {mensaje}")
print(f"Cifrado: {cifrado}")
print(f"Descifrado: {descifrado}")

# Descifrar por fuerza bruta
print("\nAnálisis de fuerza bruta:")
for i in range(26):
    print(f"Desplazamiento {i}: {descifrar_cesar(cifrado, i)}")

"""
────────────────────────────────
EJERCICIO 76 - MANEJO DE ERRORES BÁSICO
────────────────────────────────
Descripción: Usa try-except para manejar errores.

Concepto: Manejo de excepciones en Python

Código:
"""
def dividir_seguro(a, b):
    """Divide dos números manejando errores"""
    try:
        resultado = a / b
        return resultado, None
    except ZeroDivisionError:
        return None, "Error: No se puede dividir por cero"
    except TypeError:
        return None, "Error: Tipos incompatibles"

print(dividir_seguro(10, 2))
print(dividir_seguro(10, 0))

# Try-except más completo
def procesar_numero(valor):
    try:
        numero = int(valor)
        return numero * 2
    except ValueError:
        return "Error: No es un número válido"

print(procesar_numero(10))
print(procesar_numero("texto"))

# Finally
def ejemplo_finally():
    try:
        print("Intentando...")
        resultado = 10 / 2
    except ZeroDivisionError:
        print("Error")
    finally:
        print("Esto siempre se ejecuta")

ejemplo_finally()

"""
────────────────────────────────
EJERCICIO 77 - MANEJO DE ARCHIVOS BÁSICO
────────────────────────────────
Descripción: Lee y escribe archivos.

Concepto: open(), read(), write(), close()

Código:
"""
# Escribir en archivo
def escribir_archivo(nombre, contenido):
    """Escribe contenido en un archivo"""
    with open(nombre, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)
    return "Archivo escrito exitosamente"

# Leer archivo
def leer_archivo(nombre):
    """Lee el contenido de un archivo"""
    with open(nombre, 'r', encoding='utf-8') as archivo:
        return archivo.read()

# Ejemplo de uso
escribir_archivo("ejemplo.txt", "Hola, este es un archivo de prueba.\nSegunda línea.")
contenido = leer_archivo("ejemplo.txt")
print(contenido)

# Añadir contenido
def añadir_archivo(nombre, contenido):
    with open(nombre, 'a', encoding='utf-8') as archivo:
        archivo.write(contenido)

añadir_archivo("\nNueva línea añadida")
print(leer_archivo("ejemplo.txt"))

# Leer líneas
def leer_lineas(nombre):
    with open(nombre, 'r', encoding='utf-8') as archivo:
        return archivo.readlines()

print(leer_lineas("ejemplo.txt"))

"""
────────────────────────────────
EJERCICIO 78 - CONTADOR DE FRECUENCIA
────────────────────────────────
Descripción: Cuenta la frecuencia de cada elemento.

Concepto: Diccionarios, iteración

Código:
"""
def frecuencia_elementos(lista):
    """Cuenta frecuencia de cada elemento"""
    freq = {}
    for elemento in lista:
        if elemento in freq:
            freq[elemento] += 1
        else:
            freq[elemento] = 1
    return freq

# Versión con defaultdict
from collections import defaultdict

def frecuencia_dict(lista):
    freq = defaultdict(int)
    for elemento in lista:
        freq[elemento] += 1
    return dict(freq)

# Pruebas
palabras = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print(frecuencia_elementos(palabras))
print(frecuencia_dict(palabras))

# Con Counter
from collections import Counter
print(Counter(palabras))

# Encontrar más frecuente
def mas_frecuente(lista):
    freq = Counter(lista)
    return freq.most_common(1)[0]

print(mas_frecuente(palabras))

"""
────────────────────────────────
EJERCICIO 79 - FUSIÓN DE DICCIONARIOS
────────────────────────────────
Descripción: Combina múltiples diccionarios.

Concepto: Dict comprehension, merge de diccionarios

Código:
"""
# Fusionar diccionarios
def fusionar_diccionarios(*diccionarios):
    """Fusiona múltiples diccionarios"""
    resultado = {}
    for d in diccionarios:
        resultado.update(d)
    return resultado

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {"e": 5}

print(fusionar_diccionarios(d1, d2, d3))

# Fusionar sumando valores de claves repetidas
def fusionar_sumar(*diccionarios):
    resultado = {}
    for d in diccionarios:
        for clave, valor in d.items():
            resultado[clave] = resultado.get(clave, 0) + valor
    return resultado

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(fusionar_sumar(d1, d2))  # {'a': 1, 'b': 5, 'c': 4}

# Con ChainMap (Python 3)
from collections import ChainMap
print(dict(ChainMap(d1, d2)))

"""
────────────────────────────────
EJERCICIO 80 - DICCIONARIO INVERTIDO
────────────────────────────────
Descripción: Invierte las claves y valores de un diccionario.

Concepto: Dict comprehension, manejo de valores duplicados

Código:
"""
def invertir_diccionario(diccionario):
    """Invierte claves y valores"""
    return {v: k for k, v in diccionario.items()}

d = {"a": 1, "b": 2, "c": 3}
print(invertir_diccionario(d))  # {1: 'a', 2: 'b', 3: 'c'}

# Versión que maneja valores duplicados (retorna lista de claves)
def inverter_multi(diccionario):
    invertido = {}
    for clave, valor in diccionario.items():
        if valor in invertido:
            invertido[valor].append(clave)
        else:
            invertido[valor] = [clave]
    return invertido

d2 = {"a": 1, "b": 1, "c": 2}
print(inverter_multi(d2))  # {1: ['a', 'b'], 2: ['c']}

# Con defaultdict
from collections import defaultdict

def inverter_default(diccionario):
    invertido = defaultdict(list)
    for clave, valor in diccionario.items():
        invertido[valor].append(clave)
    return dict(invertido)

print(inverter_default(d2))

# ============================================================
#        EJERCICIOS 81-120: NIVEL INTERMEDIO - PARTE 1
# ============================================================

"""
────────────────────────────────
EJERCICIO 81 - DICCIONARIO DE COMPRENSIÓN
────────────────────────────────
Descripción: Crea diccionarios de forma concisa.

Concepto: Dict comprehension: {k: v for item in iterable}

Código:
"""
# Básico
cuadrados = {i: i**2 for i in range(5)}
print(cuadrados)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Con condición
pares = {i: i**2 for i in range(10) if i % 2 == 0}
print(pares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Invertir diccionario
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
print(invertido)  # {1: 'a', 2: 'b', 3: 'c'}

# Desde lista de tuplas
pares = [("a", 1), ("b", 2), ("c", 3)]
diccionario = dict(pares)
print(diccionario)

# Filtrar diccionario
productos = {"manzana": 50, "banano": 30, "naranja": 80, "uva": 120}
caros = {k: v for k, v in productos.items() if v > 60}
print(caros)  # {'naranja': 80, 'uva': 120}

"""
────────────────────────────────
EJERCICIO 82 - SET COMPREHENSION
────────────────────────────────
Descripción: Crea conjuntos de forma concisa.

Concepto: {expresion for item in iterable}

Código:
"""
# Básico
cuadrados = {x**2 for x in range(5)}
print(cuadrados)  # {0, 1, 4, 9, 16}

# Eliminar duplicados
numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unicos = {x for x in numeros}
print(unicos)  # {1, 2, 3, 4}

# Con transformación
palabras = ["hola", "mundo", "python"]
primera_letra = {palabra[0] for palabra in palabras}
print(primera_letra)  # {'h', 'm', 'p'}

# Con condición
pares = {x for x in range(20) if x % 2 == 0}
print(pares)

"""
────────────────────────────────
EJERCICIO 83 - FILTER Y MAP CON FUNCIONES
────────────────────────────────
Descripción: Usa filter() y map() con funciones.

Concepto: filter(funcion, iterable) - filtra según función
         map(funcion, iterable) - transforma cada elemento

Código:
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter - solo pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]

# Map - duplicar
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Combinar filter y map
# Primero filtrar, luego transformar
resultado = list(map(lambda x: x ** 2, filter(lambda x: x > 5, numeros)))
print(resultado)  # [36, 49, 64, 81, 100]

# Con funciones nombradas
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = list(filter(es_primo, range(1, 30)))
print(primos)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

"""
────────────────────────────────
EJERCICIO 84 - REDUCE
────────────────────────────────
Descripción: Reduce un iterable a un solo valor.

Concepto: reduce(funcion, iterable, inicial) acumula valores

Código:
"""
from functools import reduce

numeros = [1, 2, 3, 4, 5]

# Sumar todos
total = reduce(lambda acc, x: acc + x, numeros)
print(total)  # 15

# Equivalente a sum()
print(sum(numeros))

# Producto
producto = reduce(lambda acc, x: acc * x, numeros, 1)
print(producto)  # 120

# Máximo
maximo = reduce(lambda acc, x: acc if acc > x else x, numeros)
print(maximo)  # 5

# Concatenar strings
palabras = ["Hola", " ", "Mundo", "!"]
frase = reduce(lambda acc, x: acc + x, palabras)
print(frase)  # "Hola Mundo!"

# ============================================================
#        CONTINÚA EN ARCHIVO SIGUIENTE...
# ============================================================
