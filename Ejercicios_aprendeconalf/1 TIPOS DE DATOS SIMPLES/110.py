#Una juguetería tiene mucho éxito en dos de sus productos:
#payasos y muñecas. Suele hacer venta por correo y la empresa de 
#logística les cobra por peso de cada paquete así que deben calcular 
#el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
#Cada payaso pesa 112 g y cada muñeca 75 g. 
#Escribir un programa que lea el número de payasos y muñecas vendidos en 
#el último pedido y calcule el peso total del paquete que será enviado.

#Ingresamos constantes

PESO_PAYASO = 112
PESO_MUNECAS = 75

print("Calculadora de peso de paquete de payasos y muñecas".center(50))

pedido = int(input("Ingrese la cantidad de payasos vendidos: "))
pedido2 = int(input("Ingrese la cantidad de muñecas vendidas: "))
peso_total = (pedido * PESO_PAYASO) + (pedido2 * PESO_MUNECAS)
print(f"El peso total del paquete es de {peso_total} gramos")