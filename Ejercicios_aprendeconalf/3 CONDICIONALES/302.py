#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.


PASSWORD = "contras2026"

if PASSWORD.lower() == input("Ingrese la contraseña: ").lower():
    print("Contraseña correcta.")
else:
    print("Contraseña incorrecta.")