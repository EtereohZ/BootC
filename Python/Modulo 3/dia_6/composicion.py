from abc import ABC, abstractclassmethod

class Material(ABC):
    @abstractclassmethod
    def romper(self):
        pass

class MaterialPlastico(Material):
    nombre = "Plastico"
    duracion = "corta"

    def __init__(self, textura):
        self.textura = textura
    
    def romper(self): #No se esta utilizando
        pass

class Pelota():
    def __init__(self, tamaño:int, color:str, textura:str) -> None:
        self.tamaño = tamaño
        self.color = color
        self.textura = textura

        self.material = MaterialPlastico(self.textura) #Aquí podemos llamar a un atributo de otra clase llamada, en este caso MaterialPlastico. Ponerle self.textura a la clase llamada nos permite crear ese atributo con valor en la clase llamada
                                                       #No es necesario ponerle un argumento a la clase llamada, solo es necesario hacerlo si la clase llamada nos esta pidiendo un argumento que no está siendo ingresado en esa misma clase (nos pide textura)

p = Pelota(1, "rojo", "rugosa")
print(p.material.nombre) #Estamos llamando al atributo material, de la instancia "p", y asignandole el valor del atributo "nombre" que se encuentra en la clase MaterialPlastico, que llamamos en la linea 24
print(p.color)
a = MaterialPlastico(p.textura) #Le paso el valor que contiene el atributo self.textura, en la clase Pelota() a la clase MaterialPlastico(). Quee stamos llamando en  la linea 24
print(a.textura)