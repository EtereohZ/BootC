class Televisor():
    pass


class MonitorLED(Televisor):
    def __init__(self, resolucion) -> None:
        self.__resolucion = resolucion

class MonitorMultifuncion(Televisor):
    def __init__(self, resolucion) -> None:
        self.__resolucion = resolucion