from .models import Curso, Profesor, Estudiante, Direccion

# Services below

def crear_curso(codigo:str, nombre:str, version:int):
    nuevo_curso = Curso(
            codigo=codigo,
            nombre=nombre,
            version=version,
            )

    nuevo_curso.full_clean()
    nuevo_curso.save()
    return nuevo_curso

def crear_profesor(rut:str, nombre:str, apellido:str, activo:bool, codigo_curso):
    curso = obtener_curso(codigo_curso)
    nuevo_profesor = Profesor(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        activo=activo,
        cursos=curso,
        )

    nuevo_profesor.full_clean()
    nuevo_profesor.save()
    return nuevo_profesor

def crear_estudiante(rut:str, nombre:str, apellido:str, activo:bool, codigo_curso):
    curso = obtener_curso(codigo_curso)
    nuevo_estudiante = Estudiante(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        cursos = curso,
        activo = activo,
        )
    
    nuevo_estudiante.full_clean()
    nuevo_estudiante.save()
    return nuevo_estudiante

def crear_direccion(calle:str, numero:str, dpto:str, comuna:str, ciudad:str, region:str, rut:str):
    estudiante = obtener_estudiante(rut)
    nueva_direccion = Direccion(
        calle=calle,
        numero=numero,
        dpto=dpto,
        comuna=comuna,
        ciudad=ciudad,
        region=region,
        estudiante=estudiante,
    )

    nueva_direccion.full_clean()
    nueva_direccion.save()
    return nueva_direccion

def obtener_curso(codigo):
    curso = Curso.objects.filter(codigo=codigo)

    print(curso)

def obtener_profesor(rut):
    profesor = Profesor.objects.filter(rut=rut)

    print(profesor)

def obtener_estudiante(rut):
    estudiante = Estudiante.objects.filter(rut=rut)

    print(estudiante)

def agregar_profesor_a_curso(rut:str, codigo:str):
    profesor_elegido = Profesor.filter(rut=rut)
    curso_elegido = Curso.filter(codigo=codigo)
    profesor = profesor_elegido.cursos.add(curso_elegido)

    profesor.full_clean()
    profesor.save()
    return profesor
    
def agregar_curso_a_estudiante(rut:str, codigo:str):
    estudiante_elegido = Profesor.filter(rut=rut)
    curso_elegido = Curso.filter(codigo=codigo)
    estudiante = estudiante_elegido.cursos.add(curso_elegido)

    estudiante.full_clean()
    estudiante.save()
    return estudiante

def imprimir_estudiantes_en_curso(nombre:str):
    estudiantes = Curso.estudiantes.filter(nombre=nombre)
    listado = []
    for e in estudiantes:
        dict_estudiantes = {
            'Nombre' : e.nombre,
            'Apellido' : e.apellido,
        }
        listado.append(dict_estudiantes)
    print(listado)