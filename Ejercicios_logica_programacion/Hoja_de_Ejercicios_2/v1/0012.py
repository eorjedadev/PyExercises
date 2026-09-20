#Calcular el área de un rombo, teniendo en cuenta:

#AREA=
#2
#diagonal mayor×diagonal menor
#	​


#Entrada
mayor = int(input("Introduce el diagonal mayor: "))
menor = int(input("Introduce el diagonal menor: "))
#Proceso
area = mayor * menor / 2
#Salida

print("Resultados".center(45, "*"))
print(f"Área del rombo: {area}")