from error import HoraError, LargoTextoError
from reunion import Reunion
import re

titulo = None
hora = None
time_re = "^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$" #Expresion regular


while True:
    try:
        titulo = input(f"Ingrese el nombre de la reunión, hasta un maximo de 150 caracteres.")
        if len(titulo) > 150:
            raise LargoTextoError("El nombre de la reunión excede los cáracteres maximos", 150)
        if hora in None or re.search(time_re, hora) is None:
            hora = input(f"Ingrese la hora de la reunion hh:mm:ss ")
            if re.search(time_re, hora) is None:
                raise HoraError(f"Formato debe ser hh:mm:ss")
    except Exception as e:
        print(f"\n{e}\n")
        continue
    else:
        break


r = Reunion(titulo, hora)
print("Reunion creada correctamente")