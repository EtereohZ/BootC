from usuario import Usuario
import json
from datetime import datetime



instancias = []
archivo = open("usuarios.txt", "r+")
try:
    datos = json.load(archivo)
    for d in archivo:
        print(d)
        instancias.append(Usuario(d.get("nombre"), d.get("apellido"), d.get("email"), d.get("genero"),))
except Exception as e:
    with open("error.log", "a+") as log:
        now = datetime.now()
        log.write(f"[{now.strftime('$Y/%m/%d %H:%M:%S')}] Error: {e}\n")
else:
    print("Datos guardados perfectamente")




















class Error(Exception):
    pass
