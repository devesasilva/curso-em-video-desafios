'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
jogador = {}
partidas = []
jogador['nome'] = str(input('Nome: '))
total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, total_partidas):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

#Forma um de mostrar isso
print(jogador)

# Forma dois
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O jogador {jogador["nome"]} jogou {total_partidas} partidas')

# Forma três
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')


# Meu raciocicio:
# Fazer algo parecido com o exercício anterior, o dicionário jogador nasce vazio e as informações vão sendo adicionadas conforme o programa.
# A cada número colocado em partidas, é solicitado ao usuário para adicionar o número de gols feito, enquanto isso é adicionado a uma variável exclusiva para o total de gols.