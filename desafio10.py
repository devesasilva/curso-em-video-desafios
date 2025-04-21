# 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

real = float(input('Insira quanto possui em reais: '))
print(f'Com a quantidade de reais que possui, pode comprar {real / 5.49:.2f} dólares')
print(f'Com a quantidade de reais que possui, você pode comprar {real / 5.93:.2f} euros')
print(f'Com a quantidade de reais que possui, você pode comprar {real / 0.0040} wons')