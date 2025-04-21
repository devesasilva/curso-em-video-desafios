'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 - para binário
2 - para octal
3 - para hexadecimal
'''
#Bases númericas

n = int(input('Informe um número inteiro: '))
print('''Escolha uma das bases para a conversão: 
[1] Binário
[2] Octal
[3] Hexadecimal''')
base = int(input('Qual a sua opção: '))

if base == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif base == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif base == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print('Opção invalida. TENTE NOVAMENTE!')