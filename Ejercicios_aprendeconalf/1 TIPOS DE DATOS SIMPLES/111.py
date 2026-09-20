#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece 
#el 4% de interés al año. Estos ahorros debido a intereses, que no se 
#cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
#Escribir un programa que comience leyendo la cantidad de dinero depositada en la 
#cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y 
#mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
#Redondear cada cantidad a dos decimales.

print("Cuenta de ahorros".center(50, "*"))
dinero_depositado = float(input("Ingrese la cantidad de dinero depositada: "))
INTERES_ANUAL = 0.04

ahorros_1er_año = dinero_depositado * (1 + INTERES_ANUAL)
ahorros_2do_año = ahorros_1er_año * (1 + INTERES_ANUAL)
ahorros_3er_año = ahorros_2do_año * (1 + INTERES_ANUAL)

print(f"La cantidad de ahorros tras el primer año es: {round(ahorros_1er_año, 2)}")
print(f"La cantidad de ahorros tras el segundo año es: {round(ahorros_2do_año, 2)}")
print(f"La cantidad de ahorros tras el tercer año es: {round(ahorros_3er_año, 2)}")