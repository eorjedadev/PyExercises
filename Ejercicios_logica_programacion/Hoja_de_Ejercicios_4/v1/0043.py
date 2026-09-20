print("".center(50, "*"))
print("CALCULO DE SUELDO & BONIFICACIÓN".center(50))
print("".center(50, "*"))

prendas_confeccionadas = int(input("Introduce el numero de prendas confeccionadas: "))
tipo_prenda = input("¿Que tipo de prenda confeccionastes?\n")
categoria = input("Introduce tu categoria: ")

if tipo_prenda == "POLO".lower():
    total = prendas_confeccionadas * 0.50
elif tipo_prenda == "CAMISA".lower():
    total = prendas_confeccionadas * 1.00
elif tipo_prenda == "PANTALON".lower():
    total = prendas_confeccionadas * 1.50

if prendas_confeccionadas > 700:
    if categoria == "A":
        bonificacion = 250.00
    elif categoria == "B":
        bonificacion = 150.00
    elif categoria == "C":
        bonificacion = 100.00
    elif categoria == "D":
        bonificacion = 50.00
else:
    bonificacion = 0.00

total_ingreso = total + bonificacion
impuesto = total_ingreso * 9 / 100
seguro = total_ingreso * 2 / 100
solidaridad = total_ingreso * 1 / 100

descuento_total = impuesto + seguro + solidaridad

sueldo_neto = total_ingreso - descuento_total

print("".center(50, "*"))
print("RESULTADOS".center(50))
print("".center(50, "*"))
print(f"Pago por prendas: S/ {total:.2f}")
print(f"Bonificación: S/ {bonificacion:.2f}")
print(f"Ingreso total: S/ {total_ingreso:.2f}")
print(f"Impuesto (9%): S/ {impuesto:.2f}")
print(f"Seguro (2%): S/ {seguro:.2f}")
print(f"Solidaridad (1%): S/ {solidaridad:.2f}")
print(f"Descuento total: S/ {descuento_total:.2f}")
print(f"Sueldo neto: S/ {sueldo_neto:.2f}")
print("".center(50, "*"))
    

