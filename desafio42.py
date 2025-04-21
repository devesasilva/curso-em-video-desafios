'''
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados são iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''
r1 = float(input('Insira o comprimento da primeira reta: '))
r2 = float(input('Insira o comprimento da segunda reta: '))
r3 = float(input('Insira o comprimento da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print(f'As retas formam um triângulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('As retas não formam um triângulo')

