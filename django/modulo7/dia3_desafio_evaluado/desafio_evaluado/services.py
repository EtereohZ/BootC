from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    tareas =  Tarea.objects.filter(eliminada=False)
    subtareas_raw = SubTarea.objects.filter(eliminada=False)
    todas_tareas = []
    subtareas = []
    for sub in subtareas_raw:
        subtareas.append(sub)
    for tarea in tareas:
        dict_tareas = {
            'Tarea' : tarea,
            'Subtarea' : tarea.subtarea_set.filter(eliminada=False)
        }
        todas_tareas.append(dict_tareas)
    return todas_tareas

def crear_nueva_tarea(descripcion=''):
    nueva_tarea = Tarea(descripcion = descripcion, eliminada=False)
    nueva_tarea.save()

    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id, descripcion=''):
    tarea = Tarea.objects.get(tarea_id)
    nueva_subtarea = SubTarea(descripcion = descripcion, eliminada = False, tarea_id = tarea)
    nueva_subtarea.save()

    return recupera_tareas_y_sub_tareas()

def elimina_tarea(id):
    tarea = Tarea.objects.get(id)
    tarea.delete()

def elimina_sub_tarea(id):
    subtarea = SubTarea.objects.get(id)
    subtarea.delete()

def imprimir_en_pantalla():
    print(recupera_tareas_y_sub_tareas())
    