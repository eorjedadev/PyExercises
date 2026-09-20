#Determine el monto a pagar en el recibo de Agua. Esto depende del consumo 
#de agua por metro cubico donde dicho valor depende de:  
 
#Metro cubico Precio por metro ubico 
#0-20 0.894 
#21-30 1.244 
#31-50 1.737 
#51-80 2.685 
#81 a mas 3.362

#Una renta básica de S/. 14.10, donde se incluye el IGV 
#El monto a pagar se calcula sumando la renta básica y el consumo 


RENTA = float(14.10)
consumo_agua = int(input("Ingresa la cantidad de agua consumida: "))

if consumo_agua >= 0 and consumo_agua <= 20:
    monto_consumo = consumo_agua * 0.894
    monto_total = RENTA + monto_consumo
    print(f'Monto a pagar de recibo de agua es S/.{monto_total:.2f}')
    
elif consumo_agua >= 21 and consumo_agua <= 30:
    monto_consumo = consumo_agua * 1.244
    monto_total = RENTA + monto_consumo
    print(f'Monto a pagar de recibo de agua es S/.{monto_total:.2f}')
elif consumo_agua >= 31 and consumo_agua <= 50:
    monto_consumo = consumo_agua * 1.737
    monto_total = RENTA + monto_consumo
    print(f'Monto a pagar de recibo de agua es S/.{monto_total:.2f}')
elif consumo_agua >= 51 and consumo_agua <= 80:
    monto_consumo = consumo_agua * 2.685
    monto_total = RENTA + monto_consumo
    print(f'Monto a pagar de recibo de agua es S/.{monto_total:.2f}')
elif consumo_agua >= 81:
    monto_consumo = consumo_agua * 3.362
    monto_total = RENTA + monto_consumo
    print(f'Monto a pagar de recibo de agua es S/.{monto_total:.2f}')