
class Nombre():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    def __str__(self) -> str:
        return f"Un dia, {self.nombre} salió al parque " #Modulo que nos retorna un string

n1 = Nombre("Antonio")

print(n1)

class Pelota():
    def __init__(self, tamaño) -> str:
        self.tamaño = tamaño
    def __add__(self, other): #Modulo que nos permite sumar valores de atributos
        return self.tamaño + other.tamaño
    
a = Pelota(5)
b = Pelota(4)

print(a + b)

class Color():
    def __init__(self, color) -> None:
        self.color = color

    def __eq__(self, other) -> bool: #Modulo que genera equivalencias, las instancias son distintas, pero con color igual o equivalente
        return self.color == other.color

color1 = Color("rojo")
color2 = Color("rojo")

print(color1 == color2)