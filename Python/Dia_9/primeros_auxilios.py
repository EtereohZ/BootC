
print("Bienvenido a la aplicación de PPAA")
estimulo = input("La persona responde a estimulos?\n")

if  estimulo == "si":
    print("Valorar la necesidad de llevarla al centro médico mas cercano.")
else:
     print("Por favor, desobstruya la vía aérea")
     va = input("La persona se encuentra respirando?\n")
     if va == "si":
          print("Ponerlo en posición de recuperación para permitirle suficiente ventilación.")
     else:
        print(" Administrar 5 ventilaciones y llamar a servicios de urgencia")
        alo  = 1
        ambulancia = ()
        while ambulancia != "si":
            signos = input("Presenta signos de vida?\n")
            if signos == "no":
                print ("Administrar compresion torácicas hasta que llegue la ambulancia")
            elif signos == "si":
                print("Reevaluar la espera de ambulancia")
            ambulancia = input("Llegó la ambulancia?\n")
            if ambulancia == "si":
                print("Entregue al paciente a los servicios de urgencia.")
                break

