#Que pida un número del 1 al 7 y diga el día de la semana correspondiente.

#Entrada
semana_numero = int(input("Introduce el numero de la semana:\n"))

#proceso
if semana_numero == 1:
    print('Lunes')
elif semana_numero == 2:
    print('Martes')
elif semana_numero == 3:
    print('Miercoles')
elif semana_numero == 4:
    print('Jueves')
elif semana_numero == 5:
    print('Viernes')
elif semana_numero == 6:
    print('Sabado')
elif semana_numero == 7:
    print('Domingo')
else:
    print('Este numero no es un dia de semana')

#Salida