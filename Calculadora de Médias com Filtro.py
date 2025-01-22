notasValidas = []
notasIgnoradas = []
contador = 1

while (contador < 6):
        notas = int(input(f'Por favor digite a {contador}º nota: '))
        if notas < 0:
            print('Nota inválida! Ignorada.')
            notasIgnoradas.append(notas)
        elif notas > 10:
            print('Nota inválida! Ignorada.')
            notasIgnoradas.append(notas)
        else:
            notasValidas.append(notas)
        contador += 1

if notasValidas == []:
    print('Notas válidas: Nenhuma nota foi válidada.')
else:
    print(f'Notas validas: {notasValidas}')
if notasIgnoradas == []:
    print('Todas as notas foram válidas.')
else:
    print(f'Notas ignoradas: {notasIgnoradas}')

if len(notasValidas) > 0:
    mediaNotas = sum(notasValidas) / len(notasValidas)
    print(f'Média de notas: {mediaNotas:.2f}')
else:
    print('Média: Não temos notas válidas para tirar a média')


