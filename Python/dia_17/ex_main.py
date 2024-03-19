from html_template import template

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
    final = template(contenido)
    salida = open("index.html", "w+", encoding='utf-8')
    salida.write(final)
    salida.close()
    
