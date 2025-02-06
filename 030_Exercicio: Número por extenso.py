numeros_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
    "dezoito", "dezenove", "vinte"
)

while True:
    try:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        else:
            print('Número fora do intervalo tente novamente!')
    except ValueError:
        print('Entrada inválida! Por Favor digite um número entre 0 e 20: ')

relacaoDeNum = numeros_extenso[num].upper()

print(f'Você digitou o número: {relacaoDeNum}')