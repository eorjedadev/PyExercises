#Si un dólar equivale a S/ 3.25 soles. Hacer un algoritmo que imprima en dólares 
#una cantidad X de soles.

#Entrada
USD = float(3.380)
cant_dolares = float(input("Introduce la cantidad de dolares: "))
#Proceso
cambio = cant_dolares * USD
#Salida
print("Boleta de cambio USD a SOL".center(45, "*"))
print(f'''Precio actual USD a SOL S/.{USD}
Cantidad a cambiar en USD ${cant_dolares}
Cambio USD a SOL: S/.{cambio}''')
