import sys


precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

filtrado = {}
for k, v in precios.items():
    if sys.argv[2] == "menor":
        filtrado[k] = v
        print(k)
        print(f"Los productos menores al umbral son {k}")
    elif v > int(sys.argv[1]):
        filtrado[k] = v
        print(f"Los productos mayores al umbral son {k}")
    # if (comando != "menor") or (len(comando) == " "):
    #     print("Lo siento, esta operración no es valida")
