'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
valor_casa = float(input('Qual o valor da casa? '))
valor_salário = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos irá pagar? '))
#Calculo da prestação
prestacao = valor_casa / (anos * 12)
minimo = valor_salário * 30 / 100
print(f'A prestação será de R$ {prestacao:.2f}')

if prestacao > minimo:
    print(f'Empréstimo negado')
else:
    print('Empréstimo aprovado')