# Programa que determine el monto a pagar por la compra de cierta cantidad de
# unidades de un producto.
producto = {
    'id' : 1,
    'product' : 'laptop',
    'amount' : 1700
}

unit = int(input('¡Ingrese la cantidad que desea comprar!\n'))
total = unit * producto['amount']


print("BOLETA DE COMPRA FIXERGO".center(40, '*'))
print(f'Nombre del producto: {producto["product"].title()}\n'
      f'Precio unitario: ${producto["amount"]:.2f}\n'
      f'Unidades compradas: {unit}\n'
      f'Total: ${total:.2f}')

print("Muchas Gracias por tu compra!")