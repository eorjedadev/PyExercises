#Se tiene que calcular el área de un rombo, teniendo en cuenta que:

#AREA=2/(base mayor+base menor)×altura​

#Entrada
base_mayor = int(input("Introducir la base mayor: "))
base_menor = int(input("Introducir la base menor: "))
altura = int(input("Introducir la altura: "))
#Proceso
sum = base_mayor + base_menor
mul = sum * altura
area = mul / 2
#Salida
print("Resultados".center(45, "*"))
print(f"Área del trapecio: {area}")