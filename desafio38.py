'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''
n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))

if n1 > n2:
    print(f'O valor {n1} é maior que {n2}')
elif n2 > n1:
    print(f'O valor {n2} é maior que {n1}')
else:
    print(f'Não existe valor maior, os valores {n1} e {n2} são iguais')