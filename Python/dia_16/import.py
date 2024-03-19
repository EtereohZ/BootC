import requests
import json 


# def request_get(url):
#     return json.loads(requests.get(url).text)



url = "https://ghibliapi.vercel.app/films"
response = requests.get(url)
response = response.json()
# response = response.json()

lista_img = [elemento["image"] for elemento in response]

# img_template = Template('<img src ="$url">')

print(lista_img)
texto_img = ''
for img in lista_img:
    texto_img += f'<img src ="{img}">' +'\n'

# print(texto_img)

html_template = f'''
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Título de la Página</title>
</head>
<body>
<h1>Nuestra página Web</h1>
{texto_img}
</body>
</html>
'''

# html = html_template.substitute(body = texto_img)
salida = open("index.html", "w+")
salida.write(html_template)