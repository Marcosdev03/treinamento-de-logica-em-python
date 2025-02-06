#2. Função com condicional
from sys import exception

#Crie uma função chamada par_ou_impar que recebe um número e retorna "Par" se o número for par e "Ímpar" se for ímpar.


while True:
    try:
        num = int(input('Digite um número: '))
        break
    except ValueError:
        print('Por favor, digite um número inteiro válido.')


def par_ou_impar(parametro):
    if parametro % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'


print(f'O número digitado é {par_ou_impar(num)}.')