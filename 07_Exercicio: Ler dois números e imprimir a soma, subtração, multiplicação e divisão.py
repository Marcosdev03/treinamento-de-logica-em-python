numbers = []
for c in range(1, 3):
    num = int(input(f'Digite o {c}º número: '))
    numbers.append(num)
num1 = numbers[0]
num2 = numbers[1]

def soma(num1,num2):
    resultado = ''
    for c in range(1, 11):
        soma1 = num1 + c
        soma2 = num2 + c
        resultado += f'{num1} + {c} = {soma1}\t{num2} + {c} = {soma2}\n'
    return resultado


def subtracao(num1, num2):
    resultado = ''
    for c in range(1, 11):
        subtracao1 = num1 - c
        subtracao2 = num2 - c
        resultado += f'{num1} + {c} = {subtracao1}\t{num2} + {c} = {subtracao2}\n'
    return resultado


def multiplicacao(num1, num2):
    resultado = ''
    for c in range(1, 11):
        multiplicacao1 = num1 * c
        multiplicacao2 = num2 * c
        resultado += f'{num1} * {c} = {multiplicacao1}\t{num2} * {c} = {multiplicacao2}\n'
    return resultado


def divisao(num1, num2):
    resultado = ''
    for c in range(1, 11):
        divisao1 = num1 / c
        divisao2 = num2 / c
        resultado += f'{num1} / {c} = {divisao1:.2f}\t{num2} / {c} = {divisao2:.2f}\n'
    return resultado


def imprimir(funçao, nomedaoperação):
    print('='*27)   
    print(nomedaoperação.center(27))
    print('='*27)
    print(funçao)
    

imprimir(soma(num1, num2),'SOMA')
imprimir(subtracao(num1, num2),'SUBTRAÇÃO')
imprimir(multiplicacao(num1, num2),'MULTIPLICAÇÃO')
imprimir(divisao(num1, num2),'DIVISÃO')


