num = int(input('Digite um número: '))


if num % 3 == 0 and num % 5 == 0:
    print(f'O número {num} é multiplo de 3 é de 5.')
elif not num % 3 == 0 and num % 5 == 0:
    print(f'O número {num} é multiplo apenas de 5.')
elif num % 3 == 0 and not num % 5 == 0:
    print(f'O número {num} é multiplo apenas de 3')
else:
    print(f'O número {num} não é divisivel nem por 3 e nem por 5.')

