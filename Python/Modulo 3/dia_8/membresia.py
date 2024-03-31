from abc import ABC, abstractmethod

class Membresia(ABC):
    def __init__(self, correo:str, numero_tarjeta:str) -> None:
        self.__correo = correo
        self.__num_tarjeta = numero_tarjeta

    def crear_membresia(self, nueva_membresia):
        if nueva_membresia == 1:
            return Basica(self.__correo, self.__num_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.__correo, self.__num_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.__correo, self.__num_tarjeta)
        else:
            return Pro(self.__correo, self.__num_tarjeta)
        
    @abstractmethod
    def cambiar_membresia(self):
        pass

    @property
    def correo(self):
        return self.__correo
    
    @property
    def num_tarjeta(self):
        return self.__num_tarjeta
    
class Gratis(Membresia):
    costo = 0
    dispositivos_max = 1

    def cambiar_membresia(self, membresia):
        if membresia > 0 and membresia <= 4:
            return self.crear_membresia(membresia)
        else:
            return self
        
class Basica(Membresia):
    costo = 3000
    dispositivos_max = 2

    
    def cancelar_membresia(self):
        return Gratis(self.correo, self.num_tarjeta)

    def cambiar_membresia(self, membresia):
        if membresia > 1 and membresia <= 4:
            return self.crear_membresia(membresia)
        else:
            return self
        
class Familiar(Basica):
    costo = 5000
    dispositivos_max =  5
    control_parental = True

    def cambiar_membresia(self, membresia):
        if membresia in (1, 3, 4):
            return self.crear_membresia(membresia)
        else:
            return self
        
class SinConexion(Basica):
    costo = 3500
    dispositivos_max = 2
    requiere_conexion = False

    def cambiar_membresia(self, membresia):
        if membresia in (1, 2, 4):
            return self.crear_membresia(membresia)
        else:
            return self

    def contenido_sin_conexion(self):
        pass

class Pro(SinConexion, Familiar):
    costo = 7000
    dispositivos_max = 6

    def cambiar_membresia(self, membresia):
        if membresia in (1, 2, 3):
            return self.crear_membresia(membresia)
        else:
            return self

p = Gratis("yo@pan.cl", "11222333444")
print(p.crear_membresia(1))
a = p.cambiar_membresia(2)
print(a)
c = a.cambiar_membresia(4)
print(c)
print(c.control_parental)
g = c.cancelar_membresia()
print(g)