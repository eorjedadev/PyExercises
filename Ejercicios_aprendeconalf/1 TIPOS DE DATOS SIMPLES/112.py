#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, 
# el descuento que se le hace por no ser fresca y el coste final total.

PRECIO_BARRA = 3.49
DESCUENTO = 0.60

barras_vendidas = int(input("Ingrese el número de barras vendidas que no son del día: "))
precio_habitual = PRECIO_BARRA
descuento_aplicado = PRECIO_BARRA * DESCUENTO


coste_final = barras_vendidas * (precio_habitual - descuento_aplicado)
print(f"Precio habitual de una barra de pan: {precio_habitual:.2f}€")
print(f"Descuento por no ser fresca: {descuento_aplicado:.2f}€")
print(f"Coste final total: {coste_final:.2f}€")