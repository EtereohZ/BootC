import getpass
import string  


password = getpass.getpass()
chars = string.ascii_lowercase

attempt = 0
guess = ""
for i in password:
    for e in chars:
        attempt +=1
        if e == i:
            guess += e
            break
print(f"Hay {attempt} intentos")
print(f"La clave es {guess} ")

