from te import Te

print("Bienvenido a su aplicacción de té gratis, a continuación será parte de una experiencia magica blabla")
sabor = int(input(f"""
Elija el numero que corresponde al tipo de té que desea:
1. Té negro
2. Té verde
3. Agua de hierbas.   
"""))
if sabor == 1:
    sabor_te = "Té negro"
elif sabor == 2:
    sabor_te = "Té verde"
elif sabor == 3:
    sabor_te = "Agua de hierbas"

formato = int(input(f"""
¿Que formato de té desea? Elija el numero
1. 300 gramos
2. 500 gramos 
"""))
tiempo, recomendacion = Te.tiempo_y_recomendacion(sabor)
masa, precio = Te.precio(formato)


print(f"""
Gracias por elegirnos a nosotros para su maravilloso té.
El té que ha elegido es {sabor_te}, este es un té muy especial, su recomendación es {recomendacion}.
Su tiempo de preparación es de {tiempo} minutos, y tiene una duración de {Te.duracion} días
El precio de los {masa}gr elegidos corresponde a ${precio}.
Que tengas un Texcelente día!

""")