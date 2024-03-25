from chocolate_guiado import SinGluten
from abc import ABC, abstractmethod

class Chocolate(ABC):
    def __init__(self, cacao:float) -> None:
        self.p_cacao = self.validar_p_cacao(cacao)
        
    def validar_p_cacao(self, cacao:float):
        pass

class ChocolateAmargo(Chocolate):
    def validar_p_cacao(self, cacao: float):
        return min(max(0.75, cacao), 0.85) #Queda entre el rango de 0.75 y 0.85
    
class ChocolateAmargoSinGluten(ChocolateAmargo,SinGluten):
    pass

c = ChocolateAmargo(0.7)
print(c.p_cacao)

a = ChocolateAmargoSinGluten(0.8)
print(a.p_cacao)