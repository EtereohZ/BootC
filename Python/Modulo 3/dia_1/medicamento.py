class Medicamento():
    descuento = 0.05
    iva = 0.18

    @staticmethod
    def validar_mayor_a_cero(numero):
        return numero > 0