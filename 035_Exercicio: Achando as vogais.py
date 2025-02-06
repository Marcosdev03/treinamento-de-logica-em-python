palavras = ('macarrao', 'sapato')


for palavra in palavras:
    print(f'\nNa palavra {palavra} temos as vogais: ', end='')


    for p in palavra:
        if p in 'aeiou':
             print(p, end= ' ')