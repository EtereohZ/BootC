
def template(lista):
    html_template = f'''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Áves de Chile</title>
    </head>
    <body>
    <h1>Los loros son bonitos</h1>
    {lista}
    </body>
    </html>
    '''
    return html_template