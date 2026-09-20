#Una empresa repartirá un monto de dinero entre sus seis socios de la siguiente
#manera:

monto = float(input("Introduce el monto a repartir: "))
socio_1 = monto * 0.25
socio_2 = monto * 0.10
socio_3 = monto * 0.15
socio_4 = monto * 0.05
socio_5 = monto * 0.20

socio_6 = monto - (
    socio_1 + socio_2 + socio_3 + socio_4 + socio_5
)

socios = [socio_1, socio_2, socio_3, socio_4, socio_5, socio_6]

print("Calculo de monto a repartir para cada socio".center(40, '*'))

for i in range(1, 7):
    print(f"El socio {i} le toca el monto de : ${socios[i - 1 ]:.2f}")




#print(f'Monto a repartir para los socios: {monto}')
#socio1 = monto / 100 * 25
#print(socio1)
