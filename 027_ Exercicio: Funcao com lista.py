 #Função com lista
#Crie uma função chamada maior_numero que recebe uma lista de números e retorna o maior número da lista.
contador = 1
lista_num = []
while contador < 6:
        try:
            numeros = int(input('Digite um número inteiro: '))
            lista_num.append(numeros)
            contador += 1
        except ValueError:
            print('Por Favor digite um número inteiro!')


def maior_num():
    maior = max(lista_num)
    return maior

print(f'Lista: {lista_num}')
print(f'O maior número da lista é {maior_num()}.')