from campaña import Campaña


e = Campaña("La mejor", "24/05/2022", "24/07/2023") #Creamos la instancia de campaña
e.agregar_anuncio(1, 1, "wapa.cl", "clic.cl", "instream", 5) #Utilizamos el metodo para agregar anuncios a la campaña
e.agregar_anuncio(2, 2, "opa.com", "clocl.as", "native", "") #Ingresar un sub_tipo equivocado mandará error
# e.anuncios[0].sub_tipo = "be"  #Intentar cambiar el sub_tipo ingresado por unbo no habil también mandará error


try:
    e.nombre = input("Ingrese un nuevo nombre para su majestuosa campaña:\n")
    print("Muy bonito nombre")
    e.anuncios[0].sub_tipo = input("Ingrese el nuevo subtipo de video para su primer anuncio:\n")
except Exception as e:
    print(f"Error Mortal: {e}") #El metodo para cambiar subtipo e encuentra en anuncio.py, linea 52
else:
    print(e)
finally:
    print("hola")

