# Desarrolle el programa que lea tres números, y determine si los números fueron 
# ingresados en orden ascendente, descendente o en desorden 

numero = [40, 20, 5]

if numero[0] < numero[1] < numero[2]:
    print("Los números están en orden ascendente.")
elif numero[0] > numero[1] > numero[2]:
    print("Los números están en orden descendente.")
elif numero[0] == numero[1] == numero[2]:
    print("Los números son iguales.")
else:
    print("Los números están en desorden.")
