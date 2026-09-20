# Un estudiante recibe una propina mensual de S/.20. El estudiante rinde 
# mensualmente tres exámenes (matemática, lenguaje e historia). Su papá ha 
# decidido incentivarlo dándole una propina adicional de S/. 5 por cada examen 
# aprobado. Diseñe un algoritmo que determine el monto total de la propina que le 
# corresponde al estudiante en un mes determinado. 

PROPINA_FIJA = 20
PROPINA_ADICIONAL = 5

aprobado = 0

matematica = "aprobado"
lenguaje = "aprobado"
historia = "desaprobado"

if matematica == "aprobado":
    aprobado += 1
    print("Aprobo matematica!")
else:
    print("No aprobo pipipi!")

if lenguaje == "aprobado":
    aprobado += 1
    print("Aprobo lenguaje!")
else:
    print("No aprobo pipipi!")

if historia == "aprobado":
    aprobado +=1
    print("Aprobo historia!")
else:
    print("No aprobo pipipi!")

adicional = aprobado * PROPINA_ADICIONAL
total = PROPINA_FIJA + adicional

print(f"Total de propina ganadas es: {total}")
