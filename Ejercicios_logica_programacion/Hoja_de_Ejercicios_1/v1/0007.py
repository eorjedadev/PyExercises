#Diseñe un programa que determine el porcentaje de varones y de mujeres que
#hay en un salón de clases.
print("Programa para calcular el porcentaje".center(45, '*'))


varones = float(input("Ingrese la cantidad de varones en clase: \n"))
mujeres = float(input("Ingrese la cantidad de mujeres en clase: \n"))

alumnos = varones + mujeres

cantidad_varones = varones / alumnos
cantidad_mujeres = mujeres / alumnos

total_varones = cantidad_varones * 100
total_mujeres = cantidad_mujeres * 100

print("Resultados de los alumnos en el salon".center(45, "*"))
print(f'El porcentaje de varones es {total_varones}\n'
      f'El porcentaje de mujeres es {total_mujeres}')

