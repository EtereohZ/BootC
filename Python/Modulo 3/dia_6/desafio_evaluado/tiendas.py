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
                self.__productos[0].stock += stock
            else:
                self.__productos += self.__productos

    def listado_productos(self):
        if len(self.__productos) > 0:
            for i in self.__productos:
                if self.__productos.precio >= 15000:
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
                    stock_restante = self.__productos.stock - cantidad if stock_restante >= 0 else 0
                    self.__productos.stock = stock_restante
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
                self.__productos[0].stock += stock
            else:
                self.__productos += self.__productos

    def listado_productos(self):

        if len(self.__productos) > 0:
            for i in self.__productos:
                if self.__productos.stock < 10:
                    poco_producto = f"¡Quedan pocos"
                lista += f"""
NOMBRE: {self.__productos.producto}
PRECIO: {self.__productos.precio}
{poco_producto}
"""
            return lista 
        else:
            return "No hay stock para este producto"
        
    def realizar_venta(self, nombre: str, cantidad: int):
        p = Productos(nombre, cantidad)
        if p in self.__productos.producto:
            if self.__productos.stock > 0:
                stock_restante = self.__productos.stock - cantidad if stock_restante >= 0 else 0
                self.__productos.stock = stock_restante

# p = Restaurante("Sushiroll", 600)
# p.ingresar_productos("para", 1000, 20)
# p.ingresar_productos  #Para nuestro atributo nombre (linea26) llamamos a la funcion producto que nos trae el nombre del producto de la tienda
# print(p)
# a = Farmacia("cruz", 100)
# a.ingresar_productos("paradd", 100, 2000)

d = Supermercado("dd", 12)
a = Supermercado("epa", 14)
d.ingresar_productos("paracetamol", 121313, 1)
# print(d.listado_productos())
# print(d.listado_productos())
# print(d.productos.producto)

print(d)