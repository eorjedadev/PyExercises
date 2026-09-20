#Débora, Raquel y Séfora aportan cantidades de dinero para formar un capital. 
#Diseñe un programa que determine el capital formado y el porcentaje de dicho 
#capital que aporta cada uno. 

#Entrada
print("INGRESA CANTIDAD DE APORTES".center(50, "*"))
debora = int(input("Débora ingresa el dinero aportar: "))
raquel = int(input("Raquel ingresa el dinero aportar: "))
sefora = int(input("Séfora ingresa el dinero aportar: "))
#Proceso
capital = debora + raquel + sefora
p_debora = debora / capital * 100
p_raquel = raquel / capital * 100
p_sefora = sefora / capital * 100
#Salida

print("".center(50, "="))
print("DATOS DE APORTE DE CAPITAL".center(50, "*"))
print("".center(50, "="))
print(f"Total de capital formado: S/.{capital:.2f}")
print(f'''Porcentaje de los aportantes:\n
- Débora: %{int(p_debora)}
- Raquel: %{int(p_raquel)}
- Séfora: %{int(p_sefora)}''')