#Se debe leer como dato, una hora en el formato de: 
#hora  
#minutos 
#segundos  
#Diga la hora que es un segundo después. 

#Entrada
HORA = int(input("Introducir la hora: "))
MINUTOS = int(input("Introducir los minutos: "))
SEGUNDOS = int(input("Introducir los segundos: "))
#Proceso
SEGUNDOS +=1

if SEGUNDOS == 60:
    SEGUNDOS = 0
    MINUTOS +=1
if MINUTOS == 60:
    MINUTOS = 0
    HORA +=1
if HORA == 24:
    HORA = 0

#Salida

print('---Resultados---')
print(f'''HH:{HORA:02d} MM:{MINUTOS:02d} SS:{SEGUNDOS:02d}''')