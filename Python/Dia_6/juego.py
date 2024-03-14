import random


print("Bienvenido al mejor juego del mundo de piedra papel o tijera. A continuación deberás elegir entre una de las opciones y enfrentarte al campeón del mundo de este juego.")

decision = 0

while decision != "piedra" or decision != "papel" or decision != "tijera":
    decision = input("Elige, piedra, papel o tijera.\n")
    if decision == "piedra" or decision == "papel" or decision == "tijera":
      print(f"Elegiste {decision}")
      break
    else:
       print ("Elige una opción válida.")


opciones = ["piedra", "papel", "tijera"] #Las opciones que tendrá el bot para elegir
bot = random.choice(opciones)

print (f"El computador eligió {bot}")


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
