nota = []
notaSomada = sum(nota)
lenNota = len(nota)



for c in range(1, 4):
    aluno_nota = float(input(f'Digite a {c}º nota:'))
    nota.append(aluno_nota)

notaSomada = sum(nota)
lenNota = len(nota)

def mediaAluno(nota, quantidade):
    media_aluno = nota / quantidade
    return media_aluno


print(f'O total de notas do aluno foi {sum(nota):.2f} e sua media foi {mediaAluno(notaSomada, lenNota):.2f}')

if mediaAluno(notaSomada, lenNota) >= 7:
    print(f'A média do aluno foi {mediaAluno(notaSomada, lenNota):.2f}, PARABÉNS APROVADO!')
elif  5 <= mediaAluno(notaSomada, lenNota) <= 7:
    print(f'A média do aluno foi {mediaAluno(notaSomada, lenNota):.2f},ALUNO EM RECUPERAÇÃO!')
else:
    print(f'A média do aluno foi {mediaAluno(notaSomada, lenNota):.2f},ALUNO REPROVADO!')

