from abc import ABC, abstractmethod
from producto import Productos


class Tiendas(ABC):
    @abstractmethod
    def ingresar_productos(self, nombre:str, precio:int, stock:int):
        pass 
    @abstractmethod
    def listado_productos(self):
        pass
    @abstractmethod
    def realizar_venta(self, nombre:str, cantidad:int):
        pass

class Restaurante(Tiendas):
    def __init__(self, nombre_tienda:str, delivery:int) -> None:
        self.__nombre_tienda = nombre_tienda
        self.__delivery = delivery
        self.__productos = []

    @property
    def nombre_tienda(self):
        return self.__nombre_tienda

    def ingresar_productos(self, producto:str, precio:int, stock:int):
        self.__productos = [Productos(producto, precio, stock)]
        self.__productos += self.__productos

    def listado_productos(self):
        lista = []
        if len(self.__productos) > 0:
            for i in self.__productos:
                lista += f"""
NOMBRE: {self.__productos.producto}
PRECIO: {self.__productos.precio}

"""
        return lista 
    def realizar_venta(self, nombre: str, cantidad: int):
        pass

    def realizar_venta(self, nombre: str, cantidad: int):
        pass

class Farmacia():
    def __init__(self, nombre:str, delivery:int) -> None:
        self.__nombre_tienda = nombre 
        self.__delivery = delivery
        self.__productos = []

    def ingresar_productos(self, producto:str, precio:int, stock:int):
        self.__productos = [Productos(producto, precio, stock)]
        for producto in self.__productos:
            if producto in self.__productos:
                producto.stock += stock
            else:
                self.__productos.append(producto)

    def listado_productos(self):
        lista = []
        if len(self.__productos) > 0:
            for i in self.__productos:
                if i.precio >= 15000:
                    envio_gratis = f"¡Envio gratis al solicitar este producto!"
                lista += f"""
NOMBRE: {self.__productos.producto}
PRECIO: {self.__productos.precio}
{envio_gratis}
"""     
            return lista 
        else:
            return "No hay stock para este producto" 

    def realizar_venta(self, nombre: str, cantidad: int):
        if cantidad <= 3:
            p = Productos(nombre, cantidad)
            if p in self.__productos.producto:
                if self.__productos.stock > 0:
                    stock_restante = p.stock - cantidad if stock_restante >= 0 else 0
                    p.stock = stock_restante
                    print(f"El stock restante es: {stock_restante}")

class Supermercado():
    def __init__(self, nombre:str, delivery:int) -> None:
        self.__nombre_tienda = nombre
        self.__delivery = delivery
        self.__productos = []


    @property
    def productos(self):
        return self.__productos
    @productos.setter
    def productos(self, nuevos_productos):
        self.__productos = nuevos_productos
    
    def ingresar_productos(self, producto:str, precio:int, stock:int):
        self.__productos = [Productos(producto, precio, stock)]
        for producto in self.__productos:
            if producto in self.__productos:
                producto.stock += stock
            else:
                self.__productos.append(producto)

    def listado_productos(self):
        lista = []
        poco_producto = ""
        for i in self.__productos:
            if i.stock < 10:
                poco_producto = f"¡Quedan pocos"
            print(i.producto)
            lista.append(f"""
NOMBRE: {i.producto}
PRECIO: {i.precio}
STOCK:  {i.stock}
{poco_producto}
""")
        return lista 
            # else:
            #     return "No hay stock para este producto"
        
    def realizar_venta(self, producto: str, precio:int, cantidad: int):
        p = Productos(producto, precio, cantidad)
        if p.producto in p:
            if p.stock > 0:
                stock_restante = p.stock - cantidad if stock_restante >= 0 else 0
                self.__productos.stock = stock_restante

# lista = []
# p = Supermercado("Sushiroll", 600)
# p.ingresar_productos("para", 1000, 20)
# a = Supermercado("calo", 200)
# a.ingresar_productos("papa", 1244, 400)
# print(Supermercado.productos())
# # print(listado_productos())


