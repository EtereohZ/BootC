
import sys
player1 = input("please enter your name:\n")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print(f"Welcome to Treasure Island, {player1}!.\n")
if player1 == "felipe":
  print("nombre pa feo ekis d")
print("One day, you inherit a mysterious treasure map from your grandfather. As you're kinda bored and got nothing going on, you start preparing for your journey.")
equipment_backpack = input("""You have a small backpack you bought from Acuenta supermarket, it can only hold 1 thing. What do you want to take with you? A single coin? Or a torch? Type 'coin' or 'torch.'\n
""").lower()

if equipment_backpack == "coin":
  print("""--------------
You now have a coin""")
  coin = 1
  torch = 0
elif equipment_backpack == "torch":
  print("""--------------
You now have a torch.""")
  torch = 1
  coin = 0

print("""
You start your journey deciding to travel to a small village to find someone who can take you to the island's coordinates on your map.
      
After 2 days walking, you arrive at a fork in the road, the path to the right goes through a forest, and the left path takes you to a clearing. As the signs are all gone, and you don't know which way to go, and you're left to ponder.
After some time, a ragged old man approaches you, he tells you that if you want to go to the village, you have to go through the forest to the right, and that the road to the left leads to some abandoned mine.""")
crossroads_decision = input("Which way do you want to go? Type 'right' or 'left'.\n").lower()

if crossroads_decision == "left":
  print("""
--------------
You decide that trusting a suspicious old man's information really not the smartest idea, so you take the left road.
        
After what is seems like 2 hours, you start seeing some animals, and a few houses on the distance.
When you finally clear a small hill on the road, you can see it. You found the village!""")
elif crossroads_decision == "right":
  print("""
--------------
You decide to trust that guy and take the path to the right.
        
As you're walking through the forest, you start having chills down your spine, something isn't right. As soon as you turn around, an arrow flies out of the trees and hits you in the head.
With the remaining of your conciousness, you think to yourself, -did that old man lie to me?
You die.""")
  sys.exit()
if crossroads_decision == "left":
  # imagen
  print("The village looks unassuming, like a every stereotypical fishing village. The smell of seafood is everywhere and you can see fishing boats in the distance.\n")
  town_first_decision = input("You have a few options as to what to do next. you can either go straight to finding a means to get to the island, or you can explore. Type 'boat' or `explore'.\n").lower()

if town_first_decision == "explore":
  print("You decide to explore the village and, who knows, you might find something useful")
  alley_decision = input(" You find a dark alleyway, it looks scary. you can search it by typing 'go' or go back typing 'back'.\n").lower()
  while town_first_decision == "explore":
    if alley_decision == "back":
      print("You decide not to risk it, you go back in search for a boat.")
      bucket = 0

    elif alley_decision == "go":
      print("""You enter the dark alleyway, it smells moist.")
You look behind a dumpster and found a bucket!

You should go looking for a way to get to the island, now""")
      bucket = 1
else:
  bucket = 0

print("""--------------
It's getting late and you decide to go looking for the bote.""")
fisherman_decision = input("You find a fisherman who offers you a boat ride to the island, but asks for 1 coin in exchange. Wanna take him up on the offer? Type 'yes' or 'no'.\n").lower()
if fisherman_decision == "yes" and (coin == 1):
  print("You give him the coin and you prepare to set sail.")
  fisherman_decision1 = 1
elif fisherman_decision == "yes" and (coin == 0):
  print('"No coin, no boat" he says. The fisherman leaves.')
  fisherman_decision1 = 0
else:
  print("You are either poor or decided that you know better, only time will tell. You reject the fisherman's offer and leave.")
  fisherman_decision1 = 0
    
if fisherman_decision1 == 1:
  print(" You two set sail and after a few hours, you arrived unscathed to the island. Was it really that easy?")
  reach_island = 1
 
elif fisherman_decision1 == 0:
  print("""
Life has always given you it's hardest battles. You ponder about your next moves.
        
Having brain blasted for an answer for 2 whole minutes, you have narrowed it down to 2 options:""")
  life_choices = input('''You can either steal a boat or face your failures and go home. 
My cat misses me, I just wanna go home. Type "home" if this is too much.
Fuck it, "I\'m stealing that boat". Type "steal".''').lower()
  if life_choices == "home":
    print("""
--------------
You decided to abandon your quest and go home.
You win?""")
    sys.exit()
  elif life_choices == "steal":
    print("""--------------
You were always going to steal it, let's be real.
After scouting the beach for a while, you find an old looking boat out of the way, it has oars inside too! Better than nothing, I guess.")
You set sail without anyone noticing and start rowing.")

It's been an hour, and your feet start feeling... wet? You look down and, oh no. The old boat seems to have some holes, and started taking on water!""")
    if bucket == 1:
      print("""--------------
You remembered that you had a bucket, so you succesfully alternate between rowing the boat and clearing the boat of water.
You have reached the island, you are incredible!""")
      reach_island = 1
    else:
      print("""--------------
You start clearing the water using your bare hands, but you're not very good at it, and you start feeling tired.
Water keeps leaking in and you're exhausted, you collapse on the boards and the old boat starts sinking.
you decide to close your eyes...
You drowned.""")
      sys.exit()

if reach_island == 1:
  print('''



                                                   .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.              
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ''')
print("""You're finally on the island, and the sun is almost setting
There's an old structure in the middle of the island, that must be it.

As you walk to the structure, you notice a variety of flora not seen near your home or the village, it looks mesmerizing.
You walk up to it and see a strange sign, you can't read it. Oh well.
You go down the starts, it starts getting really dark.""")
if torch == 1:
  print("You magically light up your torch and you can see the path ahead. there's some holes with spikes down the path, you gracefully evade them and continue down the path.")
  reach_treasure = 1
else:
  print("""The sun has set and no amount of light is reaching down the stairs, it's pitch black. Why didn't you bring a flashlight or something?")
It's too late to go back now.""")
  corridor_size = input('You decide to stick to a wall so you can better navigate the corridor using your hands. Which side do you want to follow? Type "left" or "right".\n').lower()
  if corridor_size == "right":
    print("You decide to stick to the right wall.\n", "You can barely see your hands in front of you, but you keep following the wall.\n", "Suddenly, the floor is missing. You are falling down a hole.\n", "You land on a pit of spikes, in your last moments, you think of home.\n", "You died.")
    sys.exit()
  elif corridor_size == "left":
    print("""You decide to stick to the left wall.")
After what feels like ages, you can't feel the wall any longer, is this a turn?.""")
    reach_treasure = 1

if reach_treasure == 1:
    print("""You take another step and the ceiling lights, you made your way into a big, spherical room. You can   see something in the middle on the room.
It's a chest!
you approach it. It' s a gold plated chest, this must be it.""")
    open_chest_trick = input("The chest is there, but, no monsters? no falling rocks? Do you open it? yes or no.\n").lower()
    if open_chest_trick == "no":
      print(f"""You decide to open it anyways.")
You easily open the chest, it's filled with gold and jewels, you can't believe it.")
You cant wait to take it all, you did it. you're rich.
You won {player1}!""")
      open_chest_trick == "yes"
    elif open_chest_trick == "yes":
      print("""You easily open the chest, it's filled with gold and jewels, you can't believe it.
You cant wait to take it all, you did it. you're rich.
You won, {player1}!""")