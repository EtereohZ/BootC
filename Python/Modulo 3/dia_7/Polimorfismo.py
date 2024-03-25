class PelotaDePlastico():
    def __init__(self) -> None:
        self.rebotes = []
    def rebotar(self, altura):
        self.rebotes = []
        while altura > 0:
            self.rebotes += [int(altura), 0]
            altura //= 1.1

class PelotaDeJuguete(PelotaDePlastico):
     def rebotar(self, altura):
         self.rebotes = []
         while altura > 0:
             self.rebotes += [int(altura), 0]
             altura //= 2

p = PelotaDeJuguete()
p.rebotar(10) #Uso el metodo de la clase
print(p.rebotes)
super(type(p), p).rebotar(5) #traigo el comportamiento de la clase padre
#El super() necesita el tipo de la instancia seguido de coma, la instancia u al final .metodo
print(p.rebotes)