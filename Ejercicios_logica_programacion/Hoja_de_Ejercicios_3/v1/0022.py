#En un estacionamiento, se cobra S/. 2.5 por hora o fracción de hora. Dado el 
#tiempo de estacionamiento de un vehículo expresado indicando las horas y 
#minutos, determine el importe a pagar por concepto de estacionamiento. 

#hora - 2.5
#fraccion - 1.25

#Entrada
print("".center(50, "="))
print("ESTACIONAMIENTO DE VEHICULOS".center(50))
print("".center(50, "="))

hora = int(input('Ingrese la hora: '))
minutos = int(input('Ingrese los minutos: '))
#Proceso
if minutos > 0:
    hora +=1
    horas_cobrables = hora

importe = horas_cobrables * 2.5
#Salida

print(f'Horas cobrables: {horas_cobrables}')
print(f'Importe a pagar: {importe}')
