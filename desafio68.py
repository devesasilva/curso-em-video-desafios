'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
v = total = 0
while True:
    jogador = int(input('Diga um valor: '))
    pc = randint(1, 10)
    total = jogador + pc
    opção = ' '
    while opção not in 'PI':
        opção = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {pc}. Total deu {total}', end=" ") 
    print('PAR' if total % 2 == 0 else 'ÍMPAR')
    if opção == 'P':
        if total % 2 == 0: 
            print('Você venceu!') 
            v += 1
        else:
            print('Perdeu!')
            break
    elif opção == 'I':
        if total % 2 != 0:
            print('Você venceu!')
        else:
            print('Você perdeu!')
            break
print(f'Você teve {v} vitórias!')

            