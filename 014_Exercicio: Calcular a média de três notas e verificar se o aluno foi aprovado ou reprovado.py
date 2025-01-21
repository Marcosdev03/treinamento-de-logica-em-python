notas = []


for c in range(1, 4):
    n = float(input(f'Digite a {c}º nota: '))
    notas.append(n)
media = sum(notas) / 3

if media > 7:
    print(f'A nota do aluno foi {sum(notas):.2f} a media foi {media:.2f} [ALUNO APROVADO!]')
elif 4 <= media <= 7:
    print(f'A nota do aluno foi {sum(notas):.2f} a media foi {media:.2f} [ALUNO DE RECUPERAÇÃO!]')
else:
    print(f'A nota do aluno foi {sum(notas):.2f} a media foi {media:.2f} [ALUNO REPROVADO!]')

