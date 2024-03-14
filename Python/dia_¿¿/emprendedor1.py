
print ("Importante: No ingresar numeros negativos.")
p = int(input("Ingrese el precio de la subscripción.\n")) #Precio de subscripción
u = int(input("Ingrese la cantidad de usuarios.\n"))      #Cantidad de usuarios
gt = int(input("Ingrese los gastos totales.\n"))          #Gastos totales



utilidades = p * u - gt
print (f"Sus utilidades son ${utilidades}.")