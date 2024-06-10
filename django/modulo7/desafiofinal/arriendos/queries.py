from .models import Inmuebles

query = "select * from arriendos_inmuebles where region = 'Atacama'"

Inmuebles = Inmuebles.objects.raw(query)

archivo = open('archivo.txt', 'a')

for t in todas:
    archivo.write(t.nombre)
    archivo.write('\n')
archivo.close()