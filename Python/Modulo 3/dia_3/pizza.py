import ingredientes as i

class Pizza():
    ingredientes = ""
    tamaño = "Familiar"
    masa = ""

    @staticmethod
    def validador(string, lista):
        if string in lista:
            return True
        else:
            print("Este ingrediente no esta disponible o no se encuentra. Intentalo de nuevo.")
            return False
    
    def pedido(self):
        valido = False
        while valido == False:
            masa = input(f"Ingrese el tipo de masa que desea: {", ".join(i.lista_masas)})\n")
            valido = Pizza.validador(masa, i.lista_masas)
            self.masa = masa
        valido = False
        while valido == False:
            proteina = input(f"Ingrese el ingrediente protéico que desee: {", ".join(i.lista_proteina)}\n")
            valido = Pizza.validador(proteina, i.lista_proteina)
            self.ingrediente_1 = proteina
        valido = False
        while valido == False:
            vegetal1 = input(f"Ingrese el primer ingrediente vegetal: {", ".join(i.lista_vegetales)})\n")
            valido = Pizza.validador(vegetal1, i.lista_vegetales)
            self.ingrediente_2 = vegetal1
        valido = False
        while valido == False:
            vegetal2 = input(f"Ingrese el segundo ingrediente vegetal que desea: {", ".join(i.lista_vegetales)}\n")
            valido = Pizza.validador(vegetal2, i.lista_vegetales)
            self.ingrediente_3 = vegetal2
        # print(self.masa)
        # print(self.ingrediente_1)
        # print(self.ingrediente_2)
        # print(self.ingrediente_3)




pizza_orden = Pizza()
pizza_orden.pedido()
    