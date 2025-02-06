palavra = str(input('Digite uma palavra: ')).strip().lower()

def invertePalavra(parametro):
    palavraJunta = parametro.replace(' ', '')
    palavraAoContrario = palavraJunta[::-1]
    return palavraAoContrario

if palavra.replace(' ', '') == invertePalavra(palavra):
    print(f'{palavra} invertido forma {invertePalavra(palavra)} assim formando um palindromo.')
else:
    print(f'{palavra} invertido forma {invertePalavra(palavra)} e não forma um palindromo.')