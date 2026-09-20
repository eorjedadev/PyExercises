#Diseñe un algoritmo para repartir una cantidad de dinero a tres personas en forma 
#proporcional a sus edades. El monto que le corresponde a cada persona se calcula 
#con la siguiente fórmula: 

#monto de la persona= edad de la persona x monto a repatir / suma total de edades


#Entrada
print("".center(50, "*"))
print("Información de edad de personas".center(50))
print("".center(50, "*"))
edad_1 = int(input("Ingresar la edad de una persona: "))
edad_2 = int(input("Ingresar la edad de una persona: "))
edad_3 = int(input("Ingresar la edad de una persona: "))

print("".center(50, "*"))
print("Introducir monton".center(50))
print("".center(50, "*"))
monto = float(input("Ingresar el monto a repartir (S/.): "))
#Proceso
suma_edades = edad_1 + edad_2 + edad_3
person1 = (edad_1 * monto) / suma_edades
person2 = (edad_2 * monto) / suma_edades
person3 = (edad_3 * monto) / suma_edades 
#Salida

print("".center(50, "*"))
print("INFORMACIÓN DE RESULTADOS".center(50))
print("".center(50, "*"))
print(f"Capital/monto total a repartir\n{monto:.2f}")
print(f'''Monto correspondiente a la persona 1: {person1:.2f}
Monto correspondiente a la persona 2: {person2:.2f}
Monto correspondiente a la persona 3: {person3:.2f}''')
