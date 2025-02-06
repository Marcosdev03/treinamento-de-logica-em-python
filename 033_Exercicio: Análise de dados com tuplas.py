from itertools import count

lista_num = ()
contador = 1

while contador < 5:
    num = int(input(f'Digite o {contador}ª número: '))
    lista_num += (num,)
    contador += 1

print(f'O número 9 apareceu {lista_num.count(9)}')
if 3 in lista_num:
    print(f'O número 3 apareceu na posição {lista_num.index(3) +1}.')
else:
    print('O número 3 não foi encontrado na lista.')
print('Os valores pares digitador foram ', end= ' ')
for n in lista_num:
    if n % 2 == 0:
        print(n, end= ' ')