#Se debe ingresar los nombres y precios de 3 productos diferentes de una 
#farmacia. Imprimir el nombre del producto más barato y el promedio de precio de 
#los tres productos. 

#Entrada
producto1 = "Ibuprofeno"
producto2 = "Aspirina"
producto3 = "Paracetamol"

precio1 = 8
precio2 = 15
precio3 = 18

total = precio1 + precio2 + precio3
promedio = total / 3

#Proceso
if precio1 < precio2 and precio1 < precio3:
    print("".center(50, "*"))
    print("Resultado".center(50))
    print("".center(50, "*"))
    print(f'Producto es mas barato es: {producto1}')
    print(f'El Producto promedio es: {promedio}')
else:
    print("no es el producto mas barato")
#Salida
