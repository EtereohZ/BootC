import sys


precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

filtrado = {}
filtros = []
for k, v in precios.items():

    if len(sys.argv) < 3:  #Para tomar > al umbral
        if v > int(sys.argv[1]):
            filtrado[k] = v
            filtros.append(k)

    elif sys.argv[2] == "menor": #para < al umbral
        filtrado[k] = v
        filtros.append(k)

    else:
        print("lo sentimos, servicio no disponible")  #Despues de varios intentos, no pude lograr que al ingresar alguna letra en sys.argv[1] indicara al usuario que la operación no es valida
        break

if len(sys.argv) <3:
    print(f"Los productos mayores al umbral son {filtros}")
elif sys.argv[2] == "menor":
    print(f"Los productos menores al umbral son {filtros}")