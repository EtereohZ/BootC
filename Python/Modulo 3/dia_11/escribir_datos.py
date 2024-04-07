from datetime import datetime

# try:
#     edad = int(input("Ingrese su edad: \n"))
# except Exception as e:
#     with open(f"{round(time.time())}.log", "w") as file:   #hora ilegible
#         file.write(f"Error: {e}")  #Aquí se escribirá el resultado en el archivo


try:
    edad = int(input("Ingresar edad:\n"))
except Exception as e:
    with open(f"error.log", "a+") as log:
        log.seek(16)   #??????????????????????????
        print(log.read())
        now = datetime.now()
        log.write(f"[{now.strftime('%Y/%m/%d %H:%M:%S')}] Error: {e}\n")   #noe.strftime not permite formatear la fecha, con lo que está en parentesis
        # log.seek(0)