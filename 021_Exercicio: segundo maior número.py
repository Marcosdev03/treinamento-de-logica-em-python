lista_num = []



for c in range(1, 5):
    num = int(input(f'Digite o {c}º número: '))
    lista_num.append((num))

lista_num.sort(reverse=True)


print(f'O segundo maior item da lista é {lista_num[1]}')