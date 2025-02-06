from random import randint

lista = ()
contador = 1


while contador < 6:
    lista += (randint(1, 10),)
    contador += 1

print(lista)
print(max(lista))
print(min(lista))