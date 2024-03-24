class Personajes():

    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.nivel = 1
        self.exp = 0

    @property
    def stats(self):
        return f"""
        Tu nombre es {self.nombre}, eres nivel {self.nivel}.
        Tienes {self.exp} puntos de experiencia.
"""
    @stats.setter
    def stats(self, experiencia):
        self.exp += experiencia
        temp_exp = 0
        temp_exp += self.exp 
        if self.exp >= 100:
            leveling = temp_exp // 100
            self.nivel += leveling
            self.exp = temp_exp % 100
        elif self.exp < 0 and self.nivel > 1:
            leveling = temp_exp // 100
            self.nivel += leveling
            self.exp = 0
        else:
            pass
    
    
    def probabilidad_ganar(self, other):
        if self.nivel > other.nivel:
            return 0.66
        elif self.nivel < other.nivel:
            return 0.33
        else:
            return 0.5
        
    @staticmethod
    def dialogo(probabilidad_ganar):
        return int(input(f"""
Tienes probabilidades de {probabilidad_ganar} de ganar esta batalla
Ganarás 50 exp si ganas
Perderas 30 exp si pierdes

¿Que harás?
1. Atacar
2. Huir """))

    def __gt__(self, other):
        if self.nivel > other.nivel:
            return True
        return False

    def __lt__(self, other):
        if self.nivel < other.nivel:
            return True
        return False
    
    def __eq__(self, other) -> bool:
        if self.nivel == other.nivel:
            return True
        return False

    

