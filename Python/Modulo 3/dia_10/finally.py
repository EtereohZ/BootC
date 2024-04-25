from excepciones_clases import EdadError


intentos = 3
correcto = True

while correcto and intentos:
    try:
        edad = int(input("Ingrese su edad\n"))
        if edad <0:                                     #puedo levantar cualquier cosa que yo desee como error, para que cumpla lo que necesito
            raise EdadError("Edad debe ser mayor a 0")   #Así llamo a excepciones en un if
        divisor = int(input("Ingrese un numero para dividir su edad\n"))
        print(edad/divisor)
        correcto = False
    except ValueError as e:
        print("Debe ingresar un numero")
    except ZeroDivisionError as e:
        print("No puede dividir por 0")
    except Exception as e:    #Va a tomar los mensajes estandar de eror y anteponerá un "Error: "
        print(f"Error: {e}")   #No se ubicará en exepciones que ya tienen su error definido, como en la linea 12 y 14.
                                #Si funcionará para los raise, como linea 7

    else:        #Else solo se ejecuta cuando no hay errores
        print(f"No hubieron errores.")
        
    finally:      #Finally siempre se ejecuta, haya o no una excepción
        intentos -=1
        if intentos == 1:
            print(f"Te queda {intentos} intento")
        else:
            print(f"Te quedan {intentos} intentos")
