from .models import CustomUser, CentroMedico, Especialista, Agenda

#Algunos serviciosde utilidad para obtener, crear y eliminar objetos de interés

def obtener_usuario(id:int):
    usuario = CustomUser.objects.filter(id=id)
    print(usuario)

def obtener_especialista(id:int):
    especialistas = Especialista.objects.filter(id=id)
    print(especialistas)

def obtener_centro_medico(id:int):
    centros = CentroMedico.objects.filter(id=id)
    print(centros)

def obtener_agenda(id:int):
    agendas = Agenda.objects.filter(id=id)
    print(agendas)

def ingresar_usuario(nombre:str, apellido:str, correo:str):
    usuario = CustomUser(
        id_usuario=usuario,
        nombre = nombre,
        apellido = apellido,
        correo = correo
        )

    usuario.full_clean()
    usuario.save()
    return usuario

def ingresar_especialista(nombre:str, apellido:str, especialidad:str):
    especialista = Especialista(
        nombre = nombre,
        apellido = apellido,
        especialidad= especialidad
        )

    especialista.full_clean()
    especialista.save()
    return especialista

def borrar_usuario(id):
    usuario = obtener_usuario(id=id)
    usuario.delete()