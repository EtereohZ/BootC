class Alternativa():
    def __init__(self, contenido:str) -> None:
        self.contenido = [contenido] #La lista de alternativas
        self.ayuda = False

    def mostrar_alternativa(self):
        print(self.contenido)
        if self.ayuda:
            print(self.ayuda)