
import string
import getpass
import random
from itertools import permutations

# contraseña = getpass.getpass("Ingrese su contraseña\n")

password = getpass.getpass()
chars = string.ascii_lowercase
chars_list = list(chars)


attempt = 0
# guess = ""
# while guess != password:
#     attempt += 1
#     guess = random.choices(chars_list, k = len(password))
#     print(guess)
#     guess = "".join(guess)
#     print (guess)



# for i in range(1, len(password) + 1):
#     for p in permutations(password, i):
#         print(p)
#         p = "".join(p)
#         attempt += 1




print(f"Tu clave es {p}")
print(f"Tomo {attempt} intentos")