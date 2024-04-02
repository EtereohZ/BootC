class Superficie():
    def __init__(self):
        self.__resistencia = 2
    @property
    def resistencia(self):
        return self.__resistencia

class Pelota():

    def __init__(self, color):
        self.color = color
    def rebotar(self, altura: float):
        # Se instancia la clase que colabora con Pelota
        s = Superficie()
        rebotes = []
        while altura > 0:
            rebotes.append(altura)
            rebotes.append(0)
            # La instancia de Superficie colabora con Pelota para rebotar
            altura //= s.resistencia
        return rebotes

p = Pelota( "rojo")
print(p.color)
print(s) #Instancia s no existe fuera de la clase
# Salida: [10, 0, 5, 0, 2, 0, 1, 0]
print(p.rebotar(10))

'''
No es composición porque ninguna compone a la otra, solo colaboran o una afecta a la otra.
Por que no agregación?

'''