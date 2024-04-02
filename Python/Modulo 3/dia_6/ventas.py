

class DetalleVentaItem():
    def __init__(self, producto:str, cantidad:int):
        self.__producto = producto
        self.__cantidad = cantidad

    @property
    def producto(self):
        return self.__producto
    
    @property
    def cantidad(self):
        return self.__cantidad


class DetalleVenta():
    def __init__(self) -> None:
        self.__items = []
        
    def agregar_item(self, item:DetalleVentaItem): #Agregación normal ya que la clase DetalleVenta() no depende de este llamado a DetalleVentaItem()
        self.__items.append(item)                  #Esto es porque la clase se está creando arriba, con la función en linea 17 

    def __str__(self) -> str:
        retorno = (f""":::::::::: DETALLE DE VENTA::::::::
  PRODUCTO                 CANTIDAD""")
        items = [f"{i.producto}                 {i.cantidad}\n" for i in self.__items]
        return f"{retorno}\n {"".join(items)}"
    

class Venta():
    def __init__(self) -> None:
        self.__detalle = DetalleVenta() #Composición "fuerte"
                                        #No se crea la clase sin DetalleVenta()
    def modificar_detalle(self, producto:str, cantidad:int):
        detalle_venta_item = DetalleVentaItem(producto, cantidad)   #Esto es colaboración, al intanciar una clase dentro de otra
        self.__detalle.agregar_item(detalle_venta_item)

    @property
    def detalle(self):
        return self.__detalle



paracetamol = DetalleVentaItem("paracetamol", 100)
venta1 = DetalleVenta()
venta1.agregar_item(paracetamol)

print(venta1)
 



