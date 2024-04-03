
class Error(Exception):
    pass

class HoraError(Error):
    def __init__(self):
        pass

class LargoTextoError(Error):
    def __init__(self, mensaje, texto, largo):
        self.mensaje = mensaje
        self.texto = texto if len(texto) <150 else None
        self.largo = largo
        
    def __str__(self):
        if self.texto is None and self.largo is None:
            return super().__str__()
        
        else:
            ret = f"{self.mensaje}."
            if self.texto != None:
                ret += f"Texto ingresado: {self.texto}"
            if self.largo != None:
                ret += f"Máximo {self.largo} caracteres permitidos"
            return ret
