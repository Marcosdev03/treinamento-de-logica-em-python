nota = []

for c in range(1, 4):
    aluno_nota = float(input(f'Digite a {c}º nota:'))
    nota.append(aluno_nota)

media_aluno = sum(nota) / len(nota)

print(f'O total de notas do aluno foi {sum(nota):.2f} e sua media foi {media_aluno:.2f}')
if media_aluno >= 7:
    print(f'A média do aluno foi {media_aluno:.2f}, PARABÉNS APROVADO!')
elif  5 <= media_aluno <= 7:
    print(f'A média do aluno foi {media_aluno:.2f},ALUNO EM RECUPERAÇÃO!')
else:
    print(f'A média do aluno foi {media_aluno:.2f},ALUNO REPROVADO!')

