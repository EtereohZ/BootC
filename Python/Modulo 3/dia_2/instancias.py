from te import Te

te1 = Te()
te2 = Te()

te1 = type(te1)
te2 =type(te2)

if te1 == te2:
    print("Ambos tipos son iguales. No se por que piden esto")
else:
    print("Estas instancias no son iguales")