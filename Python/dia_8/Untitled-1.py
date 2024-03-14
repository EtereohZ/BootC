
# import sys
# import random


# buscar = int(sys.argv[1]) #numero a buscar : 

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# random.shuffle(lista)
# print(lista)

# for position, elemento in enumerate(lista):
#     if elemento == buscar:
#         print(f"elemento encontradoe, posiciom {position}")
#         break
#     else:
#         print("no encontrado")



# for numero1 in range(10):
#     print(f"\nTabla del numero {numero1}")
#     for numero2 in range(10):
#         print(f"\n{numero1} * {numero2} = {numero1 * numero2}")

########################

# paises = {
#     "Mexico": 70,
#     "chile": 50,
#     "argentina":55
# }
# filtrado = {}
# for key, values in paises.items():
#     if values <60:
#         filtrado[key] = values
# print(filtrado)
#########################

meses_1 = [
        {
        "mes":"Octubre",
        "ventas":65000
    },
    {
        "mes":"Noviembre",
        "ventas":68000
    },
    {
        "mes":"Diciembre",
        "ventas":72000
    }

]

meses_2 = {
    "mes":["Octubre", "Noviembre", "Diciembre"],
    "ventas":[65000, 68000, 72000]
}

for elemento in meses_1:
    print(elemento["mes"], elemento["ventas"])

ventas_por_10 = []
ventas_menos_20 = []
{} #diccionarios
() #tuplas

for venta in meses_1:
    nuevo_valor = {
        "mes":venta["mes"],
        "ventas":venta["ventas"]*1.1
    }
    ventas_por_10.append(nuevo_valor)  #Solo se puede hacer append sobre listas

for elemento in ventas_por_10:
    print(elemento["mes"], elemento["ventas"])

    ventas_menos_20 = [
        for venta in meses_!:
        nuevo_valor = {
            "mes":venta["mes"],
            "ventas":venta["ventas"]*0.8
            print()
        }
    ]


# for i, f in enumerate(meses_2["mes"]):
#     print(f,meses_2["ventas"][i])