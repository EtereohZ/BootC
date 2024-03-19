import requests

def request_get(url):
    response = requests.get(url)
    response =response.json()
    return response

url = 'https://aves.ninjas.cl/api/birds'
request_get(url)