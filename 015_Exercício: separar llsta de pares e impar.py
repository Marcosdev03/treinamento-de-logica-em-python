lista = []
par = []
impar = []
for c in range(1, 6):
    num = int(input(f'Digite o {c}º número:'))
    lista.append(num)
print('')
for numero in lista:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)


print(f'Números pares: {par}')
print(f'Números impares: {impar}')