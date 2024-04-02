from usuario import Usuario


class ListadoRespuestas():
    def __init__(self, lista_respuestas:list, nombre:str, u): #Estaremos pasando u como una instancia de Usuario()
        self.__lista_respuestas = lista_respuestas
        self.__encuestado = u

    @property
    def lista_respuestas(self):
        return self.__lista_respuestas
    
    @property
    def encuestado(self):
        return self.__encuestado