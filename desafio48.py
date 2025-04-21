'''
Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
s = 0
c = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        c += 1
        s += i
print(f'A soma de todos os {c} números ímpares múltiplos de 3 é igual a {s}')
