'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''

frase = str(input('Insira uma frase qualquer: ')).strip().upper().split() # pedir uma frase para o usuário, eliminando espaços do começo, deixando as letras em maiúsculo e divindo as palvras em uma coleção.
junto = ''.join(frase) # variável para juntar a frase, eliminando os espaços
inverso = '' # variável para auxiliar 
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')

    
'''
#Alternativa sem for, usando técnicas de fatiamento
frase = str(input('Insira uma frase qualquer: ')).strip().upper().split()
junto = ''.join(frase)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')
'''
