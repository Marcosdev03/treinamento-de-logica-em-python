from random import randint
lista_de_palavras = [
    "python", "desenvolvimento", "algoritmo", "programacao", "desafio",
    "computador", "internet", "inteligencia", "software", "hardware",
    "tecnologia", "educacao", "digital", "machine", "rede", "dados",
    "rede", "usuario", "projeto", "estudo", "desenvolvedor", "aplicacao"
]
indice_sorteado = randint(0, len(lista_de_palavras) -1 )
palavra_secreta = lista_de_palavras[indice_sorteado]
title_jogo = 'JOGO DA PALAVRA SECRETA'
descricao_jogo = 'Tente descubrir qual é a palavra secreta dentro das palavras abaixo.'
mensagem_erro = 'Você errou, tente novamente!'
mensagem_acerto = (f'PARABÉNS VOCÊ ACERTOU, A PALAVRA SECRETA ERA {palavra_secreta}')

print(palavra_secreta)
print('=' * len(title_jogo))
print('JOGO DA PALAVRA SECRETA')
print('=' * len(title_jogo))
print('Tente descubrir qual é a palavra secreta dentro das palavras abaixo.')
print('-' * len(descricao_jogo))
print('''
    "python", "desenvolvimento", "algoritmo", "programacao", "desafio",
    "computador", "internet", "inteligencia", "software", "hardware",
    "tecnologia", "educacao", "digital", "machine", "rede", "dados",
    "rede", "usuario", "projeto", "estudo", "desenvolvedor", "aplicacao"
''')

while True:
    palavra_digitada = str(input('tente adivinhar a palavra secreta:')).strip().lower()

    if palavra_digitada == palavra_secreta:
        print('-' * len(mensagem_acerto))
        print(f'PARABÉNS VOCÊ ACERTOU, A PALAVRA SECRETA ERA \'{palavra_secreta.upper()}\'')
        print('-' * len(mensagem_acerto))
        break
    else:
        print('-' * len(mensagem_erro))
        print('Você errou, tente novamente!')
        print('-' * len(mensagem_erro))
