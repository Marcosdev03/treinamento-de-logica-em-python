numbers = []

for c in range(1, 3):
    num = int(input(f'Digite o {c}º número: '))
    numbers.append(num)

print(f'O maior número entre {numbers[0]} e {numbers[1]} é {max(numbers)}.')