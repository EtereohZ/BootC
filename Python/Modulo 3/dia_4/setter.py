class Pelota():
    def __init__(self):
        self.tamaño_pelota = 10

    @property
    def tamaño(self):
        return self.tamaño_pelota
    
    @tamaño.setter
    def tamaño(self, tamaño):
        self.tamaño_pelota = tamaño if tamaño > 10 else 1

p1 = Pelota()
print(p1.tamaño)

p1.tamaño = 6
print(p1.tamaño)