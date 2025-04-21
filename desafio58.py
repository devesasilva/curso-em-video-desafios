#Jogo da Adivinhação
'''
Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

#usar módulo para comnseguir o número aleátorio
import random
from time import sleep
c = 0
num = random.randint(0, 10)
n = int(input('Tente descobrir o número, de 0 a 10: '))
print('\033[4;35;40mPROCESSANDO...\033[m')
sleep(1) #módulo que faz o resultado aparecer depois dos segundos definidos entre parenteses
while n != num:
     c += 1
     print(f'Errou! Por enquanto você tentou {c} vezes, continue tentando.')
     n = int(input('Insira novamente: '))
     print('\033[4;35;40mPROCESSANDO...\033[m')
     sleep(1) 
print(f'Você acertou! Parabéns\nForam necessárias {c} tentativas no total.')


'''
#Resolução Gunabara
# Opinião - Foi tão eficiente quanto o meu, mas usou boolean e adicionou dicas de mais ou menos, muito legal tbm.
from random import randint
computador = randint(0, 10)
print('Adivinhe o número que estou pensando, entre 0 e 10.')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS... Tente mais uma vez.')
        elif jogador > computador:
            print('MENOS... Tente novamente.')
print(f'Acertou! Com {palpites} palpites, parabéns!')
'''