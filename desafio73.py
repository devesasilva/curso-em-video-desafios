'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela está o time da Chapecoense 
'''
times = 'botafogo', 'fortaleza', 'palmeiras', 'flamengo', 'cruzeiro', 'são paulo', 'bahia', 'vasco', 'atlético mineiro', 'internacional', 'bragantino', 'atlético paranaense', 'juventude', 'criciúma', 'grêmio', 'fluminense', 'corinthians', 'vitória', 'cuiabá', 'atlético goianiense'

for t in times:
    print(f'{t}')
# print(f'Lista de times: {times}') # dá para usar um for para deixar um time embaixo do outro dessa forma: for t in times: print(t)
print('=' * 30)
print(f'Os cinco primeiros colocados são {times[0:5]}')
print('=' * 30)
print(f'Os últimos quatro colocados são: {times[16:20]}') #podia ser -4:
print('=' * 30)
print(f'Times em ordem alfabética {sorted(times)}')
print('=' * 30)
print(f'O {times[3]} está na {times.index('flamengo') + 1}ª posição') 
