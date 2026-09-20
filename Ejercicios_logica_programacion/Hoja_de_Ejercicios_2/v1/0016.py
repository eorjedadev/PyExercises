# Una tienda ofrece un descuento del 15% sobre el total de la compra, y un cliente 
#desea saber cuánto deberá pagar finalmente por su compra. 

#Entrada
total = float(input("Total de la compra: "))
#Proceso
desc = total * 0.15
result = total - desc
#Salida
print("Total final que debe pagar el cliente")
print("=====================================\n")
print(f"Cantidad a pagar: S/.{result}")