contador_positivos = 0
contador_negativos = 0
contador_nulos = 0

suma_positivos = 0
suma_negativos = 0

suma_total = 0


for i in range(1,11):
    numero = int(input("Ingresa un numero entero: "))
    suma_total += numero
    
    if numero > 0:
        contador_positivos += 1
        suma_positivos += numero
    if numero < 0:
        contador_negativos += 1
        suma_negativos += numero
    if numero == 0:
        contador_nulos += 1

promedio_total = suma_total / 10
if contador_positivos > 0:
    promedio_positivos = suma_positivos / contador_positivos
else:
    promedio_positivos = 0

if contador_negativos > 0:
    promedio_negativos = suma_negativos / contador_negativos
else:
    promedio_negativos = 0

print("".center(50, "="))
print("RESULTADOS DE IMPRIMIR 10 NUMEROS".center(50))
print("".center(50, "="))
print(f'Cantidad de numeros positivos: {contador_positivos}')
print(f'Cantidad de numeros negativos: {contador_negativos}')
print(f'Cantidad de numeros nulos: {contador_nulos}')
print("".center(50, "*"))
print("RESULTADOS DE LOS PROMEDIOS".center(50))
print("".center(50, "*"))
print(f'Promedio de los numeros positivos: {promedio_positivos}')
print(f'Promedio de los numeros negativos: {promedio_negativos}')
print(f'Promedio total de los numeros: {promedio_total}')
