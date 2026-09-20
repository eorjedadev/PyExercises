#Dado un partido de fútbol jugado entre dos equipos A y B, diseñe un algoritmo 
#Que determine el resultado del partido entre ganó A, ganó B o hubo empate.

#Entrada
a = int(input("Ingresa puntos del Equipo A:\n"))
b = int(input("Ingresar puntos del Equipo B:\n"))
#Proceso
if a > b:
    print('Equipo "A" gano el partido!')
elif b > a:
    print('Equipo "B" gano el partido!')
else:
    print('Empate')
