from tiendas import Restaurante, Farmacia, Supermercado


eleccion_continuar = 1

eleccion_tienda = int(input(f"""
Buenos días, que tienda le gustaría crear hoy? Ingrese el numero que corresponda a su decisión:
1. Restaurante
2. Farmacia
3. Supermercado
4. No quiero mi propia tienda
"""))
nombre_tienda = input("Elija el nombre de su tienda: ")
delivery = int(input("¿Cuanto quiere cobrar por delivery? "))

if eleccion_tienda == 1:
    mi_tienda = Restaurante(nombre_tienda, delivery)
elif eleccion_tienda == 2:
    mi_tienda = Farmacia(nombre_tienda, delivery)
elif eleccion_tienda == 3:
    mi_tienda = Supermercado(nombre_tienda, delivery)
else:
    print("Bueno, bai")

continuar = int(input(f"""quiere ingresar un producto?
1. Sí
2. No    
"""))
while continuar == 1:
    ingresar_producto = input("Ingrese producto: ")
    ingresar_precio = input("Ingrese el precio: ")
    if isinstance(mi_tienda, Restaurante):
        mi_tienda.ingresar_productos(ingresar_producto, ingresar_precio, 0)
    else:
        ingresar_stock = int(input("Ingrese stock: "))
        mi_tienda.ingresar_productos(ingresar_producto, ingresar_precio, ingresar_stock)

    print(f"Tu producto es{mi_tienda.listado_productos}")
    
    continuar = int(input(f"""Deseas agregar otro producto?
1. Sí
2. No                      
"""))

lista = mi_tienda.listado_productos()
print(f"""Estos son tus productos
{lista}""")

comprar_producto = input(f"¿Que producto quiere comprar?\n")
comprar_cuantos = int(input(f"¿Cuantos va a comprar?\n"))
mi_tienda.realizar_venta(comprar_producto, comprar_cuantos)


