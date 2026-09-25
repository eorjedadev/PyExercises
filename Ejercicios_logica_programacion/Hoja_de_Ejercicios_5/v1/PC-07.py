print("".center(50, "="))
print("TABLA DEL CUADRADO & CUBO".center(50))
print("".center(50, "="))
print("N°   Cuadrado  Cubo")
for n in range(10, 21):
    cuadrado = n * n
    cubo = n * cuadrado
    print(f'{n}   {cuadrado}      {cubo}')

