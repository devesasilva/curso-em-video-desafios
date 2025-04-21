'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente. 
'''

nomenota = []
con = ''

while con != 'N':
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    nomenota.append([nome, [nota1, nota2], media])
    con = str(input("Quer continuar? [S/N] ")).upper().strip()
print(f"{"No.":<4}{"NOME":<10}{"MÉDIA":>8}")
print("-" * 26)
for i, a in enumerate(nomenota):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print("-" * 26)
    opcao = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opcao == 999:
        print("Finalizando...")
        break
    if opcao <= len(nomenota) - 1:
        print(f"Notas de {nomenota[opcao][0]} são {nomenota[opcao][1]}")
