
class DimensionError(Exception):
    def __init__(self, *args) -> None:
        self.mensaje = args[0]
        self.dimension = args[1]
        self.maximo = args[2]

    def __str__(self):
        if self.mensaje and self.dimension and self.maximo:
            return f"Error: {self.mensaje},  valor elegido: {self.dimension}, máximo: {self.maximo}"
        elif self.mensaje and self.dimension:
            return f"Error: {self.mensaje}, valor elegido: {self.dimension}"
        elif self.mensaje:
            return f"Error: {self.mensaje}"
        else:
            return super().__str__()