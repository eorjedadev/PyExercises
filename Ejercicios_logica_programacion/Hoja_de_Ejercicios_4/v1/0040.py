# Se debe ingresar dos números. Mostrar como respuesta un mensaje que 
# indique cuál es menor, cuál es mayor o si son iguales.  
 
# Ejemplo:  
# Ingresa 75 22  
# Muestra: El primero es mayor que el segundo  
# Ingresa 16 16  
# Muestra: Ambos números son iguales  
# Ingresa 18 98  
# Muestra: El segundo es mayor que el primero

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))


if num1 > num2:
    print("El primer número es mayor que el segundo.")
elif num1 == num2:
    print("Ambos números son iguales.")
elif num2 > num1:
    print("El segundo número es mayor que el primero.")