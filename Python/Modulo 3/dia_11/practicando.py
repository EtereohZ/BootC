import os

archivo = open("lorem.txt", "r", encoding="utf-8") #Crea un archivo nuevo si no existe, borra el contenido si es que existe
                                                    #El encoding nos permite leer tildes y otras cosas
# print(archivo.read()) #Nos permite imprimir el texto dentro del archivo
print(archivo.readlines()) #Nos permite imprimir el texto, lo convierte en una lista y cada linea es un item
# print(archivo.readlines()[0]) #Podemos imprimir cada item de la lista, independientemente. Incluye lineas que separen parrafos

#Solo se puede leer el archivo 1 vez, por eso linea 7 tirará error si se ejecuta la 6 al mismo tiempo

print(archivo)

"x" #Solo crea un archivo nuevo, falla si es que yat existe
"a" #No borra texto, abre para escribir y pone al final del texto. Crea archivo si no existe
"a+"#Nos permite leer
"w" # si no existe, es creado. Si existe, se borra lo que estaba

archivo.close() #Cerramos la ejecucion