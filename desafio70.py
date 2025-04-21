'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostra:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$ 1.000.
C) Qual é o nome do produto mais barato. 
'''
totalc = mais1000 = barato = c = 0
menor = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Valor do produto: R$ '))
    c+= 1
    totalc += preço
    if preço > 1000:
        mais1000 += 1
    if c == 1 or preço < barato:
        barato = preço
        menor = produto
    con = ' '
    while con not in 'SN':
        con = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if con == 'N':
        break
print(f'O total gasto na compra foi R${totalc:.2f}')
print(f'{mais1000} produtos custam mais de R$ 1.000')
print(f'O produto mais barato foi {menor} e custa R$ {barato:.2f} ')
