#Una madre de familia recibirá un bono de acuerdo a su estado civil. Casada 
#recibe S/. 40, soltera S/. 35, viuda S/. 55. Muestre el bono a recibir.

#Entrada
print("".center(50, "*"))
print("BONO DE ACUERDO A SU ESTADO CIVIL".center(50))
print("".center(50, "*"))

estado_civil = input("Introduce tu estado civil: ")
#Proceso
dinero = [40, 35, 55]
if estado_civil == 'casada':
    print(f'La madre recibe S/.{dinero[0]}')
elif estado_civil == 'soltera':
    print(f'La madre recibe S/.{dinero[1]}')
elif estado_civil == 'viuda':
    print(f'La madre recibe S/.{dinero[2]}')
else:
    print('Error introdujo mal el estado')
