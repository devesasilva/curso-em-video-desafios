'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''
num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print(f'\033[1;35;40mPAR\033[m')    
else:
    print(f'ÍMPAR')