class Medicamentos():
    IVA = 0.18


    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock
        self.precio_bruto = 0
        self.precio_neto = 0
        self.descuento = 0
    
    @staticmethod
    def validador(numero):
        return numero > 0
    
    @property
    def precio(self):
        return self.precio_neto
    
    @precio.setter
    def precio(self, precio_bruto):
        self.precio_bruto = precio_bruto
        if self.validador(precio_bruto):
            self.precio_neto = precio_bruto + precio_bruto * self.IVA
            if self.precio_neto >= 10000 and self.precio_neto <20000:
                self.descuento = 0.1
            elif self.precio_neto >=20000:
                self.descuento = 0.2
            if self.descuento:
                self.precio_neto *= (1- self.descuento)

    def __eq__(self, other) -> bool:
        return self.nombre.lower() == other.nombre.lower()
    
    def __iadd__(self, other):
        if self.stock == other.stock:
            self.stock += other.stock
            return self