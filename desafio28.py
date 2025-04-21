'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
#usar módulo para comnseguir o número aleátorio
import random
from time import sleep
num = random.randint(0, 5) 
n = int(input('Tente descobrir o número, de 0 a 5: '))
print('\033[4;35;40mPROCESSANDO...\033[m')
sleep(3) #módulo que faz o resultado aparecer depois dos segundos definidos entre parenteses
if n == num:
    print(f'Você acertou!')
else:
    print(f'Você errou! O número era {num}, tente novamente.')