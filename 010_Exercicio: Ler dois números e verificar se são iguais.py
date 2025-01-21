number = []

for c in range(1,3):
    num = int(input(f'Digite o {c}º número: '))
    number.append(num)
    
if number[0] == number[1]:
    print(f'O número {number[0]} é igual o {number[1]}!')
else:
    print(f'O número {number[0]} é diferente do {number[1]}.')