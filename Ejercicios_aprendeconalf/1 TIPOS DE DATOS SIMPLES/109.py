#Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión.

cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))    
interes_anual = float(input("Ingrese el interés anual: "))    
num_anios = int(input("Ingrese el número de años: "))    

capital_obtenido = cantidad_invertir * (1 + interes_anual) ** num_anios
print(f"El capital obtenido en la inversión es: {capital_obtenido}")