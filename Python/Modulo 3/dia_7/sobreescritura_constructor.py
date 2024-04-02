class PelotaDeporte():
    def __init__(self, tamaño:int) -> None:
        self.tamaño = tamaño
        print("Pelota de deporte")

class PelotaPlastico():
    def __init__(self, material:str) -> None:
        self.material = material
        print("Pelota de plastico")



class PelotaPingPong(PelotaDeporte, PelotaPlastico):
    def __init__(self, tamaño:int, material:str, timbre:str) -> None:
        PelotaDeporte.__init__(self, tamaño)                            #De este forma podemos llamar un constructor de una clase padre especifica, cuando tenemos mas de 1.
        PelotaPlastico.__init__(self, material)                          #nombredeclase.__init__(self, parametro, parametro2, etc)
        self.timbre = timbre                                              #Es mas claro usar este metodo para herencia multiple que el super()
        print("Pelota de ping pong")


p = PelotaPingPong(10, "plastico", "alto")
print(p.tamaño)
print(p.timbre)