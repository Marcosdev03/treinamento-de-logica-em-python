num = []

for c in range(1, 4):
    number = int(input(f'Digite o {c}º número: '))
    num.append(number)

print(f'Os número digitados foram {num}')
print(f'O menor número digitado foi {min(num)}')