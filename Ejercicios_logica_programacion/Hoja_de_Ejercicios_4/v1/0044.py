area_casa = float(input("Ingrese el area de la casa: "))
ano_construccion = int(input("Ingrese los años de construcción: "))
material_constru = str(input("Ingrese el material de construcción: "))

if ano_construccion >= 0  and ano_construccion <= 5:
    impuesto = 2.00
elif ano_construccion >= 6 and ano_construccion <= 10:
    impuesto = 1.20
elif ano_construccion >= 11 and ano_construccion <= 15:
    impuesto = 0.85
elif ano_construccion >= 16:
    impuesto = 0.25

if material_constru == "concreto":
    aumento = 25
elif material_constru == "ladrillo":
    aumento = 12
elif material_constru == "adobe":
    aumento = 3

impuesto_base = area_casa * impuesto
aumento_base = impuesto_base * aumento / 100
impuesto_final = impuesto_base + aumento_base

print("".center(50, "="))
print("RESULTADOS ".center(50))
print("".center(50, "="))

print(f'Impuesto Final: {impuesto_final}')