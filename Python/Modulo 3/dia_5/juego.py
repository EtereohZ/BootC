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


nombres_orco = ["Jaime", "Antonio", "Julio", "Pedro", "Juan", "John"]
n_o = random.choice(nombres_orco)
orco = Personajes(n_o)
orco.nivel = (random.randint(0, 2)+ jugador.nivel)

# calculo = jugador.probabilidad_ganar

while continuar == 1:
    print(f"""
¡Vaya!, ¡ha aparecido un Orco llamado {orco.nombre}!
Es de nivel {orco.nivel}

""")
