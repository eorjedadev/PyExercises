#El cálculo del pago mensual de un empleado de una empresa se efectúa de la 
#siguiente manera: el sueldo básico se calcula en base al número total de horas 
#trabajadas basado en una tarifa horaria; al sueldo básico, se le aplica una 
#bonificación del 20% obteniéndose el sueldo bruto; al sueldo bruto, se le aplica un 
#descuento del 10% obteniéndose el sueldo neto. Escriba un programa que calcule 
#e imprima el sueldo básico, el sueldo bruto y el sueldo neto de un trabajador

# Entrada
hours_worked = float(input("Ingresa las horas trabajadas: \n"))
hourly_rate = float(input("Ingresa la tarifa horaria: \n"))
# Proceso
base_salary = hours_worked * hourly_rate
bonus = base_salary * 0.20
gross_salary = base_salary + bonus
discount = gross_salary * 0.10
net_salary = gross_salary - discount
# Salida 
print("".center(50, "="))
print("Resultados del calculo del sueldo".center(45, "*"))
print("".center(50, "="))
print(f'''Sueldo básico: S/. {base_salary}
Sueldo bruto: S/. {gross_salary}
Sueldo Neto: S/. {net_salary}
''')