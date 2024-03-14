
print ("Importante: No ingresar numeros negativos.")
p = int(input("Ingrese el precio de la subscripción.\n"))                       #Precio de subscripción
unormal = int(input("Ingrese la cantidad de usuarios con plan normal.\n"))      #Cantidad de usuarios con plan normal
upremium = int(input("Ingrese la cantidad de usuarios premium.\n"))             #Cantidad de usuarios con plan premium
gt = int(input("Ingrese los gastos totales.\n"))                                #Gastos totales



utilidades = (p * unormal) + (p * 1.5 * upremium) - gt
print (f"Sus utilidades son ${utilidades:.0f}.")