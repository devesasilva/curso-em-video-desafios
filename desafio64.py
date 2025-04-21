'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)
'''

c = 0
s = 0
num = 0
num = int(input('Informe um número: '))
while num != 999:
   c += 1
   s += num  
   num = int(input('Informe um número: '))
print(f'Foram digitados {c} números e a soma entre todos os números foi {s}')
print('Fim do programa')