from anuncio import Anuncio, Video, Display, Social
from error import LargoExcedidoError, SubTipoInvalidoError

class Campaña():
    def __init__(self, nombre:str, fecha_inicio:str, fecha_termino:str) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = []



        # self.__anuncios = [Anuncio(tipo, ancho, alto, url_archivo, url_clic, sub_tipo)]

    def agregar_anuncio(self, ancho:int, alto:int, url_archivo, url_clic, sub_tipo, duracion):  #En este metodo agregamos los anuncios a la camppaña y además validamos que el subtipo sea el correcto
        if sub_tipo in (Video.SUB_TIPOS):
            self.__anuncios += [Video(ancho, alto, url_archivo, url_clic, sub_tipo, duracion)]
        elif sub_tipo in Display.SUB_TIPOS:
            self.__anuncios += [Display(ancho, alto, url_archivo, url_clic, sub_tipo)]
        elif sub_tipo in Social.SUB_TIPOS:
            self.__anuncios += [Social(ancho, alto, url_archivo, url_clic, sub_tipo)]
        else:
            raise SubTipoInvalidoError("Solo puedes elegir dentro de los subtipos que perteneces a cada tipo de anuncio", sub_tipo)   #Desde el inicio no podremos ingresar un subtipo invalido

    def __str__(self) -> str:
        pass

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @property
    def fecha_termino(self):
        return self.__fecha_termino
    
    @property
    def anuncios(self):
        return self.__anuncios
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) < 150:
            self.__nombre = nuevo_nombre
        else:
            raise LargoExcedidoError()
    
    @fecha_inicio.setter
    def fecha_inicio(self, nueva_fecha_inicio):
        self.__nombre = nueva_fecha_inicio

    @fecha_termino.setter
    def fecha_termino(self, nueva_fecha_termino):
        self.__nombre = nueva_fecha_termino
  
    def __str__(self) -> str:    #Aquí realizamos el conto de anuncios
        videos = 0
        displays = 0
        socials = 0
        for elemento in self.__anuncios:
            if isinstance (elemento, Video):
                videos += 1
            elif isinstance (elemento, Display):
                displays += 1
            elif isinstance (elemento, Social):
                socials += 1
        return f"""
Nombre de la campaña : {self.__nombre}                             
Anuncios: {videos} Videos, {displays} Displays, {socials} Socials
""" 
