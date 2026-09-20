# Desarrollar un programa que nos permita ingresar la edad de una persona y 
# muestre a que etapa de la vida pertenece (Niñez, Infancia, Adolescencia,…)

edad = int(input("Ingrese la edad de la persona: "))

if edad >= 0 and edad <= 12:
    print("La persona se encuentra en la etapa de Niñez.")
elif edad >= 13 and edad <= 19:
    print("La persona se encuentra en la etapa de Adolescencia.")
elif edad >= 20 and edad <= 59:
    print("La persona se encuentra en la etapa de Adultez.")
else:
    print("La persona se encuentra en la etapa de Vejez.")