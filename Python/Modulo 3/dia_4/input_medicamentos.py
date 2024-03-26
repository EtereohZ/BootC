from medicamentos import Medicamentos

lista_meds = []
ingreso = input(f"""Desea ingresar un medicamento?
-si
-no 
""").lower()
lista_meds = []
while ingreso == "si":

    nombre = input(f"Ingrese el nombre del medicamento\n")
    stock = int(input(f"Ingrese el stock del medicamento\n"))

    m = Medicamentos(nombre, stock)

    if m in lista_meds:
        indice = lista_meds.index(m)
        lista_meds[indice] += m
        m.precio = precio_bruto
    else:
        lista_meds.append(m)
        precio_bruto = int(input(f"Ingrese el precio bruto del medicamento\n"))
        m.precio = precio_bruto



    print(f" El precio bruto del medicamento {m.nombre} es {m.precio_bruto}")
    if m.descuento:
        print(f"El descuento del medicamento es {m.descuento*100}%")
    print(f"El precio final del medicamento es {m.precio_neto}")
    print(f"La farmacia cuenta con un stock de {m.stock}")
    print(f"Hay {len(lista_meds)} medicamentos distintos en nuestra bodega")

    ingreso = input(f"""Desea ingresar otro medicamento?
-si
-no 
""").lower()
