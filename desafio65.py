'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

con = 'S'
quant = soma = media = maior = menor = 0
while con == 'S':
    n = int(input('Insira um valor: '))
    soma = soma + n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    con = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    media = soma/quant
print(f'Foram digitados {quant} e a média entre eles é: {media}')
print(f'O maior número é {maior} e o menor é {menor}')
print('FIM')
