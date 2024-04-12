

class Error(Exception):
    pass

class LargoExcedidoError(Error):
    pass

class SubTipoInvalidoError(Error):
    def __init__(self, mensaje, sub_tipo) -> None:
        self.mensaje = mensaje
        self.sub_tipo = sub_tipo
