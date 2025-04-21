'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
r1 = float(input('Insira o comprimento da primeira reta: '))
r2 = float(input('Insira o comprimento da segunda reta: '))
r3 = float(input('Insira o comprimento da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print(f'As retas formam um triângulo')
else:
    print('As retas não formam um triângulo')
