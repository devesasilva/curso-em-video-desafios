'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
# 35 anos de contribuição para calcular a idade que o usuário vai se aposentar
from datetime import datetime
trabalhador = {}
trabalhador['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: ')) 
trabalhador['idade'] = datetime.now().year - nascimento
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input('Ano de Contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratacao'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in trabalhador.items():
    print(f'- {k} tem o valor {v}')

