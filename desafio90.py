'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''

aluno = {}
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))

if aluno['media'] >= 7:
    aluno['situção'] = 'Aprovado'
elif 5<= aluno['media'] < 7:
    aluno['situção'] = 'Recuperação'
else:
    aluno['situção'] = 'Reprovado'
print('-=' * 15)
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["situção"]}')

'''
# Outra forma de apresentar os dados
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
'''