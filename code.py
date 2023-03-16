import string
import random

while True:
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    print(password)
#Pressione Ctrl + v para cancelar
