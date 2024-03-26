from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, hp:int, atk:int, df:int, **kwargs):
        super().__init__(**kwargs)
        self.__hp = hp
        self.__atk = atk
        self.__df = df
    
    @property
    def hp(self):
        return self.__hp
    
    @hp.setter
    def hp(self, hp):
        self.__atk = hp

    @property
    def atk(self):
        return self.__atk
    
    @atk.setter
    def atk(self, atk):
        self.__atk = atk


    @abstractmethod
    def ataque(self):
        pass

    @abstractmethod
    def defensa(self):
        pass

    @abstractmethod
    def ataque(self):
        pass
