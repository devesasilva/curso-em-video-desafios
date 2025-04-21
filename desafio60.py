#Cálculo Fatorial
'''
Faça um programa que leia um número qualquer e mostre seu fatorial;
Ex: 5! = 5x4x3x2x1 = 120

#fazer com while e for
'''
'''
# Resolução com módulo factorial
from math import factorial
num = int(input('Insira um número: '))
f = factorial(num)
print(f'O fatorial de {num} é: {f}')
'''
'''
num = int(input('Insira um número: '))
c = num
f = 1
while c > 0:
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else '=', end=' ')
    f = f * c # pode ser f*= c
    c -= 1
print(f'{f}')
'''
num = int(input('Insira um número: '))
f = 1
for p in range(num, 0, -1):
    f *= p
print(f)