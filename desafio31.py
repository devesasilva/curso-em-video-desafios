'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km e R$ 0,45 para viagens mais longas.
'''
dis = float(input('Insira a distância da viagem em Km: '))
if dis <= 200:
    print(f'O valor total da passagem é: R$ {dis * 0.50:.2f}')
else:
    print(f'O valoro total da passagem é: R$ {dis * 0.45:.2f}')