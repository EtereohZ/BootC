class PelotaDePlastico():
    def __init__(self) -> None:
        self.rebotes = []
    
    def rebotar(self, altura):
        while altura > 0:
            self.rebotes += [altura, 0]
            altura //= 1.1

class PelotaDeJuguete(PelotaDePlastico):
    def rebotar(self, altura):
        while altura > 0:
            self.rebotes += [altura, 0]
            altura //= 2

p = PelotaDeJuguete()
p.rebotar(10)
print(p.rebotes) #Llamando a la función de la misma clase.
                 #Al estar la misma función en clase padre como hija, se usa la del hijo

super(type(p), p).rebotar(10) #Así puedo llamar al metodo padre,sustituyendo al metodo hijo
print(p.rebotes)
