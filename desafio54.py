'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
   ano = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
   idade = atual - ano
   if idade >= 21:
      totmaior += 1     
   elif idade < 21:
      totmenor += 1
print(f'No total há {totmaior} pessoas maiores de idade')
print(f'No total há {totmenor} pessoas maiores de idade')
