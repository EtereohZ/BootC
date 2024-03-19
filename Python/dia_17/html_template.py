from main import orden


def template(lista):
    html_template = f'''
    <!DOCTYPE html>
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    <title>Áves de Chile</title>
    </head>
    <body>
    <h1>Nuestra página Web</h1>
    {lista}
    </body>
    </html>
    '''
    return html_template

template(orden(lista_img, ))
