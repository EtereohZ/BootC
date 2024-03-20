
class Te():
    duracion = 365


    @staticmethod
    def tiempo_y_recomendacion(sabor):
        if sabor == 1:
            return 3, "para consumir al nacer de la noche"
        elif sabor == 2:
            return 5, "para consumir luego de comer verduras"
        elif sabor == 3:
            return 6, "para conectarse con la naturaleza"

    @staticmethod
    def precio(formato):
        if formato == 1:
            return 300, 3000
        elif formato == 2:
            return 500, 5000



