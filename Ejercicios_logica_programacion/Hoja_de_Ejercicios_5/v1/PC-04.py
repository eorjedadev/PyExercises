#Suma sucesiva
acumulador = 0

numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

if numero2 < 0:
    repeticiones = -numero2
else:
    repeticiones = numero2

for i in range(repeticiones):
    if numero2 < 0:
        acumulador -= numero1    
    else:
        acumulador += numero1
        
    
print(f'Resultado es: {acumulador}')
    


