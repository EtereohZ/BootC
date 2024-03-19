from ex_main import orden
from modulo import request_get

lista_img = [elemento["images"] for elemento in request_get('https://aves.ninjas.cl/api/birds')][0:10]
lista_nom = [elemento["name"] for elemento in request_get('https://aves.ninjas.cl/api/birds')][0:10]

orden(lista_img, lista_nom)