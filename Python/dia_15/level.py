def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    if n_pregunta <= p_level:
        level = "basico"
    elif n_pregunta <= p_level * 2:
        level = "intermedio"
    else:
        level = "avanzado"
    
    #No tengo idea por que me tira el error "TypeError: '<=' not supported between instances of 'int' and 'str'"
        #tanto n_pregunta como p_level son int
    
    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias