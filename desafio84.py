'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''


nomepeso = []
con = ''
maior = menor = 0

while con != 'N':
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    pessoa = [nome, peso]
    nomepeso.append(pessoa)
    maior = max(p[1] for p in nomepeso)
    menor = min(p[1] for p in nomepeso)
    con = str(input('Inserir mais nomes? [S/N] ')).upper().strip()
    if con not in ['S', 'N']:
        print('Apenas S ou N! Tente novamente.')
print(f"Você cadastrou {len(nomepeso)} pessoas!")
print("Pessoas mais pesadas: ")
for p in nomepeso:
    if p[1] == maior:
        print(f" {p[0]}")

print(f"Pessoas mais leves: ")
for p in nomepeso:
    if p[1] == menor:
        print(f" {p[0]}")
'''
# Solução Guanabara

temp = [] # Lista que armazena os dados temporariamente
princ = [] # Lista principal
maior = menor = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:]) #[:] Cria uma cópia, gera um fatiamento total
    temp.clear()

    resp = str(input("Quer continuar? [S/N]? "))
    if resp in "Nn":
        break
print(f"Os dados foram: {princ}")
print(f"Você cadastrou {len(princ)} pessoas. ")
print(f"O maior peso foi de {maior} Kg. Peso de: ", end="")
for p in princ:
    if p[1] == maior:
        print(f"[{p[0]}] ", end="")
print()
print(f"O menor peso foi de {menor} Kg. Peso de: ", end="")
for p in princ:
    if p[1] == menor:
        print(f"{p[0]} ", end="")
print()
'''