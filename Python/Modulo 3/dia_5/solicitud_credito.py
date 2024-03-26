from abc import ABC, abstractmethod

class Solicitud_credito(ABC):
    @abstractmethod
    def validar_monto(self, monto):
        pass

    @abstractmethod
    def validar_correo(self, correo):
        pass

class Solicitud_credito_consumo(Solicitud_credito):
    __terminaciones = (".cl", ".com") #Atributo de clase privado

    def __init__(self, correo, monto) -> None:
        self.__monto = self.validar_monto(monto)
        self.correo = self.validar_correo(correo)

    def validar_monto(self, monto):
        # return super().validar_monto(monto) #Que es esto
        if monto < 1000000:
            monto = 1000000
        elif monto > 5000000:
            monto = 50000000

            return 
        
    def validar_correo(self, correo):
        return correo if correo.count("@") == 1 and correo.endswith(Solicitud_credito_consumo.__terminaciones) else "" #La wea fea
    
