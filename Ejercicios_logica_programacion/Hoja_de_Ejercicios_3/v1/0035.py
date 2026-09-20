# Una empresa registra el sexo, edad y estado civil de sus empleados a través de 
# un número entero positivo de cuatro cifras de acuerdo a lo siguiente: la primera 
# cifra de la izquierda representa el estado civil (1 soltero, 2 casado, 3 divorciado, 
# 4 viudo); las siguientes dos cifras representan la edad y la cuarta cifra representa 
# el sexo (1 masculino, 2 femenino). Desarrolle el programa de determine el estado 
# civil, edad y sexo de un empleado conociendo su número asignado. 


print("".center(50, "="))
print("REGISTRO DE EMPLEADO ASIGNADO".center(50))
print("".center(50, "="))
print()

numero = int(input("Ingrese el número asignado al empleado (4 cifras):"))

edad = (numero // 10) % 100
estado_civil = numero // 1000
sexo = numero % 10

print("".center(50, "*"))
print("Edad del empleado: ".center(50))
print("".center(50, "*"))

print(f"La edad del empleado es: {edad} años.")

print("".center(50, "*"))
print("Estado civil: ".center(50))
print("".center(50, "*"))

if estado_civil == 1:
    print("El empleado es soltero.")
elif estado_civil == 2:
    print("El empleado es casado.")
elif estado_civil == 3:
    print("El empleado es divorciado.")
elif estado_civil == 4:
    print("El empleado es viudo.")

print("".center(50, "*"))
print("Sexo: ".center(50))
print("".center(50, "*"))

if sexo == 1:
    print("El empleado es masculino.")
elif sexo == 2:
    print("El empleado es femenino.")