import json

# instancias = []

class Producto():
    def __init__(self, nombre:str, precio:int):
        self.nombre= nombre
        self.precio = precio
    

# with open("productos.txt" as productos):
#     linea = 

archivo = open("producto.json", "r+")
datos = json.load(archivo)
for d in datos:
    for k,v in d.items():
        print(v)
archivo.close()
# print(datos)

