'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
d = 0
n = int(input('Insira um número inteiro: '))
for c in range(1, n + 1):
    if n % c == 0:
        d += 1
print(f'O número {c} foi divisível {d} vezes', end=' ')
if d >= 2:
    print('e por isso ele é PRIMO')
else:
    print('e por isso ele NÃO É PRIMO!')
    