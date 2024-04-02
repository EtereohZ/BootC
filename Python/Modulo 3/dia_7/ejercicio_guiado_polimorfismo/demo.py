from jugador import Jugador
from monstruo import Monstruo

enfrentamiento = [Jugador(500, 10, 5, "espada"), Monstruo(100, 1, 8)]
atk = 0

while any(e.hp <= 0 for e in enfrentamiento) == False: #Mientras cualqueira tenga mas de 0 hp, se ejecuta
    for e in enfrentamiento:

        if e.hp > 0:
            atk = e.ataque() #El resultado del metodo se guarda

        if atk:
            e.defensa(atk)  #se ingresa el ataque para calcular hp


        

        else:
            print(f"Oh no, {e.__class__.__name__} ha muerto ):") #nombre e la clase que muere
    
        print(e)