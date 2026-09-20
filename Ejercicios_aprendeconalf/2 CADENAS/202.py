#Escribir un programa que pregunte el nombre completo del usuario en la consola y 
#después muestre por pantalla el nombre completo del usuario tres veces, 
#una con todas las letras minúsculas, otra con todas las letras mayúsculas y 
#otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
#El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre_completo = input("Ingrese su nombre completo: ")

print(f"Nombre completo en minúsculas: {nombre_completo.lower()}")
print(f"Nombre completo en mayúsculas: {nombre_completo.upper()}")
print(f"Nombre completo con primera letra en mayúscula: {nombre_completo.title()}")