#Função com repetição
#Crie uma função chamada contagem_regressiva que recebe um número e imprime uma contagem regressiva a partir desse número até 0.
import time
from time import sleep

def contagemRegressiva(parametro):
    contagem = []
    for c in range(parametro, 0, -1):
        contagem.append(c)
        time.sleep(1)
        print(c, end= ' ', flush=True)

def titulo(parametro):
    titulo_texto = parametro
    tamanho_texto = len(titulo_texto)
    print('-'*tamanho_texto)
    print(titulo_texto)
    print('-' * tamanho_texto)

while True:
    try:
        num = int(input('Digite um número para contagem regressiva: '))
        titulo('Contagem Regressiva')
        contagemRegressiva(num)
        break
    except ValueError:
        print('Por Favor Digite Um Número inteiro: ')
