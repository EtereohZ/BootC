from .models import CustomUser, Inmuebles


def obtener_usuario(id:int):
    usuario = CustomUser.objects.filter(id=id)
    print(usuario)

def obtener_inmueble(id:int):
    inmuebles = Inmuebles.objects.filter(id=id)
    print(inmuebles)

def ingresar_inmueble(id, nombre:str, descripcion:str, m2_construidos, m2_totales, estacionamientos:int, habitaciones:int, baños:int, direccion:str, region:str, comuna:str, inmueble, precio:str):
    usuario = obtener_usuario(id)
    inmueble = Inmuebles(
        id_usuario=usuario,
        nombre = nombre,
        descripcion = descripcion,
        m2_construidos = m2_construidos,
        m2_totales = m2_totales,
        cantidad_estacionamientos = estacionamientos,
        cantidad_habitaciones = habitaciones,
        cantidad_baños = baños,
        direccion = direccion,
        region = region,
        comuna = comuna,
        tipo_inmueble = inmueble,
        precio_mensual = precio,
        )

    inmueble.full_clean()
    inmueble.save()
    return inmueble



def borrar_inmueble():
    inmueble = obtener_inmueble(id)
    inmueble.delete()
    