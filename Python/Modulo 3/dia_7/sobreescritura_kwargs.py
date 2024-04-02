class PelotaDeporte():
    def __init__(self, tamaño:int, **kwargs) -> None:  #Recordar que un **kwargs es un diccionario con forma: key=valor
        super().__init__(**kwargs)
        self.tamaño = tamaño
        print("Pelota 1")

class PelotaPlastico():
    def __init__(self, material:str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.material = material
        print("Pelota 2")

class PelotaTennis(PelotaDeporte, PelotaPlastico):
    def __init__(self, timbre:str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.timbre = timbre
        print("Pelota 3")

p = PelotaTennis(tamaño=10, material="plastico", timbre="agudo")

print(p.tamaño)
print(p.material)
print(p.timbre)