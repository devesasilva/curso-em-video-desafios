'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
contagem = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
con = 'S'.upper().strip()
while con != 'N':
    while True:
        num = int(input('Digite um número de 0 a 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente! Apenas números entre 0 e 20')
    print(f'O número é {contagem[num]}')
    while True:
        con = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
        if con in ['S', 'N']:
           break
        print(f'Tente novamente. Apenas S ou N!')