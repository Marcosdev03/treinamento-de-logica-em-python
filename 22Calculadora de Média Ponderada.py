valores = []
pesos = []
for c in range (1, 4 ):
    v_valores = int(input(f'Digite o {c}º valor: '))
    valores.append(v_valores)
    p_pesos = int(input(f'Digite o o peso do {c}º valor: kg '))
    pesos.append(p_pesos)

valor_pesos = sum(pesos)
valor_nota1 = valores[0] * pesos[0]
valor_nota2 = valores[1] * pesos[1]
valor_nota3 = valores[2] * pesos[2]
valor_sum_notas = valor_nota1 + valor_nota2 + valor_nota3
media_poderada = ( valor_sum_notas / valor_pesos)

print(f'A média ponderada é {media_poderada}')
