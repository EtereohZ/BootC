
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

# Output

#Punto1
recordatorios.insert(1, ["2021-02-01", "06:00", "Empezar el año"])
#Punto 2
recordatorios[3].pop(0)
print(recordatorios) #Para imprimir el calendario sin la fecha equivocada
recordatorios[3].insert(0, "2021-07-16") #Redundante con el pop de arriba pero me sirve para jugar con los metodos
#Punto 3
recordatorios.pop(2) #sad
#Punto 4
recordatorios.insert(4, ["2021-12-24", "22:00", "Cena de Navidad"])
recordatorios.insert(-1, ['2021-12-31', '22:00', 'Cena de Año Nuevo'])
recordatorios.sort() #}Porque la cena de año nuevo no se quiso poner al último

# print((recordatorios))
# for index, value in enumerate(recordatorios):
#     print(index, value)

print(recordatorios)