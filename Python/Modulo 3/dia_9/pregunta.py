from alternativa import Alternativa

class Pregunta():
    def __init__(self, enunciado, alternativas:str, requerido:bool) -> None:
        self.enunciado = enunciado
        self.ayuda = False
        self.alternativas = [Alternativa(alternativas)]
        self.requerido = requerido


    def mostrar_pregunta(self): #Vamos a asumir que son 4 alternativas por pregunta
        print(f"""
{self.enunciado}:
{self.alternativas.contenido[0]} 
{self.alternativas.contenido[1]}
{self.alternativas.contenido[2]}
{self.alternativas.contenido[3]}
""")
        
        if self.ayuda:
            print(self.ayuda)