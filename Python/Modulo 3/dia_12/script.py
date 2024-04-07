import json



try:
    archivo = [json.loads(line) for line in open("usuarios.txt", "r+")]
    print(archivo.read())
except Exception as e:
    print(f"Error: {e}")


















class Error(Exception):
    pass
