# Programa que lea una cantidad de grados centígrados y la pase a grados 
# Fahrenheit. La fórmula correspondiente es: F = 32 + ( 9 * C / 5) 
F = 32
#Entrada
c = int(input("Cantidad de grados centigrados (°C)\n"))
#Proceso
mul =  c * 9 
div = mul / 5
sum = div + F
#Salida
print("Convertidor de centigrados (°C) a fahrenheit (°F)")
print(f"Grados Centigrados es : {c}")
print("Resultados de conversión".center(45, "*"))
print(f"Grados Fahrenheit es: {sum} ")