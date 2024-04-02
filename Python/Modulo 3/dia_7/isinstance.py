class PelotaDeporte():
    def __init__(self, tamaño:str) -> None:
        self.tamaño = tamaño

class PingPong(PelotaDeporte):
    def __init__(self, *args) -> None:
        self.color = args[0]
        self.rebote = args[1]


d = PelotaDeporte("grande")

ping = PingPong("blanco", "poco")

print(d.tamaño)

print(ping.color)
print(ping.rebote)
print()
if isinstance(ping, PelotaDeporte):
    print(f"ping es instancia de PelotaDeporte")

if isinstance(ping, PingPong):
    print(f"ping es instancia de PingPong, se convierte en instancia de la clase padre cuando la heredamos")  #Si estamos heredando una clase, la instancia de la clase hija también será instancia de la clase padre

print()
if isinstance(d, PelotaDeporte):
    print("d es instacia de PelotaDeporte")

if isinstance(d, PingPong):
    print("d es instancia de Ping Pong")
else:
    print("d no es instancia de PingPong, la instancia de la clase padre no es instancia de la hija")  #la instancia de la clase padre no es instancia de la clase hija