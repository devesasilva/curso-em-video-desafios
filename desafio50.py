'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for ímpar, desconsidere-o.
'''
s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Insira o número {c}: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Você informou {cont} números PARES e a soma entre eles é: {s}')