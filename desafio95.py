'''
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador. 
'''

'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
jogador = {}
partidas = []
time = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()

    for c in range(0, total_partidas):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        opcao = str(input('Adicionar mais jogadores? [S/N] ')).upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Apenas S ou N')
    if opcao == 'N':
        break

print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)

while True:
    busca = int(input('Quer os dados de qual jogador? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com o código {busca}')
    else:
        print(f' --Levantamento do {time[busca] ["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-=' * 40)
print('Fim do programa!')