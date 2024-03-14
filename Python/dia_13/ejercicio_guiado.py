
preguntas = ["Como te llamas?", "Donde naciste?", "Cual es tu color favorito?"]

respuestas = []

def menu():
    for pregunta in preguntas:
        print(pregunta)
        print('Opciones: ')
        print('1). De acuerdo')
        print('2). En desacuerdo')
        print('3). No me interesa')
        respuestas.append(input(""))

    print(respuestas)
menu()
