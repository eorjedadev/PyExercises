#Realizar un algoritmo que calcule la posible edad de una persona.

AGE = 2026
birth = int(input("Introduce tu año de nacimiento: "))

results = (f'Tu edad es: '
           f'{AGE - birth}')

print("Calculo de edad".center(20, "*"))
print(results)