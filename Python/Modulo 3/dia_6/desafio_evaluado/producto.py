class Productos():
    def __init__(self, producto:str, precio:int, stock:int) -> None:
        self.__producto = producto
        self.__precio = precio
        self.__stock = stock if stock > 0 else 0 #Solo aceptamos valores iniciales de >-1
    
    @property
    def producto(self):
        return self.__producto
    
    @property
    def precio(self):
        return self.__precio
    
    @property
    def stock(self):
        return self.__stock

    @producto.setter
    def producto(self, nuevo_producto):
        self.__producto = nuevo_producto

    @precio.setter
    def precio(self, precio):
        self.__precio = precio if precio is False else self.__precio #Solo se cambia precio si no existe, de todas formas no se dará la opción de cambiarlo una vez ingresado

    @stock.setter
    def stock(self, nuevo_stock:int):
        self.__stock = nuevo_stock if nuevo_stock > 0 else 0 #Actualizamos el stock y validamos la cantidad
  
    def __add__(self, other):
        return self.__stock + other.__stock

    def __sub__(self, other):
        return self.__stock - other.__stock

    def __eq__(self, other) -> bool:
        return self.__producto == other.__producto




