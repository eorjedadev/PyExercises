#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.


print("Bienvenido al programa de verificación de edad.")
edad = int(input("Por favor, ingrese su edad: "))

if edad >= 18:
    print("Usted es mayor de edad.")
else:
    print("Usted no es mayor de edad.")