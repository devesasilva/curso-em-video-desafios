'''
Faça um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00,calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

sal = float(input('Qual o seu salário: '))

if sal > 1250:
    novo_salario = sal + (10 * sal) / 100
    print(f'O seu aumento será de 10%. O seu novo salário é: R${novo_salario:.2f}')
else:
    novo_salario = sal + (15 * sal) / 100
    print(f'O seu aumento será de 15%. O seu novo salário é: R${novo_salario:.2f}')
