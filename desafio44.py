'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- á vista dinheiro/cheque: 10% de desconto
- á vista no cartão: 5% de desconto
- em até duas vezes no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''
print(f'{'LOJINHA DA LALA' :=^40}')
valor = float(input('Qual o valor do produto? R$ '))
pagamento = int(input('''Insira a forma de pagamento:
[1] - Á vista em DINHEIRO ou CHEQUE
[2] - Á vista no CARTÃO
[3] - 2x vezes no CARTÃO
[4] - 3x vezes ou mais no CARTÃO
Qual a sua opção? '''))
if pagamento == 1:
    print(f'A forma de pagamento selecionada foi á vista em dinheiro ou cheque, obtendo 10% de desconto. O valor do produto era R$ {valor} e você pagará R$ {valor - (valor * 10 / 100):.2f}')
elif pagamento == 2:
    print(f'A forma de pagamento selecionada foi á vista no cartão, obtendo 5% de desconto. O valor do produto era R$ {valor} e você pagará R$ {valor - (valor * 5 / 100):.2f}')
elif pagamento == 3:
    print(f'A forma de pagamento selecionada foi de 2x no cartão. Você pagará R$ {valor}')
elif pagamento == 4:
    print(f'A forma de pagamento selecionada foi de 3x ou mais no cartão, com juros de 20%. Você pagará {valor + (valor * 20 / 100):.2f}')
else:
    print(f'OPÇÃO INVÁLIDA. Tente novamente.')