import random


print("Bienvenido al mejor juego del mundo de piedra papel o tijera. A continuación deberás elegir entre una de las opciones y enfrentarte al campeón del mundo de este juego.")

decision = 0
opciones = ["piedra", "papel", "tijera"] #Las opciones posibles

while True:
   while decision not in opciones:
      decision = input("Elige, piedra, papel o tijera.\n")
      print(f"-------------\nElegiste {decision}.")

   opciones = ["piedra", "papel", "tijera"] #Las opciones que tendrá el bot para elegir
   bot = random.choice(opciones)

   print (f"El computador eligió {bot}.\n-------------")


   if decision == bot:
      print("Empataron.")
   elif decision == "piedra" and bot == "tijera":
      print ("Ganaste! Sos el mejor.")
   elif decision == "papel" and bot == "piedra":
      print ("Ganaste! Sos el mejor.")
   elif decision == "tijera" and bot == "papel":
      print ("Ganaste! Sos el mejor.")
   else:
      print ("Perdiste, desinstala el juego pls.")

   continuar = int(input(f"""Quieres jugar de nuevo? Elige el numero que corresponda:
1. Sí
2. No
"""))
   if continuar != 1:
      print("bai")
      break
   else:
      decision = 0