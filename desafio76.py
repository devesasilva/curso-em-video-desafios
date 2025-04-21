'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços organizando os dados em forma tabular.
'''
listagem = 'Pão', 1.00, 'Leite', 5.90, 'Arroz', 20.99, 'Bolacha', 4.50, 'Café', 10
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    elif pos % 2 == 1:
        print(f'R$ {listagem[pos]:>5.2f}')
    