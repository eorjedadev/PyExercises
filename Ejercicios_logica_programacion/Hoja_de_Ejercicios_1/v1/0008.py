#Escribir un programa que convierta un número de segundos en su equivalente 
#en minutos y segundos 

MINUTO = 60
#Entrada
segundos = int(input("Ingresa la cantidad de segundos:\n"))
#proceso
obtener_minutos = segundos / MINUTO #cociente
obtener_segundos = segundos % MINUTO #residuo
#Salida

print("Resultados esperados".center(45, "="))
print(f"Minutos: {int(obtener_minutos)} segundos: {obtener_segundos}")