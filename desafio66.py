'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

n = s = c = 0
while True:
    n = int(input('Insira um número: '))
    if n == 999:
        break
    c = c + 1
    s = s + n
print(f'Foram digitados {c} números e a soma entre eles é: {s}')