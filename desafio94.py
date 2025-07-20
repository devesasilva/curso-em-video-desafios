'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todos as mulheres
D) Uma lista com todas pessoas com idade acima da média
'''
galera = []
pessoa = {}
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ').capitalize()
    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if opcao == 'N':
        break
print('-=' * 15)

quant_cadastrados = len(galera)
media_idade = soma / quant_cadastrados
print(f'Ao todo temos {quant_cadastrados} pessoas cadastradas')
print(f'A média de idade das pessoas é {media_idade:5.2f}')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista de pessoas com idade acima da média: ')
for p in galera:
    if p['idade'] >= media_idade:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('Fim do programa!')