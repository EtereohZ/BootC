from medicamento import Medicamento

precio = int(input("Ingrese precio a validar\n"))
es_valido = Medicamento.validar_mayor_a_cero(precio)

if es_valido: #si el numero es > 0 automaticamente se declara como True, haciendo que se active el if
    print("Es valido")
else: #si es false, va acá
    print("No es valido")

m1 = Medicamento()
m2 = Medicamento()

if m1.iva == m2.iva and m1.descuento == m2.descuento:
    print("Todas las instancias tienen igual descuento e iva")
    print("El valor del iva es: ", Medicamento.iva)
    print("el valor del descuento es: ", Medicamento.descuento)