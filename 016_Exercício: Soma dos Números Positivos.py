numeros = []
num_positivos = []
num_negativos = []

while True:
    num = int(input('Digite um número ou digite (0) para sair: '))
    if num == 0:
        break
    numeros.append(num)
    if num > 0:
         num_positivos.append(num)
    else:
        num_negativos.append(num)

print(f'Números positivos: {num_positivos}')
print(f'Números negativos: {num_negativos}')
