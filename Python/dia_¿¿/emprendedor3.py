
print ("Importante: No ingresar numeros negativos.")
p = int(input("Ingrese el precio de la subscripción.\n"))        #Precio de subscripción
u = int(input("Ingrese la cantidad de usuarios.\n"))             #Cantidad de usuarios
gt = int(input("Ingrese los gastos totales.\n"))                 #Gastos totales
uti = int(input("Ingrese las utilidades del año anterior"))      #Utilidades del año anterior


utilidades = p * u - gt
razon = utilidades / uti
print (f"Sus utilidades son ${utilidades}.")
print(f"La razón entre las utilidades de este año y las del año pasado son ${razon:.2f}")