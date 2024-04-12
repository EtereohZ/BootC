from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self, ancho:int, alto:int, url_archivo:str, url_clic:str, sub_tipo:str) -> None:
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def ancho(self):
        return self.__ancho
    
    @property
    def alto(self):
        return self.__alto
    
    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @property
    def url_clic(self):
        return self.__url_clic
    
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @ancho.setter
    def ancho(self, nuevo_ancho:int):
        self.__ancho = nuevo_ancho if nuevo_ancho > 0 else 1
    
    @alto.setter
    def alto(self, nuevo_alto:int):
        self.__alto = nuevo_alto if nuevo_alto > 0 else 1

    @url_archivo.setter
    def url_archivo(self, nuevo_url:str):
        self.__url_archivo = nuevo_url
    
    @url_clic.setter
    def url_clic(self, nuevo_url_clic):
        self.__url_clic = nuevo_url_clic

    @sub_tipo.setter
    def sub_tipo(self, nuevo_subtipo):   #cambiamos el subtipo y validamos que este sea correcto

        if nuevo_subtipo in Video.SUB_TIPOS:
            self.__sub_tipo = nuevo_subtipo
        elif nuevo_subtipo in Display.SUB_TIPOS:
            self.__sub_tipo = nuevo_subtipo
        elif nuevo_subtipo in Social.SUB_TIPOS:
            self.__sub_tipo = nuevo_subtipo
        else:
            raise SubTipoInvalidoError("Solo puedes elegir dentro de los subtipos que perteneces a cada tipo de anuncio", nuevo_subtipo)   



    
    @staticmethod
    def mostrar_formatos():
        print(f"""
FORMATO VIDEO ------------- FORMATO DISPLAY ------------- FORMATO SOCIAL
-instream                   -tradicional                  -facebook                                                     
-oustream                   -native                       -linkedin
""")

    @abstractmethod
    def comprimir_anuncio():
        pass

    @abstractmethod
    def redimensionar_anuncio():
        pass

class Video(Anuncio):  
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    def __init__(self,ancho, alto:int, url_archivo: str, url_clic: str, sub_tipo, duracion:int) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
        self.__duracion = duracion if duracion > 0 else 5

    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self, nueva_duracion:int):
        self.__duracion = nueva_duracion if nueva_duracion > 0 else 5

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AUN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    FORMATO = "DISPLAY"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
        
    def redimensinar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOSCIALES NO IMPLEMENTADO AÚN")
