class PelotaDeDeporte():

    def __init__(self, color:str) -> None:
        self.__color = color

    @property
    def color(self):
        return self.__color
    
class PelotaDeFutbol(PelotaDeDeporte): #Estamos heredando la clase padre

    def mostrar_color(self):
        print(f"Mi color es {self.color}")

pdf = PelotaDeFutbol("Blanco")

pdf.mostrar_color()