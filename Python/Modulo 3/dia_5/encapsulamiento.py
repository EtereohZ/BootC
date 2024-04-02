from abc import ABC, abstractmethod

class Pelota(ABC):
    @abstractmethod
    def rebotar(self, altura):
        pass

class Pelotajuguete(Pelota):
    def __init__(self, color:str):
        self.rebotes = []
        self.__color = color #Uso del encapsulamiento para crear atirbuto privado. Ahora el atributo se llama __color

    def rebotar(self, altura):
        self.rebotes = []
        while altura > 0:
            self.rebotes.append(altura)
            self.rebotes.append(0)
            altura //= 2
        return self.rebotes
    
    @property              #Podemos utilizar un getter para llamar al atributo privado
    def color(self):
        return self.__color #retornamos el atributo privado
    
    @color.setter           #Tambien podemos utilizar setter para cambiar el atributo privado
    def color(self, nuevo_color):
         self.__color = nuevo_color

p = Pelotajuguete("amarilla")

print(p.color)   #Solo va a funcionar si tenemos un metodo getter, como en la linea 21, de otra manera no funciona.
                 #AQUÍ ESTAMOS LLAMANDO AL METODO GETTER "color" DE LA LINEA 22, NO AL ATRIBUTO self.__color NO AL ATRIBUTO NO AL ATRIBUTO
# p.color = "roko "
# print(p._Pelotajuguete__color) #La única forma de acceder al atributo es (*sin un getter*) anteponiendo el nombre de la clase con un underscore = _clase --> _Pelotajuguete seguido del nombre del atributo --> __color =====>>> p._Pelotajuguete__color
# print(p.__color) #Esta nunca va a funcionar

p.rebotar(10)