from pizza import Pizza
from ingredientes import salsas as s

print(f"""
Los valores de los atributos de la clase Pizza() son los siguientes:
-Atributo masa tiene el valor de {Pizza.masa}
-Atributo tamaño tiene el valor de {Pizza.tamaño}
-Atributo ingredientes tiene el valor de {Pizza.ingredientes}
-Atributo precio tiene el valor de {Pizza.precio}
""")

salsa = "salsa de tomate"
salsa_valida = Pizza.validador(salsa, s)
print(f"El estado de la presencia de la salsa de tomate en la lista de salsas es: {salsa_valida}")
print()
pizza_orden = Pizza()
pizza_orden.pedido()

masa = pizza_orden.masa #En estas variables guardamos los valores de los atributos que contienen los ingredientes asignados
ingrediente1 = pizza_orden.ingrediente_1
ingrediente2 = pizza_orden.ingrediente_2
ingrediente3 = pizza_orden.ingrediente_3
valida = pizza_orden.valida
print(f"""
Los ingredientes elegidos son:
El tipo de masa elegida es {masa}.
El ingrediente proteico es {ingrediente1}.
El primer ingrediente vegetal es {ingrediente2}.
El segundo ingrediente vegetal es {ingrediente3}.
El valor de tu pizza es ${Pizza.precio}
¡Felicidades! Su pizza es {valida}
No se si hice trampa porque al volver a preguntar frente a valores invalidos, la pizza nunca puede ser False
""")