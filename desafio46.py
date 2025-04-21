''' 
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 um segundo entre eles.
'''
from time import sleep
print('=-' * 15)
print('     FOGOS DE ARTIFÍCIO')
print('=-' * 15)
#c é uma variável de controle
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVO!')