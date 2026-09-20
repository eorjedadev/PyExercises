
#Hacer un algoritmo que imprima el nuevo sueldo de un empleado, si tuvo un 
#aumento del 10%. 

AUMENTO = 10


#Entrada
sueldo = float(input("Introduce el sueldo actual del empleado: \n"))
#Proceso
obtener_procentaje = sueldo / 100 * AUMENTO
sumar = sueldo + obtener_procentaje
#Salida
print("Actualización del sueldo del empleado")
print(f'Sueldo anterior: {sueldo}')
print(f"Nuevo sueldo: {sumar}")
