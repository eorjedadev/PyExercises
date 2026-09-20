#Se lee un número correspondiente al radio de la circunferencia, visualizando la 
#longitud de la misma y el área del círculo correspondiente.  
#Se recuerda:  
#AREA = PI * RADIO2 y LONGITUD = 2 * PI * RADIO 

import math

#Entrada
PI = math.pi
radio = int(input("Introduce el radio: "))
#Proceso
area = PI * radio * 2
longitud = 2 * PI * radio
#Salida
print("Resultado".center(45, "="))
print(f'''La area del circulo es: {area}
    La longitud es: {longitud}''')