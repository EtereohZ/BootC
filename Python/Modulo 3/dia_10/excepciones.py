from excepciones_clases import EdadError

consultar = True

while consultar:
    try:
        edad = int(input("Ingrese su edad\n"))
        if edad <0:                                     #puedo levantar cualquier cosa que yo desee como error, para que cumpla lo que necesito
            raise EdadError("Edad debe ser mayor a 0", edad)   #Así llamo a excepciones en un if
        divisor = int(input("Ingrese un numero para dividir su edad\n"))
        print(edad/divisor)
        consultar = False

    except ValueError as e:
        print("Debe ingresar un numero")
    except ZeroDivisionError as e:
        print("No puede dividir por 0")
    except Exception as e:    #Va a tomar los mensajes estandar de eror y anteponerá un "Error: "
        print(f"Error: {e}")   #No se ubicará en exepciones que ya tienen su error definido, como en la linea 12 y 14.
                                #Si funcionará para los raise, como linea 7