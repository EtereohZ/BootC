class Pelota(): #Se define la clase on mayuscula y ()
    color = "Variado" #Estos son atributos de clase, o estaticos
    forma = "redondeada"

class Medicamento():
    descuento = 0.05
    iva = 0.19

paracetamol = Medicamento() #Para crear la instancia "paracetamol"
print(paracetamol.descuento) #imprimimos el atributo de clase de la intancia