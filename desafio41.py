'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Júnior
- Até 20 anos: Sênior
- Acima: Master
'''
print('-=' * 15)
print('     CATEGORIA DE ATLETAS')
print('-=' * 15)

from datetime import date
ano = int(input('Informa o seu ano de nascimento: '))
idade = date.today().year - ano
print(f'O atleta que nasceu em {ano}, possui {idade} anos')
if idade <= 9:
    print('A sua categoria é MIRIM')
elif idade <= 14:
    print('A sua categoria é Infantil')
elif idade <= 19:
    print('A sua categoria é Júnior')
elif idade <= 25:
    print('A sua categoria é SÊNIOR')
else:
    print('A sua categoria é MASTER')