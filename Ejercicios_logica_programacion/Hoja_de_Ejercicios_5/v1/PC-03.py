suma_total = 0

for i in range(1, 11):
    numero = int(input("Ingresa un numero: "))
    suma_total += numero

media = suma_total / 10
print(f'La media aritmética de los numeros es: {media}')