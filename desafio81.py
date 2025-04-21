'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados #USE LEN
B) A lista de valores ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista
'''
valores = []
con = 'S'
while con == 'S':
    valores.append(int(input('Insira um valor: ')))
    while True:
        con = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if con in ['S', 'N']:
            break
        print('Apenas S ou N!')
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O valor 5 foi digitado')
else:
    print(f'O valor 5 não está na lista!')
#Aprimorar