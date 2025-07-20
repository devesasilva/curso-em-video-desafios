'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
'''
from random import randint
resultados = []
jogadores = {}

for i in range(1, 5):
    jogadores[f'jogador{i}'] = randint(0, 6)
    resultados.append(jogadores)

print(f'O {resultados[0]}')
    
'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = []
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("=-" * 15)
print(" == RANKING DOS JOGADORES == ")
for i, v in enumerate(ranking):
    print(f"{i+1}º lugar:  {v[0]} com {v[1]}.")