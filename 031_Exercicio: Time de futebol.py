times_brasileirao = (
    "Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional",
    "Athletico Paranaense", "Atlético Mineiro", "Grêmio", "Red Bull Bragantino",
    "Fluminense", "São Paulo", "Corinthians", "Cuiabá", "Criciúma",
    "Vasco da Gama", "Bahia", "América Mineiro", "Atlético Goianiense",
    "Juventude",
)
times_ordenados = sorted(times_brasileirao)
print('=-'*20)
print(f'Lista de times: {times_brasileirao}')
print('=-'*20)
print(f'Lista de times em ordem alfabética: {times_ordenados}')
print('=-'*20)
print(f'Os cinco primeiro times são: {times_brasileirao[0:5]}')
print('=-'*20)
print(f'Os quatro ultimos times são: {times_brasileirao[-4:]}')
print('=-'*20)
print(f'O Atletico mineiro está na {times_brasileirao.index("Atlético Mineiro")+1}º posição.')
print('=-'*20)