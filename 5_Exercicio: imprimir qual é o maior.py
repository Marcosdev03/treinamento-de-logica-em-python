num = []

for c in range(1, 3):
   num1 = int(input(f'Digite o {c}º número: '))
   num.append(num1)
   
print(f'Os número digitados foram {num}')  
print(f'O maior número é {max(num)}.')