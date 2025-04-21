'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou o tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
print('-=-'*15)
print('           ALISTAMENTO MILITAR')
print('-=-'*15)

sexo = int(input('''Selecione qual o seu genero:
[1] - Feminino
[2] - Masculino
'''))

if sexo == 1:
    print('Mulheres não precisam se alistar!')
elif sexo == 2:
    ano = int(input('Informe o ano de nascimento: '))
    idade = date.today().year - ano

    if idade < 18:
        print(f'O usuário possui {idade} anos, ele ainda irá se alistar.')
    elif idade == 18:
        print(f'O usuário possui {idade} anos, está na hora de se alistar!')
    else:
        print(f'O usuário possui {idade} anos, já passou da hora de se alistar!')


