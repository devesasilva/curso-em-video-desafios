#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

m = (n1 + n2) / 2

print(f'A média é {m:.1f}')