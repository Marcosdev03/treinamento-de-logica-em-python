num = int(input('Digite um número: '))


if num % 3 == 0 and num % 5 == 0:
    print(f'O número {num} é multiplo de 3 é o número {num} também é multiplo de 5.')
elif num % 3 == 0:
    print(f'O número {num} é divisível apenas pelo número 3')
elif num %  5 == 0:
    print(f'O número {num} é divisível apenas pelo número 5.')
else:
    print(f'O número {num} não e divisível por nenhum dos dois!')
