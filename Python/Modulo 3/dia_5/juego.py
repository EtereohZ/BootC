from personaje import Personajes
import random

nombre = input(f"""
Bienvenido al gran juego de acción RPG MMORPG JRPG de estrategia mas famoso del mundo!
Por favor, escoja el nombre de su personaje: """)
jugador = Personajes(nombre)

print(f"""
bienvenido, {jugador.nombre}. Al empezar, tu personaje será nivel 1.
Podrás adquirir experiencia para avanzar de nivel mientras seas un RealGamer™.

Tu personaje fue enviado por el rey a encontrar un tesoro perdido en un antiguo laberinto.
Al llegar, observas que este ha sido asentado por una tribu de orcos. Oh, well.""")

print(jugador.stats)

continuar = int(input("""Empezamos?
1. Si
2. Mejor me voy\n"""))

while continuar == 1:
    nombres_orco = ["Jaime", "Antonio", "Julio", "Pedro", "Juan", "Alberto"]
    n_o = random.choice(nombres_orco)
    orco = Personajes(n_o)
    orco.nivel = (random.randint(-1, 2)+ jugador.nivel)

    probabilidad_ganar = jugador.probabilidad_ganar(orco)
    print(f"""
-------------------------------------------------         
¡Vaya!, ¡ha aparecido un Orco llamado {orco.nombre}!

        {orco.nombre} el orco      
        -Nivel {orco.nivel}
    

        {jugador.nombre}           
        -Nivel {jugador.nivel}
        -{jugador.exp} puntos de experiencia
   
        """)
    dialogo = jugador.dialogo(probabilidad_ganar)
    if dialogo == 1:
        chance = random.uniform(0, 1)
        if chance < probabilidad_ganar:
            print(f"""¡Has vencido al orco!
+50 exp""")
            jugador.stats = 50
        else:
            print(f"""
-------------------------------------------------
El orco te ha derotado.
-30 exp""")
            jugador.stats = -30
    continuar = int(input(f"""Deseas continuar?
1. Sí
2. No
"""))


else:
    print("Te fuiste a tu casa a vivir en paz y harmonía.")
    
