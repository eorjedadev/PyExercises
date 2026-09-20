# ============================================================
# 300 PROBLEMAS PARA PRACTICAR LÓGICA Y ALGORITMOS EN PYTHON
# ============================================================
#
# Estos problemas están diseñados para que desarrolles tu capacidad
# de análisis y resolución de problemas algorítmicos.
#
# NO INCLUYE SOLUCIONES - ¡RESUÉLVELOS POR TU CUENTA!
#
# Niveles:
# - BÁSICO (1-100): Variables, condicionales, bucles
# - INTERMEDIO (101-200): Funciones, estructuras de datos, recursion
# - AVANZADO (201-300): Algoritmos complejos, POO, optimización
#
# ============================================================

# ═══════════════════════════════════════════════════════════════════
#                           NIVEL BÁSICO (1-100)
# ═══════════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Variables y Operadores
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 1 - INTERCAMBIO DE VALORES
────────────────────────────────────
Descripción: Sin usar variables auxiliares, intercambia los valores 
de dos variables 'a' y 'b' que contienen números enteros.

Entrada: a = 5, b = 10
Salida esperada: a = 10, b = 5
"""
a = 5
b = 10

print(f'Intercambio antes: a={a}, b={b}')
"""
PROBLEMA 2 - CONVERSIÓN DE TEMPERATURAS
────────────────────────────────────
Descripción: Convierte una temperatura de Celsius a Fahrenheit y Kelvin.
La fórmula es: F = C × 9/5 + 32, K = C + 273.15

Entrada: 25°C
Salida esperada: 77.0°F, 298.15K
"""
celsius = 25
fahrenheit = celsius * 9/5 + 32
kelvin = celsius + 273.15

print(f'{fahrenheit}°F, {kelvin}K')
"""
PROBLEMA 3 - ÁREA Y PERÍMETRO
────────────────────────────────────
Descripción: Calcula el área y perímetro de un rectángulo dados 
sus lados.

Entrada: lado1 = 5, lado2 = 3
Salida esperada: Área = 15, Perímetro = 16

"""
lado1 = 5
lado2 = 3

area = lado1 * lado2
perimetro = 2 (lado1 + lado2)
"""
PROBLEMA 4 - CIFRA SIGNIFICATIVA
────────────────────────────────────
Descripción: Extrae la tercera cifra significativa de un número 
entero positivo (de izquierda a derecha).

Entrada: 45892
Salida esperada: 8
"""
cifra = 45892
cifra_str = str(cifra)
if len(cifra_str) >= 3:
    tercera_cifra = cifra_str[2]
    print(f'La tercera cifra significativa es: {tercera_cifra}')
else:
    print('El número no tiene una tercera cifra significativa')

"""
PROBLEMA 5 - NÚMERO INVERTIDO
────────────────────────────────────
Descripción: Invierte un número de tres dígitos.

Entrada: 123
Salida esperada: 321
"""
numero_invertido = 123
numero_invertido_str = str(numero_invertido)
if len(numero_invertido_str) == 3:
    invertido = numero_invertido_str[::-1]
    print(f'El número invertido es: {invertido}')
else:
    print('El número no tiene tres dígitos')

"""
PROBLEMA 6 - SUMA DE DÍGITOS
────────────────────────────────────
Descripción: Calcula la suma de todos los dígitos de un número.

Entrada: 12345
Salida esperada: 15
"""
numeros = 12345
numeros_str = str(numeros)
suma_digitos = sum(int(digito) for digito in numeros_str)
print(f'La suma de los dígitos es: {suma_digitos}')
"""
PROBLEMA 7 - DÍGITO MAYOR
────────────────────────────────────
Descripción: Encuentra el dígito mayor de un número.

Entrada: 983
Salida esperada: 9
"""
numero_mayor = 983
numero_mayor_str = str(numero_mayor)
digito_mayor = max(int(digito) for digito in numero_mayor_str)
print(f'El dígito mayor es: {digito_mayor}')

"""
PROBLEMA 8 - OPERACIONES MÚLTIPLES
────────────────────────────────────
Descripción: Dados tres números, calcula: suma, producto, 
promedio y resta del primero menos la suma de los otros dos.

Entrada: a=8, b=3, c=5
Salida esperada: Suma=16, Producto=120, Promedio=5.33, Resta=-2
"""

"""
PROBLEMA 9 - DISTANCIA EUCLIDIANA
────────────────────────────────────
Descripción: Calcula la distancia entre dos puntos (x1,y1) y (x2,y2)
usando la fórmula: √((x2-x1)² + (y2-y1)²)

Entrada: (1,2) y (4,6)
Salida esperada: 5.0
"""

"""
PROBLEMA 10 - ECUACIÓN LINEAL
────────────────────────────────────
Descripción: Resuelve una ecuación lineal ax + b = 0

Entrada: a=3, b=-6
Salida esperada: x = 2.0
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Condicionales
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 11 - MAYOR DE TRES
────────────────────────────────────
Descripción: Determina el mayor de tres números.

Entrada: 15, 8, 23
Salida esperada: 23
"""

"""
PROBLEMA 12 - CLASIFICACIÓN DE TRIÁNGULO
────────────────────────────────────
Descripción: Dados tres lados, determina si forma un triángulo 
escaleno, isósceles o equilátero.

Entrada: 3, 4, 5
Salida esperada: "Escaleno"
"""

"""
PROBLEMA 13 - DÍAS DEL MES
────────────────────────────────────
Descripción: Dado un número de mes, retorna la cantidad de días.

Entrada: 2
Salida esperada: 28 (año no bisiesto)
"""

"""
PROBLEMA 14 - CALIFICACIÓN LETRA
────────────────────────────────────
Descripción: Convierte una nota numérica (0-100) a letra.

Entrada: 85
Salida esperada: "B"
(90-100=A, 80-89=B, 70-79=C, 60-69=D, <60=F)
"""

"""
PROBLEMA 15 - AÑO BISIESTO
────────────────────────────────────
Descripción: Determina si un año es bisiesto.

Entrada: 2024
Salida esperada: True
"""

"""
PROBLEMA 16 - NÚMERO PAR O IMPAR
────────────────────────────────────
Descripción: Determina si un número es par, impar o cero.

Entrada: 7
Salida esperada: "Impar"
"""

"""
PROBLEMA 17 - SIGNO ZODIACAL
────────────────────────────────────
Descripción: Determina el signo zodiacal dada la fecha de nacimiento.
(Día y mes)

Entrada: dia=15, mes=8
Salida esperada: "Leo"
"""

"""
PROBLEMA 18 - CATEGORÍA DE EDAD
────────────────────────────────────
Descripción: Clasifica a una persona por su edad.

Entrada: edad=65
Salida esperada: "Adulto Mayor"
(0-12=Niño, 13-17=Adolescente, 18-64=Adulto, 65+=Adulto Mayor)
"""

"""
PROBLEMA 19 - TRIO PITAGÓRICO
────────────────────────────────────
Descripción: Verifica si tres números forman un trío pitagórico.

Entrada: 3, 4, 5
Salida esperada: True
"""

"""
PROBLEMA 20 - RANGO NUMÉRICO
────────────────────────────────────
Descripción: Verifica si un número está en el rango de 1 a 100.

Entrada: 50
Salida esperada: True
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Bucles
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 21 - SUMA HASTA N
────────────────────────────────────
Descripción: Calcula la suma de los números del 1 hasta n.

Entrada: n=5
Salida esperada: 15
"""

"""
PROBLEMA 22 - NÚMEROS PARES
────────────────────────────────────
Descripción: Lista todos los números pares desde 1 hasta n.

Entrada: n=10
Salida esperada: [2, 4, 6, 8, 10]
"""

"""
PROBLEMA 23 - FACTORIAL
────────────────────────────────────
Descripción: Calcula el factorial de un número n.

Entrada: n=5
Salida esperada: 120
"""

"""
PROBLEMA 24 - FIBONACCI
────────────────────────────────────
Descripción: Genera los primeros n números de Fibonacci.

Entrada: n=7
Salida esperada: [0, 1, 1, 2, 3, 5, 8]
"""

"""
PROBLEMA 25 - NÚMEROS PRIMOS
────────────────────────────────────
Descripción: Lista todos los primos hasta n.

Entrada: n=20
Salida esperada: [2, 3, 5, 7, 11, 13, 17, 19]
"""

"""
PROBLEMA 26 - POTENCIAS DE 2
────────────────────────────────────
Descripción: Lista las primeras n potencias de 2.

Entrada: n=5
Salida esperada: [2, 4, 8, 16, 32]
"""

"""
PROBLEMA 27 - SUMA IMPARES
────────────────────────────────────
Descripción: Suma los números impares desde 1 hasta n.

Entrada: n=10
Salida esperada: 25
"""

"""
PROBLEMA 28 - CONTADOR DE DÍGITOS
────────────────────────────────────
Descripción: Cuenta cuántos dígitos tiene un número.

Entrada: 123456
Salida esperada: 6
"""

"""
PROBLEMA 29 - SERIE SUMA
────────────────────────────────────
Descripción: Calcula: 1 + 1/2 + 1/3 + ... + 1/n

Entrada: n=4
Salida esperada: 2.083333333333333
"""

"""
PROBLEMA 30 - PRODUCTO DE RANGO
────────────────────────────────────
Descripción: Calcula el producto de todos los números en un rango.

Entrada: inicio=2, fin=5
Salida esperada: 120 (2×3×4×5)
"""

"""
PROBLEMA 31 - TABLA DE MULTIPLICAR
────────────────────────────────────
Descripción: Genera la tabla de multiplicar del 1 al n.

Entrada: n=3
Salida esperada:
1×1=1, 1×2=2, 1×3=3
2×1=2, 2×2=4, 2×3=6
3×1=3, 3×2=6, 3×3=9
"""

"""
PROBLEMA 32 - PIRÁMIDE DE NÚMEROS
────────────────────────────────────
Descripción: Imprime una pirámide de números.

Entrada: n=5
Salida esperada:
1
12
123
1234
12345
"""

"""
PROBLEMA 33 - NÚMERO CAPICÚA
────────────────────────────────────
Descripción: Verifica si un número es capicúa.

Entrada: 121
Salida esperada: True
"""

"""
PROBLEMA 34 - SUMA DE CUADRADOS
────────────────────────────────────
Descripción: Calcula 1² + 2² + 3² + ... + n²

Entrada: n=4
Salida esperada: 30
"""

"""
PROBLEMA 35 - CONTEO DE CEROS
────────────────────────────────────
Descripción: Cuenta cuántos ceros hay desde 1 hasta n.

Entrada: n=20
Salida esperada: 2 (solo 10 y 20)
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Listas
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 36 - MAYOR Y MENOR
────────────────────────────────────
Descripción: Encuentra el mayor y menor de una lista.

Entrada: [3, 1, 4, 1, 5, 9, 2, 6]
Salida esperada: mayor=9, menor=1
"""

"""
PROBLEMA 37 - PROMEDIO DE LISTA
────────────────────────────────────
Descripción: Calcula el promedio de los números en una lista.

Entrada: [10, 20, 30, 40]
Salida esperada: 25.0
"""

"""
PROBLEMA 38 - ELEMENTOS ÚNICOS
────────────────────────────────────
Descripción: Retorna los elementos sin duplicados.

Entrada: [1, 2, 2, 3, 4, 4, 5]
Salida esperada: [1, 2, 3, 4, 5]
"""

"""
PROBLEMA 39 - INVERTIR LISTA
────────────────────────────────────
Descripción: Invierte una lista sin usar reverse().

Entrada: [1, 2, 3, 4, 5]
Salida esperada: [5, 4, 3, 2, 1]
"""

"""
PROBLEMA 40 - SEGUNDO MAYOR
────────────────────────────────────
Descripción: Encuentra el segundo número mayor.

Entrada: [5, 8, 2, 9, 1]
Salida esperada: 8
"""

"""
PROBLEMA 41 - FRECUENCIA DE NÚMEROS
────────────────────────────────────
Descripción: Cuenta la frecuencia de cada número.

Entrada: [1, 2, 2, 3, 3, 3]
Salida esperada: {1:1, 2:2, 3:3}
"""

"""
PROBLEMA 42 - INTERSECCIÓN DE LISTAS
────────────────────────────────────
Descripción: Encuentra los elementos comunes entre dos listas.

Entrada: [1,2,3,4] y [3,4,5,6]
Salida esperada: [3, 4]
"""

"""
PROBLEMA 43 - DIFERENCIA DE LISTAS
────────────────────────────────────
Descripción: Elementos en lista1 pero no en lista2.

Entrada: [1,2,3,4] y [3,4,5,6]
Salida esperada: [1, 2]
"""

"""
PROBLEMA 44 - PALABRAS MÁS LARGAS
────────────────────────────────────
Descripción: Encuentra las n palabras más largas.

Entrada: palabras=["hola", "mundo", "python", "es", "genial"], n=3
Salida esperada: ["python", "mundo", "genial"]
"""

"""
PROBLEMA 45 - APLANAR LISTA
────────────────────────────────────
Descripción: Convierte lista de listas en una sola lista.

Entrada: [[1,2], [3,4], [5]]
Salida esperada: [1, 2, 3, 4, 5]
"""

"""
PROBLEMA 46 - PARES E IMPARES
────────────────────────────────────
Descripción: Separa números pares e impares.

Entrada: [1, 2, 3, 4, 5, 6]
Salida esperada: pares=[2,4,6], impares=[1,3,5]
"""

"""
PROBLEMA 47 - NÚMEROS FALTANTES
────────────────────────────────────
Descripción: Encuentra los números faltantes en un rango.

Entrada: [1, 2, 4, 5]
Salida esperada: [3]
"""

"""
PROBLEMA 48 - SUMA DE LISTAS
────────────────────────────────────
Descripción: Suma elemento a elemento dos listas.

Entrada: [1,2,3] y [4,5,6]
Salida esperada: [5, 7, 9]
"""

"""
PROBLEMA 49 - ORDENAR POR LONGITUD
────────────────────────────────────
Descripción: Ordena palabras por su longitud.

Entrada: ["python", "es", "genial", "编程"]
Salida esperada: ["es", "genial", "python", "编程"]
"""

"""
PROBLEMA 50 - ELIMINAR ELEMENTO
────────────────────────────────────
Descripción: Elimina todas las ocurrencias de un elemento.

Entrada: [1,2,3,2,4,2], elemento=2
Salida esperada: [1, 3, 4]
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Strings
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 51 - CONTAR VOCALES
────────────────────────────────────
Descripción: Cuenta las vocales en un texto.

Entrada: "Hola Mundo"
Salida esperada: 4
"""

"""
PROBLEMA 52 - CONTAR PALABRAS
────────────────────────────────────
Descripción: Cuenta las palabras en un texto.

Entrada: "Hola mundo, soy Python"
Salida esperada: 4
"""

"""
PROBLEMA 53 - MAYÚSCULAS Y MINÚSCULAS
────────────────────────────────────
Descripción: Cuenta mayúsculas y minúsculas.

Entrada: "Hola Mundo"
Salida esperada: mayúsculas=2, minúsculas=7
"""

"""
PROBLEMA 54 - REEMPLAZAR PALABRAS
────────────────────────────────────
Descripción: Reemplaza una palabra por otra.

Entrada: "Hola mundo", buscar="mundo", reemplazar="Python"
Salida esperada: "Hola Python"
"""

"""
PROBLEMA 55 - PRIMERA MAYÚSCULA
────────────────────────────────────
Descripción: Pone la primera letra de cada palabra en mayúscula.

Entrada: "hola mundo python"
Salida esperada: "Hola Mundo Python"
"""

"""
PROBLEMA 56 - SIN ESPACIOS
────────────────────────────────────
Descripción: Elimina espacios en blanco.

Entrada: "  Hola   Mundo  "
Salida esperada: "HolaMundo"
"""

"""
PROBLEMA 57 - DÍGITOS EN TEXTO
────────────────────────────────────
Descripción: Extrae todos los dígitos de un string.

Entrada: "a1b2c3"
Salida esperada: "123"
"""

"""
PROBLEMA 58 - INVERTIR PALABRAS
────────────────────────────────────
Descripción: Invierte el orden de las palabras.

Entrada: "Hola mundo"
Salida esperada: "mundo Hola"
"""

"""
PROBLEMA 59 - PALÍNDROMO
────────────────────────────────────
Descripción: Verifica si una palabra es palíndromo.

Entrada: "radar"
Salida esperada: True
"""

"""
PROBLEMA 60 - ANAGRAMA
────────────────────────────────────
Descripción: Verifica si dos palabras son anagramas.

Entrada: "listen" y "silent"
Salida esperada: True
"""

"""
PROBLEMA 61 - REPETICIONES
────────────────────────────────────
Descripción: Encuentra el carácter que más se repite.

Entrada: "hola mundo"
Salida esperada: "o"
"""

"""
PROBLEMA 62 - REMOVER CARÁCTER
────────────────────────────────────
Descripción: Remueve un carácter específico.

Entrada: "hello", carácter="l"
Salida esperada: "heo"
"""

"""
PROBLEMA 63 - DIVIDIR POR ESPACIOS
────────────────────────────────────
Descripción: Divide texto por espacios y ordena.

Entrada: "gato perro pez loro"
Salida esperada: ["gato", "loro", "perro", "pez"]
"""

"""
PROBLEMA 64 - TEXTO A NÚMERO
────────────────────────────────────
Descripción: Convierte texto con números a entero.

Entrada: "12345"
Salida esperada: 12345
"""

"""
PROBLEMA 65 - CENSURA
────────────────────────────────────
Descripción: Censura palabras de una lista.

Entrada: "Este texto tiene palabras prohibidas", prohibited=["palabras"]
Salida esperada: "Este texto tiene ****
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Diccionarios
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 66 - AGRUPAR POR LETRA
────────────────────────────────────
Descripción: Agrupa palabras por su primera letra.

Entrada: ["apple", "banana", "apricot", "blueberry"]
Salida esperada: {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
"""

"""
PROBLEMA 67 - INVERTIR DICCIONARIO
────────────────────────────────────
Descripción: Invierte claves y valores.

Entrada: {'a': 1, 'b': 2}
Salida esperada: {1: 'a', 2: 'b'}
"""

"""
PROBLEMA 68 - FUSIONAR DICCIONARIOS
────────────────────────────────────
Descripción: Fusiona dos diccionarios, sumando valores de claves repetidas.

Entrada: {'a': 1, 'b': 2} y {'b': 3, 'c': 4}
Salida esperada: {'a': 1, 'b': 5, 'c': 4}
"""

"""
PROBLEMA 69 - DICCIONARIO DESDE LISTAS
────────────────────────────────────
Descripción: Crea diccionario desde dos listas.

Entrada: claves=['a','b','c'], valores=[1,2,3]
Salida esperada: {'a':1, 'b':2, 'c':3}
"""

"""
PROBLEMA 70 - VALORES ÚNICOS
────────────────────────────────────
Descripción: Extrae valores únicos de un diccionario.

Entrada: {'a':1, 'b':2, 'c':1, 'd':3}
Salida esperada: [1, 2, 3]
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas Misceláneos
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 71 - NÚMEROS AMIGOS
────────────────────────────────────
Descripción: Verifica si dos números son amigos.
(Suma de divisores propios de uno equals al otro)

Entrada: 220 y 284
Salida esperada: True
"""

"""
PROBLEMA 72 - NÚMERO PERFECTO
────────────────────────────────────
Descripción: Verifica si un número es perfecto.
(Suma de divisores propios equals al número)

Entrada: 6
Salida esperada: True
"""

"""
PROBLEMA 73 - SERIE DE COLLATZ
────────────────────────────────────
Descripción: Genera la secuencia de Collatz.
(SI par: n/2, si impar: 3n+1)

Entrada: 6
Salida esperada: [6, 3, 10, 5, 16, 8, 4, 2, 1]
"""

"""
PROBLEMA 74 - CONTEO DE MONEDAS
────────────────────────────────────
Descripción: Mínimo número de monedas para una cantidad.
(Monedas: 1, 5, 10, 25)

Entrada: 67
Salida esperada: 6 (25+25+10+5+1+1)
"""

"""
PROBLEMA 75 - TORRES DE HANOI
────────────────────────────────────
Descripción: Resuelve Torres de Hanoi para n discos.

Entrada: n=3
Salida esperada: Movimientos para mover de A a C
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Lógica
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 76 - ADIVINAR NÚMERO
────────────────────────────────────
Descripción: Implementa el juego de adivinar el número.

Entrada: número_secreto=50, intento=55
Salida esperada: "El número es menor"
"""

"""
PROBLEMA 77 - CONTADOR DE MONEDAS
────────────────────────────────────
Descripción: Cuenta cuántas monedas de cada tipo hay.

Entrada: [25, 10, 5, 1, 10, 25, 1]
Salida esperada: {25:2, 10:2, 5:1, 1:2}
"""

"""
PROBLEMA 78 - CIFRADO CÉSAR
────────────────────────────────────
Descripción: Implementa el cifrado César con desplazamiento n.

Entrada: "ABC", desplazamiento=3
Salida esperada: "DEF"
"""

"""
PROBLEMA 79 - VALIDAR CONTRASEÑA
────────────────────────────────────
Descripción: Valida que la contraseña tenga:
- Mínimo 8 caracteres
- Al menos una mayúscula
- Al menos un número
- Al menos un carácter especial

Entrada: "Password1!"
Salida esperada: True
"""

"""
PROBLEMA 80 - JUEGO PIEDRA PAPEL TIJERA
────────────────────────────────────
Descripción: Determina el ganador.

Entrada: jugador="piedra", computadora="tijera"
Salida esperada: "Ganaste"
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Fechas
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 81 - DÍAS ENTRE FECHAS
────────────────────────────────────
Descripción: Calcula los días entre dos fechas.

Entrada: fecha1=2024-01-01, fecha2=2024-01-15
Salida esperada: 14
"""

"""
PROBLEMA 82 - DÍA DE LA SEMANA
────────────────────────────────────
Descripción: Determina el día de la semana.

Entrada: 2024-01-01
Salida esperada: "Lunes"
"""

"""
PROBLEMA 83 - FORMATO DE FECHA
────────────────────────────────────
Descripción: Convierte formato de fecha.

Entrada: 01/15/2024
Salida esperada: 15-01-2024
"""

"""
PROBLEMA 84 - EDAD EXACTA
────────────────────────────────────
Descripción: Calcula edad exacta en años, meses, días.

Entrada: nacimiento=2000-05-15, hoy=2024-01-10
Salida esperada: 23 años, 7 meses, 26 días
"""

"""
PROBLEMA 85 - LUNAR CALENDAR
────────────────────────────────────
Descripción: Determina la fase lunar.

Entrada: fecha=2024-01-15
Salida esperada: "Luna Llena"
"""

"""
PROBLEMA 86 - SEGUNDO A HH:MM:SS
────────────────────────────────────
Descripción: Convierte segundos a formato hora.

Entrada: 3665
Salida esperada: "1:1:5"
"""

"""
PROBLEMA 87 - DÍAS LABORABLES
────────────────────────────────────
Descripción: Cuenta días laborables entre fechas.

Entrada: inicio=2024-01-01, fin=2024-01-31
Salida esperada: 22
"""

"""
PROBLEMA 88 - AÑO FISCAL
────────────────────────────────────
Descripción: Determina el trimestre fiscal.

Entrada: mes=7
Salida esperada: Q2
"""

"""
PROBLEMA 89 - JUEGO DE CRAPS SIMPLE
────────────────────────────────────
Descripción: Simula una ronda de dados.

Entrada: dados=[3, 4]
Salida esperada: "Ganaste" (si suma es 7 u 11)
"""

"""
PROBLEMA 90 - GENERADOR DE CC
────────────────────────────────────
Descripción: Genera un código de verificación simple.

Entrada: "1234"
Salida esperada: "1234-7" (dígito verificador)
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Matemáticas
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 91 - MCM (Mínimo Común Múltiplo)
────────────────────────────────────
Descripción: Calcula el MCM de dos números.

Entrada: 12, 15
Salida esperada: 60
"""

"""
PROBLEMA 92 - MCD (Máximo Común Divisor)
────────────────────────────────────
Descripción: Calcula el MCD usando Euclidean.

Entrada: 48, 18
Salida esperada: 6
"""

"""
PROBLEMA 93 - ES PRIMO
────────────────────────────────────
Descripción: Verifica primalidad de un número.

Entrada: 17
Salida esperada: True
"""

"""
PROBLEMA 94 - NÚMEROS PRIMOS GEMELOS
────────────────────────────────────
Descripción: Encuentra primos gemelos hasta n.

Entrada: n=20
Salida esperada: [(3,5), (5,7), (11,13), (17,19)]
"""

"""
PROBLEMA 95 - FACTORIZACIÓN
────────────────────────────────────
Descripción: Factoriza un número en primos.

Entrada: 12
Salida esperada: [2, 2, 3]
"""

"""
PROBLEMA 96 - RAÍZ CUADRADA
────────────────────────────────────
Descripción: Calcula raíz cuadrada sin usar sqrt().

Entrada: 16
Salida esperada: 4.0
"""

"""
PROBLEMA 97 - LOGARITMO NATURAL
────────────────────────────────────
Descripción: Calcula ln(x) sin funciones externas.

Entrada: 2.718
Salida esperada: aproximadamente 1.0
"""

"""
PROBLEMA 98 - SERIE EXPONENCIAL
────────────────────────────────────
Descripción: Calcula e^x usando serie.

Entrada: x=1, n=10
Salida esperada: aproximadamente 2.71828
"""

"""
PROBLEMA 99 - NÚMERO ARMSTRONG
────────────────────────────────────
Descripción: Verifica si es número de Armstrong.

Entrada: 153
Salida esperada: True (1³+5³+3³=153)
"""

"""
PROBLEMA 100 - MEDIA Y DESVIACIÓN
────────────────────────────────────
Descripción: Calcula media y desviación estándar.

Entrada: [2, 4, 4, 4, 5, 5, 7, 9]
Salida esperada: media=5.0, desviación=2.0
"""

# ═══════════════════════════════════════════════════════════════════
#                    NIVEL INTERMEDIO (101-200)
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 101 - ORDENAMIENTO BURBUJA
────────────────────────────────────
Descripción: Implementa Bubble Sort.

Entrada: [5, 2, 8, 1, 9]
Salida esperada: [1, 2, 5, 8, 9]
"""

"""
PROBLEMA 102 - ORDENAMIENTO SELECCIÓN
────────────────────────────────────
Descripción: Implementa Selection Sort.

Entrada: [64, 25, 12, 22, 11]
Salida esperada: [11, 12, 22, 25, 64]
"""

"""
PROBLEMA 103 - ORDENAMIENTO INSERCIÓN
────────────────────────────────────
Descripción: Implementa Insertion Sort.

Entrada: [12, 11, 13, 5, 6]
Salida esperada: [5, 6, 11, 12, 13]
"""

"""
PROBLEMA 104 - BÚSQUEDA BINARIA
────────────────────────────────────
Descripción: Implementa búsqueda binaria.

Entrada: [1,2,3,4,5,6,7,8,9], objetivo=7
Salida esperada: 6
"""

"""
PROBLEMA 105 - MERGE DE LISTAS ORDENADAS
────────────────────────────────────
Descripción: Fusiona dos listas ordenadas.

Entrada: [1,3,5] y [2,4,6]
Salida esperada: [1, 2, 3, 4, 5, 6]
"""

"""
PROBLEMA 106 - QUICKSORT
────────────────────────────────────
Descripción: Implementa Quick Sort.

Entrada: [10, 7, 8, 9, 1, 5]
Salida esperada: [1, 5, 7, 8, 9, 10]
"""

"""
PROBLEMA 107 - BUSCAR SUBSTRING
────────────────────────────────────
Descripción: Busca un substring sin usar find().

Entrada: "hello world", "world"
Salida esperada: 6
"""

"""
PROBLEMA 108 - STRINGS ROTATIVOS
────────────────────────────────────
Descripción: Verifica si s2 es rotación de s1.

Entrada: "abcde", "cdeab"
Salida esperada: True
"""

"""
PROBLEMA 109 - ÚLTIMA PALABRA
────────────────────────────────────
Descripción: Encuentra la última palabra.

Entrada: "Hola mundo cruel"
Salida esperada: "cruel"
"""

"""
PROBLEMA 110 - COMPRESIÓN DE STRING
────────────────────────────────────
Descripción: Comprime caracteres repetidos.

Entrada: "aabbbcccc"
Salida esperada: "a2b3c4"
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Funciones
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 111 - FIBONACCI RECURSIVO
────────────────────────────────────
Descripción: Implementa Fibonacci con recursión.

Entrada: n=10
Salida esperada: 55
"""

"""
PROBLEMA 112 - SUMA RECURSIVA
────────────────────────────────────
Descripción: Suma números recursivamente.

Entrada: n=5
Salida esperada: 15
"""

"""
PROBLEMA 113 - INVERTIR RECURSIVO
────────────────────────────────────
Descripción: Invierte string recursivamente.

Entrada: "python"
Salida esperada: "nohtyp"
"""

"""
PROBLEMA 114 - CONTAR RECURSIVO
────────────────────────────────────
Descripción: Cuenta elementos recursivamente.

Entrada: [1,2,3,4,5]
Salida esperada: 5
"""

"""
PROBLEMA 115 - POTENCIA RECURSIVA
────────────────────────────────────
Descripción: Calcula potencia recursivamente.

Entrada: base=2, exponente=10
Salida esperada: 1024
"""

"""
PROBLEMA 116 - BACKSPACE STRING
────────────────────────────────────
Descripción: Procesa string con backspaces.

Entrada: "ab#c", "ad#c"
Salida esperada: "True" (ambos resultan en "ac")
"""

"""
PROBLEMA 117 - EXPRESIÓN EQUILIBRADA
────────────────────────────────────
Descripción: Verifica paréntesis equilibrados.

Entrada: "({[]})"
Salida esperada: True
"""

"""
PROBLEMA 118 - PODER DE 2
────────────────────────────────────
Descripción: Verifica si n es potencia de 2.

Entrada: 16
Salida esperada: True
"""

"""
PROBLEMA 119 - SUMA DE RANGO
────────────────────────────────────
Descripción: Suma desde left hasta right.

Entrada: left=3, right=7
Salida esperada: 22
"""

"""
PROBLEMA 120 - CONTAR BITS
────────────────────────────────────
Descripción: Cuenta bits en 1 de un número.

Entrada: 11 (1011 en binario)
Salida esperada: 3
"""

"""
PROBLEMA 121 - NÚMERO A BINARY
────────────────────────────────────
Descripción: Convierte número a binario como string.

Entrada: 5
Salida esperada: "101"
"""

"""
PROBLEMA 122 - SUMA DE ARRAYS
────────────────────────────────────
Descripción: Suma arrays elemento a elemento.

Entrada: nums1=[1,2,3], nums2=[4,5,6]
Salida esperada: [5, 7, 9]
"""

"""
PROBLEMA 123 - PRODUCTO EXCEPTO ÉL
────────────────────────────────────
Descripción: Producto de todos menos el actual.

Entrada: [1,2,3,4]
Salida esperada: [24, 12, 8, 6]
"""

"""
PROBLEMA 124 - MÁXIMO SUBARRAY
────────────────────────────────────
Descripción: Encuentra suma máxima de subarray (Kadane).

Entrada: [-2,1,-3,4,-1,2,1,-5,4]
Salida esperada: 6 (subarray [4,-1,2,1])
"""

"""
PROBLEMA 125 - ELEMENTO MAYORITARIO
────────────────────────────────────
Descripción: Encuentra elemento que aparece > n/2 veces.

Entrada: [3,2,3]
Salida esperada: 3
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Matrices
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 126 - SUMA DE MATRIZ
────────────────────────────────────
Descripción: Suma todos los elementos de una matriz.

Entrada: [[1,2,3],[4,5,6],[7,8,9]]
Salida esperada: 45
"""

"""
PROBLEMA 127 - TRANSPUESTA
────────────────────────────────────
Descripción: Calcula la transpuesta de una matriz.

Entrada: [[1,2],[3,4],[5,6]]
Salida esperada: [[1,3,5],[2,4,6]]
"""

"""
PROBLEMA 128 - DIAGONAL PRINCIPAL
────────────────────────────────────
Descripción: Suma diagonal principal.

Entrada: [[1,2,3],[4,5,6],[7,8,9]]
Salida esperada: 15
"""

"""
PROBLEMA 129 - BUSCAR EN MATRIZ
────────────────────────────────────
Descripción: Busca valor en matriz ordenada.

Entrada: matrix=[[1,3,5],[7,9,11],[13,15,17]], target=9
Salida esperada: True
"""

"""
PROBLEMA 130 - ESPiral MATRIZ
────────────────────────────────────
Descripción: Imprime matriz en espira.

Entrada: [[1,2,3],[4,5,6],[7,8,9]]
Salida esperada: [1,2,3,6,9,8,7,4,5]
"""

"""
PROBLEMA 131 - CEROS A FIN
────────────────────────────────────
Descripción: Mueve todos los ceros al final.

Entrada: [0,1,0,3,12]
Salida esperada: [1,3,12,0,0]
"""

"""
PROBLEMA 132 - MATRIZ IDENTIDAD
────────────────────────────────────
Descripción: Genera matriz identidad n×n.

Entrada: n=3
Salida esperada: [[1,0,0],[0,1,0],[0,0,1]]
"""

"""
PROBLEMA 133 - SUMA DE DIAGONALES
────────────────────────────────────
Descripción: Suma ambas diagonales.

Entrada: [[1,2,3],[4,5,6],[7,8,9]]
Salida esperada: 30
"""

"""
PROBLEMA 134 - UNIR INTERVALOS
────────────────────────────────────
Descripción: Fusiona intervalos superpuestos.

Entrada: [[1,3],[2,6],[8,10],[15,18]]
Salida esperada: [[1,6],[8,10],[15,18]]
"""

"""
PROBLEMA 135 - MATRIZ ROTADA
────────────────────────────────────
Descripción: Rota matriz 90° clockwise.

Entrada: [[1,2,3],[4,5,6],[7,8,9]]
Salida esperada: [[7,4,1],[8,5,2],[9,6,3]]
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Algoritmos
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 136 - PERMUTACIONES
────────────────────────────────────
Descripción: Genera todas las permutaciones.

Entrada: [1,2,3]
Salida esperada: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

"""
PROBLEMA 137 - COMBINACIONES
────────────────────────────────────
Descripción: Genera combinaciones de n tomados de k.

Entrada: n=4, k=2
Salida esperada: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
"""

"""
PROBLEMA 138 - SUBSETS
────────────────────────────────────
Descripción: Genera todos los subconjuntos.

Entrada: [1,2,3]
Salida esperada: [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
"""

"""
PROBLEMA 139 - CAMINO MÍNIMO
────────────────────────────────────
Descripción: Mínimo camino en grid.

Entrada: m=3, n=7
Salida esperada: 28
"""

"""
PROBLEMA 140 - MONEDAS CAMBIO
────────────────────────────────────
Descripción: Mínimo cambio con monedas.

Entrada: amount=11, coins=[1,2,5]
Salida esperada: 3 (5+5+1)
"""

"""
PROBLEMA 141 - SUBSTRING PALÍNDROMO
────────────────────────────────────
Descripción: Encuentra substring palíndromo más largo.

Entrada: "babad"
Salida esperada: "bab" o "aba"
"""

"""
PROBLEMA 142 - DISTANCIA LEVENSHTEIN
────────────────────────────────────
Descripción: Calcula distancia entre strings.

Entrada: "kitten", "sitting"
Salida esperada: 3
"""

"""
PROBLEMA 143 - LCS
────────────────────────────────────
Descripción: Subsecuencia común más larga.

Entrada: "AGGTAB", "GXTXAYB"
Salida esperada: 4 ("GTAB")
"""

"""
PROBLEMA 144 - KNAPSACK
────────────────────────────────────
Descripción: Problema de la mochila.

Entrada: weights=[2,3,4,5], values=[3,4,5,6], capacity=5
Salida esperada: 7 (items 1 y 2)
"""

"""
PROBLEMA 145 - ÁRBOL GENEALÓGICO
────────────────────────────────────
Descripción: Determina ancestro común.

Entrada: root, p, q
Salida esperada: nodo ancestro
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Grafos
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 146 - BFS
────────────────────────────────────
Descripción: Breadth-First Search en grafo.

Entrada: grafo, inicio
Salida esperada: nodos en orden BFS
"""

"""
PROBLEMA 147 - DFS
────────────────────────────────────
Descripción: Depth-First Search.

Entrada: grafo, inicio
Salida esperada: nodos en orden DFS
"""

"""
PROBLEMA 148 - DETECTAR CICLO
────────────────────────────────────
Descripción: Detecta ciclo en grafo.

Entrada: grafo dirigido
Salida esperada: True/False
"""

"""
PROBLEMA 149 - COMPONENTES CONEXOS
────────────────────────────────────
Descripción: Cuenta componentes conexos.

Entrada: grafo no dirigido
Salida esperada: número de componentes
"""

"""
PROBLEMA 150 - ORDEN TOPOLÓGICO
────────────────────────────────────
Descripción: Orden topológico de DAG.

Entrada: grafo dirigido acíclico
Salida esperada: orden topológico
"""

"""
PROBLEMA 151 - RUTA MÁS CORTA
────────────────────────────────────
Descripción: Dijkstra shortest path.

Entrada: grafo, inicio, destino
Salida esperada: distancia mínima
"""

"""
PROBLEMA 152 - ÁRBOL MST
────────────────────────────────────
Descripción: Minimum Spanning Tree (Prim/Kruskal).

Entrada: grafo ponderado
Salida esperada: peso MST
"""

"""
PROBLEMA 153 - DETECTAR BIPARTITA
────────────────────────────────────
Descripción: Verifica si grafo es bipartita.

Entrada: grafo
Salida esperada: True/False
"""

"""
PROBLEMA 154 - NÚMERO DE ISLAS
────────────────────────────────────
Descripción: Cuenta islas en grid.

Entrada: grid binario
Salida esperada: número de islas
"""

"""
PROBLEMA 155 - RODEADO DE AGUA
────────────────────────────────────
Descripción: Encuentra regiones rodeadas por X.

Entrada: grid con X y O
Salida esperada: grid modificado
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Trees
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 156 - RECORRIDOS ÁRBOL
────────────────────────────────────
Descripción: Inorder, preorder, postorder.

Entrada: árbol binario
Salida esperada: tres listas de recorridos
"""

"""
PROBLEMA 157 - BUSCAR EN BST
────────────────────────────────────
Descripción: Busca en Binary Search Tree.

Entrada: BST, valor
Salida esperada: True/False
"""

"""
PROBLEMA 158 - INSERTAR EN BST
────────────────────────────────────
Descripción: Inserta nodo en BST.

Entrada: BST, valor
Salida esperada: BST modificado
"""

"""
PROBLEMA 159 - ÁRBOL EQUILIBRADO
────────────────────────────────────
Descripción: Verifica si está balanceado.

Entrada: árbol binario
Salida esperada: True/False
"""

"""
PROBLEMA 160 - DIÁMETRO ÁRBOL
────────────────────────────────────
Descripción: Calcula diámetro del árbol.

Entrada: árbol binario
Salida esperada: diámetro
"""

"""
PROBLEMA 161 - PROFUNDIDAD MÁXIMA
────────────────────────────────────
Descripción: Máxima profundidad del árbol.

Entrada: árbol
Salida esperada: profundidad
"""

"""
PROBLEMA 162 - INVERTIR ÁRBOL
────────────────────────────────────
Descripción: Invierte árbol binario.

Entrada: árbol
Salida esperada: árbol invertido
"""

"""
PROBLEMA 163 - SERIALIZAR ÁRBOL
────────────────────────────────────
Descripción: Convierte árbol a string y viceversa.

Entrada: árbol
Salida esperada: string y reconstrucción
"""

"""
PROBLEMA 164 - MENOR MAYOR
────────────────────────────────────
Descripción: Encuentra menor y mayor en BST.

Entrada: BST
Salida esperada: menor, mayor
"""

"""
PROBLEMA 165 - VALIDAR BST
────────────────────────────────────
Descripción: Verifica si es BST válido.

Entrada: árbol
Salida esperada: True/False
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Listas Enlazadas
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 166 - REVERSE LINKED LIST
────────────────────────────────────
Descripción: Invierte lista enlazada simple.

Entrada: lista enlazada
Salida esperada: lista invertida
"""

"""
PROBLEMA 167 - DETECTAR CICLO
────────────────────────────────────
Descripción: Detecta ciclo en lista enlazada.

Entrada: lista enlazada
Salida esperada: nodo inicio de ciclo o None
"""

"""
PROBLEMA 168 - ENLACE MEDIO
────────────────────────────────────
Descripción: Encuentra nodo medio.

Entrada: lista enlazada
Salida esperada: nodo medio
"""

"""
PROBLEMA 169 - ELIMINAR NODO
────────────────────────────────────
Descripción: Elimina nodo en posición dada.

Entrada: lista, posición
Salida esperada: lista sin ese nodo
"""

"""
PROBLEMA 170 - SUMA DE LISTAS
────────────────────────────────────
Descripción: Suma dos números como listas enlazadas.

Entrada: [2,4,3] + [5,6,4] (342 + 465)
Salida esperada: [7,0,8]
"""

"""
PROBLEMA 171 - PALÍNDROMO LISTA
────────────────────────────────────
Descripción: Verifica si lista es palíndromo.

Entrada: lista enlazada
Salida esperada: True/False
"""

"""
PROBLEMA 172 - INTERSECCIÓN
────────────────────────────────────
Descripción: Encuentra intersección de dos listas.

Entrada: dos listas enlazadas
Salida esperada: nodo intersección
"""

"""
PROBLEMA 173 - ELIMINAR DUPLICADOS
────────────────────────────────────
Descripción: Elimina duplicados de lista ordenada.

Entrada: lista ordenada con duplicados
Salida esperada: lista sin duplicados
"""

"""
PROBLEMA 174 - PARTITION LIST
────────────────────────────────────
Descripción: Particiona por valor x.

Entrada: lista, x
Salida esperada: <x | >=x
"""

"""
PROBLEMA 175 - SWAP NODOS
────────────────────────────────────
Descripción: Intercambia nodos en pares.

Entrada: 1->2->3->4
Salida esperada: 2->1->4->3
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Strings Avanzados
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 176 - REORGANIZAR STRING
────────────────────────────────────
Descripción: Reorganiza letras alternadas mayús/minus.

Entrada: "abcdef"
Salida esperada: "AbCdEf"
"""

"""
PROBLEMA 177 - PRIMER ÚNICO
────────────────────────────────────
Descripción: Primer carácter no repetido.

Entrada: "lovelinux"
Salida esperada: "v"
"""

"""
PROBLEMA 178 - GRUPO ANAGRAMAS
────────────────────────────────────
Descripción: Agrupa anagramas.

Entrada: ["eat","tea","tan","ate","nat","bat"]
Salida esperada: [["eat","tea","ate"],["tan","nat"],["bat"]]
"""

"""
PROBLEMA 179 - SUBSTRING ÚNICO
────────────────────────────────────
Descripción: Longitud de substring único más largo.

Entrada: "abcabcbb"
Salida esperada: 3 ("abc")
"""

"""
PROBLEMA 180 - EXPRESIÓN REGULAR
────────────────────────────────────
Descripción: Valida formato email simple.

Entrada: "test@example.com"
Salida esperada: True
"""

"""
PROBLEMA 181 - DISTANCIA HAMMING
────────────────────────────────────
Descripción: Calcula distancia de Hamming.

Entrada: "karolin", "kathrin"
Salida esperada: 3
"""

"""
PROBLEMA 182 - ROTAR STRING
────────────────────────────────────
Descripción: Rotar string k posiciones.

Entrada: "abcdef", k=2
Salida esperada: "cdefab"
"""

"""
PROBLEMA 183 - CONVERTIR NÚMERO
────────────────────────────────────
Descripción: String a entero (sin int()).

Entrada: "4192"
Salida esperada: 4192
"""

"""
PROBLEMA 184 - ZIGZAG CONVERT
────────────────────────────────────
Descripción: Convertir a patrón zigzag.

Entrada: "PAYPALISHIRING", numRows=4
Salida esperada: "PINALSIGYAHRPI"
"""

"""
PROBLEMA 185 - ATOI IMPLEMENTATION
────────────────────────────────────
Descripción: Implementa atoi (ASCII to Integer).

Entrada: "   -42"
Salida esperada: -42
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Diseño
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 186 - MIN STACK
────────────────────────────────────
Descripción: Stack con getMin() en O(1).

Entrada: push(2), push(0), push(3), getMin(), pop(), top(), getMin()
Salida esperada: 0, 3, 0
"""

"""
PROBLEMA 187 - QUEUE CON STACKS
────────────────────────────────────
Descripción: Implementa queue usando dos stacks.

Entrada: push(1), push(2), pop(), push(3), pop()
Salida esperada: 1, 2
"""

"""
PROBLEMA 188 - TWO SUM OPTIMIZADO
────────────────────────────────────
Descripción: Two Sum con hashmap.

Entrada: nums=[2,7,11,15], target=9
Salida esperada: [0,1]
"""

"""
PROBLEMA 189 - LRU CACHE
────────────────────────────────────
Descripción: Implementa Least Recently Used Cache.

Entrada: put(1,1), put(2,2), get(1), put(3,3), get(2)
Salida esperada: 1, -1
"""

"""
PROBLEMA 190 - SHUFFLE ARRAY
────────────────────────────────────
Descripción: Implementa shuffle aleatorio.

Entrada: [1,2,3]
Salida esperada: array mezclado aleatoriamente
"""

"""
PROBLEMA 191 - CIRCULAR ARRAY
────────────────────────────────────
────────────────────────────────────
Descripción: Recorrer array circular.

Entrada: [1,2,3], k=1
Salida esperada: [3,1,2]
"""

"""
PROBLEMA 192 - COUNTER SIMPLE
────────────────────────────────────
Descripción: Implementa Counter básico.

Entrada: ["a","b","a","c","a"]
Salida esperada: {"a":3,"b":1,"c":1}
"""

"""
PROBLEMA 193 - STACK SIMPLE
────────────────────────────────────
Descripción: Implementa Stack básico.

Entrada: push(1), push(2), pop(), peek(), isEmpty()
Salida esperada: 2, 1, False
"""

"""
PROBLEMA 194 - PRIORITY QUEUE
────────────────────────────────────
Descripción: Cola de prioridad simple.

Entrada: enqueue(5), enqueue(1), enqueue(3), dequeue()
Salida esperada: 1 (el menor)
"""

"""
PROBLEMA 195 - HASH MAP
────────────────────────────────────
Descripción: Implementa HashMap básico.

Entrada: put("a",1), get("a"), put("a",2), get("a")
Salida esperada: 1, 2
"""

# ═══════════════════════════════════════════════════════════════════
#                    NIVEL AVANZADO (196-300)
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 196 - SEGMENT TREE
────────────────────────────────────
Descripción: Construye segment tree para range sum.

Entrada: nums=[1,3,5,7,9,11], queries=[[0,2],[1,3]]
Salida esperada: [9, 15]
"""

"""
PROBLEMA 197 - TRIE (PREFIX TREE)
────────────────────────────────────
Descripción: Implementa Trie para autocompletar.

Entrada: insert("apple"), search("app"), startsWith("app")
Salida esperada: True, True
"""

"""
PROBLEMA 198 - ÁRBOL DE SUFIJOS
────────────────────────────────────
Descripción: Construye suffix tree básico.

Entrada: "banana"
Salida esperada: estructura de sufijos
"""

"""
PROBLEMA 199 - KMP ALGORITHM
────────────────────────────────────
Descripción: Implementa KMP para pattern matching.

Entrada: text="ABABDABACDABABCABAB", pattern="ABABCABAB"
Salida esperada: índice donde aparece
"""

"""
PROBLEMA 200 - RABIN KARP
────────────────────────────────────
Descripción: Implementa Rabin-Karp hashing.

Entrada: texto="GEEKS FOR GEEKS", patrón="GEEK"
Salida esperada: índices [0, 10]
"""

"""
PROBLEMA 201 - BITMASK BASICS
────────────────────────────────────
Descripción: Operaciones con bits.

Entrada: x=5 (101), y=3 (011)
Salida esperada: AND=1, OR=7, XOR=6
"""

"""
PROBLEMA 202 - SINGLE NUMBER II
────────────────────────────────────
Descripción: Número que aparece una vez, otros tres.

Entrada: [2,2,3,2]
Salida esperada: 3
"""

"""
PROBLEMA 203 - NÚMERO FALTANTE
────────────────────────────────────
Descripción: Encuentra número faltante en array 1..n.

Entrada: [1,2,4]
Salida esperada: 3
"""

"""
PROBLEMA 204 - DUPLICATE NUMBER
────────────────────────────────────
Descripción: Encuentra duplicado.

Entrada: [1,3,4,2,2]
Salida esperada: 2
"""

"""
PROBLEMA 205 - MAX XOR
────────────────────────────────────
Descripción: Máximo XOR de dos números en array.

Entrada: [3, 10, 5, 25, 2, 8]
Salida esperada: 28 (5^25)
"""

"""
PROBLEMA 206 - COUNT BITS
────────────────────────────────────
Descripción: Cuenta bits de 0 a n.

Entrada: n=5
Salida esperada: [0,1,1,2,1,2]
"""

"""
PROBLEMA 207 - REVERSE BITS
────────────────────────────────────
Descripción: Invierte bits de número.

Entrada: n=43261596
Salida esperada: 964176192
"""

"""
PROBLEMA 208 - BITWISE AND RANGE
────────────────────────────────────
Descripción: Bitwise AND de rango.

Entrada: m=5, n=7
Salida esperada: 4
"""

"""
PROBLEMA 209 - SUMA MÍNIMA ARREGLO
────────────────────────────────────
Descripción: Mínima suma posible de k subarrays.

Entrada: nums=[1,2,3,2,1], k=3
Salida esperada: 5
"""

"""
PROBLEMA 210 - CONTENER AGUA
────────────────────────────────────
Descripción: Trapping Rain Water.

Entrada: [0,1,0,2,1,0,1,3,2,1,2,1]
Salida esperada: 6
"""

"""
PROBLEMA 211 - PRODUCTOR CONSUMIDOR
────────────────────────────────────
Descripción: Implementa patrón producer-consumer.

Entrada: productores=2, consumidores=2, items=10
Salida esperada: ejecución concurrente
"""

"""
PROBLEMA 212 - READ N CHARS
────────────────────────────────────
Descripción: Read 4K chars con puntero.

Entrada: file con más de 4KB
Salida esperada: primeros 4KB
"""

"""
PROBLEMA 213 - ONE EDIT DISTANCE
────────────────────────────────────
Descripción: Verifica si son distancia 1.

Entrada: "ab", "acb"
Salida esperada: True
"""

"""
PROBLEMA 214 - SHORTEST PALINDROME
────────────────────────────────────
Descripción: Encuentra palíndromo más corto.

Entrada: "aacecaaa"
Salida esperada: "aaacecaaa"
"""

"""
PROBLEMA 215 - ENTERO A ROMANO
────────────────────────────────────
Descripción: Convierte entero a romano.

Entrada: 354
Salida esperada: "CCCLIV"
"""

"""
PROBLEMA 216 - ROMANO A ENTERO
────────────────────────────────────
Descripción: Convierte romano a entero.

Entrada: "MCMXCIV"
Salida esperada: 1994
"""

"""
PROBLEMA 217 - LONGEST COMMON PREFIX
────────────────────────────────────
Descripción: Encuentra prefijo común más largo.

Entrada: ["flower","flow","flight"]
Salida esperada: "fl"
"""

"""
PROBLEMA 218 - TRAPPING RAIN WATER II
────────────────────────────────────
Descripción: Water trap en 2D grid.

Entrada: heightMap=[[1,4,3,1,3,2],[3,2,1,3,2,2],[2,3,3,2,3,1]]
Salida esperada: 4
"""

"""
PROBLEMA 219 - JSON PARSER
────────────────────────────────────
Descripción: Parsea JSON manualmente.

Entrada: '{"a":2,"b":[1,2]}'
Salida esperada: diccionario parseado
"""

"""
PROBLEMA 220 - Serialize Deserialize TREE
────────────────────────────────────
Descripción: Serializa y deserializa árbol.

Entrada: root de árbol binario
Salida esperada: reconstrucción idéntica
"""

"""
PROBLEMA 221 - EXCEL SHEET COLUMN
────────────────────────────────────
Descripción: Título de columna a número.

Entrada: "A" -> 1, "Z" -> 26, "AA" -> 27
"""

"""
PROBLEMA 222 - EXCEL SHEET NUMBER
────────────────────────────────────
Descripción: Número a título de columna.

Entrada: 1 -> "A", 26 -> "Z", 27 -> "AA"
"""

"""
PROBLEMA 223 - MAJORITY ELEMENT II
────────────────────────────────────
Descripción: Encuentra elementos > n/3.

Entrada: [1,1,1,3,3,2,2,2]
Salida esperada: [1,2]
"""

"""
PROBLEMA 224 - CONTINUOUS SUBARRAY SUM
────────────────────────────────────
Descripción: Verifica múltiplo de k en subarray.

Entrada: [23,2,6,4,7], k=6
Salida esperada: True
"""

"""
PROBLEMA 225 - COMPLEMENT BASE 10
────────────────────────────────────
Descripción: Complemento a 10 del número.

Entrada: num=5 (0101 binario)
Salida esperada: 2 (0010)
"""

"""
PROBLEMA 226 - UGLY NUMBER II
────────────────────────────────────
Descripción: n-ésimo número feo.

Entrada: n=10
Salida esperada: 12
"""

"""
PROBLEMA 227 - MISSING NUMBER II
────────────────────────────────────
Descripción: Encuentra número faltante de array permutado.

Entrada: [1,2,3,4,6,7,8]
Salida esperada: 5
"""

"""
PROBLEMA 228 - INTEGER BREAK
────────────────────────────────────
Descripción: Maximiza producto de partes.

Entrada: n=10
Salida esperada: 36 (3+3+4)
"""

"""
PROBLEMA 229 - RECURSIVE MULTIPLY
────────────────────────────────────
Descripción: Multiplica sin operador *.

Entrada: 3 * 5
Salida esperada: 15
"""

"""
PROBLEMA 230 - BIT FLIPS
────────────────────────────────────
Descripción: Mínimos flips para convertir a.

Entrada: start=00101, goal=10000
Salida esperada: flips mínimos
"""

"""
PROBLEMA 231 - DIVIDE INTEGERS
────────────────────────────────────
Descripción: Divide sin operador /.

Entrada: dividend=10, divisor=3
Salida esperada: 3
"""

"""
PROBLEMA 232 - POW X N
────────────────────────────────────
Descripción: Calcula x^n sin pow().

Entrada: x=2.0, n=-2
Salida esperada: 0.25
"""

"""
PROBLEMA 233 - SUBSET SUM IIDescripción: Subset sum con
────────────────────────────────────
 duplicados.

Entrada: nums=[1,2,2], target=3
Salida esperada: todas las combinaciones
"""

"""
PROBLEMA 234 - MAXIMUM PRODUCT SUBARRAY
────────────────────────────────────
Descripción: Máximo producto de subarray.

Entrada: [2,3,-2,4]
Salida esperada: 6
"""

"""
PROBLEMA 235 - FIND PEAK ELEMENT
────────────────────────────────────
Descripción: Encuentra pico en array mountain.

Entrada: [1,2,3,4,5,3,1]
Salida esperada: índice 4
"""

"""
PROBLEMA 236 - MISSING RANGES
────────────────────────────────────
Descripción: Encuentra rangos faltantes.

Entrada: [0,1,3,50,75], lower=0, upper=99
Salida esperada: ["2","4-49","51-74","76-99"]
"""

"""
PROBLEMA 237 - ZOOMOS INTERVIEW
────────────────────────────────────
Descripción: Merge overlapping intervals optimizado.

Entrada: intervals=[[1,3],[2,6],[8,10],[15,18]]
Salida esperada: [[1,6],[8,10],[15,18]]
"""

"""
PROBLEMA 238 - TASK SCHEDULER
────────────────────────────────────
Descripción: Planificador de tareas.

Entrada: tasks=["A","A","A","B","B","B"], n=2
Salida esperada: 8
"""

"""
PROBLEMA 239 - REORGANIZE STRING
────────────────────────────────────
Descripción: Reorganiza para que no haya adyacentes iguales.

Entrada: "aaabbc"
Salida esperada: "ababac"
"""

"""
PROBLEMA 240 - MAX CHUNKS TO SORT
────────────────────────────────────
Descripción: Máximos chunks para ordenar.

Entrada: [1,0,1,3,2]
Salida esperada: 3
"""

"""
PROBLEMA 241 - DECODE STRING
────────────────────────────────────
Descripción: Decodifica string codificado.

Entrada: "3[a2[c]]"
Salida esperada: "accaccacc"
"""

"""
PROBLEMA 242 - MAXIMUM NESTED DEPTH
────────────────────────────────────
Descripción: Máxima profundidad anidada.

Entrada: "(1+(2*3)+((8)/4))+1"
Salida esperada: 3
"""

"""
PROBLEMA 243 - CAR FLEET II
────────────────────────────────────
Descripción: Calcula fleet到达目的地.

Entrada: position=[10,2,8,3,5], speed=[2,4,1,3,6]
Salida esperada: [0,1,2,2,3]
"""

"""
PROBLEMA 244 - EMPLOYEE FREE TIME
────────────────────────────────────
Descripción: Empleados tiempo libre.

Entrada: [[[1,2],[5,6]],[[2,3]],[[2,4],[7,9]]]
Salida esperada: [[4,5]]
"""

"""
PROBLEMA 245 - SWIM IN RISING WATER
────────────────────────────────────
Descripción: Nadar en agua subiendo.

Entrada: grid=[[0,2,1],[3,8,2],[4,7,6,5],[1,9,0,10,11]]
Salida esperada: 7
"""

"""
PROBLEMA 246 - MIN COST TO REACH END
────────────────────────────────────
Descripción: Costo mínimo para llegar al final.

Entrada: grid=[[1,2,3],[4,5,6],[7,8,9]]
Salida esperada: 21
"""

"""
PROBLEMA 247 - MAX AREA OF ISLAND
────────────────────────────────────
Descripción: Área máxima de isla.

Entrada: [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Salida esperada: 4
"""

"""
PROBLEMA 248 - NUMBER OF PROVINCES
────────────────────────────────────
Descripción: Cuenta provincias (DFS).

Entrada: isConnected=[[1,1,0],[1,1,0],[0,0,1]]
Salida esperada: 2
"""

"""
PROBLEMA 249 - MATCHSTICKS TO SQUARE
────────────────────────────────────
Descripción: Formar cuadrado con fósforos.

Entrada: [1,1,2,2,2]
Salida esperada: True
"""

"""
PROBLEMA 250 - VALIDATE STACK SEQUENCES
────────────────────────────────────
Descripción: Valida secuencias de push/pop.

Entrada: pushed=[1,2,3,4,5], popped=[4,5,3,2,1]
Salida esperada: True
"""

"""
PROBLEMA 251 - CACHE LRU IMPLEMENTATION
────────────────────────────────────
Descripción: Implementa LRU Cache desde cero.

Entrada: LRUCache(2), put(1,1), put(2,2), get(1), put(3,3), get(2)
Salida esperada: 1, -1
"""

"""
PROBLEMA 252 - LFUCACHE IMPLEMENTATION
────────────────────────────────────
Descripción: Implementa LFU Cache.

Entrada: LFUCache(2), put(1,1), put(2,2), get(1), put(3,3), get(2)
Salida esperada: 1, -1
"""

"""
PROBLEMA 253 - MIN STACK WITH MIN VALUE
────────────────────────────────────
Descripción: Stack que retorna mínimo en O(1).

Entrada: push(5), push(2), push(8), getMin(), pop(), getMin()
Salida esperada: 2, 5
"""

"""
PROBLEMA 254 - CIRCULAR QUEUE
────────────────────────────────────
Descripción: Implementa cola circular.

Entrada: enqueue(1), enqueue(2), dequeue(), enqueue(3)
Salida esperada: 1, [2,3]
"""

"""
PROBLEMA 255 - LINKED LIST CYCLE LENGTH
────────────────────────────────────
Descripción: Longitud del ciclo en lista.

Entrada: lista con ciclo
Salida esperada: longitud del ciclo
"""

"""
PROBLEMA 256 - MERGE K LINKED LISTS
────────────────────────────────────
Descripción: Fusiona k listas ordenadas.

Entrada: listas [[1,4,5],[1,3,4],[2,6]]
Salida esperada: [1,1,2,3,4,4,5,6]
"""

"""
PROBLEMA 257 - SORT LIST
────────────────────────────────────
Descripción: Ordena lista enlazada O(n log n).

Entrada: lista enlazada desordenada
Salida esperada: lista ordenada
"""

"""
PROBLEMA 258 - COPY LIST WITH RANDOM
────────────────────────────────────
Descripción: Copia lista con puntero random.

Entrada: lista con random pointers
Salida esperada: copia profunda
"""

"""
PROBLEMA 259 - REVERSE LINKED LIST II
────────────────────────────────────
Descripción: Invierte desde m hasta n.

Entrada: 1->2->3->4->5, m=2, n=4
Salida esperada: 1->4->3->2->5
"""

"""
PROBLEMA 260 - FLATTEN MULTILEVEL LIST
────────────────────────────────────
Descripción: Aplana lista multinivel.

Entrada: lista con next y child
Salida esperada: lista aplanada
"""

"""
PROBLEMA 261 - CONNECT ALL SIBLINGS
────────────────────────────────────
Descripción: Conecta todos next derechos.

Entrada: árbol nivel por nivel
Salida esperada: cada nodo conecta al derecho
"""

"""
PROBLEMA 262 - RIGHT VIEW TREE
────────────────────────────────────
Descripción: Vista derecha del árbol.

Entrada: árbol binario
Salida esperada: [1,3,4]
"""

"""
PROBLEMA 263 - BOTTOM VIEW TREE
────────────────────────────────────
Descripción: Vista inferior del árbol.

Entrada: árbol binario
Salida esperada: nodos inferiores
"""

"""
PROBLEMA 264 - SYMMETRIC TREE
────────────────────────────────────
Descripción: Verifica simetría del árbol.

Entrada: [1,2,2,3,4,4,3]
Salida esperada: True
"""

"""
PROBLEMA 265 - CONVERT BST TO LIST
────────────────────────────────────
Descripción: BST a lista doble enlazada.

Entrada: BST
Salida esperada: lista circular
"""

"""
PROBLEMA 266 - CONSTRUCT FROM PREORDER
────────────────────────────────────
Descripción: Construye BST desde preorder.

Entrada: preorder=[8,5,1,7,10,12]
Salida esperada: BST válida
"""

"""
PROBLEMA 267 - INORDER SUCCESSOR BST
────────────────────────────────────
Descripción: Sucesor inorder en BST.

Entrada: nodo con valor
Salida esperada: siguiente inorder
"""

"""
PROBLEMA 268 - LCA BINARY TREE
────────────────────────────────────
Descripción: Lowest Common Ancestor.

Entrada: root, p, q
Salida esperada: nodo LCA
"""

"""
PROBLEMA 269 - SERIALIZE BST
────────────────────────────────────
Descripción: Serializa BST a string.

Entrada: BST
Salida esperada: string, reconstruible
"""

"""
PROBLEMA 270 - MAXIMUM PATH SUM
────────────────────────────────────
Descripción: Suma máxima en path.

Entrada: árbol con valores
Salida esperada: suma máxima
"""

"""
PROBLEMA 271 - WORD SEARCH
────────────────────────────────────
Descripción: Busca palabra en grid.

Entrada: board=[[A,B],[C,D]], word="ABCD"
Salida esperada: True/False
"""

"""
PROBLEMA 272 - WORD SEARCH II
────────────────────────────────────
Descripción: Encuentra palabras en board.

Entrada: board, palabras
Salida esperada: palabras encontradas
"""

"""
PROBLEMA 273 - SUDOKU SOLVER
────────────────────────────────────
Descripción: Resuelve Sudoku.

Entrada: tablero Sudoku
Salida esperada: solución
"""

"""
PROBLEMA 274 - N-QUEENS
────────────────────────────────────
Descripción: Resuelve N-Reinas.

Entrada: n=4
Salida esperada: todas las soluciones
"""

"""
PROBLEMA 275 - PERMUTE STRING
────────────────────────────────────
Descripción: Permutaciones con caracteres repetidos.

Entrada: "aab"
Salida esperada: ["aba","baa","aab"]
"""

"""
PROBLEMA 276 - GENERATE PARENTHESES
────────────────────────────────────
Descripción: Genera paréntesis válidos.

Entrada: n=3
Salida esperada: ["((()))","(()())","(())()","()(())","()()()"]
"""

"""
PROBLEMA 277 - COMBINE SUM
────────────────────────────────────
Descripción: Combination Sum III.

Entrada: k=3, n=9
Salida esperada: [[1,2,6],[1,3,5],[2,3,4]]
"""

"""
PROBLEMA 278 - LETTER COMBINATIONS
────────────────────────────────────
Descripción: Combinaciones de teléfono.

Entrada: digits="23"
Salida esperada: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""

"""
PROBLEMA 279 - PALINDROME PARTITIONING
────────────────────────────────────
Descripción: Particiona en palíndromos.

Entrada: s="aab"
Salida esperada: [["a","a","b"],["aa","b"]]
"""

"""
PROBLEMA 280 - SUBSET II
────────────────────────────────────
Descripción: Subsets con duplicados.

Entrada: nums=[1,2,2]
Salida esperada: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""

"""
PROBLEMA 281 - RESTORE IP ADDRESSES
────────────────────────────────────
Descripción: Restaura direcciones IP.

Entrada: s="25525511135"
Salida esperada: ["255.255.11.135","255.255.111.35"]
"""

"""
PROBLEMA 282 - EXPRESSION ADD OPERATORS
────────────────────────────────────
Descripción: Añade operadores a expresión.

Entrada: num="123", target=6
Salida esperada: ["1+2+3","1*2*3"]
"""

"""
PROBLEMA 283 - WILD CARD MATCHING
────────────────────────────────────
Descripción: Wildcard matching.

Entrada: s="aa", p="a*"
Salida esperada: True
"""

"""
PROBLEMA 284 - REGEX MATCHING
────────────────────────────────────
Descripción: Regular expression matching.

Entrada: s="ab", p=".*"
Salida esperada: True
"""

"""
PROBLEMA 285 - MINIMUM WINDOW SUBSTRING
────────────────────────────────────
Descripción: Minimum window substring.

Entrada: s="ADOBECODEBANC", t="ABC"
Salida esperada: "BANC"
"""

"""
PROBLEMA 286 - LONGEST SUBSTRING NO REPEAT
────────────────────────────────────
Descripción: Longest substring sin repetición.

Entrada: "abcabcbb"
Salida esperada: 3 ("abc")
"""

"""
PROBLEMA 287 - FIND ALL ANAGRAMS
────────────────────────────────────
Descripción: Encuentra todos los anagramas.

Entrada: s="cbaebabacd", p="abc"
Salida esperada: [0,6]
"""

"""
PROBLEMA 288 - MINIMUM WINDOW SUBSEQ
────────────────────────────────────
Descripción: Minimum window subsequence.

Entrada: s="abcdebdde", t="bde"
Salida esperada: "bcde"
"""

"""
PROBLEMA 289 - INTERLEAVING STRING
────────────────────────────────────
Descripción: Interleaving string.

Entrada: s1="aab", s2="axy", s3="aaxaby"
Salida esperada: True
"""

"""
PROBLEMA 290 - LONGEST PALINDROMIC SUB
────────────────────────────────────
Descripción: Longest Palindromic Subsequence.

Entrada: s="bbbab"
Salida esperada: 4
"""

"""
PROBLEMA 291 - WORD BREAK
────────────────────────────────────
Descripción: Verifica word break.

Entrada: s="leetcode", wordDict=["leet","code"]
Salida esperada: True
"""

"""
PROBLEMA 292 - WORD BREAK II
────────────────────────────────────
Descripción: Genera todas las frases.

Entrada: s="catsanddog", dict=["cat","cats","and","sand","dog"]
Salida esperada: ["cat sand dog","cats and dog"]
"""

"""
PROBLEMA 293 - HOUSE ROBBER II
────────────────────────────────────
Descripción: House Robber II (circular).

Entrada: nums=[2,3,2]
Salida esperada: 3
"""

"""
PROBLEMA 294 - COIN CHANGE II
────────────────────────────────────
Descripción: Ways to form amount.

Entrada: amount=5, coins=[1,2,5]
Salida esperada: 4
"""

"""
PROBLEMA 295 - LONGEST INCREASING PATH
────────────────────────────────────
Descripción: Longest increasing path in matrix.

Entrada: [[3,4,5],[3,2,6],[2,2,1]]
Salida esperada: 4
"""

"""
PROBLEMA 296 - STONE GAME IV
────────────────────────────────────
Descripción: Winner Stone Game.

Entrada: n=4
Salida esperada: "First"
"""

"""
PROBLEMA 297 - CHAMPAGNE TOWER
────────────────────────────────────
Descripción: Copa de champagne.

Entrada: poured=4, query_glass=2, query_row=1
Salida esperada: 0.5
"""

"""
PROBLEMA 298 - POURED WATER
────────────────────────────────────
Descripción: Water within queries.

Entrada: C=[], queries=[[1,1,2],[2,3,5]]
Salida esperada: [0, 100]
"""

"""
PROBLEMA 299 - SCORE OF PARENTHESES
────────────────────────────────────
Descripción: Score of Parentheses.

Entrada: "(()(()))"
Salida esperada: 6
"""

"""
PROBLEMA 300 - FINAL VALUE
────────────────────────────────────
Descripción: Final value after operations.

Entrada: ["--X","X++","X++"]
Salida esperada: 1
"""

# ═══════════════════════════════════════════════════════════════════
#                          FIN DEL DOCUMENTO
# ═══════════════════════════════════════════════════════════════════
# 
# ¡Felicitaciones! Tienes 300 problemas para practicar.
# Intenta resolverlos sin ver las soluciones.
# El aprendizaje viene de la práctica y el esfuerzo.
#
# ═══════════════════════════════════════════════════════════════════
