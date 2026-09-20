#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
num_horas = int(input("Ingresa el numero de horas: "))
coste = 4.27

resul = num_horas * coste

print(f"El pago correspondiente a las horas trabajadas es: {resul} Nuevos soles")