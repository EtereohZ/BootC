import json

# instancias = []

class Producto():
    def __init__(self, nombre:str, apellido:int):
        self.nombre= nombre
        self.apellido = apellido
    

# with open("productos.txt" as productos):
#     linea = 
instancias = []
archivo = open("producto.json", "r+")
datos = json.load(archivo)
for d in datos:
    Producto(d.get('nombre'), d.get('apellido'))
    instancias.append(Producto(d.get('nombre'), d.get('apellido')))
    print(d)


# print(instancias)
    # for i in instancias:
    #     print(i.nombre)
archivo.close()
# print(datos)

