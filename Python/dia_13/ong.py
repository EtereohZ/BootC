def factorial(numero):
    if numero <= 1:
        return 1
    else:
        resultado = numero * factorial(numero-1)
    return resultado
        
def productoria(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

def calcular (**kwargs):
    for k, v in kwargs.items():
        if (type(v) is int):
            print(f"el factorial de {v} es {factorial(v)}")
        else:
            print(f"La productoria de {v} es {productoria(v)}")

calcular(prod_i = [2, 4, 5], fact_i = 4)
