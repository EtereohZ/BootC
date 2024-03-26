class Pelota():
    
    def asignar(self, nuevo_color, nuevo_rebote):
        self.color = nuevo_color
        self.rebote = nuevo_rebote

    def leer_resultado(self):
        print(f"El color de la pelota de {self} es {self.color}")
        print(f"El rebote de la pelota de {self} es {self.rebote}")


tennis = Pelota()
basket = Pelota()
volley = Pelota()

tennis.asignar("Amarilla", " Poco")
basket.asignar("Naranjo", "Harto")

tennis.leer_resultado()
basket.leer_resultado()
    