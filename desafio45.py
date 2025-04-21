'''
Crie um programa que faça o computador jogar jokenpô com você.
'''
import random
from time import sleep
pc = random.randint(1, 3)
j = int(input('''
[1] - Pedra
[2] - Papel
[3] - Tesoura
Qual a sua jogada? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
#Jogada do computador
if pc == 1:
    print('Computador jogou PEDRA')
elif pc == 2:
    print('Computador jogou PAPEL')
elif pc == 3:
    print('Computador jogou TESOURA')
#Jogada do usuário
if j == 1:
    print('A sua jogada foi PEDRA')
elif j == 2:
    print('A sua jogada foi PAPEL')
elif j == 3:
    print('A sua jogada foi TESOURA')
#Verificando quem ganhou
if pc == j:
    print('EMPATE!')
elif (j == 1 and pc == 3) or (j == 3 and pc == 2) or (j == 2 and pc == 1):
    print('VOCÊ VENCEU!')
else: 
    print('VOCÊ PERDEU!')
