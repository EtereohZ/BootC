from usuario import Usuario
import json
from datetime import datetime



instancias = []
archivo = open("usuarios.txt", "r+")
try:
    datos = json.load(archivo)
    for d in archivo:
        print(d)
        instancias.append(Usuario(d.get("nombre"), d.get("apellido"), d.get("email"), d.get("genero"),)) #Intentamos crear las instancias de usuario según los datos entregados
except Exception as e:
    with open("error.log", "a+") as log:
        now = datetime.now()
        log.write(f"[{now.strftime('$Y/%m/%d %H:%M:%S')}] Error: {e}\n")  #Creamos el log de errores con fecha
else:
    print("Datos guardados perfectamente") #No va a pasar




















class Error(Exception):
    pass
