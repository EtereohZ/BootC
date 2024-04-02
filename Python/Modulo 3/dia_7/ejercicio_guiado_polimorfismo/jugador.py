from personaje import Personaje
import random

class Jugador(Personaje):
    def ataque(self):
        return (self.atk + random.randint(1, 5)) if self.arma else self.atk
    
    def defensa(self, ataque):
        self.hp -= max(ataque - random.randint(1, self.df), 0)