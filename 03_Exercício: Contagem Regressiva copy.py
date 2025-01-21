from time import sleep
title = 'CONTAGEM REGRESSIVA'
num = int(input('Digite um número inteiro: '))

print('='*len(title))
print(title)
print('='*len(title))

for c in range(num, -1, -1):
     sleep(1)
     print(c,end=' ')    
print('.')    


    



