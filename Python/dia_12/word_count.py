import re

with open("lorem_ipsum.txt", "r") as file:
    texto=file.read()

texto = texto.replace(",", "").replace(".", "").replace(";", "") # Así eliminamos las comas, puntos y punto y coma. quedan solo las palabras separadas por espacios.
 
palabras = texto
letras = (len(set(texto.replace(" ", "")))) #Eliminamos los espacios para que todas las palabras queden juntas, luego convertimos a set para eliminar las repeticiones y luego len para contar.
(letras)
letras -= 1 #Para eliminar el conteo del "\n" presente en el set

palabras = len(set(palabras.split())) #Separamos las palabras individuales y luego convertimos a set para eliminar palabras duplicadas, luego contamos

print(f"""
Hay {letras} letras.
Hay {palabras} palabras.
""")