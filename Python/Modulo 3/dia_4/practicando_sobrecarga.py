class Numero():
    def __init__(self, par, impar) -> None:
        self.numero_par = par
        self.numero_impar = impar

    def __add__(self, other):
        return self.numero_par + other.numero_impar 
    
    def __add__(self, other): #La última anula a la primera, solo dando este resultado
        return self.numero_impar + other.numero_par
    
    def __str__(self) -> str:
        hola = f"{n1.numero_par}"
        chao = f"{n2.numero_impar}"
        return f"{hola}     {chao}"
    
n1 = Numero(4, 5)
n2 = Numero(2, 7)

# print(n1 + n2)
print(n1)