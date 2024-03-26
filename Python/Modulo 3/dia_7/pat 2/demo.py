from jugador import Jugador
from monstruo import Monstruo

m = Monstruo(hp = 1000, atk = 1, df = 8, nombre = "Bégimo")
m.mostrar_dialogo("GRAAAARRR")

enfrentados = [Jugador(500, 10, 5, "Espada"), m]
atk  = 0

while any(e.hp <= 0 for e in enfrentados) == False:
    for e in enfrentados:
        if atk:
            e.defensa(atk)
        if e.hp > 0:
            atk = e.ataque()
        else:
            if isinstance(e, Monstruo):
                print("Felicidades, has vencido al monstruo.")
            elif isinstance(e, Jugador):
                print("Has sido asesinado")
            print(f"Oh no, {e.__class__.__name__} ha muerto ):")