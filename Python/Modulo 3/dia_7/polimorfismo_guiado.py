from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, hp:int, atk:int, df:int, arma:str = ""):
        self.hp = hp
        self.atk = atk
        self.df = df
        self.arma = arma
    
    @abstractmethod
    def ataque(self):
        pass

    @abstractmethod
    def defensa(self):
        pass

    @abstractmethod
    def ataque(self):
        pass
