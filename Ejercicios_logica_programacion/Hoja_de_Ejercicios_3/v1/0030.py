# Una tienda vende un producto a un precio unitario igual a S/. 20. Como oferta, la 
# tienda ofrece un porcentaje de descuento sobre el importe de la compra. 
# Adicionalmente la tienda regala caramelos en base al número de unidades 
# adquiridas del producto. Desarrolle el programa que determine el importe de la 
# compra, el descuento, total a pagar y el número de caramelos del obsequio que 
# se da al cliente por la compra realizada.


PRECIO_UNITARIO = 20
PORCENTAJE = [16, 14, 12]

print("".center(50, "*"))
print("INGRESA LAS CANTIDADES".center(50))
print("".center(50, "*"))
print()
cantidadProducto = int(input("Introduce la cantidad del producto a comprar: \n"))

total_precio = cantidadProducto * PRECIO_UNITARIO

descuento_uno = total_precio * PORCENTAJE[0] / 100
descuento_dos = total_precio * PORCENTAJE[1] / 100
descuento_tres = total_precio * PORCENTAJE[2] / 100


print("".center(50, "="))
print("BOLETA DE LA COMPRA".center(50))
print("".center(50, "="))

if total_precio > 700:
    print(f'Cantidad de producto: {cantidadProducto}')
    print(f'Importe: {total_precio}')
    print(f'Descuento: S/. {descuento_uno:.2f}')
    print(f'Total a pagar: S/.{total_precio - descuento_uno:.2f}')
elif total_precio >= 501:
    print(f'Cantidad de producto: {cantidadProducto}')
    print(f'Importe: {total_precio}')
    print(f'Descuento: S/. {descuento_dos:.2f}')
    print(f'Total a pagar: S/.{total_precio - descuento_dos:.2f}')
elif total_precio < 501:
    print(f'Cantidad de producto: {cantidadProducto}')
    print(f'Importe: {total_precio}')
    print(f'Descuento: S/. {descuento_tres:.2f}')
    print(f'Total a pagar: S/.{total_precio - descuento_tres:.2f}')

print("CARAMELOS DE REGALO".center(50, "*"))
if cantidadProducto <= 50:
    print("Has obtenido 5 caramelos!")
elif cantidadProducto >= 51 and cantidadProducto <= 100:
    print("Has obtenido 10 caramelos!")
elif cantidadProducto > 100:
    print(f'Has obtenido 15 caramelos!')

