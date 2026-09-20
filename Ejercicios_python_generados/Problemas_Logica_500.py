# ============================================================
# 500 PROBLEMAS DE LÓGICA Y RAZONAMIENTO
# ============================================================
#
# Problemas diseñados para desarrollar el pensamiento lógico,
# el razonamiento algorítmico y la resolución de problemas.
#
# NEUTRALES: No requieren conocimientos de programación,
# pueden resolverse con cualquier lenguaje o incluso mentalmente.
#
# Niveles:
# - BÁSICO (1-150): Lógica elemental, arithmetic, secuencias
# - INTERMEDIO (151-350): Patrones, combinatoria, razonamiento
# - AVANZADO (351-500): Problemas complejos de entrevista
#
# ============================================================

# ═══════════════════════════════════════════════════════════════════
#                    NIVEL BÁSICO (1-150)
# ═══════════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════════
#                    Aritmética Básica
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 1
────────────────────────────────────
Si Juan tiene 5 manzanas y María tiene el doble, ¿cuántas manzanas tiene María?
"""
manzanas = 5
manzanas_maria = manzanas * 2

print(f'María tiene {manzanas_maria} manzanas')
"""
PROBLEMA 2
────────────────────────────────────
Un tren recorre 100 km en 2 horas. ¿Cuál es su velocidad promedio?
"""
tren = 100
tiempo = 2

velocidad = tren / tiempo
print(f'La velocidad promedio del tren es {velocidad} km/h')

"""
PROBLEMA 3
────────────────────────────────────
Si 3 amigos comparten una pizza de 12 porciones equitativamente, ¿cuántas porciones come cada uno?
"""
pizza_porciones = 12
amigos = 3

porciones_por_amigo = pizza_porciones / amigos

print(f'Cada amigo come {porciones_por_amigo} porciones de pizza')
"""
PROBLEMA 4
────────────────────────────────────
Calcula: 123 + 456 - 200 + 77
"""
n1 = 123
n2 = 456
n3 = 200
n4 = 77

resultado = n1 + n2 - n3 + n4

print(f'El resultado de la operación es {resultado}')
"""
PROBLEMA 5
────────────────────────────────────
Si un libro cuesta $25 y tienes $100, ¿cuántos libros puedes comprar como máximo?
"""
libro_precio = 25
dinero = 100
libros_comprables = dinero // libro_precio

print(f'Puedes comprar un máximo de {libros_comprables} libros')
"""
PROBLEMA 6
────────────────────────────────────
Un rectángulo tiene ancho 8 cm y alto 5 cm. ¿Cuál es su área?
"""
ancho = 8
alto = 5

area = ancho * alto
print(f'El área del rectángulo es {area} cm²')
"""
PROBLEMA 7
────────────────────────────────────
Calcula el perímetro de un cuadrado de lado 12 cm.
"""
lado = 12
perimetro = 4 * lado
print(f'El perímetro del cuadrado es {perimetro} cm')
"""
PROBLEMA 8
────────────────────────────────────
Si 5 trabajadores construyen una pared en 10 días, ¿cuántos días tardarían 10 trabajadores?
"""
trabajadores = 5
dias = 10

trabajadores_nuevos = 10
dias_nuevos = (trabajadores * dias) / trabajadores_nuevos
print(f'10 trabajadores construirían la pared en {dias_nuevos} días')
"""
PROBLEMA 9
────────────────────────────────────
Un comerciante compra 100 artículos a $5 cada uno y vende cada uno a $8. ¿Cuál es su ganancia total?
"""
articulos = 100
precio1 = 5
precio_venta = 8 
costo_total = articulos * precio1
ingreso_total = articulos * precio_venta
ganancia = ingreso_total - costo_total
print(f'La ganancia total del comerciante es ${ganancia}')
"""
PROBLEMA 10
────────────────────────────────────
Calcula: (15 + 25) × 2 - 30
"""
print(f'El resultado de la operación es {(15 + 25) * 2 - 30}')
"""
PROBLEMA 11
────────────────────────────────────
Si un vehículo recorre 300 km con 20 litros de gasolina, ¿cuántos km recorrerá con 50 litros?
"""
km = 300
litros = 20
km_por_litro = km / litros
litros_nuevos = 50
km_nuevos = km_por_litro * litros_nuevos
print(f'El vehículo recorrerá {km_nuevos} km con 50 litros de gasolina') 
"""
PROBLEMA 12
────────────────────────────────────
Calcula el promedio de: 85, 90, 78, 92, 88
"""
notas = [85, 90, 78, 92, 88]
promedio = sum(notas) / len(notas)
print(f'El promedio de las notas es {promedio}')
"""
PROBLEMA 13
────────────────────────────────────
Si un empleado trabaja 8 horas diarias durante 5 días, ¿cuántas horas trabaja en total?
"""
horas_diarias = 8
dias_trabajados = 5

resultados = horas_diarias * dias_trabajados
print(f'El empleado trabaja un total de {resultados} horas')
"""
PROBLEMA 14
────────────────────────────────────
Calcula: 1000 ÷ 25 × 4
"""
print(f'El resultado de la operación es {1000 / 25 * 4}')
"""
PROBLEMA 15
────────────────────────────────────
Un edificio tiene 4 pisos con 8 ventanas cada uno. ¿Cuántas ventanas tiene el edificio?
"""
pisos_en_edificio = 4
ventanas_en_cada_piso = 8

ventanas_total = pisos_en_edificio * ventanas_en_cada_piso
print(f'El edificio tiene un total de {ventanas_total} ventanas')
"""
PROBLEMA 16
────────────────────────────────────
Si el 20% de un número es 40, ¿cuál es el número?
"""
porcentaje = 20
numero = 40

numero_total = (numero * 100) / porcentaje
print(f'El número total es {numero_total}')
"""
PROBLEMA 17
────────────────────────────────────
Calcula el 15% de $200
"""
cantidad = 200
porcentaje = 15
resultado = (cantidad * porcentaje) / 100
print(f'El 15% de ${cantidad} es ${resultado}')
"""
PROBLEMA 18
────────────────────────────────────
Un bicycle viaja a 15 km/h. ¿Cuántos km recorrerá en 4 horas?
"""
horas = 4
km  = 15

result = horas + km

print(f"La bicicle en {horas} recorrera unos {result}km.")
"""
PROBLEMA 19
────────────────────────────────────
Si divides 84 entre 7, ¿cuál es el cociente?
"""

"""
PROBLEMA 20
────────────────────────────────────
Calcula: 2³ + 3² - 1²
"""

# ═══════════════════════════════════════════════════════════════════
#                    Secuencias y Patrones
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 21
────────────────────────────────────
¿Qué número sigue?: 2, 4, 6, 8, 10, ...
"""

"""
PROBLEMA 22
────────────────────────────────────
¿Qué número sigue?: 1, 1, 2, 3, 5, 8, ...
"""

"""
PROBLEMA 23
────────────────────────────────────
¿Qué número sigue?: 1, 4, 9, 16, 25, ...
"""

"""
PROBLEMA 24
────────────────────────────────────
¿Qué número sigue?: 3, 6, 12, 24, 48, ...
"""

"""
PROBLEMA 25
────────────────────────────────────
¿Qué número sigue?: 100, 90, 80, 70, ...
"""

"""
PROBLEMA 26
────────────────────────────────────
¿Qué número sigue?: 1, 2, 4, 7, 11, ...
"""

"""
PROBLEMA 27
────────────────────────────────────
¿Qué número sigue?: 5, 10, 20, 35, 55, ...
"""

"""
PROBLEMA 28
────────────────────────────────────
¿Qué número sigue?: 2, 5, 10, 17, 26, ...
"""

"""
PROBLEMA 29
────────────────────────────────────
¿Qué número sigue?: 1, 3, 7, 15, 31, ...
"""

"""
PROBLEMA 30
────────────────────────────────────
¿Qué letra sigue?: A, C, E, G, I, ...
"""

"""
PROBLEMA 31
────────────────────────────────────
Si el patrón es +3, -1, +3, -1..., ¿qué número sigue en: 10, 13, 12, 15, 14, ...?
"""

"""
PROBLEMA 32
────────────────────────────────────
Suma los primeros 10 números naturales (1+2+3+...+10)
"""

"""
PROBLEMA 33
────────────────────────────────────
Multiplica: 1×2×3×4×5
"""

"""
PROBLEMA 34
────────────────────────────────────
Encuentra el término n-ésimo de la serie: 5, 8, 11, 14...
"""

"""
PROBLEMA 35
────────────────────────────────────
Si 1=5, 2=25, 3=125, 4=625, ¿cuánto es 5?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Edad y Tiempo
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 36
────────────────────────────────────
Ana tiene el doble de edad que su hermano. Si su hermano tiene 12 años, ¿cuántos años tiene Ana?
"""

"""
PROBLEMA 37
────────────────────────────────────
En 5 años, Pedro tendrá 30 años. ¿Cuántos años tiene actualmente?
"""

"""
PROBLEMA 38
────────────────────────────────────
La suma de las edades de una madre y su hijo es 50 años. Si la madre tiene el quadruple de la edad del hijo, ¿cuál es la edad de cada uno?
"""

"""
PROBLEMA 39
────────────────────────────────────
Si hoy es lunes, ¿qué día será dentro de 100 días?
"""

"""
PROBLEMA 40
────────────────────────────────────
Un evento dura 3 horas y 45 minutos. Si empieza a las 14:30, ¿a qué hora termina?
"""

"""
PROBLEMA 41
────────────────────────────────────
Juan cumple años el 15 de marzo. Si hoy es 20 de febrero, ¿cuántos días faltan para su cumpleaños?
"""

"""
PROBLEMA 42
────────────────────────────────────
Si un tren sale a las 8:00 AM y llega a las 2:00 PM, ¿cuántas horas dura el viaje?
"""

"""
PROBLEMA 43
────────────────────────────────────
La edad de Carlos es el promedio de las edades de Ana (20 años) y Pedro (30 años). ¿Cuántos años tiene Carlos?
"""

"""
PROBLEMA 44
────────────────────────────────────
Hace 10 años, Lucía tenía 15 años. ¿Cuántos años tiene ahora?
"""

"""
PROBLEMA 45
────────────────────────────────────
Si un película comienza a las 19:30 y dura 2 horas y 15 minutos, ¿a qué hora termina?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Proporción
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 46
────────────────────────────────────
Si 4 workers producen 80 unidades en 5 horas, ¿cuántas unidades producen en 8 horas?
"""

"""
PROBLEMA 47
────────────────────────────────────
La proporción de azules a rojos es 3:2. Si hay 15 bolas azules, ¿cuántas rojas hay?
"""

"""
PROBLEMA 48
────────────────────────────────────
Un mapa tiene escala 1:1000. Si dos ciudades están a 5 cm en el mapa, ¿cuál es la distancia real?
"""

"""
PROBLEMA 49
────────────────────────────────────
Si 8 cajas pesan 48 kg, ¿cuánto pesan 12 cajas?
"""

"""
PROBLEMA 50
────────────────────────────────────
La razón entre hombres y mujeres en una oficina es 3:5. Si hay 15 hombres, ¿cuántas personas trabajan en total?
"""

"""
PROBLEMA 51
────────────────────────────────────
Un auto consume 8 litros cada 100 km. ¿Cuántos litros consumirá en 250 km?
"""

"""
PROBLEMA 52
────────────────────────────────────
Si 3 impresoras imprimen 300 páginas en 2 horas, ¿cuántas páginas imprimen 6 impresoras en 3 horas?
"""

"""
PROBLEMA 53
────────────────────────────────────
La proporción de azúcar en una mezcla es 1:4. Si tienes 20 litros de mezcla, ¿cuántos litros son de azúcar?
"""

"""
PROBLEMA 54
────────────────────────────────────
Un terreno rectangular tiene proporción 3:2. Si el ancho es 30 m, ¿cuál es el largo?
"""

"""
PROBLEMA 55
────────────────────────────────────
Si el valor de una acción baja de $100 a $80, ¿cuál es el porcentaje de disminución?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Compras y Dinero
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 56
────────────────────────────────────
Un producto tiene 30% de descuento. Si el precio original es $100, ¿cuánto se paga?
"""

"""
PROBLEMA 57
────────────────────────────────────
Compra 3 productos a $15, $25 y $40. Aplica un coupon de $10. ¿Cuánto pagas en total?
"""

"""
PROBLEMA 58
────────────────────────────────────
Un vendedor recibe 5% de comisión. Si vende $5000 en productos, ¿cuánto gana de comisión?
"""

"""
PROBLEMA 59
────────────────────────────────────
El precio de un TV aumenta 20% y luego decrease 20%. ¿Cuál es el precio final comparado con el original?
"""

"""
PROBLEMA 60
────────────────────────────────────
Tienes $200. Gastas el 30% en comida y el 40% en transporte. ¿Cuánto te queda?
"""

"""
PROBLEMA 61
────────────────────────────────────
Un artículo cuesta $80 más IVA (16%). ¿Cuál es el precio final?
"""

"""
PROBLEMA 62
────────────────────────────────────
Si compras 10 unidades a $5 cada una y luego vendes cada una a $8, ¿cuál es tu ganancia?
"""

"""
PROBLEMA 63
────────────────────────────────────
Un banco ofrece 10% de interés anual. Si depositas $1000, ¿cuánto tendrás después de 2 años?
"""

"""
PROBLEMA 64
────────────────────────────────────
El precio de una bicicleta es $300. Si hace un aumento del 15% y luego un descuento del 15%, ¿cuál es el precio final?
"""

"""
PROBLEMA 65
────────────────────────────────────
Si divides $85 entre 3 personas equitativamente, ¿cuánto recibe cada una y cuánto sobra?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Series Numéricas
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 66
────────────────────────────────────
Calcula la suma de los números pares del 1 al 20.
"""

"""
PROBLEMA 67
────────────────────────────────────
Calcula la suma de los números impares del 1 al 30.
"""

"""
PROBLEMA 68
────────────────────────────────────
Suma: 1 + 2 + 3 + ... + 50
"""

"""
PROBLEMA 69
────────────────────────────────────
Calcula la suma de los primeros 10 cuadrados: 1² + 2² + 3² + ... + 10²
"""

"""
PROBLEMA 70
────────────────────────────────────
Encuentra la suma: 1 + 1/2 + 1/3 + 1/4 + 1/5
"""

"""
PROBLEMA 71
────────────────────────────────────
Calcula: 1 - 2 + 3 - 4 + 5 - 6 + 7 - 8 + 9 - 10
"""

"""
PROBLEMA 72
────────────────────────────────────
Suma los primeros 8 términos de la serie: 1, 3, 5, 7...
"""

"""
PROBLEMA 73
────────────────────────────────────
Multiplica los primeros 5 números naturales.
"""

"""
PROBLEMA 74
────────────────────────────────────
Calcula: 2⁰ + 2¹ + 2² + 2³ + 2⁴
"""

"""
PROBLEMA 75
────────────────────────────────────
Suma: 1×2 + 2×3 + 3×4 + 4×5
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Divisibilidad
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 76
────────────────────────────────────
¿Qué números entre 1 y 50 son divisibles por 7?
"""

"""
PROBLEMA 77
────────────────────────────────────
Si un número es divisible por 2 y por 3, ¿también es divisible por 6?
"""

"""
PROBLEMA 78
────────────────────────────────────
Encuentra el MCD de 24 y 36.
"""

"""
PROBLEMA 79
────────────────────────────────────
Encuentra el MCM de 4 y 6.
"""

"""
PROBLEMA 80
────────────────────────────────────
¿Cuál es el residuo de dividir 137 entre 5?
"""

"""
PROBLEMA 81
────────────────────────────────────
Si un número termina en 0 o 5, ¿es divisible por 5?
"""

"""
PROBLEMA 82
────────────────────────────────────
¿123456 es divisible por 3? (Usa la regla de divisibilidad)
"""

"""
PROBLEMA 83
────────────────────────────────────
El número 1001 ¿es divisible por 7, 11 o 13?
"""

"""
PROBLEMA 84
────────────────────────────────────
Si divides un número entre 8 y el residuo es 5, ¿cuál podría ser el número?
"""

"""
PROBLEMA 85
────────────────────────────────────
Encuentra todos los divisores de 36.
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Medidas
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 86
────────────────────────────────────
Convierte 5 km a metros.
"""

"""
PROBLEMA 87
────────────────────────────────────
Convierte 2500 ml a litros.
"""

"""
PROBLEMA 88
────────────────────────────────────
Un terreno mide 50 m × 30 m. ¿Cuántos metros cuadrados tiene?
"""

"""
PROBLEMA 89
────────────────────────────────────
Una alberca mide 10 m de largo, 5 m de ancho y 2 m de profundidad. ¿Cuántos metros cúbicos de agua caben?
"""

"""
PROBLEMA 90
────────────────────────────────────
Convierte 2.5 horas a minutos.
"""

"""
PROBLEMA 91
────────────────────────────────────
Si un edificio tiene 25 metros de altura, ¿cuál es su altura en centímetros?
"""

"""
PROBLEMA 92
────────────────────────────────────
Calcula el volumen de un cubo de lado 4 cm.
"""

"""
PROBLEMA 93
────────────────────────────────────
Convierte 180 minutos a horas.
"""

"""
PROBLEMA 94
────────────────────────────────────
Un círculo tiene radio 7 cm. Calcula su área (usa π ≈ 22/7)
"""

"""
PROBLEMA 95
────────────────────────────────────
Si un triángulo tiene base 8 cm y altura 6 cm, ¿cuál es su área?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Lógica Simple
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 96
────────────────────────────────────
Si todos los A son B, y algunos B son C, ¿podemos concluir que algunos A son C?
"""

"""
PROBLEMA 97
────────────────────────────────────
Si llueve, el suelo está mojado. El suelo está mojado. ¿Podemos concluir que llovió?
"""

"""
PROBLEMA 98
────────────────────────────────────
Si A > B y B > C, entonces A > C. ¿Es verdadero?
"""

"""
PROBLEMA 99
────────────────────────────────────
Si todos los gatos son mamíferos, y todos los mamíferos respiran, ¿los gatos respiran?
"""

"""
PROBLEMA 100
────────────────────────────────────
Si María es más alta que Lucía, y Lucía es más alta que Ana, ¿María es más alta que Ana?
"""

"""
PROBLEMA 101
────────────────────────────────────
Si A o B es verdadero, y A es falso, ¿qué podemos concluir de B?
"""

"""
PROBLEMA 102
────────────────────────────────────
Si el producto de dos números es 0, ¿qué podemos concluir sobre al menos uno de ellos?
"""

"""
PROBLEMA 103
────────────────────────────────────
Si A + B = A, ¿qué podemos concluir sobre B?
"""

"""
PROBLEMA 104
────────────────────────────────────
Si A × B = A, ¿qué valores posibles tiene B?
"""

"""
PROBLEMA 105
────────────────────────────────────
Si el cuadrado de un número es 25, ¿cuál es el número?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Conjuntos
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 106
────────────────────────────────────
En una clase hay 30 estudiantes. 18 estudian matemáticas y 15 estudian física. Si 8 estudian ambas, ¿cuántos estudian solo matemáticas?
"""

"""
PROBLEMA 107
────────────────────────────────────
Hay 50 personas en una fiesta. 30 prefieren té, 25 prefieren café, y 10 prefieren ambos. ¿Cuántos prefieren solo té?
"""

"""
PROBLEMA 108
────────────────────────────────────
En una encuesta: 100 personas usan Twitter, 80 usan Facebook, 60 usan Instagram. Si 30 usan las tres redes, ¿cuál es el mínimo de personas surveyed?
"""

"""
PROBLEMA 109
────────────────────────────────────
Un grupo de 100 personas: 70 speak español, 60 speak francés. ¿Cuál es el mínimo que speak ambos?
"""

"""
PROBLEMA 110
────────────────────────────────────
Hay 40 libros en una biblioteca. 25 son novelas, 20 son rojos. Si 10 son novelas rojas, ¿cuántos NO son novelas ni rojos?
"""

"""
PROBLEMA 111
────────────────────────────────────
En una escuela hay 200 estudiantes. 120 estudian inglés, 100 estudian francés. ¿Cuál es el mínimo que estudian inglés o francés?
"""

"""
PROBLEMA 112
────────────────────────────────────
50 personas tienen mascotas: 30 tienen perros, 25 tienen gatos, 15 tienen ambos. ¿Cuántos tienen solo perros?
"""

"""
PROBLEMA 113
────────────────────────────────────
En un examen: 45 aprobaron matemáticas, 40 aprobaron física. Si 25 aprobaron ambos de 80 estudiantes, ¿cuántos reprobaron ambos?
"""

"""
PROBLEMA 114
────────────────────────────────────
En un concurso: 80 participantes, 50 resolvieron problema A, 60 resolvieron problema B. Si 30 resolvieron ambos, ¿cuántos resolvieron solo A?
"""

"""
PROBLEMA 115
────────────────────────────────────
Un restaurante: 100 clientes, 70 ordered entrada, 60 ordered postre. Si 40 ordered ambos, ¿cuántos ordered solo entrada?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Probabilidad Básica
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 116
────────────────────────────────────
Lanzas una moneda公平的. ¿Cuál es la probabilidad de obtener cara?
"""

"""
PROBLEMA 117
────────────────────────────────────
En una bolsa hay 3 bolas rojas y 7 bolas azules. ¿Cuál es la probabilidad de extraer una bola azul?
"""

"""
PROBLEMA 118
────────────────────────────────────
Lanzas un dado公平的. ¿Cuál es la probabilidad de obtener un número par?
"""

"""
PROBLEMA 119
────────────────────────────────────
En una reunión hay 5 hombres y 10 mujeres. Se escoge una persona al azar. ¿Cuál es la probabilidad de que sea hombre?
"""

"""
PROBLEMA 120
────────────────────────────────────
Extraes una carta de una baraja estándar (52 cartas). ¿Cuál es la probabilidad de que sea un as?
"""

"""
PROBLEMA 121
────────────────────────────────────
Lanzas dos monedas. ¿Cuál es la probabilidad de obtener exactamente una cara?
"""

"""
PROBLEMA 122
────────────────────────────────────
En una caja hay 8 bombones buenos y 2 vencidos. ¿Cuál es la probabilidad de extraer uno vencido?
"""

"""
PROBLEMA 123
────────────────────────────────────
Lanzas un dado dos veces. ¿Cuál es la probabilidad de que la suma sea 7?
"""

"""
PROBLEMA 124
────────────────────────────────────
Extraes sin mirar dos socks de un cajón con 4 negros y 4 blancos. ¿Cuál es la probabilidad de que sean del mismo color?
"""

"""
PROBLEMA 125
────────────────────────────────────
En una rifa participan 100 personas. ¿Cuál es la probabilidad de ganar si compras 1 boleto?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Razonamiento
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 126
────────────────────────────────────
Si A dice la verdad y B miente, y A dice "B miente", ¿quién miente realmente?
"""

"""
PROBLEMA 127
────────────────────────────────────
María es más rápida que Juana, y Juana es más rápida que Carmen. ¿Quién es la más rápida?
"""

"""
PROBLEMA 128
────────────────────────────────────
Si todos los cuadrados son rectángulos, y este objeto es un cuadrado, ¿qué podemos concluir?
"""

"""
PROBLEMA 129
────────────────────────────────────
Hay 3 cajas: una dice "Oro", otra "Plata", otra "Oro o Plata". Solo una es correcta. ¿Dónde está el oro?
"""

"""
PROBLEMA 130
────────────────────────────────────
Si me preguntas, siempre miento. Si esto es verdadero, ¿estoy mintiendo?
"""

"""
PROBLEMA 131
────────────────────────────────────
Cinco personas viven en casas diferentes de colores diferentes. El inglés vive en la casa roja. El español tiene un perro. ¿Quién tiene el perro?
"""

"""
PROBLEMA 132
────────────────────────────────────
Si A > 0 y B > 0, y A × B > A + B, ¿qué puedes concluir?
"""

"""
PROBLEMA 133
────────────────────────────────────
Hay 5 casas de diferentes colores. En cada casa vive una persona de diferente nacionalidad. ¿Puedes deducir quién vive en qué casa?
"""

"""
PROBLEMA 134
────────────────────────────────────
Un granjero tiene cerdos y gallinas. Entre todos tienen 50 cabezas y 140 patas. ¿Cuántos cerdos hay?
"""

"""
PROBLEMA 135
────────────────────────────────────
Si 5 máquinas hacen 5 piezas en 5 minutos, ¿cuánto tiempo tardan 100 máquinas en hacer 100 piezas?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Geometría
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 136
────────────────────────────────────
Un triángulo tiene lados 3, 4, 5. ¿Es un triángulo rectángulo?
"""

"""
PROBLEMA 137
────────────────────────────────────
Calcula el área de un triángulo con base 10 cm y altura 8 cm.
"""

"""
PROBLEMA 138
────────────────────────────────────
Un círculo tiene diámetro 14 cm. Calcula su perímetro.
"""

"""
PROBLEMA 139
────────────────────────────────────
Calcula el volumen de una esfera con radio 6 cm.
"""

"""
PROBLEMA 140
────────────────────────────────────
Un cilindro tiene radio 5 cm y altura 10 cm. Calcula su volumen.
"""

"""
PROBLEMA 141
────────────────────────────────────
Calcula la diagonal de un rectángulo de 6 cm × 8 cm.
"""

"""
PROBLEMA 142
────────────────────────────────────
Un cono tiene radio 3 cm y altura 4 cm. Calcula su volumen.
"""

"""
PROBLEMA 143
────────────────────────────────────
Si el área de un cuadrado es 64 cm², ¿cuál es su perímetro?
"""

"""
PROBLEMA 144
────────────────────────────────────
Calcula el área de un hexágono regular con lado 4 cm.
"""

"""
PROBLEMA 145
────────────────────────────────────
Un prisma rectangular tiene dimensiones 6×4×3 cm. Calcula su volumen.
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de промежуточный уровень
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 146
────────────────────────────────────
Encuentra el dígito que ocupa la posición 1000 en la secuencia: 12345678910111213...
"""

"""
PROBLEMA 147
────────────────────────────────────
Un hombre camina a 5 km/h. ¿Cuántos metros recorre en 30 segundos?
"""

"""
PROBLEMA 148
────────────────────────────────────
Si el 40% de A es igual al 60% de B, ¿cuál es la proporción A:B?
"""

"""
PROBLEMA 149
────────────────────────────────────
Calcula el 25% del 80% de 200.
"""

"""
PROBLEMA 150
────────────────────────────────────
Un reloj se atrasa 5 minutos cada día. ¿Cuántos días tardará en atrasarse 2 horas?
"""

# ═══════════════════════════════════════════════════════════════════
#                    NIVEL INTERMEDIO (151-350)
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 151
────────────────────────────────────
Dos números suman 50. El triple del primero menos el segundo es 30. ¿Cuáles son los números?
"""

"""
PROBLEMA 152
────────────────────────────────────
La diferencia entre dos números es 12. El cociente entre ellos es 4. ¿Cuáles son?
"""

"""
PROBLEMA 153
────────────────────────────────────
Un número más su inverso (1/x) es 2.5. ¿Cuál es el número?
"""

"""
PROBLEMA 154
────────────────────────────────────
La suma de tres números consecutivos es 45. ¿Cuáles son?
"""

"""
PROBLEMA 155
────────────────────────────────────
Dos números están en razón 3:5. Su suma es 48. ¿Cuáles son?
"""

"""
PROBLEMA 156
────────────────────────────────────
El producto de dos números es 96 y su diferencia es 4. ¿Cuáles son?
"""

"""
PROBLEMA 157
────────────────────────────────────
Un número es 5 más que otro. El doble del mayor menos el menor es 22. ¿Cuáles son?
"""

"""
PROBLEMA 158
────────────────────────────────────
Tres veces un número más 5 equivale a 50. ¿Cuál es el número?
"""

"""
PROBLEMA 159
────────────────────────────────────
La raíz cuadrada de un número más 10 es 15. ¿Cuál es el número?
"""

"""
PROBLEMA 160
────────────────────────────────────
Un número aumentado en su 20% es igual a 60. ¿Cuál es el número?
"""

"""
PROBLEMA 161
────────────────────────────────────
Dos hermanos tienen edades que suman 30 años. El mayor tiene el doble de edad que el menor. ¿Qué edad tiene cada uno?
"""

"""
PROBLEMA 162
────────────────────────────────────
Si a un número le restas 5 y lo divides entre 3, obtienes 7. ¿Cuál es el número?
"""

"""
PROBLEMA 163
────────────────────────────────────
La edad de un padre es 4 veces la de su hijo. En 20 años, será solo el doble. ¿Qué edad tienen ahora?
"""

"""
PROBLEMA 164
────────────────────────────────────
Un estudiante obtuvo 80 puntos en matemáticas y 70 en ciencias. El promedio fue 76. ¿Cuántas materias tomó?
"""

"""
PROBLEMA 165
────────────────────────────────────
La suma de las cifras de un número de dos dígitos es 12. El dígito de las decenas es el doble del de las unidades. ¿Cuál es el número?
"""

"""
PROBLEMA 166
────────────────────────────────────
Un número de tres cifras tiene la suma de cifras igual a 15. La cifra de las centenas es el triple de las unidades. ¿Cuál es el número?
"""

"""
PROBLEMA 167
────────────────────────────────────
El perímetro de un rectángulo es 30 cm. Su largo es el doble del ancho más 3 cm. ¿Cuáles son las dimensiones?
"""

"""
PROBLEMA 168
────────────────────────────────────
El área de un rectángulo es 48 cm². Su largo es 4 cm mayor que el ancho. ¿Cuáles son las dimensiones?
"""

"""
PROBLEMA 169
────────────────────────────────────
Un triángulo rectángulo tiene perímetro 24 cm. Los catetos miden 6 cm y 8 cm. ¿Cuánto mide la hipotenusa?
"""

"""
PROBLEMA 170
────────────────────────────────────
El volumen de un cubo es 125 cm³. ¿Cuánto mide su arista?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Torres y Boxes
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 171
────────────────────────────────────
Para construir una torre se necesitan 100 bloques. El primer nivel tiene 20 bloques, y cada nivel superior tiene 2 menos. ¿Cuántos niveles puede tener?
"""

"""
PROBLEMA 172
────────────────────────────────────
Una pila de cajas tiene 10 en la base, 8 en el siguiente nivel, y así sucesivamente. Si hay 5 niveles, ¿cuántas cajas hay en total?
"""

"""
PROBLEMA 173
────────────────────────────────────
Se acomodan pelotas en un triángulo: 1 en la primera fila, 2 en la segunda, etc. Si hay 10 filas, ¿cuántas pelotas hay?
"""

"""
PROBLEMA 174
────────────────────────────────────
Un edificio tiene 20 pisos. El primer piso tiene 15 departamentos, y cada piso siguiente tiene 2 menos. ¿Cuántos departamentos hay?
"""

"""
PROBLEMA 175
────────────────────────────────────
Se apilan sogas: la primera mide 10m, la siguiente 9m, y así sucesivamente. ¿Cuántas sogas hay si miden 0.5m cada nudo?
"""

"""
PROBLEMA 176
────────────────────────────────────
Un triangulo tiene bolas numeradas. La fila 1 tiene 1 bola, la fila 2 tiene 2, etc. Si la suma es 78, ¿cuántas filas hay?
"""

"""
PROBLEMA 177
────────────────────────────────────
Se acomodan cuadros en forma de L. La primera tiene 1, la segunda tiene 3, la tercera tiene 6. ¿Cuántas cuadros tiene la quinta?
"""

"""
PROBLEMA 178
────────────────────────────────────
Un hotel tiene habitaciones en forma de cuadrado mágico. Si la primera tiene 1 habitación, la segunda tiene 4, la tercera 9. ¿Cuántas hay en la número 10?
"""

"""
PROBLEMA 179
────────────────────────────────────
Se construye una pirámide triangular. La base tiene 10 balls, la siguiente fila tiene 9, etc. ¿Cuántas balls hay en total?
"""

"""
PROBLEMA 180
────────────────────────────────────
Un stack de pratos: el primero tiene 1 prato, el segundo 2, el tercero 3. Si hay 15 pratos en total, ¿cuántos niveles hay?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Calendario y Tiempo
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 181
────────────────────────────────────
¿Qué día de la semana fue el 1 de enero de 2000?
"""

"""
PROBLEMA 182
────────────────────────────────────
Si el 15 de marzo es miércoles, ¿qué día será el 15 de mayo?
"""

"""
PROBLEMA 183
────────────────────────────────────
Un reloj marca las 3:00. ¿Qué ángulo forman las agujas?
"""

"""
PROBLEMA 184
────────────────────────────────────
Un reloj se atrasa 3 minutos cada hora. ¿Cuántas horas tardará en atrasarse 1 hora completa?
"""

"""
PROBLEMA 185
────────────────────────────────────
A las 6:00, ¿qué ángulo forman las agujas del reloj?
"""

"""
PROBLEMA 186
────────────────────────────────────
Si hoy es lunes, ¿qué día de la semana será dentro de 1000 días?
"""

"""
PROBLEMA 187
────────────────────────────────────
Un año tiene 365 días. ¿Cuántas semanas completas tiene?
"""

"""
PROBLEMA 188
────────────────────────────────────
Febrero de 2024 tiene 29 días porque es año bisiesto. ¿Cuántos años bisiestos hay entre 2000 y 2024?
"""

"""
PROBLEMA 189
────────────────────────────────────
A las 9:15, ¿cuál es el ángulo entre las agujas?
"""

"""
PROBLEMA 190
────────────────────────────────────
Si un evento ocurre cada 8 días y otro cada 12 días, ¿cada cuántos días coincidirán?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Caminos y Rutas
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 191
────────────────────────────────────
De la ciudad A a la B hay 3 caminos, de B a C hay 4. ¿De cuántas formas puedes ir de A a C?
"""

"""
PROBLEMA 192
────────────────────────────────────
Un auto puede tomar 2 rutas de X a Y, y 3 de Y a Z. ¿Cuántas rutas diferentes hay de X a Z?
"""

"""
PROBLEMA 193
────────────────────────────────────
En un tablero de 2×3, ¿cuántos caminos cortos hay del punto A al punto B (solo derecha y abajo)?
"""

"""
PROBLEMA 194
────────────────────────────────────
De tu casa a la escuela hay 4 calles para ir y 4 para volver. ¿Cuántas rutas distintas puedes tomar?
"""

"""
PROBLEMA 195
────────────────────────────────────
En un laberinto de 3×3, ¿cuántos movimientos mínimos necesitas para ir de una esquina a la opuesta?
"""

"""
PROBLEMA 196
────────────────────────────────────
Puedes moverte 1 o 2 pasos. ¿De cuántas formas puedes subir 5 escaleras?
"""

"""
PROBLEMA 197
────────────────────────────────────
En una cuadrícula 4×4, ¿cuántos cuadrados puedes formar?
"""

"""
PROBLEMA 198
────────────────────────────────────
Un虫子 se mueve 1 step right o 1 step up. ¿Cuántos paths hay de (0,0) a (3,3)?
"""

"""
PROBLEMA 199
────────────────────────────────────
De A a B hay 3 caminos, de B a C hay 2, y hay un camino directo de A a C. ¿Cuántas formas de ir de A a C?
"""

"""
PROBLEMA 200
────────────────────────────────────
Puedes subir escalera de 1 o 2 escalones. ¿De cuántas formas puedes subir 10 escalones?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Dados y Cartas
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 201
────────────────────────────────────
Lanzas un dado. ¿Cuál es la probabilidad de obtener un número mayor que 4?
"""

"""
PROBLEMA 202
────────────────────────────────────
Lanzas dos dados. ¿Cuál es la probabilidad de que la suma sea 9?
"""

"""
PROBLEMA 203
────────────────────────────────────
En una baraja de 52 cartas, ¿cuál es la probabilidad de obtener un corazón?
"""

"""
PROBLEMA 204
────────────────────────────────────
Lanzas tres monedas. ¿Cuál es la probabilidad de obtener exactamente 2 caras?
"""

"""
PROBLEMA 205
────────────────────────────────────
En una baraja, ¿cuál es la probabilidad de obtener una carta roja que sea par?
"""

"""
PROBLEMA 206
────────────────────────────────────
Lanzas un dado 3 veces. ¿Cuál es la probabilidad de obtener tres 6s seguidos?
"""

"""
PROBLEMA 207
────────────────────────────────────
Extraes 2 cartas sin reemplazo. ¿Cuál es la probabilidad de que ambas sean ases?
"""

"""
PROBLEMA 208
────────────────────────────────────
En una caja hay 5 bolas rojas, 3 azules, 2 verdes. ¿Cuál es la probabilidad de extraer una bola roja o verde?
"""

"""
PROBLEMA 209
────────────────────────────────────
Lanzas dos dados. ¿Cuál es la probabilidad de que el primer dado sea mayor que el segundo?
"""

"""
PROBLEMA 210
────────────────────────────────────
Un dado está cargado. P(1)=P(2)=P(3)=1/12, P(4)=P(5)=P(6)=1/4. ¿Cuál es P(obtener par)?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Combinatoria
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 211
────────────────────────────────────
¿De cuántas formas puedes elegir 3 personas de un grupo de 10?
"""

"""
PROBLEMA 212
────────────────────────────────────
¿De cuántas formas puedes arreglar 5 libros en un estante?
"""

"""
PROBLEMA 213
────────────────────────────────────
Un equipo tiene 8 jugadores. ¿De cuántas formas puedes elegir un capitán y un副capitán?
"""

"""
PROBLEMA 214
────────────────────────────────────
¿De cuántas formas puedes formar un committee de 3 personas de 7?
"""

"""
PROBLEMA 215
────────────────────────────────────
Un password consiste de 2 letras seguidas de 2 dígitos. ¿Cuántos passwords son posibles?
"""

"""
PROBLEMA 216
────────────────────────────────────
¿De cuántas formas puedes sentar 4 personas en una mesa redonda?
"""

"""
PROBLEMA 217
────────────────────────────────────
Con las letras A,B,C,D,E, ¿cuántas palabras de 3 letras puedes formar (sin repetición)?
"""

"""
PROBLEMA 218
────────────────────────────────────
En una lotería hay 6 números winners de 49. ¿Cuántas combinaciones posibles hay?
"""

"""
PROBLEMA 219
────────────────────────────────────
¿De cuántas formas puedes distribuir 5 premios diferentes entre 3 personas?
"""

"""
PROBLEMA 220
────────────────────────────────────
Un código tiene 4 dígitos. ¿Cuántos códigos tienen al menos un dígito repetido?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Progresión
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 221
────────────────────────────────────
El primer término de una progresión aritmética es 5 y la diferencia es 3. ¿Cuál es el término 20?
"""

"""
PROBLEMA 222
────────────────────────────────────
El primer término es 2, el último es 50, hay 12 términos. ¿Cuál es la diferencia?
"""

"""
PROBLEMA 223
────────────────────────────────────
El primer término de una progresión geométrica es 2 y la razón es 3. ¿Cuál es el término 6?
"""

"""
PROBLEMA 224
────────────────────────────────────
Suma los primeros 15 términos de: 5, 10, 15, 20...
"""

"""
PROBLEMA 225
────────────────────────────────────
El término 5 es 20 y el término 10 es 40. ¿Cuál es el término 15?
"""

"""
PROBLEMA 226
────────────────────────────────────
Una progresión aritmética tiene a1=3, d=4. Suma los primeros 10 términos.
"""

"""
PROBLEMA 227
────────────────────────────────────
En una progresión geométrica, el 3er término es 8 y el 5to es 32. ¿Cuál es la razón?
"""

"""
PROBLEMA 228
────────────────────────────────────
El término 4 de una PA es 14 y la diferencia es 3. ¿Cuál es el primer término?
"""

"""
PROBLEMA 229
────────────────────────────────────
Calcula la suma: 1 + 1/2 + 1/4 + 1/8 + ... (infinito)
"""

"""
PROBLEMA 230
────────────────────────────────────
En una PA, a3 + a7 = 20. Si la diferencia es 2, ¿cuál es a5?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Fracciones
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 231
────────────────────────────────────
Simplifica: 24/36
"""

"""
PROBLEMA 232
────────────────────────────────────
Ordena de menor a mayor: 3/4, 2/3, 5/6
"""

"""
PROBLEMA 233
────────────────────────────────────
Calcula: 2/3 + 1/4
"""

"""
PROBLEMA 234
────────────────────────────────────
Calcula: 3/5 × 10/9
"""

"""
PROBLEMA 235
────────────────────────────────────
Calcula: 5/8 ÷ 3/4
"""

"""
PROBLEMA 236
────────────────────────────────────
¿Qué fracción de la hora son 45 minutos?
"""

"""
PROBLEMA 237
────────────────────────────────────
Un Worker recibe 3/7 de $140. ¿Cuánto recibe?
"""

"""
PROBLEMA 238
────────────────────────────────────
Calcula: 0.75 como fracción simplificada.
"""

"""
PROBLEMA 239
────────────────────────────────────
Expresa 3/8 como decimal.
"""

"""
PROBLEMA 240
────────────────────────────────────
El 60% de un número es 30. ¿Cuál es el número?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Trabajo y Eficiencia
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 241
────────────────────────────────────
Un Worker hace un trabajo en 6 horas. Otro lo hace en 9 horas. ¿Cuánto tardan juntos?
"""

"""
PROBLEMA 242
────────────────────────────────────
3 máquinas producen 100 unidades en 5 horas. ¿Cuántas unidades producen 5 máquinas en 8 horas?
"""

"""
PROBLEMA 243
────────────────────────────────────
Un grifo llena un tanque en 4 horas. Otro lo vacía en 6 horas. ¿Cuánto tiempo tarda en llenarse?
"""

"""
PROBLEMA 244
────────────────────────────────────
Si 5 personas pintan una casa en 8 días, ¿cuántas personas se necesitan para pintarla en 4 días?
"""

"""
PROBLEMA 245
────────────────────────────────────
Un auto recorre 240 km con 20 litros. ¿Cuántos litros necesita para 600 km?
"""

"""
PROBLEMA 246
────────────────────────────────────
Una máquina produce 200 piezas en 4 horas. ¿Cuántas piezas produce en 7 horas?
"""

"""
PROBLEMA 247
────────────────────────────────────
Dos trabajadores juntos ganan $100 en 5 horas. Uno gana $4/hora más que el otro. ¿Cuánto gana cada uno?
"""

"""
PROBLEMA 248
────────────────────────────────────
Un tren sale de A a 60 km/h. Otro sale de B a 80 km/h hacia A. Se encuentran en 3 horas. ¿Cuál es la distancia AB?
"""

"""
PROBLEMA 249
────────────────────────────────────
Un nadador nada a favor de la corriente a 15 km/h y en contra a 5 km/h. ¿Cuál es su velocidad en agua quieta?
"""

"""
PROBLEMA 250
────────────────────────────────────
Un bicycle recorre 60 km. El tiempo de ida es 3 horas y el de vuelta es 2 horas. ¿Cuál es la velocidad promedio?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Mezclas
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 251
────────────────────────────────────
Tienes 20 litros al 30% de sal. ¿Cuántos litros de agua pura agregar para que sea 10%?
"""

"""
PROBLEMA 252
────────────────────────────────────
Mezclas 10 kg a $8/kg con 20 kg a $12/kg. ¿Cuál es el precio por kg de la mezcla?
"""

"""
PROBLEMA 253
────────────────────────────────────
Un vaso de 200 ml tiene 40% jugo. ¿Cuánto jugo hay en el vaso?
"""

"""
PROBLEMA 254
────────────────────────────────────
Si reduces el contenido de sal de 50 kg al 20% a 50 kg al 10%, ¿cuánta agua agregaste?
"""

"""
PROBLEMA 255
────────────────────────────────────
Un alloy tiene 70% cobre y 30% zinc. ¿Cuánto zinc hay en 500g de alloy?
"""

"""
PROBLEMA 256
────────────────────────────────────
Mezclas soluciones: 10L al 5% + 15L al 15%. ¿Cuál es la concentración final?
"""

"""
PROBLEMA 257
────────────────────────────────────
Si evaporas 10 kg de agua marina (3% sal), ¿cuánta sal queda?
"""

"""
PROBLEMA 258
────────────────────────────────────
Un contenedor tiene 100L al 40%. Sacas 20L y agregas 20L de agua. ¿Cuál es la nueva concentración?
"""

"""
PROBLEMA 259
────────────────────────────────────
Mezclas 5kg de arroz a $10/kg con 15kg a $15/kg. ¿A qué precio vendes para ganar 20%?
"""

"""
PROBLEMA 260
────────────────────────────────────
Si el precio baja de $80 a $50, ¿cuál es el porcentaje de disminución?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Matrices
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 261
────────────────────────────────────
Suma las diagonales de una matriz 3×3.
"""

"""
PROBLEMA 262
────────────────────────────────────
Multiplica matrices 2×3 por 3×2.
"""

"""
PROBLEMA 263
────────────────────────────────────
Calcula el determinante de una matriz 2×2.
"""

"""
PROBLEMA 264
────────────────────────────────────
Invierte una matriz 2×2.
"""

"""
PROBLEMA 265
────────────────────────────────────
Calcula la transpuesta de una matriz 3×2.
"""

"""
PROBLEMA 266
────────────────────────────────────
Si A+B = [[1,2],[3,4]] y A = [[1,0],[0,1]], ¿cuál es B?
"""

"""
PROBLEMA 267
────────────────────────────────────
Multiplica [[1,2],[3,4]] × 2.
"""

"""
PROBLEMA 268
────────────────────────────────────
Calcula el trace de [[1,2,3],[4,5,6],[7,8,9]].
"""

"""
PROBLEMA 269
────────────────────────────────────
¿Son perpendiculares los vectores (1,2) y (-2,1)?
"""

"""
PROBLEMA 270
────────────────────────────────────
Calcula la norma del vector (3,4).
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Grafos
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 271
────────────────────────────────────
Un grafo tiene 5 vértices y 7 aristas. ¿Es posible? Explica.
"""

"""
PROBLEMA 272
────────────────────────────────────
El grado de cada vértice en un grafo es 3. Si hay 6 vértices, ¿cuántas aristas hay?
"""

"""
PROBLEMA 273
────────────────────────────────────
En un grafo, el camino más corto entre A y B es 5. ¿Puede haber un camino más largo de A a B?
"""

"""
PROBLEMA 274
────────────────────────────────────
Un grafo tiene 4 vértices. ¿Cuál es el máximo número de aristas sin ciclos?
"""

"""
PROBLEMA 275
────────────────────────────────────
Si un grafo es completo con n vértices, ¿cuántas aristas tiene?
"""

"""
PROBLEMA 276
────────────────────────────────────
Un árbol tiene 10 vértices. ¿Cuántas aristas tiene?
"""

"""
PROBLEMA 277
────────────────────────────────────
Un ciclo tiene n vértices. ¿Cuántas aristas tiene?
"""

"""
PROBLEMA 278
────────────────────────────────────
El grado mínimo de un grafo es k. ¿Cuál es el tamaño máximo del conjunto independiente?
"""

"""
PROBLEMA 279
────────────────────────────────────
En un bipartite graph con bipartición (3,4), ¿cuántas aristas hay como máximo?
"""

"""
PROBLEMA 280
────────────────────────────────────
Un Eulerian trail existe si hay exactamente 0 o 2 vértices de grado impar. ¿Es el grafo traversable?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Árboles
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 281
────────────────────────────────────
Un binary tree tiene altura 4. ¿Cuál es el máximo número de nodos?
"""

"""
PROBLEMA 282
────────────────────────────────────
Un tree con 15 nodos tiene 10 hojas. ¿Cuántos nodos internos hay?
"""

"""
PROBLEMA 283
────────────────────────────────────
Un BST tiene 10 nodos. ¿Cuál es la altura máxima posible?
"""

"""
PROBLEMA 284
────────────────────────────────────
Un binary tree tiene 8 hojas. ¿Cuál es el mínimo número de nodos internos?
"""

"""
PROBLEMA 285
────────────────────────────────────
Un tree con n nodos tiene n-1 aristas. ¿Por qué?
"""

"""
PROBLEMA 286
────────────────────────────────────
Un heap tiene 20 elementos. ¿Cuál es la posición del último nodo no-hoja?
"""

"""
PROBLEMA 287
────────────────────────────────────
Un BST tiene elementos 10,5,15. Si insertas 7, ¿dónde queda?
"""

"""
PROBLEMA 288
────────────────────────────────────
Un binary tree tiene preorder: A,B,D,E,C,F. ¿Cuál es el inorder si el raíz es A?
"""

"""
PROBLEMA 289
────────────────────────────────────
Un tree tiene profundidad 3. ¿Cuál es el máximo número de nodos?
"""

"""
PROBLEMA 290
────────────────────────────────────
Un binary tree tiene 31 nodos. ¿Cuál es su altura mínima?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Algoritmos
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 291
────────────────────────────────────
Ordena [5,2,8,1,9] con bubble sort. ¿Cuántas comparaciones necesitas?
"""

"""
PROBLEMA 292
────────────────────────────────────
Con binary search en un array de 1000 elementos, ¿cuántas iteraciones máximo?
"""

"""
PROBLEMA 293
────────────────────────────────────
Merge sort tiene complejidad O(n log n). ¿Cuántas operaciones para n=1000?
"""

"""
PROBLEMA 294
────────────────────────────────────
El Big O de buscar en lista es O(n). ¿Cuánto tiempo para n=10000?
"""

"""
PROBLEMA 295
────────────────────────────────────
Un algoritmo tiene dos loops anidados de n. ¿Cuál es su complejidad?
"""

"""
PROBLEMA 296
────────────────────────────────────
El tiempo de búsqueda en hash table es O(1). ¿Por qué?
"""

"""
PROBLEMA 297
────────────────────────────────────
Quick sort tiene peor caso O(n²). ¿Cuándo ocurre?
"""

"""
PROBLEMA 298
────────────────────────────────────
Para n=1000, ¿cuál es más rápido: O(n log n) u O(n²)?
"""

"""
PROBLEMA 299
────────────────────────────────────
Un algoritmo divide el problema a la mitad cada vez. ¿Cuántas iterations para n=1000000?
"""

"""
PROBLEMA 300
────────────────────────────────────
Space complexity de recursive Fibonacci sin memoization es O(n). ¿Por qué?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Programación Dinámica
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 301
────────────────────────────────────
Fibonacci(10) con programación dinámica usa O(n) tiempo. ¿Cuántas llamadas recursivas evita?
"""

"""
PROBLEMA 302
────────────────────────────────────
Para coin change con monedas [1,5,10,25] y amount=30, ¿cuál es el mínimo número de monedas?
"""

"""
PROBLEMA 303
────────────────────────────────────
En subset sum con n=5, ¿cuántos subconjuntos son posibles?
"""

"""
PROBLEMA 304
────────────────────────────────────
Knapsack con weights [2,3,4,5] y values [3,4,5,6], capacity=5. ¿Cuál es el máximo valor?
"""

"""
PROBLEMA 305
────────────────────────────────────
Longest common subsequence de "ABCD" y "ACBD". ¿Cuál es su longitud?
"""

"""
PROBLEMA 306
────────────────────────────────────
Coin change: ¿cuántas formas de hacer 5 con [1,2,5]?
"""

"""
PROBLEMA 307
────────────────────────────────────
Maximum subarray en [-2,1,-3,4,-1,2,1,-5,4]. ¿Cuál es la suma máxima?
"""

"""
PROBLEMA 308
────────────────────────────────────
Edit distance entre "kitten" y "sitting".
"""

"""
PROBLEMA 309
────────────────────────────────────
House robber en [1,2,3,1]. ¿Cuál es el máximo?
"""

"""
PROBLEMA 310
────────────────────────────────────
Climbing stairs con 10 escalones, puedes tomar 1 o 2. ¿De cuántas formas?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Grafos y Redes
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 311
────────────────────────────────────
BFS desde A alcanza nodos B,C,D. ¿Cuántas aristas se visitaron?
"""

"""
PROBLEMA 312
────────────────────────────────────
Dijkstra desde A: distancias [0,4,∞,∞]. La siguiente arista es A-B con peso 4. ¿Por qué?
"""

"""
PROBLEMA 313
────────────────────────────────────
Un MST tiene 5 nodos y 4 aristas. ¿Son únicas?
"""

"""
PROBLEMA 314
────────────────────────────────────
DFS traversal de un grafo con 6 nodos. ¿Cuántas llamadas recursivas máximo?
"""

"""
PROBLEMA 315
────────────────────────────────────
El graph coloring problema: ¿cuántos colors mínimo para bipartito?
"""

"""
PROBLEMA 316
────────────────────────────────────
En Ford-Fulkerson, el flujo máximo es 10. ¿Cuántos augmenting paths encontró?
"""

"""
PROBLEMA 317
────────────────────────────────────
Topological sort de A→B→C. ¿Cuántos orderings posibles?
"""

"""
PROBLEMA 318
────────────────────────────────────
Un connected graph tiene 7 vértices y 6 aristas. ¿Es un árbol?
"""

"""
PROBLEMA 319
────────────────────────────────────
PageRank de un nodo sin outgoing links.
"""

"""
PROBLEMA 320
────────────────────────────────────
Kruskal vs Prim en dense graph. ¿Cuál es más eficiente?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Búsqueda
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 321
────────────────────────────────────
Binary search en [1,3,5,7,9,11,13] buscando 7. ¿En qué índice está?
"""

"""
PROBLEMA 322
────────────────────────────────────
Linear search hace n comparaciones. Para n=1000000, ¿cuántas?
"""

"""
PROBLEMA 323
────────────────────────────────────
Interpolation search: ¿cuándo es mejor que binary search?
"""

"""
PROBLEMA 324
────────────────────────────────────
Search en hash table con separate chaining. ¿Cuál es el worst case?
"""

"""
PROBLEMA 325
────────────────────────────────────
BFS encuentra shortest path en graph no ponderado. ¿Por qué?
"""

"""
PROBLEMA 326
────────────────────────────────────
A* usa heurística. ¿Cuándo es admissible?
"""

"""
PROBLEMA 327
────────────────────────────────────
Bidirectional search reduce complejidad de O(b^d) a O(b^(d/2)). ¿Cuánto para b=2, d=10?
"""

"""
PROBLEMA 328
────────────────────────────────────
Depth-first search en tree de 100 niveles. ¿Cuánta memoria necesita?
"""

"""
PROBLEMA 329
────────────────────────────────────
Jump search con block size √n. ¿Cuál es su complejidad?
"""

"""
PROBLEMA 330
────────────────────────────────────
Exponential search vs binary search para unbounded arrays.
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Ordenamiento
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 331
────────────────────────────────────
Merge sort: ¿por qué es estable?
"""

"""
PROBLEMA 332
────────────────────────────────────
Quick sort con pivot = first element. ¿Cuándo tiene peor caso?
"""

"""
PROBLEMA 333
────────────────────────────────────
Counting sort: ¿para qué valores de n es mejor que quicksort?
"""

"""
PROBLEMA 334
────────────────────────────────────
Heap sort: ¿cuál es su complejidad siempre?
"""

"""
PROBLEMA 335
────────────────────────────────────
Radix sort: ¿cuántos passes para números hasta 1 millón?
"""

"""
PROBLEMA 336
────────────────────────────────────
Unstable sort algorithms: ¿cuáles son?
"""

"""
PROBLEMA 337
────────────────────────────────────
In-place sorting algorithms: ¿cuáles son?
"""

"""
PROBLEMA 338
────────────────────────────────────
Best case de bubble sort. ¿Cuál es?
"""

"""
PROBLEMA 339
────────────────────────────────────
Space complexity de merge sort.
"""

"""
PROBLEMA 340
────────────────────────────────────
External sorting: ¿cuándo se usa?
"""

# ═══════════════════════════════════════════════════════════════════
#                    NIVEL AVANZADO (351-500)
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 341
────────────────────────────────────
En P vs NP, si P=NP, ¿qué cambia?
"""

"""
PROBLEMA 342
────────────────────────────────────
SAT problem: ¿por qué es NP-complete?
"""

"""
PROBLEMA 343
────────────────────────────────────
Un problema NP-hard puede resolverse en tiempo polinomial si P=NP. Cierto o falso?
"""

"""
PROBLEMA 344
────────────────────────────────────
NP-complete problems: ¿cuál de ellos se puede resolver eficientemente si P=NP?
"""

"""
PROBLEMA 345
────────────────────────────────────
Traveling salesman es NP-hard. ¿Por qué?
"""

"""
PROBLEMA 346
────────────────────────────────────
Si reducimos un problema NP-complete a nuestro problema, ¿qué implica?
"""

"""
PROBLEMA 347
────────────────────────────────────
Clases de complejidad: ¿cuál es la relación entre P, NP y NP-complete?
"""

"""
PROBLEMA 348
────────────────────────────────────
Approximation algorithm: ¿cuándo se usa?
"""

"""
PROBLEMA 349
────────────────────────────────────
Un algoritmo greedy puede NO encontrar solución óptima. Da un ejemplo.
"""

"""
PROBLEMA 350
────────────────────────────────────
Dynamic programming vs memoization: ¿cuál es la diferencia?
"""

"""
PROBLEMA 351
────────────────────────────────────
Undecidable problems: ¿pueden resolverse algorítmicamente?
"""

"""
PROBLEMA 352
────────────────────────────────────
Halting problem: ¿por qué no puede resolverse?
"""

"""
PROBLEMA 353
────────────────────────────────────
Rice's theorem: ¿qué dice?
"""

"""
PROBLEMA 354
────────────────────────────────────
Turing completeness: ¿qué significa?
"""

"""
PROBLEMA 355
────────────────────────────────────
Church-Turing thesis: ¿cuál es su implicación?
"""

"""
PROBLEMA 356
────────────────────────────────────
¿Qué significa que un problema sea decidible?
"""

"""
PROBLEMA 357
────────────────────────────────────
Oracle machines: ¿qué son y para qué sirven?
"""

"""
PROBLEMA 358
────────────────────────────────────
Complexity classes: ¿cuál es la relación entre SPACE y TIME?
"""

"""
PROBLEMA 359
────────────────────────────────────
Co-NP: ¿cuál es su relación con NP?
"""

"""
PROBLEMA 360
────────────────────────────────────
Probabilistic algorithms: ¿qué tipos existen?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Entrevista Técnica
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 361
────────────────────────────────────
Explain Big O notation: ¿qué significa O(1)?
"""

"""
PROBLEMA 362
────────────────────────────────────
Difference between array and linked list.
"""

"""
PROBLEMA 363
────────────────────────────────────
When to use hash table vs binary search tree?
"""

"""
PROBLEMA 364
────────────────────────────────────
Explain recursion and its pros/cons.
"""

"""
PROBLEMA 365
────────────────────────────────────
What is deadlock in operating systems?
"""

"""
PROBLEMA 366
────────────────────────────────────
Difference between process and thread.
"""

"""
PROBLEMA 367
────────────────────────────────────
What is virtual memory?
"""

"""
PROBLEMA 368
────────────────────────────────────
Explain database normalization.
"""

"""
PROBLEMA 369
────────────────────────────────────
SQL vs NoSQL: ¿cuándo usar cada uno?
"""

"""
PROBLEMA 370
────────────────────────────────────
What is ACID in databases?
"""

"""
PROBLEMA 371
────────────────────────────────────
Explain CAP theorem.
"""

"""
PROBLEMA 372
────────────────────────────────────
Microservices vs monolithic architecture.
"""

"""
PROBLEMA 373
────────────────────────────────────
What is load balancing?
"""

"""
PROBLEMA 374
────────────────────────────────────
Explain caching strategies.
"""

"""
PROBLEMA 375
────────────────────────────────────
What is message queue?
"""

"""
PROBLEMA 376
────────────────────────────────────
Difference between HTTP and HTTPS.
"""

"""
PROBLEMA 377
────────────────────────────────────
REST vs GraphQL.
"""

"""
PROBLEMA 378
────────────────────────────────────
What is OAuth?
"""

"""
PROBLEMA 379
────────────────────────────────────
Explain JWT.
"""

"""
PROBLEMA 380
────────────────────────────────────
What is Docker?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Diseño de Sistemas
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 381
────────────────────────────────────
Design a URL shortener service.
"""

"""
PROBLEMA 382
────────────────────────────────────
Design a Twitter feed system.
"""

"""
PROBLEMA 383
────────────────────────────────────
Design a parking lot system.
"""

"""
PROBLEMA 384
────────────────────────────────────
Design an elevator system.
"""

"""
PROBLEMA 385
────────────────────────────────────
Design a chess game.
"""

"""
PROBLEMA 386
────────────────────────────────────
Design a ride-sharing app like Uber.
"""

"""
PROBLEMA 387
────────────────────────────────────
Design a CDN.
"""

"""
PROBLEMA 388
────────────────────────────────────
Design a search autocomplete system.
"""

"""
PROBLEMA 389
────────────────────────────────────
Design a distributed cache.
"""

"""
PROBLEMA 390
────────────────────────────────────
Design a news feed algorithm.
"""

"""
PROBLEMA 391
────────────────────────────────────
Design a distributed job scheduler.
"""

"""
PROBLEMA 392
────────────────────────────────────
Design a file sharing system.
"""

"""
PROBLEMA 393
────────────────────────────────────
Design a chat system.
"""

"""
PROBLEMA 394
────────────────────────────────────
Design a recommendation system.
"""

"""
PROBLEMA 395
────────────────────────────────────
Design a distributed locking mechanism.
"""

"""
PROBLEMA 396
────────────────────────────────────
Design a rate limiter.
"""

"""
PROBLEMA 397
────────────────────────────────────
Design a distributed transaction system.
"""

"""
PROBLEMA 398
────────────────────────────────────
Design a key-value store.
"""

"""
PROBLEMA 399
────────────────────────────────────
Design a web crawler.
"""

"""
PROBLEMA 400
────────────────────────────────────
Design a distributed logger.
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Algoritmos Avanzados
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 401
────────────────────────────────────
Maximum flow: ¿cuál es el algoritmo más común?
"""

"""
PROBLEMA 402
────────────────────────────────────
Minimum spanning tree: ¿cuál algoritmo usar para grafos densos?
"""

"""
PROBLEMA 403
────────────────────────────────────
Shortest path con pesos negativos: ¿qué algoritmo?
"""

"""
PROBLEMA 404
────────────────────────────────────
Strongly connected components: ¿qué algoritmo?
"""

"""
PROBLEMA 405
────────────────────────────────────
LCA in binary tree: ¿cuál es el enfoque más eficiente?
"""

"""
PROBLEMA 406
────────────────────────────────────
Segment tree: ¿para qué se usa?
"""

"""
PROBLEMA 407
────────────────────────────────────
Trie: ¿cuál es su aplicación principal?
"""

"""
PROBLEMA 408
────────────────────────────────────
Fenwick tree: ¿qué operaciones soporta eficientemente?
"""

"""
PROBLEMA 409
────────────────────────────────────
Disjoint Set Union: ¿para qué sirve?
"""

"""
PROBLEMA 410
────────────────────────────────────
Bloom filter: ¿cuál es su trade-off?
"""

"""
PROBLEMA 411
────────────────────────────────────
Skip list: ¿por qué es mejor que linked list?
"""

"""
PROBLEMA 412
────────────────────────────────────
Splay tree: ¿cuál es su propiedad especial?
"""

"""
PROBLEMA 413
────────────────────────────────────
Red-black tree: ¿cuál es su altura máxima?
"""

"""
PROBLEMA 414
────────────────────────────────────
B-tree vs B+tree: ¿cuál es mejor para databases?
"""

"""
PROBLEMA 415
────────────────────────────────────
AVL tree: ¿cuál es la condición de balance?
"""

"""
PROBLEMA 416
────────────────────────────────────
Suffix array: ¿qué permite hacer eficientemente?
"""

"""
PROBLEMA 417
────────────────────────────────────
Burrows-Wheeler transform: ¿para qué sirve?
"""

"""
PROBLEMA 418
────────────────────────────────────
Rabin-Karp: ¿cuál es su ventaja sobre KMP?
"""

"""
PROBLEMA 419
────────────────────────────────────
Aho-Corasick: ¿qué problema resuelve?
"""

"""
PROBLEMA 420
────────────────────────────────────
Manacher's algorithm: ¿qué encuentra?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Concurrencia
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 421
────────────────────────────────────
Race condition: ¿qué es y cómo evitarla?
"""

"""
PROBLEMA 422
────────────────────────────────────
Deadlock: ¿cuáles son las 4 condiciones necesarias?
"""

"""
PROBLEMA 423
────────────────────────────────────
Mutex vs Semaphore: ¿cuál es la diferencia?
"""

"""
PROBLEMA 424
────────────────────────────────────
Thread pool: ¿cuál es su ventaja?
"""

"""
PROBLEMA 425
────────────────────────────────────
Lock-free data structures: ¿cuándo usarlas?
"""

"""
PROBLEMA 426
────────────────────────────────────
ABA problem: ¿qué es?
"""

"""
PROBLEMA 427
────────────────────────────────────
Memory barrier: ¿para qué sirve?
"""

"""
PROBLEMA 428
────────────────────────────────────
Producer-consumer problem: ¿cómo resolverlo?
"""

"""
PROBLEMA 429
────────────────────────────────────
Readers-writers problem: ¿qué estrategia usarías?
"""

"""
PROBLEMA 430
────────────────────────────────────
Starvation: ¿qué lo causa?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Seguridad
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 431
────────────────────────────────────
SQL injection: ¿cómo prevenirlo?
"""

"""
PROBLEMA 432
────────────────────────────────────
XSS attack: ¿qué tipos existen?
"""

"""
PROBLEMA 433
────────────────────────────────────
CSRF: ¿cómo funciona y cómo prevenirlo?
"""

"""
PROBLEMA 434
────────────────────────────────────
Man-in-the-middle attack: ¿cómo funciona?
"""

"""
PROBLEMA 435
────────────────────────────────────
Password hashing: ¿qué algoritmos usar?
"""

"""
PROBLEMA 436
────────────────────────────────────
Digital signature: ¿cómo funciona?
"""

"""
PROBLEMA 437
────────────────────────────────────
Public key infrastructure: ¿qué es?
"""

"""
PROBLEMA 438
────────────────────────────────────
TLS/SSL handshake: ¿cuáles son los pasos?
"""

"""
PROBLEMA 439
────────────────────────────────────
JWT vs session: ¿cuándo usar cada uno?
"""

"""
PROBLEMA 440
────────────────────────────────────
OAuth 2.0 flow: ¿cuáles son los pasos?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Sistemas Distribuidos
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 441
────────────────────────────────────
CAP theorem: ¿qué dice?
"""

"""
PROBLEMA 442
────────────────────────────────────
Consistent hashing: ¿cuál es su ventaja?
"""

"""
PROBLEMA 443
────────────────────────────────────
Two-phase commit: ¿para qué sirve?
"""

"""
PROBLEMA 444
────────────────────────────────────
Raft consensus algorithm: ¿cuáles son los roles?
"""

"""
PROBLEMA 445
────────────────────────────────────
Gossip protocol: ¿cuál es su ventaja?
"""

"""
PROBLEMA 446
────────────────────────────────────
Leader election: ¿cómo funciona Raft?
"""

"""
PROBLEMA 447
────────────────────────────────────
Vector clocks: ¿para qué sirven?
"""

"""
PROBLEMA 448
────────────────────────────────────
Read-after-write consistency: ¿qué garantiza?
"""

"""
PROBLEMA 449
────────────────────────────────────
Sharding: ¿cuáles son las estrategias?
"""

"""
PROBLEMA 450
────────────────────────────────────
Database replication: syncrhonous vs asynchronous.
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Machine Learning Concepts
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 451
────────────────────────────────────
Overfitting: ¿cómo detectarlo y prevenirlo?
"""

"""
PROBLEMA 452
────────────────────────────────────
Bias-variance tradeoff: ¿qué significa?
"""

"""
PROBLEMA 453
────────────────────────────────────
Cross-validation: ¿por qué usarla?
"""

"""
PROBLEMA 454
────────────────────────────────────
Regularization: ¿qué tipos conoces?
"""

"""
PROBLEMA 455
────────────────────────────────────
Gradient descent: ¿cómo evitar mínimos locales?
"""

"""
PROBLEMA 456
────────────────────────────────────
Decision tree pruning: ¿cuál es el objetivo?
"""

"""
PROBLEMA 457
────────────────────────────────────
Ensemble methods: ¿qué son?
"""

"""
PROBLEMA 458
────────────────────────────────────
Confusion matrix: ¿qué métricas contiene?
"""

"""
PROBLEMA 459
────────────────────────────────────
ROC curve: ¿qué representa?
"""

"""
PROBLEMA 460
────────────────────────────────────
Clustering: ¿cuál es la diferencia entre k-means y hierarchical?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas de Algoritmos Especiales
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 461
────────────────────────────────────
Floyd's cycle detection: ¿cuál es la fórmula?
"""

"""
PROBLEMA 462
────────────────────────────────────
Dutch national flag: ¿qué problema resuelve?
"""

"""
PROBLEMA 463
────────────────────────────────────
Kadane's algorithm: ¿qué encuentra?
"""

"""
PROBLEMA 464
────────────────────────────────────
LRU cache: ¿cómo funciona?
"""

"""
PROBLEMA 465
────────────────────────────────────
Reservoir sampling: ¿cuándo usarla?
"""

"""
PROBLEMA 466
────────────────────────────────────
Fisher-Yates shuffle: ¿por qué es correcto?
"""

"""
PROBLEMA 467
────────────────────────────────────
Tower of Hanoi: ¿cuál es el mínimo número de movimientos?
"""

"""
PROBLEMA 468
────────────────────────────────────
Eight queens problem: ¿cuántas soluciones hay?
"""

"""
PROBLEMA 469
────────────────────────────────────
Sudoku solver: ¿qué algoritmo usar?
"""

"""
PROBLEMA 470
────────────────────────────────────
Traveling salesman: ¿por qué es NP-hard?
"""

"""
PROBLEMA 471
────────────────────────────────────
Knapsack: ¿cuál es la diferencia entre 0/1 y unbounded?
"""

"""
PROBLEMA 472
────────────────────────────────────
Edit distance: ¿cuál es la fórmula de recurrencia?
"""

"""
PROBLEMA 473
────────────────────────────────────
Longest increasing subsequence: ¿cuál es la complejidad?
"""

"""
PROBLEMA 474
────────────────────────────────────
Counting inversions: ¿qué algoritmo usar?
"""

"""
PROBLEMA 475
────────────────────────────────────
Convex hull: ¿cuál es el algoritmo más común?
"""

"""
PROBLEMA 476
────────────────────────────────────
String matching: ¿cuál es la complejidad de Z algorithm?
"""

"""
PROBLEMA 477
────────────────────────────────────
Cartesian tree: ¿qué propiedades tiene?
"""

"""
PROBLEMA 478
────────────────────────────────────
Rolling hash: ¿cuál es su aplicación?
"""

"""
PROBLEMA 479
────────────────────────────────────
Monotonic stack: ¿para qué sirve?
"""

"""
PROBLEMA 480
────────────────────────────────────
Sliding window maximum: ¿cuál es la complejidad?
"""

# ═══════════════════════════════════════════════════════════════════
#                    Problemas Finales
# ═══════════════════════════════════════════════════════════════════

"""
PROBLEMA 481
────────────────────────────────────
You have two eggs and 100 floors. Find the minimum number of drops to find the highest safe floor.
"""

"""
PROBLEMA 482
────────────────────────────────────
100 prisoners and a light bulb. What is the strategy?
"""

"""
PROBLEMA 483
────────────────────────────────────
Two jars and 100 marbles. How to measure exactly 50?
"""

"""
PROBLEMA 484
────────────────────────────────────
3 bulbs and 3 switches. How to identify which switch controls which bulb with one trip?
"""

"""
PROBLEMA 485
────────────────────────────────────
12 balls, one is different weight. How to find it with 3 weighings?
"""

"""
PROBLEMA 486
────────────────────────────────────
Bridge crossing at night. What's the minimum time?
"""

"""
PROBLEMA 487
────────────────────────────────────
 wolf, goat, cabbage problem. How to solve?
"""

"""
PROBLEMA 488
────────────────────────────────────
Two ropes burning. How to measure 45 minutes?
"""

"""
PROBLEMA 489
────────────────────────────────────
Blue-eyed islanders puzzle. What is the solution?
"""

"""
PROBLEMA 490
────────────────────────────────────
 Monty Hall problem. Should you switch?
"""

"""
PROBLEMA 491
────────────────────────────────────
100 doors toggle. Which ones remain open after n passes?
"""

"""
PROBLEMA 492
────────────────────────────────────
12 clocks, 4 moves each. How to set all to 12 o'clock?
"""

"""
PROBLEMA 493
────────────────────────────────────
 Poisoned wine. How to find the poisoned bottle with minimum tests?
"""

"""
PROBLEMA 494
────────────────────────────────────
3 hats and prisoners. How to guarantee survival?
"""

"""
PROBLEMA 495
────────────────────────────────────
100 pirates and gold coins. What is the optimal strategy?
"""

"""
PROBLEMA 496
────────────────────────────────────
 Chessboard and grains of rice. How many squares to exceed 1 million?
"""

"""
PROBLEMA 497
────────────────────────────────────
Ants on a stick. What is the time until all fall off?
"""

"""
PROBLEMA 498
────────────────────────────────────
 Burning ropes as timers. What times can you measure?
"""

"""
PROBLEMA 499
────────────────────────────────────
Fork and spoon problem. What is the maximum eating time?
"""

"""
PROBLEMA 500
────────────────────────────────────
Induction puzzles: How to solve them systematically?
"""

# ═══════════════════════════════════════════════════════════════════
#                          FIN
# ═══════════════════════════════════════════════════════════════════

"""
¡FELICIDADES!
Has completado los 500 problemas de lógica y razonamiento.

Estos problemas están diseñados para:
- Desarrollar pensamiento algorítmico
- Preparar entrevistas técnicas  
- Mejorar habilidades de resolución de problemas
- Entender conceptos fundamentales

Recuerda: La práctica hace al maestro. ¡Sigue resolviendo!
"""
