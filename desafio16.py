#Crie um programa que leia um número real qualquer pelo teclado e mostre a sua porção inteira

#Importando módulos
from math import trunc
real = float(input('Insira um número real qualquer: '))
print(f'O  número {real} tem a parte inteira {trunc(real)}')

# Sem importar módulos
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua parte inteira é {int(num)}')