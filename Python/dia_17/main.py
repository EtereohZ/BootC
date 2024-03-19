from modulo import request_get 
from html_template import template

#Metodo 1###################################################################################

# lista_img = [(elemento["images"], elemento["name"]) for elemento in response][0:10]

# imagen = ""
# for index, valor in enumerate(lista_img):
#     for t1, t2 in lista_img: #t1 y t2 por tupla 
#         # print(t1["main"])
#         # print(t2["spanish"])
#         imagen += f'''
# <img src ="{t1["main"]}"> +'\n'
# <h1>{t2["spanish"]}</h1>'''


#Metodo 2 ######################################################################################
lista_img = [elemento["images"] for elemento in request_get('https://aves.ninjas.cl/api/birds')][0:10]
lista_nom = [elemento["name"] for elemento in request_get('https://aves.ninjas.cl/api/birds')][0:10]

imagen = ''

def orden (lista_img, lista_nom):
    contenido = ''
    for index, value in enumerate(lista_img):
        imagen = value["main"]
        for index, value in enumerate(lista_nom):
            nom_español = value["spanish"]
            nom_ingles = value["english"]
        contenido += f'''
    <h1>{nom_español}</h1>
    <h3>{nom_ingles}</h3>
    # <img src ="{imagen}"> +'\n'
    # '''
    return contenido

orden (lista_img, lista_nom)


    salida = open("index.html", "w+")
    salida.write(html_template)


