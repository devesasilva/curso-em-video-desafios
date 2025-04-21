'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0:
Reprovado
- Média entre 5.0 e 6.9:
Recuperação
- Média 7.0 ou superior:
Aprovado
'''
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
m = (n1 + n2) / 2

if m < 5:
    print(f'A sua média foi {m:.1f}, por isso foi REPROVADO.')
elif m <= 6.9:
    print(f'A sua média foi {m:.1f}, por isso está de RECUPERAÇÃO.')
else:
    print(f'A sua média foi {m:.1f}, por isso foi APROVADO.')