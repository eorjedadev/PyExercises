# Los ángulos se clasifican de la siguiente manera: nulo (0°), Agudo (0°< x < 
# 90°), Recto (90°), Obtuso (90° < x <180°), Llano (180°), Cóncavo (180°< x < 
# 360°), Completo (360°). Desarrolle el programa que determine la clasificación 
# de un ángulo dado en grados. 

angulo = float(input("Ingrese el ángulo en grados: "))

if angulo == 0:
    print("El ángulo es nulo.")
elif angulo > 0 and angulo < 90:
    print("El ángulo es agudo.")
elif angulo == 90:
    print("El ángulo es recto.")
elif angulo > 90 and angulo < 180:
    print("El ángulo es obtuso.")
elif angulo == 180:
    print("El ángulo es llano.")
elif angulo > 180 and angulo < 360:
    print("El ángulo es cóncavo.")
elif angulo == 360:
    print("El ángulo es completo.")
else:
    print("El ángulo ingresado no es válido.")
