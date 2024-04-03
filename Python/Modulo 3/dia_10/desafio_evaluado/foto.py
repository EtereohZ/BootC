from error import DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if ancho < 1 or ancho >2500:
            raise DimensionError("el ancho debe ser mayor a 1", ancho, 2500)
        else:
            self.__ancho = ancho


    @property
    def alto(self) -> int:
        return self.__alto 

    @alto.setter
    def alto(self, alto) -> None:
        if alto < 1 or alto >2500:
            raise DimensionError("El alto debe ser mayor a 1", alto, 2500)
        else:
            self.__alto = alto 
        

f = Foto(10, 10, "no se")

f.ancho = 30000