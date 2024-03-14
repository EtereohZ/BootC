diccionario1 = {
    "Nombre": "José Tomás",
    "Edad": "27 años",
    "Estado civil": "Soltero",
    "Lugar de nacimiento": "Santiago",
    "Nacionalidad": "Chileno",
    "Conflicto": "No"
}

diccionario2 = {
    "Color": "Rojo",
    "Comida": "Sushi",
    "Dulce": "Chocolate",
    "Estación": "Otoño",
    "Conflicto": "Si"
}

diccionario1["Sexo"] = "Masculino" #Agregamos una key nueva con un valor al diccionario

print(diccionario1)
print(diccionario2)
print("")
print(diccionario1["Nombre"])
print(diccionario2["Comida"])
print("")
borrar = diccionario2.pop("Estación")
print(diccionario2) #Imprimimos la lista con elemento borrado
print(borrar) #Imprimimos elemento borrato

diccionario1.update(diccionario2)
print(diccionario1) #Imprimimos la lista combinada
