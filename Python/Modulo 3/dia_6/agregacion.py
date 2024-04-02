class Material():
    def __init__(self, nombre:str, duracion:str, textura:str) -> None:
        self.nombre = nombre
        self.duracion = duracion
        self.textura = textura

class Pelota():
    def __init__(self, tamaño:int, color:str, material:Material) -> None: #en material: Material, estamos diciendo que el valor material vendra de algun atributo de la clase Material(). 
        self.tamaño = tamaño                                              #Al pasarle el atributo en la ejecución, hay que pasarle una instancia de la clase Material. en este caso la creamos en la linea 14
        self.color = color                                                                        
        self.material = material


m = Material("Plastico", "Corta", "Lisa")

p = Pelota("16", "Amarillo", m) #Aquí le estamos pasando la instancia "m" que pertenece a la clase Material()

print(p.material.nombre)  #Estamos imprimiendo el valor que contiene el atributo "material", que se encuentra llamando a un atributo de la clase Material()
print(p.material.textura) #La secuencia es: instancia.atributo.atributo de clase que estamos llamando(Material())
print(p.color)            #