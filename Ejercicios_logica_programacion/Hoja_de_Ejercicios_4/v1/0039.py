# Calcular el monto que debe pagar el socio de un club por derecho de 
# pertenencia. Si es socio EXCLUSIVO pagará S/. 500.00, si es socio EJECUTIVO 
# pagará S/. 300.00, y si es socio REGULAR pagará S/. 150.00. Si el socio tiene 
# deuda, tendrá un recargo del 15% sobre el total de su deuda. En ningún caso el 
# recargo será mayor de S/. 120.00 ni menor de S/. 30.00.

socio = input("Ingrese el tipo de socio (EXCLUSIVO, EJECUTIVO, REGULAR): ")
deuda = input("¿El socio tiene deuda? (SI/NO): ")

if socio.upper() == "EXCLUSIVO":
    monto = 500
    print("El socio es EXCLUSIVO, por lo que debe pagar S/. 500.00.")
elif socio.upper() == "EJECUTIVO":
    monto = 300
    print("El socio es EJECUTIVO, por lo que debe pagar S/. 300.00.")
elif socio.upper() == "REGULAR":
    monto = 150
    print("El socio es REGULAR, por lo que debe pagar S/. 150.00.")

if deuda.lower() == "SI".lower():
    recargo = monto * 0.15
    print(f"El socio tiene deuda, por lo que se le aplicará un recargo del 15% sobre el total de su deuda: S/. {recargo:.2f}.")
    if recargo > 120:
        recargo = 120
        print("El recargo por deuda es de S/. 120.00.")
    elif recargo < 30:
        recargo = 30
        print("El recargo por deuda es de S/. 30.00.")
    monto += recargo
    print(f"El monto total a pagar por el socio es: S/. {monto:.2f}.")