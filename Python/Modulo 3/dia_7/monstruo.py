from polimorfismo_guiado import Personaje

class Monstruo(Personaje):

    def ataque(self):
        return self.atk + int(self.hp*0.01)
    
    def defensa(self, atk:int):
        self.hp -= max(atk-(self.df + int(self.hp*0.001)), 0)

