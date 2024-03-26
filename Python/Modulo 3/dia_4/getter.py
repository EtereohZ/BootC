class Pelota():
    def __init__(self, color):
        self.color = color #Valor del atributo dado por parametro en el metodo, linea 8
        self.tamaño_pelota = 10 #Valor dado desde el cuerpo del metodo
        self.tipo = "goma" #Valor dado directamente

    @property
    def tamaño(self):
        return f"Es una pelota de color {self.tamaño_pelota} y está hecha de {self.tipo}"
    
    @tamaño.setter
    def tamaño(self, tamaño):
        self.tamaño_pelota = tamaño if tamaño > 120 else 1


basket = Pelota("rojo")
print(basket.tamaño) #Invocamos la función poniendo la instancia con uun punto seguida del nombre de la funcion: instacia.funcion -->> basket.propiedades. y se imprime el return

basket.tamaño = 3
print(basket.tamaño)