import requests

def request_get(url):
    response = requests.get(url)
    response =response.json()
    return response

url = ''
request_get(url)


# response = requests.get(url)
# response = response.json()