# En una oficina de empleos, categorizan a los postulantes en función del sexo y 
# de la edad de acuerdo a lo siguiente: Si la persona es de sexo femenino: 
# categoría FA si tiene menos de 23 años, y FB en caso contrario. Si la persona 
# es de sexo masculino: categoría MA si tiene menos de 25 años, y MB en caso 
# contrario. Muestre la categoría que le corresponde según los datos 
# proporcionados.   

print("".center(50, "*"))
print("CATEGORIZAR POSTULANTES".center(50))
print("".center(50, "*"))

sex = str(input("Introduce tu sexo: "))
age = int(input("Introduce tu edad: "))


if sex == "femenino":
    if age < 23:
            print("Pertenece a la categoria FA")
    else:
        print("Pertenece a FB")
elif sex == "masculino":
    if age < 25:
        print("Pertenece a la categoria MA")
    else:
        print("Pertenece a MB")
