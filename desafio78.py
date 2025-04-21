'''
Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(f'A lista tem os seguintes valores: {valores}')
maior = valores[0]
menor = valores[0]

for valor in valores:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f'O maior valor foi {maior} e está nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print(f'O menor valor foi {menor} e está nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()
