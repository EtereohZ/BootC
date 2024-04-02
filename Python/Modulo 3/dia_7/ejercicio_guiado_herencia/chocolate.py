from sin_gluten import SinGluten
from abc import ABC, abstractmethod

class Chocolate(ABC):
    def __init__(self, porc_cacao) -> None:
        self.porc_cacao = self.validar_porc_cacao(porc_cacao) #Está ejecutando la función, no es necesario ejecutar la función de validar de forma independiente
                                                              #Primero se valida el parametro en la función y luego se ingresa al atributo

    @abstractmethod
    def validar_porc_cacao(self, cacao:float):
        pass

class ChocolateAmargo(Chocolate):
    def validar_porc_cacao(self, porc: float):
        return min(max(0.75, porc), 0.85)
    

class ChocolateAmargoSinGluten(ChocolateAmargo, SinGluten):
    pass

c = ChocolateAmargo(0.4)
a = ChocolateAmargoSinGluten(0.3)
print(c.porc_cacao)
print(a.tipo_producto)
print(a.porc_cacao) #ChocolateAmargoSinGluten() está heredando la función de validar_porc_cacao() desde ChocolateAmargo() y el atributo tipo_producto desde SinGluten()