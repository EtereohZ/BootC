
from encuesta import Encuesta


class Usuario():
    def __init__(self, nombre:str, edad:int, correo:str, region:int) -> None:
        self.__nombre = nombre
        self.__edad = edad
        self.__correo = correo
        self.__region = region

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def correo(self):
        return self.__correo
    
    @property
    def region(self):
        return self.__region
    
    # def contestar_encuesta():
    #     enc = Encuesta()
    #     enc.agregar_listado_respuestas()
