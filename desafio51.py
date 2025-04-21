'''
Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética (PA). No final, mostre os 10 primeiros termos dessa progressão.
'''
#forma que encontrei para aparcer os 10 primeiros termos
'''
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
for i in range(termo, 20, razão):
    print(f'{i}', end=' -> ')
print('FIM')
'''
#resolução da aula
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = termo + (10 - 1) * razão
for i in range(termo, décimo + 1, razão):
    print(f'{i}', end=' -> ')
print('FIM')