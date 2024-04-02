from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas

class Encuesta():
    def __init__(self, nombre, preguntas:list, lista_respuestas) -> None:
        self.nombre = nombre
        self.__preguntas = [
            Pregunta(
                p["Enunciado"],
                p["Alternativas"],
                p["Requerido"],
            ) for p in preguntas
        ]
        self.__lista_respuestas = [ListadoRespuestas(lista_respuestas)]

    def mostrar_encuesta(self):
        print(self.nombre)
        for p in self.__preguntas:
            p.mostrar_preguntas()

    def agregar_listado_respuestas(self, listado_respuestas):
        self.__lista_respuestas.append(listado_respuestas)

class EncuentaLimitadaRegion(Encuesta):
        def __init__(self, nombre:str, preguntas:list, regiones:list):
             Encuesta.__init__(self, nombre, preguntas)
             self.__regiones = regiones

        @property
        def regiones(self):
            return self.__regiones
        
        @regiones.setter
        def regiones(self, nueva_region):
            self.__regiones = nueva_region

        def agregar_respuesta(self, respuestas):
            if self.__regiones in ListadoRespuestas.Usuario.region:
                super().agregar_listado_respuestas(respuestas)

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre:str, preguntas:list, edad_min:int, edad_max:int) -> None:
        Encuesta.__init__(self, nombre, preguntas)
        self.__edad_min = edad_min
        self.__edad_max = edad_max

    @property
    def edad_min(self):
         return self.__edad_min
    
    @property
    def edad_max(self):
        return self.__edad_max
    
    @edad_min.setter
    def edad_min (self, nueva_edad_min):
        self.__edad_min = nueva_edad_min

    @edad_min.setter
    def edad_max (self, nueva_edad_max):
        self.__edad_max = nueva_edad_max 

    def agregar_respuesta(self, respuestas:list):
        if self.__edad_min >= ListadoRespuestas.Usuario.edad <= self.__edad_max:
            super().agregar_listado_respuestas(respuestas)

