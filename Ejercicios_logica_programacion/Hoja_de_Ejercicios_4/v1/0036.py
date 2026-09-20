# Se ingresa tres números. Si el tercer número es mayor a los demás, se debe de 
# mostrar el promedio de los números ingresados; de lo contrario evaluar si los 
# tres números son impares, si es así, muestre cada uno de los números con un 
# incremento del 89%. 


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num3 > num1 and num3 > num2:
    promedio = (num1 + num2 + num3) / 3
    print(f"El promedio de los números ingresados es: {promedio}")
else:
    if num1 % 2 == 1 and num2 % 2 == 1 and num3 % 2 == 1:
        print(f"El primer número incrementado en un 89% es: {num1 * 1.89}")
        print(f"El segundo número incrementado en un 89% es: {num2 * 1.89}")
        print(f"El tercer número incrementado en un 89% es: {num3 * 1.89}")