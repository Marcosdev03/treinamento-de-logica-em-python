lista_de_precos = (
        'feijão', 8.90,
        'arroz', 27.90,
        'óleo', 8.90,
        'Macarrão',3.50,
        'carne', 35.90
)
print('-'*40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-'*40)
for pos in range(0, len(lista_de_precos)):
    if pos % 2 == 0:
        print(f'{lista_de_precos[pos]:.<30}',end= ' ')
    else:
        print(f'R${lista_de_precos[pos]:>7.2f}')
print('-'*40)