#Escribe un programa que lee un número entero por teclado y obtiene y muestra
#por pantalla el doble y el triple de ese número

num = int(input("Introduce un numero entero: "))

doble = num * 2
triple = num * 3

print("Resultado final".center(30, "#"))

print(f'El doble del numero es: {doble}')
print(f'El triple del numero es: {triple}')