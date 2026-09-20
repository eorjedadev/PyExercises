#El promedio final de un curso se obtiene en base al promedio simple de tres 
#prácticas calificadas. Para ayudar a los alumnos, el profesor del curso ha 
#prometido incrementar en dos puntos la nota de la tercera práctica calificada, si 
#es que esta es no menor que 10. Diseñe un programa que determine el promedio 
#final de un alumno conociendo sus tres notas. No use operadores lógicos en la 
#solución y considere que la nota máxima es 20.

PUNTOS = 2
#Entrada
print("".center(50, "="))
print("NOTAS DE PRACTICAS CALIFICADAS".center(50))
print("".center(50, "="))

one_note = int(input('Introduce la primera nota: '))
two_note = int(input('Introduce la segunda nota: '))
tree_note = int(input('Introduce la tercera nota: '))

if tree_note > 10:
    tree_note += PUNTOS

promedio = (one_note + two_note + tree_note) / 3

print("".center(50, "*"))
print("RESULTADOS DE NOTAS CALIFICADAS FINAL".center(50))
print("".center(50, "*"))
print(f'1° Nota calificada:{one_note}')
print(f'2° Nota calificada:{two_note}')
print(f'3° Nota calificada:{tree_note}')
print(f'Promedio Final:\n{promedio:.2f}')