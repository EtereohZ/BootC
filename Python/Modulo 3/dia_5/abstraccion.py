from abc import ABC, abstractmethod

class Pelota(ABC): #Creamos clase abstracta
    @abstractmethod  #Decorador para crear metodo abstracto
    def rebotar(self, altura): 
        pass #La clase abstracta solo se le pone un self

class Pelotajuguete(Pelota): #Llamamos a la clase abstracta dentro de una clase nueva, hija
    def __init__(self):
        self.rebotes = []

    def rebotar(self, altura): #Utilizamos el metodo abstracto importado de la clase padre
        self.rebotes = []
        while altura > 0:
            self.rebotes.append(altura)
            self.rebotes.append(0)
            altura //= 2
        return self.rebotes

p = Pelotajuguete()
p.rebotar(10)