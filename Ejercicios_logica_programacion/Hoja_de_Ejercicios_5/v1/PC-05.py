numerador = 3
denominador = 4
suma_total = 0

for num in range(1, 11):
    suma_total += numerador / denominador
    print(f'{numerador} / {denominador}')
    numerador += 2
    denominador += 3
print(f'La suma total de la serie es: {suma_total}')

