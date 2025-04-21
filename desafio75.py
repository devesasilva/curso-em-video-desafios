'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posção foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

valores = (int(input('Digite o primeiro valor: ')),
           int(input('Digite o segundo valor: ')),
           int(input('Digite o terceiro valor: ')),
           int(input('Digite o quarto valor: ')))
print(f'Você digitou os valores: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu pela primeira vez na {valores.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

pares = [n for n in valores if n % 2 == 0] #Acabei usando o conceito de listas.
if pares:
    print(f'Os valores pares que foram digitados são: {pares}.')
else:
    print(f'Nenhum número par foi digitado.')
# O código estava assim na verificação de números pares
    #|
    #v
'''
print(f'Os valores pares que foram digitados são: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
'''



'''
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
v4 = int(input('Digite o quarto valor: '))
valores = v1, v2, v3, v4
'''