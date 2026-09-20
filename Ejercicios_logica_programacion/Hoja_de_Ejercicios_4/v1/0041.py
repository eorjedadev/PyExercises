# El gobierno ha implementado como parte de su programa social, un subsidio 
# familiar por escolaridad, que será otorgado por vez única a las madres de familia 
# trabajadoras, bajo la siguiente reglamentación:  
# Las familias que tienen hasta 3 hijos reciben S/. 75.00, las que tienen 4, 5 y 6 
# hijos reciben S/. 60.00; y las que tienen más de 6 hijos reciben S/. 55.00 por 
# derecho de escolaridad. Los montos indicados son por cada hijo que tiene la 
# madre.  
# Además, puede recibir un subsidio extra si la madre de familia fuese:  
# Viuda recibirá un adicional de S/. 55  
# Casada recibirá un adicional de S/. 25  
# Mostrar el monto por subsidio y el subsidio extra si le corresponde a la madre 
# trabajadora

print("".center(50, "="))
print("PROGRAMA SOCIAL".center(50))
print("".center(50, "="))

cantidadHijos = int(input("¿Cuantos hijos tienes?\n"))
estadoCivil = input("¿Usted es viuda o casada?\n")


print("RESULTADOS ADQUIRIDOS".center(50, "*"))
print(f"La madre tiene: {cantidadHijos}")
print(f"Estado civil: {estadoCivil}")
if cantidadHijos <= 3:
    monto = cantidadHijos * 75
    print(f"Monto de subsidio adquirido es S/.{monto}")
elif cantidadHijos >= 4 and cantidadHijos <= 6:
    monto = cantidadHijos * 60
    print(f"Monto de subsidio adquirido es S/.{monto}")
elif cantidadHijos > 6:
    monto = cantidadHijos * 55
    print(f"Monto de subsidio adquirido es S/.{monto}")

if estadoCivil == "VIUDA".lower():
    subsidioMonto = 55
    print(f"Subsidio adicional de S/. {subsidioMonto}")
elif estadoCivil == "CASADA".lower():
    subsidioMonto = 25
    print(f"Subsidio adicional de S/. {subsidioMonto}")

