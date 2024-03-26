from jugador import Jugador
from monstruo import Monstruo

enfrentados = [Jugador(500, 10, 5, "Espada"), Monstruo(5000, 1 , 8)]
atk  = 0

while any(e.hp <= 0 for e in enfrentados) == False:
    for e in enfrentados:
        if atk:
            e.defensa(atk)
        if e.hp > 0:
            atk = e.ataque()
        else:
            print(f"Oh no, {e.__class__.__name__} ha muerto ):")