class PelotaDeporte():
    def __init__(self, color) -> None:
        self.__color = color

    @property
    def color(self):
        return self.__color
    

class PelotaFutbol(PelotaDeporte):
    def mostrar_color(self):
        return f"mi color es {self.color}"  #Estamos heredando el atributo colo presente en el padre
                                            #Si le pongo return, imprimo el resultado cuando llamo la función.
                                             #Si le pongo el print vez del return, no es necesario llamar a la función con print, como en linea 16
p = PelotaFutbol("Rojo")
print(p.mostrar_color()) #Demostramos que PelotaFutbol() hereda atributos padre


