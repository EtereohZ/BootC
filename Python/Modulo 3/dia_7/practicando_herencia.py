class Animal():
    def __init__(self, especie, edad) -> None:
        self.especie = especie
        self.edad = edad

    def sonido(self):
        pass

class Perro(Animal):
    # def __init__(self,color):                   #Al hacer un __init__ en la clase hija estamos reemplazando el metodo __init heredado,
    #     self.color = color                       #lo que significa que no heredamos esos atributos y en cambio solo creamos el atributo color

    
    def __init__(self, especie, edad, color): 
        #Alternativa 1                          #Si queremos que nuestro Perro() tenga un parametro extra (ej, "color") en el constructor tenemos 2 opciones: 
        # self.especie = especie                  #Creamos un nuevo __init__ con todas las variables(especie, edad y color)
        # self.edad = edad
        # self.color = color                                      

        #Alternativa 2
        super().__init__(especie, edad)         #Usamos el super() para llamar al __init__ de la lase padre que ya aceptaba especie y edad
        self.color = color                      #Y aquí asignamos el atributo nuevo con su variable
                                                #Los parametros en el __init__ deben mantenersse y su orden
    def sonido(self):
        print("Guau")

p = Perro("mamifero", 10, "rojo")
a = Animal("desconocida", 10)

print(p.especie)
print(p.color)
print(a.edad)
p.sonido()
print(type(p).__name__) #Esto imprime el nombre de la clase