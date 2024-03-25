class PelotaDeDeporte():
    tipo = "Deporte"

class PelotaDePlastico():
    tipo = "Plastico"

class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico): #Tiene prioridad el primero en heredarse
    pass                                                   #Si ambas clases padre tienen constructores, solo se inicia el primero


print(PelotaDePingPong.tipo)#Al haber mismo tipo o metodo, tiene prioridad el que se ingresa primero
