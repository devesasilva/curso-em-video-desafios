#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Insira o valor do produto : '))
novo_preco= 5 * preco / 100
desconto = preco - novo_preco

print(f'O valor do produto com o desconto de 5% é R$ {desconto:.2f}')