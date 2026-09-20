# Se tiene un número. Evalúa si es que está en el rango de -18 a 29 o de 90 a 105 
# o en el rango de 140 a 250. De estar en uno de los rangos, se evaluará si el 
# número es positivo; si es verdad, se debe de ingresar 3 números más, y como 
# resultado mostrar el mayor número de estos últimos tres número ingresados; de 
# estar en el rango esperado y de no ser positivo el número ingresado inicialmente, 
# se debe de ingresar dos números, y mostrar como respuesta el menor de estos 
# últimos números ingresados. 

numero = int(input("Introduce un numero de rango"))

rango_uno = numero >= -18 and numero <= 29
rango_dos = numero >= 90 and numero <= 105
rango_tres = numero >= 140 and numero <= 250

if rango_uno or rango_dos or rango_tres:
    if numero > 0:
        print("El numero es positivo")
        numero_1 = int(input("Ingresa el primer numero"))
        numero_2 = int(input("Ingresa el segundo numero"))
        numero_3 = int(input("Ingresa el tercer numero"))

        if numero_1 > numero_2 and numero_1 > numero_3:
            print(f'El numero es mayor {numero_1}')
        elif numero_2 > numero_1 and numero_2 > numero_3:
            print(f'El numero es mayor {numero_2}')
        elif numero_3 > numero_1 and numero_3 > numero_2:
            print(f'El numero es mayor {numero_3}')
    else:
        numero_uno = int(input("Ingresa el primero numero"))
        numero_dos = int(input("Ingresa el segundo numero"))

        if numero_uno < numero_dos:
            print(f'El numero es menor {numero_uno}')
        elif numero_dos < numero_uno:
            print(f'El numero es menor {numero_dos}') 