'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''

c = 0
h = 0
m = 0 
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        c += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo in 'Mm':
        h += 1
    if idade <= 20 and sexo in 'Ff':
        m += 1
    print('-' * 20)
    cont = str(input('Quer continiuar [S/N] ')).strip().upper()[0]
    if cont != 'S':
        break
    print('-' * 20)
print(f'Total de pessoas com mais de 18 anos: {c}')
print(f'Ao total temos {h} homens cadastrados')
print(f'E temos {m} mulheres com menos de 20 anos')